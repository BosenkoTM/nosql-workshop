# Система рекомендаций MongoDB - Jupyter Notebook
# Устанавливаем необходимые библиотеки
!pip install pymongo pandas numpy matplotlib seaborn plotly

import pymongo
from pymongo import MongoClient
from datetime import datetime, timedelta
from bson import ObjectId
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Настройка стилей для графиков
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

print("📦 Библиотеки загружены успешно!")

# =============================================================================
# 🔌 ПОДКЛЮЧЕНИЕ К MONGODB
# =============================================================================

# Подключение к MongoDB
try:
    client = MongoClient("mongodb://root:abc123!@mongo-1:27017/")
    db = client.recommendation_db
    collection = db.user_interactions
    
    # Проверка подключения
    client.server_info()
    print("✅ Успешное подключение к MongoDB!")
    
    # Создание индексов для оптимизации
    collection.create_index([("user_id", 1)])
    collection.create_index([("item_id", 1)])
    collection.create_index([("timestamp", -1)])
    collection.create_index([("interaction_type", 1)])
    collection.create_index([("item_details.category", 1)])
    print("📊 Индексы созданы")
    
except Exception as e:
    print(f"❌ Ошибка подключения: {e}")

# =============================================================================
# 🎲 ГЕНЕРАЦИЯ ТЕСТОВЫХ ДАННЫХ
# =============================================================================

def generate_sample_data(num_users=50, num_items=200, num_interactions=1000):
    """Генерация тестовых данных для демонстрации"""
    
    print(f"🎯 Генерируем {num_interactions} взаимодействий...")
    
    # Базовые данные
    categories = ["electronics", "clothing", "books", "home", "sports", "beauty"]
    brands = ["Apple", "Samsung", "Nike", "Zara", "Amazon", "Ikea"]
    interaction_types = ["view", "like", "purchase", "share"]
    devices = ["mobile", "desktop", "tablet"]
    locations = ["home", "office", "store"]
    time_periods = ["morning", "afternoon", "evening", "night"]
    age_groups = ["18-25", "26-35", "36-45", "46-55", "55+"]
    genders = ["male", "female", "other"]
    interests = ["tech", "fashion", "sports", "cooking", "travel", "music"]
    
    import random
    interactions = []
    
    for i in range(num_interactions):
        user_id = f"user_{random.randint(1, num_users)}"
        item_id = f"item_{random.randint(1, num_items)}"
        
        interaction = {
            "user_id": user_id,
            "item_id": item_id,
            "interaction_type": random.choice(interaction_types),
            "timestamp": datetime.now() - timedelta(
                days=random.randint(0, 30),
                hours=random.randint(0, 23)
            ),
            "rating": round(random.uniform(1, 5), 1) if random.random() > 0.3 else None,
            "duration": random.randint(30, 1800),
            "context": {
                "device": random.choice(devices),
                "location": random.choice(locations),
                "time_of_day": random.choice(time_periods),
                "session_id": f"session_{random.randint(1000, 9999)}"
            },
            "item_details": {
                "category": random.choice(categories),
                "brand": random.choice(brands),
                "price": round(random.uniform(10, 500), 2),
                "tags": random.sample(["popular", "new", "sale", "premium"], 
                                    random.randint(1, 2))
            },
            "user_profile": {
                "age_group": random.choice(age_groups),
                "gender": random.choice(genders),
                "interests": random.sample(interests, random.randint(2, 3))
            }
        }
        interactions.append(interaction)
    
    # Очищаем коллекцию и вставляем новые данные
    collection.delete_many({})
    collection.insert_many(interactions)
    
    print(f"✅ Данные сгенерированы: {len(interactions)} записей")
    
    # Показываем статистику
    stats = collection.aggregate([
        {"$group": {
            "_id": None,
            "total_users": {"$addToSet": "$user_id"},
            "total_items": {"$addToSet": "$item_id"},
            "interactions_by_type": {
                "$push": "$interaction_type"
            }
        }}
    ])
    
    stat = list(stats)[0]
    print(f"👥 Уникальных пользователей: {len(stat['total_users'])}")
    print(f"📦 Уникальных товаров: {len(stat['total_items'])}")
    
    return True

# Генерируем данные
generate_sample_data()

# =============================================================================
# 📊 АНАЛИЗ БАЗОВЫХ МЕТРИК
# =============================================================================

