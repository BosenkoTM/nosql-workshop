import pymongo
from pymongo import MongoClient
from datetime import datetime
import pandas as pd
import json
from pprint import pprint

# =============================================================================
# 🔌 ПОДКЛЮЧЕНИЕ К MONGODB
# =============================================================================

def connect_to_mongodb():
    """Подключение к MongoDB и проверка соединения"""
    try:
        # Подключение к MongoDB (используем адрес из docker-compose)
        client = MongoClient("mongodb://root:abc123!@mongo-1:27017/")
        
        # Альтернативный способ подключения для локального использования:
        # client = MongoClient("mongodb://root:abc123!@localhost:27017/")
        
        # Проверка подключения
        client.server_info()
        print("✅ Успешное подключение к MongoDB!")
        
        # Получение базы данных и коллекции
        db = client.recommendation_db
        collection = db.user_interactions
        
        return client, db, collection
        
    except Exception as e:
        print(f"❌ Ошибка подключения к MongoDB: {e}")
        print("\n🔍 Возможные решения:")
        print("1. Проверьте, что контейнер MongoDB запущен: docker ps")
        print("2. Попробуйте localhost вместо mongo-1 в строке подключения")
        print("3. Убедитесь, что порт 27017 доступен")
        return None, None, None

# Подключаемся к MongoDB
client, db, collection = connect_to_mongodb()

if collection is None:
    print("🛑 Не удалось подключиться к MongoDB. Проверьте подключение.")
else:
    print(f"🗄️  Работаем с базой данных: {db.name}")
    print(f"📋 Работаем с коллекцией: {collection.name}")

# =============================================================================
# 📊 ОСНОВНЫЕ ПРОВЕРКИ ДАННЫХ
# =============================================================================

def check_collection_stats():
    """Проверка основной статистики коллекции"""
    
    if collection is None:
        return
    
    print("\n" + "="*60)
    print("📊 ОСНОВНАЯ СТАТИСТИКА КОЛЛЕКЦИИ")
    print("="*60)
    
    # Общее количество документов
    total_docs = collection.count_documents({})
    print(f"📄 Общее количество документов: {total_docs}")
    
    if total_docs == 0:
        print("⚠️  Коллекция пуста! Запустите генерацию данных.")
        return
    
    # Уникальные пользователи
    unique_users = len(collection.distinct("user_id"))
    print(f"👥 Уникальных пользователей: {unique_users}")
    
    # Уникальные товары
    unique_items = len(collection.distinct("item_id"))
    print(f"📦 Уникальных товаров: {unique_items}")
    
    # Типы взаимодействий
    interaction_types = collection.distinct("interaction_type")
    print(f"🎯 Типы взаимодействий: {interaction_types}")
    
    # Категории товаров
    categories = collection.distinct("item_details.category")
    print(f"🏷️  Категории товаров: {categories}")
    
    # Временной диапазон
    pipeline_time = [
        {"$group": {
            "_id": None,
            "min_date": {"$min": "$timestamp"},
            "max_date": {"$max": "$timestamp"}
        }}
    ]
    
    time_range = list(collection.aggregate(pipeline_time))
    if time_range:
        min_date = time_range[0]['min_date']
        max_date = time_range[0]['max_date']
        print(f"📅 Временной диапазон: {min_date.strftime('%Y-%m-%d')} - {max_date.strftime('%Y-%m-%d')}")

check_collection_stats()

# =============================================================================
# 🔍 ПРОСМОТР ПРИМЕРОВ ДАННЫХ
# =============================================================================