def show_basic_analytics():
    """Показ базовой аналитики данных"""
    
    print("📈 БАЗОВАЯ АНАЛИТИКА\n" + "="*50)
    
    # 1. Распределение по типам взаимодействий
    pipeline_interactions = [
        {"$group": {
            "_id": "$interaction_type",
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1}}
    ]
    
    interaction_data = list(collection.aggregate(pipeline_interactions))
    interaction_df = pd.DataFrame(interaction_data)
    interaction_df.columns = ['Тип взаимодействия', 'Количество']
    
    print("🎯 Распределение взаимодействий:")
    print(interaction_df.to_string(index=False))
    
    # График распределения взаимодействий
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Pie chart
    ax1.pie(interaction_df['Количество'], labels=interaction_df['Тип взаимодействия'], 
            autopct='%1.1f%%', startangle=90)
    ax1.set_title('Распределение типов взаимодействий')
    
    # Bar chart
    ax2.bar(interaction_df['Тип взаимодействия'], interaction_df['Количество'], 
            color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
    ax2.set_title('Количество взаимодействий по типам')
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    # 2. Активность пользователей
    pipeline_users = [
        {"$group": {
            "_id": "$user_id",
            "total_interactions": {"$sum": 1},
            "purchases": {
                "$sum": {"$cond": [{"$eq": ["$interaction_type", "purchase"]}, 1, 0]}
            },
            "avg_rating": {"$avg": "$rating"}
        }},
        {"$sort": {"total_interactions": -1}},
        {"$limit": 10}
    ]
    
    top_users = list(collection.aggregate(pipeline_users))
    users_df = pd.DataFrame(top_users)
    users_df.columns = ['Пользователь', 'Всего взаимодействий', 'Покупки', 'Средняя оценка']
    
    print(f"\n👑 ТОП-10 активных пользователей:")
    print(users_df.to_string(index=False))

show_basic_analytics()

# =============================================================================
# 🔍 ФУНКЦИИ РЕКОМЕНДАТЕЛЬНОЙ СИСТЕМЫ
# =============================================================================

class SimpleRecommender:
    """Упрощенный класс рекомендательной системы для Jupyter"""
    
    def __init__(self):
        self.collection = collection
    
    def get_similar_items(self, item_id, limit=5):
        """Рекомендации похожих товаров"""
        
        pipeline = [
            {"$match": {"item_id": item_id}},
            {"$lookup": {
                "from": "user_interactions",
                "let": {"current_user": "$user_id"},
                "pipeline": [
                    {"$match": {
                        "$expr": {"$eq": ["$user_id", "$$current_user"]},
                        "item_id": {"$ne": item_id}
                    }}
                ],
                "as": "user_other_items"
            }},
            {"$unwind": "$user_other_items"},
            {"$group": {
                "_id": "$user_other_items.item_id",
                "category": {"$first": "$user_other_items.item_details.category"},
                "brand": {"$first": "$user_other_items.item_details.brand"},
                "price": {"$first": "$user_other_items.item_details.price"},
                "similarity_score": {"$sum": 1},
                "avg_rating": {"$avg": "$user_other_items.rating"}
            }},
            {"$sort": {"similarity_score": -1}},
            {"$limit": limit}
        ]
        
        results = list(self.collection.aggregate(pipeline))
        return pd.DataFrame(results) if results else pd.DataFrame()
    
    def get_popular_items(self, category=None, limit=10):
        """Популярные товары (опционально по категории)"""
        
        match_stage = {"timestamp": {"$gte": datetime.now() - timedelta(days=7)}}
        if category:
            match_stage["item_details.category"] = category
        
        pipeline = [
            {"$match": match_stage},
            {"$group": {
                "_id": "$item_id",
                "category": {"$first": "$item_details.category"},
                "brand": {"$first": "$item_details.brand"},
                "price": {"$first": "$item_details.price"},
                "total_interactions": {"$sum": 1},
                "unique_users": {"$addToSet": "$user_id"},
                "purchases": {
                    "$sum": {"$cond": [{"$eq": ["$interaction_type", "purchase"]}, 1, 0]}
                },
                "avg_rating": {"$avg": "$rating"}
            }},
            {"$addFields": {
                "unique_users_count": {"$size": "$unique_users"},
                "popularity_score": {
                    "$add": [
                        "$total_interactions",
                        {"$multiply": ["$purchases", 3]},
                        {"$multiply": [{"$ifNull": ["$avg_rating", 0]}, 2]}
                    ]
                }
            }},
            {"$sort": {"popularity_score": -1}},
            {"$limit": limit}
        ]
        
        results = list(self.collection.aggregate(pipeline))
        return pd.DataFrame(results) if results else pd.DataFrame()
    
    def get_user_recommendations(self, user_id, limit=5):
        """Персональные рекомендации для пользователя"""
        
        pipeline = [
            {"$match": {"user_id": user_id}},
            {"$lookup": {
                "from": "user_interactions",
                "let": {"current_item": "$item_id"},
                "pipeline": [
                    {"$match": {
                        "$expr": {"$eq": ["$item_id", "$$current_item"]},
                        "user_id": {"$ne": user_id}
                    }}
                ],
                "as": "similar_users"
            }},
            {"$unwind": "$similar_users"},
            {"$lookup": {
                "from": "user_interactions",
                "let": {"similar_user": "$similar_users.user_id"},
                "pipeline": [
                    {"$match": {
                        "$expr": {"$eq": ["$user_id", "$$similar_user"]}
                    }},
                    {"$lookup": {
                        "from": "user_interactions",
                        "let": {"check_item": "$item_id"},
                        "pipeline": [
                            {"$match": {
                                "$expr": {
                                    "$and": [
                                        {"$eq": ["$item_id", "$$check_item"]},
                                        {"$eq": ["$user_id", user_id]}
                                    ]
                                }
                            }}
                        ],
                        "as": "user_has_item"
                    }},
                    {"$match": {"user_has_item": {"$size": 0}}}
                ],
                "as": "recommendations"
            }},
            {"$unwind": "$recommendations"},
            {"$group": {
                "_id": "$recommendations.item_id",
                "category": {"$first": "$recommendations.item_details.category"},
                "brand": {"$first": "$recommendations.item_details.brand"},
                "price": {"$first": "$recommendations.item_details.price"},
                "recommendation_score": {"$sum": 1}
            }},
            {"$sort": {"recommendation_score": -1}},
            {"$limit": limit}
        ]
        
        results = list(self.collection.aggregate(pipeline))
        return pd.DataFrame(results) if results else pd.DataFrame()

# Создаем экземпляр рекомендателя
recommender = SimpleRecommender()

# =============================================================================
# 🎯 ДЕМОНСТРАЦИЯ РЕКОМЕНДАЦИЙ
# =============================================================================

def demo_recommendations():
    """Демонстрация работы рекомендательной системы"""
    
    print("🎯 ДЕМОНСТРАЦИЯ РЕКОМЕНДАЦИЙ\n" + "="*60)
    
    # 1. Похожие товары
    print("1️⃣ Рекомендации похожих товаров для item_1:")
    similar = recommender.get_similar_items("item_1", limit=3)
    if not similar.empty:
        print(similar[['_id', 'category', 'brand', 'similarity_score']].to_string(index=False))
    else:
        print("   Нет данных для рекомендаций")
    
    # 2. Популярные товары
    print(f"\n2️⃣ Популярные товары:")
    popular = recommender.get_popular_items(limit=5)
    if not popular.empty:
        print(popular[['_id', 'category', 'brand', 'popularity_score']].to_string(index=False))
    
    # 3. Персональные рекомендации
    print(f"\n3️⃣ Персональные рекомендации для user_1:")
    personal = recommender.get_user_recommendations("user_1", limit=3)
    if not personal.empty:
        print(personal[['_id', 'category', 'brand', 'recommendation_score']].to_string(index=False))
    else:
        print("   Нет персональных рекомендаций")

demo_recommendations()

# =============================================================================
# 📊 ВИЗУАЛИЗАЦИЯ АНАЛИТИКИ
# =============================================================================

def create_analytics_dashboard():
    """Создание дашборда аналитики"""
    
    print("📊 СОЗДАНИЕ ДАШБОРДА АНАЛИТИКИ\n" + "="*50)
    
    # 1. Активность по времени
    pipeline_time = [
        {"$group": {
            "_id": "$context.time_of_day",
            "interactions": {"$sum": 1},
            "unique_users": {"$addToSet": "$user_id"}
        }},
        {"$addFields": {
            "unique_users_count": {"$size": "$unique_users"}
        }}
    ]
    
    time_data = list(collection.aggregate(pipeline_time))
    time_df = pd.DataFrame(time_data)
    
    if not time_df.empty:
        # График активности по времени
        fig = px.bar(time_df, x='_id', y='interactions', 
                    title='Активность пользователей по времени дня',
                    labels={'_id': 'Время дня', 'interactions': 'Количество взаимодействий'})
        fig.show()
    
    # 2. Популярность категорий
    pipeline_categories = [
        {"$group": {
            "_id": "$item_details.category",
            "total_interactions": {"$sum": 1},
            "avg_price": {"$avg": "$item_details.price"},
            "purchases": {
                "$sum": {"$cond": [{"$eq": ["$interaction_type", "purchase"]}, 1, 0]}
            }
        }},
        {"$sort": {"total_interactions": -1}}
    ]
    
    cat_data = list(collection.aggregate(pipeline_categories))
    cat_df = pd.DataFrame(cat_data)
    
    if not cat_df.empty:
        # График категорий
        fig = px.scatter(cat_df, x='total_interactions', y='purchases',
                        size='avg_price', hover_name='_id',
                        title='Анализ категорий товаров',
                        labels={
                            'total_interactions': 'Всего взаимодействий',
                            'purchases': 'Покупки'
                        })
        fig.show()
    
    # 3. Конверсия по устройствам
    pipeline_devices = [
        {"$group": {
            "_id": "$context.device",
            "views": {
                "$sum": {"$cond": [{"$eq": ["$interaction_type", "view"]}, 1, 0]}
            },
            "purchases": {
                "$sum": {"$cond": [{"$eq": ["$interaction_type", "purchase"]}, 1, 0]}
            }
        }},
        {"$addFields": {
            "conversion_rate": {
                "$cond": [
                    {"$gt": ["$views", 0]},
                    {"$divide": ["$purchases", "$views"]},
                    0
                ]
            }
        }}
    ]
    
    device_data = list(collection.aggregate(pipeline_devices))
    device_df = pd.DataFrame(device_data)
    
    if not device_df.empty:
        # График конверсии
        fig, ax = plt.subplots(figsize=(10, 6))
        x = range(len(device_df))
        
        ax.bar([i-0.2 for i in x], device_df['views'], width=0.4, 
               label='Просмотры', alpha=0.7)
        ax.bar([i+0.2 for i in x], device_df['purchases'], width=0.4, 
               label='Покупки', alpha=0.7)
        
        ax.set_xlabel('Устройство')
        ax.set_ylabel('Количество')
        ax.set_title('Просмотры vs Покупки по устройствам')
        ax.set_xticks(x)
        ax.set_xticklabels(device_df['_id'])
        ax.legend()
        
        # Добавляем линию конверсии
        ax2 = ax.twinx()
        ax2.plot(x, device_df['conversion_rate'], 'ro-', label='Конверсия')
        ax2.set_ylabel('Коэффициент конверсии')
        ax2.legend(loc='upper right')
        
        plt.tight_layout()
        plt.show()

create_analytics_dashboard()

# =============================================================================
# 🎮 ИНТЕРАКТИВНЫЕ ФУНКЦИИ
# =============================================================================

def interactive_recommendations():
    """Интерактивное получение рекомендаций"""
    
    print("🎮 ИНТЕРАКТИВНЫЕ РЕКОМЕНДАЦИИ\n" + "="*50)
    
    # Получаем список пользователей
    users = collection.distinct("user_id")[:10]  # Первые 10
    print(f"📋 Доступные пользователи: {users[:5]}...")
    
    # Получаем список товаров
    items = collection.distinct("item_id")[:10]  # Первые 10
    print(f"📦 Доступные товары: {items[:5]}...")
    
    # Получаем список категорий
    categories = collection.distinct("item_details.category")
    print(f"🏷️  Доступные категории: {categories}")
    
    return {
        'users': users,
        'items': items,
        'categories': categories
    }

available_data = interactive_recommendations()

# Функция для быстрого получения рекомендаций
def quick_recommend(user_id=None, item_id=None, category=None):
    """Быстрое получение рекомендаций"""
    
    print(f"\n🚀 БЫСТРЫЕ РЕКОМЕНДАЦИИ")
    print("="*30)
    
    if user_id:
        print(f"👤 Для пользователя {user_id}:")
        recs = recommender.get_user_recommendations(user_id, limit=3)
        if not recs.empty:
            print(recs[['_id', 'category', 'brand']].to_string(index=False))
        else:
            print("   Нет рекомендаций")
    
    if item_id:
        print(f"\n📦 Похожие на {item_id}:")
        similar = recommender.get_similar_items(item_id, limit=3)
        if not similar.empty:
            print(similar[['_id', 'category', 'brand']].to_string(index=False))
        else:
            print("   Нет похожих товаров")
    
    if category:
        print(f"\n🏷️  Популярные в категории {category}:")
        popular = recommender.get_popular_items(category, limit=3)
        if not popular.empty:
            print(popular[['_id', 'brand', 'popularity_score']].to_string(index=False))
        else:
            print("   Нет популярных товаров")

# Пример использования
print("\n" + "="*60)
print("💡 ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ:")
print("="*60)
print("quick_recommend(user_id='user_1')  # Рекомендации для пользователя")
print("quick_recommend(item_id='item_5')  # Похожие товары") 
print("quick_recommend(category='electronics')  # Популярные в категории")
print("quick_recommend(user_id='user_2', category='clothing')  # Комбинированный запрос")

# Демонстрация
quick_recommend(user_id='user_1', item_id='item_5', category='electronics')