def show_sample_documents(limit=3):
    """Показ примеров документов из коллекции"""
    
    if collection is None:
        return
    
    print("\n" + "="*60)
    print("🔍 ПРИМЕРЫ ДОКУМЕНТОВ")
    print("="*60)
    
    # Получаем несколько случайных документов
    sample_docs = list(collection.aggregate([{"$sample": {"size": limit}}]))
    
    for i, doc in enumerate(sample_docs, 1):
        print(f"\n📄 Документ #{i}:")
        print("-" * 40)
        
        # Красивый вывод JSON
        doc_copy = doc.copy()
        doc_copy['_id'] = str(doc_copy['_id'])  # Конвертируем ObjectId в строку
        doc_copy['timestamp'] = doc_copy['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
        
        print(json.dumps(doc_copy, indent=2, ensure_ascii=False))

show_sample_documents(limit=2)

# =============================================================================
# 📋 СТРУКТУРИРОВАННЫЙ ПРОСМОТР ДАННЫХ
# =============================================================================

def show_data_as_table(limit=10):
    """Показ данных в табличном формате"""
    
    if collection is None:
        return
    
    print("\n" + "="*60)
    print("📋 ДАННЫЕ В ТАБЛИЧНОМ ФОРМАТЕ")
    print("="*60)
    
    # Получаем данные и преобразуем в DataFrame
    cursor = collection.find().limit(limit)
    
    data = []
    for doc in cursor:
        flat_doc = {
            'user_id': doc['user_id'],
            'item_id': doc['item_id'],
            'interaction_type': doc['interaction_type'],
            'timestamp': doc['timestamp'].strftime('%Y-%m-%d %H:%M'),
            'rating': doc.get('rating', 'N/A'),
            'duration': doc['duration'],
            'device': doc['context']['device'],
            'location': doc['context']['location'],
            'time_of_day': doc['context']['time_of_day'],
            'category': doc['item_details']['category'],
            'brand': doc['item_details']['brand'],
            'price': doc['item_details']['price'],
            'age_group': doc['user_profile']['age_group'],
            'gender': doc['user_profile']['gender']
        }
        data.append(flat_doc)
    
    if data:
        df = pd.DataFrame(data)
        print(df.to_string(index=False))
    else:
        print("⚠️  Нет данных для отображения")

show_data_as_table(limit=5)

# =============================================================================
# 📊 ДЕТАЛЬНЫЙ АНАЛИЗ ПО КАТЕГОРИЯМ
# =============================================================================

def analyze_by_categories():
    """Анализ данных по категориям"""
    
    if collection is None:
        return
    
    print("\n" + "="*60)
    print("📊 АНАЛИЗ ПО КАТЕГОРИЯМ")
    print("="*60)
    
    pipeline = [
        {"$group": {
            "_id": "$item_details.category",
            "total_interactions": {"$sum": 1},
            "unique_users": {"$addToSet": "$user_id"},
            "unique_items": {"$addToSet": "$item_id"},
            "avg_price": {"$avg": "$item_details.price"},
            "purchases": {
                "$sum": {"$cond": [{"$eq": ["$interaction_type", "purchase"]}, 1, 0]}
            },
            "likes": {
                "$sum": {"$cond": [{"$eq": ["$interaction_type", "like"]}, 1, 0]}
            },
            "views": {
                "$sum": {"$cond": [{"$eq": ["$interaction_type", "view"]}, 1, 0]}
            },
            "avg_rating": {"$avg": "$rating"}
        }},
        {"$addFields": {
            "unique_users_count": {"$size": "$unique_users"},
            "unique_items_count": {"$size": "$unique_items"}
        }},
        {"$sort": {"total_interactions": -1}}
    ]
    
    results = list(collection.aggregate(pipeline))
    
    if results:
        # Создаем DataFrame для красивого отображения
        df_data = []
        for result in results:
            df_data.append({
                'Категория': result['_id'],
                'Взаимодействия': result['total_interactions'],
                'Пользователи': result['unique_users_count'],
                'Товары': result['unique_items_count'],
                'Покупки': result['purchases'],
                'Лайки': result['likes'],
                'Просмотры': result['views'],
                'Средняя цена': f"${result['avg_price']:.2f}" if result['avg_price'] else 'N/A',
                'Средняя оценка': f"{result['avg_rating']:.1f}" if result['avg_rating'] else 'N/A'
            })
        
        df = pd.DataFrame(df_data)
        print(df.to_string(index=False))
    else:
        print("⚠️  Нет данных для анализа")

analyze_by_categories()

# =============================================================================
# 👥 АНАЛИЗ АКТИВНОСТИ ПОЛЬЗОВАТЕЛЕЙ
# =============================================================================

def analyze_user_activity():
    """Анализ активности пользователей"""
    
    if collection is None:
        return
    
    print("\n" + "="*60)
    print("👥 АНАЛИЗ АКТИВНОСТИ ПОЛЬЗОВАТЕЛЕЙ")
    print("="*60)
    
    pipeline = [
        {"$group": {
            "_id": "$user_id",
            "total_interactions": {"$sum": 1},
            "purchases": {
                "$sum": {"$cond": [{"$eq": ["$interaction_type", "purchase"]}, 1, 0]}
            },
            "total_spent": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$interaction_type", "purchase"]},
                        "$item_details.price",
                        0
                    ]
                }
            },
            "avg_rating": {"$avg": "$rating"},
            "categories": {"$addToSet": "$item_details.category"},
            "devices": {"$addToSet": "$context.device"},
            "first_interaction": {"$min": "$timestamp"},
            "last_interaction": {"$max": "$timestamp"}
        }},
        {"$addFields": {
            "categories_count": {"$size": "$categories"},
            "devices_count": {"$size": "$devices"},
            "days_active": {
                "$divide": [
                    {"$subtract": ["$last_interaction", "$first_interaction"]},
                    86400000  # миллисекунды в день
                ]
            }
        }},
        {"$sort": {"total_interactions": -1}},
        {"$limit": 10}
    ]
    
    results = list(collection.aggregate(pipeline))
    
    if results:
        print("🏆 ТОП-10 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:")
        print("-" * 60)
        
        for i, user in enumerate(results, 1):
            print(f"{i:2d}. {user['_id']}")
            print(f"    💫 Взаимодействий: {user['total_interactions']}")
            print(f"    🛒 Покупок: {user['purchases']}")
            print(f"    💰 Потратил: ${user['total_spent']:.2f}")
            print(f"    ⭐ Средняя оценка: {user['avg_rating']:.1f}" if user['avg_rating'] else "    ⭐ Оценок нет")
            print(f"    🏷️  Категорий: {user['categories_count']}")
            print(f"    📱 Устройств: {user['devices_count']}")
            print(f"    📅 Дней активности: {user['days_active']:.1f}")
            print()
    else:
        print("⚠️  Нет данных о пользователях")

analyze_user_activity()

# =============================================================================
# 🎯 ПРОВЕРКА КОНКРЕТНЫХ ЗАПИСЕЙ
# =============================================================================

def check_specific_data():
    """Проверка конкретных записей и связей"""
    
    if collection is None:
        return
    
    print("\n" + "="*60)
    print("🎯 ПРОВЕРКА КОНКРЕТНЫХ ЗАПИСЕЙ")
    print("="*60)
    
    # Проверим данные для конкретного пользователя
    user_id = "user_1"
    user_data = list(collection.find({"user_id": user_id}).limit(5))
    
    if user_data:
        print(f"👤 Данные для пользователя {user_id}:")
        print(f"   Найдено записей: {len(user_data)}")
        
        for i, record in enumerate(user_data[:3], 1):
            print(f"   {i}. {record['interaction_type']} -> {record['item_id']} "
                  f"({record['item_details']['category']}) "
                  f"на {record['context']['device']}")
    else:
        print(f"⚠️  Данных для пользователя {user_id} не найдено")
    
    # Проверим данные для конкретного товара
    item_id = "item_1"
    item_data = list(collection.find({"item_id": item_id}).limit(5))
    
    if item_data:
        print(f"\n📦 Данные для товара {item_id}:")
        print(f"   Найдено записей: {len(item_data)}")
        
        for i, record in enumerate(item_data[:3], 1):
            print(f"   {i}. {record['user_id']} сделал {record['interaction_type']} "
                  f"на {record['context']['device']}")
    else:
        print(f"⚠️  Данных для товара {item_id} не найдено")

check_specific_data()

# =============================================================================
# 🔧 СЛУЖЕБНЫЕ ФУНКЦИИ
# =============================================================================

def check_data_quality():
    """Проверка качества данных"""
    
    if collection is None:
        return
    
    print("\n" + "="*60)
    print("🔧 ПРОВЕРКА КАЧЕСТВА ДАННЫХ")
    print("="*60)
    
    total_docs = collection.count_documents({})
    
    # Проверка на пустые значения
    checks = [
        ("user_id", {"user_id": {"$exists": False}}),
        ("item_id", {"item_id": {"$exists": False}}),
        ("interaction_type", {"interaction_type": {"$exists": False}}),
        ("timestamp", {"timestamp": {"$exists": False}}),
        ("category", {"item_details.category": {"$exists": False}}),
        ("price", {"item_details.price": {"$exists": False}})
    ]
    
    print("🔍 Проверка обязательных полей:")
    all_good = True
    
    for field_name, query in checks:
        missing_count = collection.count_documents(query)
        if missing_count > 0:
            print(f"   ❌ {field_name}: отсутствует в {missing_count} документах")
            all_good = False
        else:
            print(f"   ✅ {field_name}: присутствует во всех документах")
    
    if all_good:
        print("\n🎉 Все проверки качества данных пройдены!")
    else:
        print("\n⚠️  Обнаружены проблемы с качеством данных")
    
    # Проверка диапазонов значений
    print(f"\n📊 Диапазоны значений:")
    
    # Цены
    price_stats = list(collection.aggregate([
        {"$group": {
            "_id": None,
            "min_price": {"$min": "$item_details.price"},
            "max_price": {"$max": "$item_details.price"},
            "avg_price": {"$avg": "$item_details.price"}
        }}
    ]))
    
    if price_stats:
        stats = price_stats[0]
        print(f"   💰 Цены: ${stats['min_price']:.2f} - ${stats['max_price']:.2f} "
              f"(среднее: ${stats['avg_price']:.2f})")
    
    # Рейтинги
    rating_stats = list(collection.aggregate([
        {"$match": {"rating": {"$ne": None}}},
        {"$group": {
            "_id": None,
            "min_rating": {"$min": "$rating"},
            "max_rating": {"$max": "$rating"},
            "avg_rating": {"$avg": "$rating"},
            "count": {"$sum": 1}
        }}
    ]))
    
    if rating_stats:
        stats = rating_stats[0]
        print(f"   ⭐ Рейтинги: {stats['min_rating']} - {stats['max_rating']} "
              f"(среднее: {stats['avg_rating']:.1f}, записей: {stats['count']})")

check_data_quality()

# =============================================================================
# 🎮 ИНТЕРАКТИВНЫЕ ФУНКЦИИ ДЛЯ ТЕСТИРОВАНИЯ
# =============================================================================

def quick_search(user_id=None, item_id=None, interaction_type=None, limit=5):
    """Быстрый поиск записей по параметрам"""
    
    if collection is None:
        print("❌ Нет подключения к базе данных")
        return
    
    # Строим запрос
    query = {}
    if user_id:
        query["user_id"] = user_id
    if item_id:
        query["item_id"] = item_id
    if interaction_type:
        query["interaction_type"] = interaction_type
    
    # Выполняем поиск
    results = list(collection.find(query).limit(limit))
    
    print(f"\n🔎 Найдено записей: {len(results)}")
    print(f"🔍 Запрос: {query}")
    print("-" * 50)
    
    for i, doc in enumerate(results, 1):
        print(f"{i}. {doc['user_id']} -> {doc['interaction_type']} -> {doc['item_id']} "
              f"({doc['item_details']['category']}) на {doc['context']['device']} "
              f"в {doc['timestamp'].strftime('%Y-%m-%d %H:%M')}")

def get_available_values():
    """Получение доступных значений для поиска"""
    
    if collection is None:
        return
    
    print("\n📋 ДОСТУПНЫЕ ЗНАЧЕНИЯ ДЛЯ ПОИСКА:")
    print("="*50)
    
    users = collection.distinct("user_id")[:10]
    items = collection.distinct("item_id")[:10]
    interactions = collection.distinct("interaction_type")
    
    print(f"👥 Пользователи (первые 10): {users}")
    print(f"📦 Товары (первые 10): {items}")
    print(f"🎯 Типы взаимодействий: {interactions}")

# Показываем доступные значения
get_available_values()

# =============================================================================
# 💡 ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ
# =============================================================================

print("\n" + "="*60)
print("💡 ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ ФУНКЦИЙ:")
print("="*60)
print("# Поиск всех действий пользователя:")
print("quick_search(user_id='user_1')")
print()
print("# Поиск всех взаимодействий с товаром:")
print("quick_search(item_id='item_5')")
print()
print("# Поиск всех покупок:")
print("quick_search(interaction_type='purchase')")
print()
print("# Комбинированный поиск:")
print("quick_search(user_id='user_2', interaction_type='like')")

# Демонстрация работы функций
print("\n🚀 ДЕМОНСТРАЦИЯ:")
quick_search(user_id='user_1', limit=3)
quick_search(interaction_type='purchase', limit=3)