# Работа с MongoDB

В этом семинаре научимся использовать базу данных MongoDB NoSQL.

Предполагаем, что платформа, описанная [здесь](../01-environment), запущена и доступна.

## Подключение к среде MongoDB

### Использование утилиты командной строки MongoDB

Можно найти утилиту командной строки `mongo` внутри контейнера Docker MongoDB, работающего как часть платформы. Подключитесь к хосту Docker и выполните следующую команду `docker exec`

```
sudo docker exec -ti mongo-1 mongosh -u "root" -p "abc123!"
```

Это позволит вам подключиться к контейнеру `mongo` и запустить оболочку `mongo` внутри него.

Вы должны увидеть вывод, аналогичный приведенному ниже.

```bash
bigdata@bigdata:~$ docker exec -ti mongo-1 mongosh -u "root" -p "abc123!"
Current Mongosh Log ID: 67b215162e08a3633d544ca6
Connecting to:          mongodb://<credentials>@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.3.8
Using MongoDB:          7.0.16
Using Mongosh:          2.3.8

For mongosh info see: https://www.mongodb.com/docs/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

------
   The server generated these startup warnings when booting
   2025-02-16T16:10:32.061+00:00: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
   2025-02-16T16:10:33.459+00:00: vm.max_map_count is too low
------

test> 

```

Теперь вы находитесь в командной строке MongoDB, готовой к выполнению любых операторов MongoDB. Также можно увидеть версию сервера MongoDB и оболочки MongoDB.

Оболочка запускает JavaScript. Есть несколько глобальных команд, которые вы можете выполнить, например help или exit. Команды, которые вы выполняете для текущей базы данных, выполняются для объекта db, например `db.help()` или `db.stats()`.

Команды, которые выполняются для определенной коллекции, выполняются для объекта `db.COLLECTION_NAME`, например `db.movies.help()` или `db.movies.countDocuments()`.

Выполнив команду `db.help()`,  получите список команд, которые вы можете выполнить для объекта db.

**Примечание:** Поскольку это оболочка JavaScript, если выполните метод и опустите скобки (),  увидите тело метода, а не выполнение метода. Первый раз, когда выполните запрос и получите ответ, который начинается с function (...){, вас это не удивляло. Например, если  введете db.help (без скобок),  увидите внутреннюю реализацию метода help.

### Использование браузерного графического интерфейса

Вместо работы в командной строке и, следовательно, необходимости подключаться к Docker Host, можем использовать браузерный графический интерфейс для доступа к MongoDB. В рамках платформы доступны две браузерные утилиты.

#### Mongo Express

Первый — [Mongo Express](https://github.com/mongo-express/mongo-express), веб-интерфейс администратора MongoDB, написанный с помощью Node.js, Express и Bootstrap3.

В окне браузера перейдите на <http://localhost:28203/>, с именем пользователя `admin` и паролем `pass`, переходим на главный экран, как показано ниже.

![Alt ​​Image Text](./images/mongo-express-home.png "Mongo Express")

#### Admin Mongo
Второй — [Admin Mongo](https://github.com/adicom-systems/adminMongo), открытый исходный интерфейс администратора для MongoDB.

В окне браузера перейдите на <http://localhost:28204/> и войдите с именем пользователя `admin` и паролем `pass`, и вы должны увидеть главный экран, как показано ниже.

![Alt ​​Image Text](./images/admin-mongo-home.png "Admin Mongo")

Чтобы подключиться к экземпляру MongoDB, добавьте новое подключение к Admin Mongo. Введите `Data Platform` в поле **Имя подключения** и `mongodb://mongo-1:27017` в поле **Строка подключения** и нажмите **Добавить подключение**. Должно появиться сообщение о том, что подключение было успешно добавлено.

![Alt ​​Image Text](./images/admin-mongo-connection.png "Admin Mongo Connection")

Нажатие кнопки **Подключить** открывает страницу сведений об администрировании Mongo для подключения.

### Использование настольных приложений

Существуют также различные настольные приложения для управления и администрирования MongoDB, которые можно загрузить и установить на рабочем столе, например `Mongo Compass`. Оттуда можете подключиться как к локальному, так и к удаленному экземпляру Mongo.

#### Studio 3T (ранее известная как Robo 3T или Robomongo)

[Studio 3T](https://robomongo.org/) - приложение, встраивающее оболочку MongoDB. Оно доступно для Windows, Mac и Linux.

![Alt ​​Image Text](./images/studio3T.png "Studio 3T")

Нажмите на значок **Подключить** в левом верхнем углу и нажмите **Новое подключение**, чтобы создать новое подключение.

Введите `NosqlPlatform` или IP-адрес вашего Docker Host в поле **Сервер**. Оставьте порт 27017 и нажмите **Сохранить**. Выбрав только что созданное подключение, нажмите **Подключить**. С правой стороны должны увидеть список доступных баз данных.

## Работа с MongoDB

Рассмотрим основные механизмы работы с MongoDB. Это основа для понимания MongoDB.

 # 6 Основных Концепций MongoDB

## 1. База данных (Database)
- 📁 Верхний уровень организации данных
- 💾 Аналог схемы в традиционных СУБД
- 🔍 Содержит коллекции данных
- ⚡ В одном экземпляре MongoDB может быть несколько баз данных

## 2. Коллекции (Collections)
- 📊 Аналог таблиц в реляционных БД
- 📝 Группа связанных документов
- 🔄 Динамическая схема
- 💡 Пример: `users`, `products`, `orders`

## 3. Документы (Documents)
- 📄 Аналог строк в таблице
- 🔠 Хранятся в формате BSON
- 📌 Каждый документ имеет уникальный `_id`
- ✨ Пример:
```json
{
    "_id": ObjectId("5099803df3f4948bd2f98391"),
    "name": "iPhone",
    "price": 699,
    "category": "Electronics"
}
```

## 4. Поля (Fields)
- 📋 Аналог столбцов в таблице
- 🔤 Могут содержать различные типы данных
- 🔗 Поддерживают вложенные структуры
- 🎯 Пример:
```json
{
    "name": "String",
    "age": "Number",
    "address": {
        "street": "String",
        "city": "String"
    },
    "hobbies": ["Array", "of", "Strings"]
}
```

## 5. Индексы (Indexes)
- 🚀 Ускоряют поиск документов
- 📑 Поддерживают различные типы индексов
- ⚠️ Влияют на производительность записи
- 💻 Пример создания:
```javascript
db.collection.createIndex({ "field": 1 })  // 1 для возрастания, -1 для убывания
```

## 6. Курсоры (Cursors)
- 👆 Указатель на результат запроса
- 🔄 Позволяют итерировать по результатам
- 📊 Поддерживают методы обработки данных
- 🎮 Пример использования:
```javascript
const cursor = db.collection.find()
cursor.forEach(doc => {
    console.log(doc)
})
```

### Практический пример всех концепций:
```javascript
// База данных: shop
use shop

// Коллекция: products
db.products.insertOne({
    name: "Laptop",
    price: 999.99,
    specs: {
        cpu: "Intel i7",
        ram: "16GB",
        storage: "512GB SSD"
    },
    tags: ["electronics", "computers"]
})

// Создание индекса
db.products.createIndex({ "name": 1 })

// Использование курсора
const cursor = db.products.find({ price: { $gt: 500 } })
while(cursor.hasNext()) {
    printjson(cursor.next())
}
```

### Важные замечания:
- 🔑 Каждый документ должен иметь уникальный `_id`
- 📈 Индексы улучшают чтение, но замедляют запись
- 🔄 Курсоры автоматически закрываются через 10 минут
- 📝 Коллекции не требуют предварительного определения схемы
- 💡 MongoDB оптимизирована для частых операций чтения/записи


 # Структура и Терминология MongoDB

## Основная Структура
```mermaid
graph TD
    A[База данных] --> B[Коллекции]
    B --> C[Документы]
    C --> D[Поля]
    B --> E[Индексы]
    C --> F[Курсоры]
```

## Сравнение с Реляционными БД

| MongoDB | Реляционные БД | Ключевое отличие |
|---------|----------------|------------------|
| База данных | База данных | Аналогичны |
| Коллекция | Таблица | Коллекция не имеет фиксированной схемы |
| Документ | Строка | Документ может иметь уникальную структуру |
| Поле | Столбец | Поля определяются на уровне документа |

## Практический Пример
```javascript
// Переключение на базу данных
use filmdb

// Проверка существующих коллекций
db.getCollectionNames()  // Вернёт: []

// Создание документа в новой коллекции
db.movies.insertOne({
    title: "Inception",
    year: 2010,
    director: "Christopher Nolan",
    genres: ["Sci-Fi", "Action"],
    ratings: {
        imdb: 8.8,
        metacritic: 74
    }
})
```

## Важные Особенности

### Гибкая Схема
- Каждый документ может иметь свою структуру
- Нет необходимости предварительно определять схему
- Можно добавлять новые поля "на лету"

### Создание Структур
```javascript
// Документ 1
{
    title: "Inception",
    year: 2010
}

// Документ 2 в той же коллекции
{
    title: "The Matrix",
    director: "Wachowski",
    cast: ["Keanu Reeves", "Laurence Fishburne"]
}
```

### Работа с Данными
```javascript
// Создание индекса
db.movies.createIndex({ "title": 1 })

// Использование курсора
const movieCursor = db.movies.find()
while(movieCursor.hasNext()) {
    printjson(movieCursor.next())
}
```

## Примечания
1. База данных создаётся автоматически при создании первой коллекции
2. Коллекции создаются автоматически при добавлении первого документа
3. Каждый документ может иметь свой набор полей
4. Курсоры оптимизируют работу с большими наборами данных

### Команды для Начала Работы
```javascript
use filmdb                    // Переключение/создание БД
db.getCollectionNames()       // Список коллекций
db.movies.insertOne({...})    // Добавление документа
```

 # Практическая работа 1. Создание документов в MongoDB
 
## 1. Подключение к существующей MongoDB
1. Откройте `MongoDB Compass`
2. В поле URI введите:
```
mongodb://root:abc123!@localhost:27017
```
ИЛИ заполните поля отдельно:
- Hostname: `localhost`
- Port: `27017`
- Authentication: `Username/Password`
- Username: `root`
- Password: `abc123!`

3. Нажмите "Connect"

## 2. После успешного подключения
1. Вы увидите список баз данных
2. Создадим новую базу данных:
   - Нажмите "Create Database"
   - Database Name: `filmdb`
   - Collection Name: `movies`
   - Нажмите "Create Database"

## 3. Вставка Документа в MongoDB Compass. Вставка документа фильма в коллекцию `movies`

### Структура документа `movies`
```javascript
{
    // Основная информация
    "id": String,            // ID фильма
    "title": String,         // Название
    "year": Number,          // Год выпуска
    "runtime": Number,       // Продолжительность в минутах
    
    // Массивы данных
    "languages": [String],   // Список языков
    "genres": [String],      // Список жанров
    
    // Рейтинги
    "rating": Number,        // Оценка
    "votes": Number,         // Количество голосов
    
    // Текстовое описание
    "plotOutline": String,   // Сюжет
    
    // Медиа
    "coverUrl": String,      // URL постера
    
    // Вложенные массивы объектов
    "actors": [{             // Актёры
        "actorID": String,
        "name": String
    }],
    "directors": [{          // Режиссёры
        "directorID": String,
        "name": String
    }],
    "producers": [{          // Продюсеры
        "producerID": String,
        "name": String
    }]
}
```

## 3.1. Создание Документа
1. В MongoDB Compass:
   - Выберите базу данных `filmdb`
   - Выберите коллекцию `movies`
   - Нажмите "Add Data" → "Insert Document"

2. В окне редактора вставьте JSON:
```json
{ 
    "id": "0110912", 
    "title": "Pulp Fiction",
    "year": 1994,
    "runtime": 154,
    "languages": ["en", "es", "fr"],
    "rating": 8.9,
    "votes": 2084331,
    "genres": ["Crime", "Drama"],
    "plotOutline": "Jules Winnfield (Samuel L. Jackson) and Vincent Vega (John Travolta) are two hit men who are out to retrieve a suitcase stolen from their employer, mob boss Marsellus Wallace (Ving Rhames). Wallace has also asked Vincent to take his wife Mia (Uma Thurman) out a few days later when Wallace himself will be out of town. Butch Coolidge (Bruce Willis) is an aging boxer who is paid by Wallace to lose his fight. The lives of these seemingly unrelated people are woven together comprising of a series of funny, bizarre and uncalled-for incidents.",
    "coverUrl": "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY150_CR1,0,101,150_.jpg",
    "actors": [
        { "actorID": "0000619", "name": "Tim Roth"},
        { "actorID": "0001625", "name": "Amanda Plummer"},    
        { "actorID": "0522503", "name": "Laura Lovelace"},         
        { "actorID": "0000237", "name": "John Travolta"},   
        { "actorID": "0000168", "name": "Samuel L. Jackson"},   
        { "actorID": "0482851", "name": "Phil LaMarr"},   
        { "actorID": "0001844", "name": "Frank Whaley"},  
        { "actorID": "0824882", "name": "Burr Steers"},  
        { "actorID": "0000246", "name": "Bruce Willis"}, 
        { "actorID": "0000609", "name": "Ving Rahmes"},         
        { "actorID": "0000235", "name": "Uma Thurman"},
        { "actorID": "0000233", "name": "Quentin Tarantino"}
    ],
    "directors": [
        { "directorID": "0000233", "name": "Quentin Tarantino"}
    ],
    "producers": [
        { "producerID": "0004744", "name": "Lawrence Bender"},
        { "producerID": "0000362", "name": "Danny DeVito"},
        { "producerID": "0321621", "name": "Richard N. Gladstein"},        
        { "producerID": "0787834", "name": "Michael Shamberg"},        
        { "producerID": "0792049", "name": "Stacey Sher"},  
        { "producerID": "0918424", "name": "Bob Weinstein"},  
        { "producerID": "0005544", "name": "Harvey Weinstein"}  
    ]
}
```

3. Нажмите "Insert"

## 4. Проверка Вставки
После вставки:
1. Обновите вид коллекции
2. Вы должны увидеть новый документ
3. MongoDB автоматически добавит поле `_id`

## 5. Структура Документа
Документ содержит:
- Простые поля (`id`, `title`, `year`, etc.)
- Массивы (`languages`, `genres`)
- Вложенные массивы объектов (`actors`, `directors`, `producers`)

## 6. Поиск Документа
В Compass:
1. Перейдите во вкладку "Find"
2. Введите фильтр:
```json
{
  "title": "Pulp Fiction"
}
```
3. Нажмите "Find"

## 7. Возможные Проблемы
Если возникает ошибка:
- Проверьте формат JSON (все кавычки должны быть двойными)
- Убедитесь, что все скобки закрыты
- Проверьте, что нет trailing comma (запятой после последнего элемента)

## 8. Проверка данных
- В коллекции `movies` должен появиться новый документ
- Можно использовать вкладку "Find" для поиска данных
- Попробуйте фильтр: `{title: "Pulp Fiction"}`

## Дополнительно
- Используйте вкладку "Indexes" для создания индексов
- "Explain Plan" поможет оптимизировать запросы
- "Aggregation" для сложных запросов
- "Schema" покажет структуру документов

### Результат вставки
```javascript
{
    acknowledged: true,
    insertedId: ObjectId('66cb796c8137d3ecf9c76a8d')
}
```

## Важные моменты:
1. MongoDB автоматически создаёт `_id`, если не указан
2. Документ может содержать:
   - Простые типы (строки, числа)
   - Массивы
   - Вложенные объекты
   - Массивы объектов

## Проверка вставки
```javascript
// Поиск вставленного документа
db.movies.findOne({ "title": "Pulp Fiction" })

// Подсчёт документов в коллекции
db.movies.countDocuments()
```

## Примечания:
- `insertOne()` вставляет один документ
- Для вставки нескольких документов используйте `insertMany()`
- Коллекция создаётся автоматически при первой вставке
- Все поля в документе необязательны (гибкая схема)

В графических инструментах в большинстве случаев нужно только предоставить документ JSON, без указания команды `db.movies.insertOne()`.

Приведенная выше строка выполняет вставку в коллекцию **movies**, передавая ей один параметр. Внутри MongoDB использует двоичный сериализованный формат JSON, называемый BSON. Внешне это означает, что мы часто используем JSON, как и в случае с нашими параметрами.

Давайте также добавим фильм "The Matrix"

```javascript
db.movies.insertOne(
{ 
    "id": "0133093", 
    "title": "The Matrix",
    "year": 1999,
    "runtime": 136,
    "languages": ["en"],
    "rating": 8.7,
    "votes": 1496538,
    "genres": ["Action", "Sci-Fi"],
    "plotOutline": "Thomas A. Anderson is a man living two lives. By day he is an average computer programmer and by night a hacker known as Neo. Neo has always questioned his reality, but the truth is far beyond his imagination. Neo finds himself targeted by the police when he is contacted by Morpheus, a legendary computer hacker branded a terrorist by the government. Morpheus awakens Neo to the real world, a ravaged wasteland where most of humanity have been captured by a race of machines that live off of the humans' body heat and electrochemical energy and who imprison their minds within an artificial reality known as the Matrix. As a rebel against the machines, Neo must return to the Matrix and confront the agents: super-powerful computer programs devoted to snuffing out Neo and the entire human rebellion.",
    "coverUrl": "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX101_CR0,0,101,150_.jpg",
    "actors": [
        { "actorID": "0000206", "name": "Keanu Reeves"},
        { "actorID": "0000401", "name": "Laurence Fishburne"},    
        { "actorID": "0005251", "name": "Carrie-Anne Moss"},         
        { "actorID": "0915989", "name": "Hugo Weaving"},   
        { "actorID": "0287825", "name": "Gloria Foster"},   
        { "actorID": "0001592", "name": "Joe Pantoliano"},   
        { "actorID": "0159059", "name": "Marcus Chong"},  
        { "actorID": "0032810", "name": "Julian Arahanga"},  
        { "actorID": "0000246", "name": "Bruce Willis"}, 
        { "actorID": "0000609", "name": "Ving Rahmes"},         
        { "actorID": "0000235", "name": "Uma Thurman"},
        { "actorID": "0000233", "name": "Quentin Tarantino"}
    ],
    "directors": [
        { "directorID": "0905154", "name": "Lana Wachowski"},
        { "directorID": "0905152", "name": "Lilly Wachowski"}
    ],
    "producers": [
        { "producerID": "0075732", "name": "Bruce Berman"},
        { "producerID": "0185621", "name": "Dan Cracchiolo"},
        { "producerID": "0400492", "name": "Carol Hughes"}  
    ]        
})
```

Если выполним `db.getCollectionNames()`  увидем коллекцию, в которую  только что добавили документы

```javascript
> db.getCollectionNames()
[ 'movies' ]
```

Теперь можно использовать команду `find` для коллекции **movies**, чтобы вернуть список документов:

```javascript
db.movies.find()
```

На самом деле выполняется оператор.

```javascript
db.movies.find({})
```

Пустой документ передается в качестве параметра. Этот документ позже будет содержать фактический запрос для выполнения ограничения на возвращаемые документы. Пустой документ просто означает возврат всех и является значением по умолчанию.

Чтобы отобразить результаты в отформатированном виде, используем метод `pretty()`

```javascript
db.movies.find().pretty()
```

Обратите внимание, что в дополнение к указанным данным есть поле `_id`. Каждый документ должен иметь уникальное поле идентификатора.
Можно сгенерировать его самостоятельно, либо разрешить MongoDB сгенерировать значение, которое имеет тип `ObjectId`. В большинстве случаев MongoDB автоматически генерирует. По умолчанию поле `_id` индексируется, что можно проверить с помощью команды `db.persons.getIndexes()`

```javascript
> db.movies.getIndexes()
[ { "v" : 2, "key" : { "_id" : 1 }, "name" : "_id_" } ]
```

Видно имя индекса, базу данных и коллекцию, в которой он был создан, а также поля, включенные в индекс.


## Создание документов актеров в коллекции `persons`

Добавим несколько актеров в  новую коллекцию с именем `persons`. Один и тот же человек может иметь разные роли в одном или нескольких фильмах.

Давайте сначала добавим актера "Bruce Willis"

```javascript
db.persons.insertOne (
{ 
    "id": 0000246, 
    "name": "Bruce Willis",
    "headshot": "https://m.media-amazon.com/images/M/MV5BMjA0MjMzMTE5OF5BMl5BanBnXkFtZTcwMzQ2ODE3Mw@@._V1_UY98_CR8,0,67,98_AL_.jpg",
    "birthDate": "1955-03-19",
    "tradeMarks": ['Frequently plays a man who suffered a tragedy, had lost something or had a  crisis of confidence or conscience.',
					  'Frequently plays likeable wisecracking heroes with a moral centre',
					  'Headlines action-adventures, often playing a policeman, hitman or someone in the military',
					  'Often plays men who get caught up in situations far beyond their control',
					  'Sardonic one-liners',
					  'Shaven head',
					  'Distinctive, gravelly voice',
					  'Smirky grin.',
					  'Known for playing cynical anti-heroes with unhappy personal lives'],
    "actedInMovies": [
        { "movieId": "0110912", "title": "Pulp Fiction"},
        { "movieId": "1606378", "title": "A Good Day to Die Hard"},
        { "movieId": "0217869", "title": "Unbreakable"},
        { "movieId": "0377917", "title": "The Fifth Element"},
        { "movieId": "0112864", "title": "Die Hard: With a Vengeance"}
    ]        
})
```

затем добавьте актера "Keanu Reeves"

```javascript
db.persons.insertOne (
{ 
    "id": 0000206, 
    "name": "Keanu Reeves",
    "headshot": "https://m.media-amazon.com/images/M/MV5BMjA0MjMzMTE5OF5BMl5BanBnXkFtZTcwMzQ2ODE3Mw@@._V1_UY98_CR8,0,67,98_AL_.jpg",
    "birthDate": "1955-03-19",
    "tradeMarks": ['Intense contemplative gaze',
		  'Deep husky voice',
		  'Known for playing stoic reserved characters'],
    "actedInMovies": [
        { "movieId": "0133093", "title": "The Matrix"},
        { "movieId": "0234215", "title": "The Matrix Reloaded"},
        { "movieId": "0111257", "title": "Speed"}
    ]        
})
```

 актрису "Sandra Bullock"

```javascript
db.persons.insertOne (
{ 
    "id": 0000113, 
    "name": "Sandra Bullock",
    "headshot": "https://m.media-amazon.com/images/M/MV5BMTI5NDY5NjU3NF5BMl5BanBnXkFtZTcwMzQ0MTMyMw@@._V1_UX67_CR0,0,67,98_AL_.jpg",
    "birthDate": "1964-07-26",
    "actedInMovies": [
        { "movieId": "2737304", "title": "Bird Box"},
        { "movieId": "0120179", "title": "Speed 2: Cruise Control"},
        { "movieId": "0111257", "title": "Speed"},
        { "movieId": "0212346", "title": "Miss Congeniality"}
    ]        
})
```

и наконец  добавляем "Quentin Tarantino"

```javascript
db.persons.insertOne (
{ 
    "id": 0000233, 
    "name": "Quentin Tarantino",
    "headshot": "https://m.media-amazon.com/images/M/MV5BMTgyMjI3ODA3Nl5BMl5BanBnXkFtZTcwNzY2MDYxOQ@@._V1_UX67_CR0,0,67,98_AL_.jpg",
    "birthDate": "1963-03-27",
    "tradeMarks": ['Lead characters usually drive General Motors vehicles, particularly Chevrolet and Cadillac, such as Jules 1974 Nova and Vincents 1960s Malibu.',
          'Briefcases and suitcases play an important role in Pulp Fiction (1994), Reservoir Dogs (1992), Jackie Brown (1997), True Romance (1993) and Kill Bill: Vol. 2 (2004).',
          'Makes references to cult movies and television',
          'Frequently works with Harvey Keitel, Tim Roth, Michael Madsen, Uma Thurman, Michael Bowen, Samuel L. Jackson, Michael Parks and Christoph Waltz.',
          'His films usually have a shot from inside an automobile trunk',
          'He always has a Dutch element in his films: The opening tune, Little Green Bag, in Reservoir Dogs (1992) was performed by George Baker Selection and written by Jan Gerbrand Visser and Benjamino Bouwens who are all Dutch. The character Freddy Newandyke, played by Tim Roth is a direct translation to a typical Dutch last name, Nieuwendijk. The code name of Tim Roth is Mr. Orange, the royal color of Holland and the last name of the royal family. The Amsterdam conversation in Pulp Fiction (1994), Vincent Vega smokes from a Dutch tobacco shag (Drum), the mentioning of Rutger Hauer in Jackie Brown (1997), the brides name is Beatrix, the name of the Royal Dutch Queen.',
		  '[The Mexican Standoff] All his movies (including True Romance (1993), which he only wrote and did not direct) feature a scene in which three or more characters are pointing guns at each other at the same time.',
         'Often uses an unconventional storytelling device in his films, such as retrospect (Reservoir Dogs (1992)), non-linear (Pulp Fiction (1994)), or "chapter" format (Kill Bill: Vol. 1 (2003)).',
         'His films will often include one long, unbroken take where a character is  followed around somewhere.'],
    "actedInMovies": [
        { "movieId": "0378194", "title": "Kill Bill: Vol. 2"},
        { "movieId": "0110912", "title": "Speed 2: Cruise Control"},
        { "movieId": "0116367", "title": "From Dusk Till Dawn"},
        { "movieId": "0119396", "title": "Jackie Brown"}
    ]        
})
```

Теперь давайте также проверим, что все 4 человека добавлены в коллекцию

```javascript
db.persons.find()
```

Использовать метод `countDocuments()`, чтобы вернуть количество документов в коллекции.

```javascript
db.persons.find().count()
```

или метод `estimatedDocumentCount()` для получения предполагаемого количества (на основе метаданных)

```javascript
db.persons.estimatedDocumentCount()
```

Что в этом случае (поскольку мы не указываем селектор запроса) то же самое, что и

```javascript
db.persons.countDocuments()
```

**Примечание:** обратите внимание, что не все документы абсолютно одинаковы. Документ «Сандра Буллок» не содержит массив `tradeMark`. Коллекции не содержат схемы, выполняется только парсинг JSON, поэтому документ должен быть допустимым JSON. Давайте посмотрим, что произойдет, если  используем недопустимый документ.

```javascript
db.persons.insertOne (
{
"id: 0000113,
"name": "Invalid Actor"
})
```

Обратите внимание, что мы не закрыли должным образом ключ `id` (missing  "). При вставке  получим следующую ошибку

```json
> db.persons.insertOne (
... {
...     "id: 0000113,
Uncaught:
SyntaxError: Unterminated string constant. (3:4)

  1 | db.persons.insertOne (
  2 | {
> 3 |     "id: 0000113,
    |     ^
  4 |

filmdb>     "name": "Invalid Actor"
Uncaught:
SyntaxError: Missing semicolon. (1:10)

> 1 |     "name": "Invalid Actor"
    |           ^
  2 |
```

Таким образом, хотя документы в одной коллекции могут полностью отличаться от других документов в этой коллекции, они всегда должны быть допустимыми документами JSON.

## Запрос документов с помощью селектора запросов

До сих пор использовали `find` для извлечения всех документов в коллекции. Это нормально, если у вас ограниченный набор документов, как здесь, но, конечно, если у вас миллион документов, вам потребуется запрос на извлечение только некоторых документов.

В дополнение к шести концепциям, которые рассмотрели ранее, есть один практический аспект MongoDB, который нужно усвоить, прежде чем переходить к более сложным темам, **селекторы запросов**.

**селектор запросов** MongoDB похож на предложение where оператора SQL. Таким образом, вы используете его при поиске, счете, обновлении и удалении документов из коллекций. Селектор — это объект JSON, простейшим из которых является {}, который соответствует всем документам. Если бы  хотели найти все фильмы жанра боевик, могли бы использовать `{ geners:'Action' }`.

Прежде чем глубоко погружаться в селекторы, давайте настроим несколько дополнительных фильмов для игры. Будем использовать 50 лучших фильмов из IMDB, без двух фильмов, которые уже добавили ранее. Будем добавлять «полноценные» документы, мы только добавим ограниченную информацию для каждого фильма. Видим, что MongoDB «schema-less», в том смысле, что не все документы должны содержать всю информацию.

Используем метод `insertMany` для добавления нескольких документов JSON одновременно.

```javascript
db.movies.insertMany([
	{"id": "0111161", "title": "The Shawshank Redemption", "genres": ["Drama"], "year": 1994, "rating": 9.2, "rank": 1},
	{"id": "0068646", "title": "The Godfather", "genres": ["Crime", "Drama"], "year": 1972, "rating": 9.2, "rank": 2},
	{"id": "0071562", "title": "The Godfather: Part II", "genres": ["Crime", "Drama"], "year": 1974, "rating": 9.0, "rank": 3},
	{"id": "0468569", "title": "The Dark Knight", "genres": ["Action", "Crime", "Drama", "Thriller"], "year": 2008, "rating": 9.0, "rank": 4},
	{"id": "0050083", "title": "12 Angry Men", "genres": ["Drama"], "year": 1957, "rating": 8.9, "rank": 5},
	{"id": "0108052", "title": "Schindler's List", "genres": ["Biography", "Drama", "History"], "year": 1993, "rating": 8.9, "rank": 6},
	{"id": "0167260", "title": "The Lord of the Rings: The Return of the King", "genres": ["Adventure", "Drama", "Fantasy"], "year": 2003, "rating": 8.9, "rank": 7},
	{"id": "0060196", "title": "The Good, the Bad and the Ugly", "genres": ["Western"], "year": 1966, "rating": 8.8, "rank": 9},
	{"id": "0137523", "title": "Fight Club", "genres": ["Drama"], "year": 1999, "rating": 8.8, "rank": 10},
	{"id": "4154796", "title": "Avengers: Endgame", "genres": ["Action", "Adventure", "Fantasy", "Sci-Fi"], "year": 2019, "rating": 8.8, "rank": 11},
	{"id": "0120737", "title": "The Lord of the Rings: The Fellowship of the Ring", "genres": ["Adventure", "Drama", "Fantasy"], "year": 2001, "rating": 8.8, "rank": 12},
	{"id": "0109830", "title": "Forrest Gump", "genres": ["Drama", "Romance"], "year": 1994, "rating": 8.7, "rank": 13},
	{"id": "0080684", "title": "Star Wars: Episode V - The Empire Strikes Back", "genres": ["Action", "Adventure", "Fantasy", "Sci-Fi"], "year": 1980, "rating": 8.7, "rank": 14},
	{"id": "1375666", "title": "Inception", "genres": ["Action", "Adventure", "Sci-Fi", "Thriller"], "year": 2010, "rating": 8.7, "rank": 15},
	{"id": "0167261", "title": "The Lord of the Rings: The Two Towers", "genres": ["Adventure", "Drama", "Fantasy"], "year": 2002, "rating": 8.7, "rank": 16},
	{"id": "0073486", "title": "One Flew Over the Cuckoo's Nest", "genres": ["Drama"], "year": 1975, "rating": 8.7, "rank": 17},
	{"id": "0099685", "title": "Goodfellas", "genres": ["Biography", "Crime", "Drama"], "year": 1990, "rating": 8.7, "rank": 18},
	{"id": "0047478", "title": "Seven Samurai", "genres": ["Adventure", "Drama"], "year": 1954, "rating": 8.6, "rank": 20},
	{"id": "0114369", "title": "Se7en", "genres": ["Crime", "Drama", "Mystery", "Thriller"], "year": 1995, "rating": 8.6, "rank": 21},
	{"id": "0317248", "title": "City of God", "genres": ["Crime", "Drama"], "year": 2002, "rating": 8.6, "rank": 22},
	{"id": "0076759", "title": "Star Wars: Episode IV - A New Hope", "genres": ["Action", "Adventure", "Fantasy", "Sci-Fi"], "year": 1977, "rating": 8.6, "rank": 23},
	{"id": "0102926", "title": "The Silence of the Lambs", "genres": ["Crime", "Drama", "Thriller"], "year": 1991, "rating": 8.6, "rank": 24},
	{"id": "0038650", "title": "It's a Wonderful Life", "genres": ["Drama", "Family", "Fantasy"], "year": 1946, "rating": 8.6, "rank": 25},
	{"id": "0118799", "title": "Life Is Beautiful", "genres": ["Comedy", "Drama", "Romance", "War"], "year": 1997, "rating": 8.6, "rank": 26},
	{"id": "0245429", "title": "Spirited Away", "genres": ["Animation", "Adventure", "Family", "Fantasy", "Mystery"], "year": 2001, "rating": 8.5, "rank": 27},
	{"id": "0120815", "title": "Saving Private Ryan", "genres": ["Drama", "War"], "year": 1998, "rating": 8.5, "rank": 28},
	{"id": "0114814", "title": "The Usual Suspects", "genres": ["Crime", "Mystery", "Thriller"], "year": 1995, "rating": 8.5, "rank": 29},
	{"id": "0110413", "title": "L\u00e9on: The Professional", "genres": ["Action", "Crime", "Drama", "Thriller"], "year": 1994, "rating": 8.5, "rank": 30},
	{"id": "0120689", "title": "The Green Mile", "genres": ["Crime", "Drama", "Fantasy", "Mystery"], "year": 1999, "rating": 8.5, "rank": 31},
	{"id": "0816692", "title": "Interstellar", "genres": ["Adventure", "Drama", "Sci-Fi"], "year": 2014, "rating": 8.5, "rank": 32},
	{"id": "0054215", "title": "Psycho", "genres": ["Horror", "Mystery", "Thriller"], "year": 1960, "rating": 8.5, "rank": 33},
	{"id": "0120586", "title": "American History X", "genres": ["Drama"], "year": 1998, "rating": 8.5, "rank": 34},
	{"id": "0021749", "title": "City Lights", "genres": ["Comedy", "Drama", "Romance"], "year": 1931, "rating": 8.5, "rank": 35},
	{"id": "0034583", "title": "Casablanca", "genres": ["Drama", "Romance", "War"], "year": 1942, "rating": 8.5, "rank": 36},
	{"id": "0064116", "title": "Once Upon a Time in the West", "genres": ["Western"], "year": 1968, "rating": 8.5, "rank": 37},
	{"id": "0253474", "title": "The Pianist", "genres": ["Biography", "Drama", "Music", "War"], "year": 2002, "rating": 8.5, "rank": 38},
	{"id": "0027977", "title": "Modern Times", "genres": ["Comedy", "Drama", "Family", "Romance"], "year": 1936, "rating": 8.5, "rank": 39},
	{"id": "1675434", "title": "The Intouchables", "genres": ["Biography", "Comedy", "Drama"], "year": 2011, "rating": 8.5, "rank": 40},
	{"id": "0407887", "title": "The Departed", "genres": ["Crime", "Drama", "Thriller"], "year": 2006, "rating": 8.5, "rank": 41},
	{"id": "0088763", "title": "Back to the Future", "genres": ["Adventure", "Comedy", "Sci-Fi"], "year": 1985, "rating": 8.5, "rank": 42},
	{"id": "0103064", "title": "Terminator 2: Judgment Day", "genres": ["Action", "Sci-Fi"], "year": 1991, "rating": 8.5, "rank": 43},
	{"id": "2582802", "title": "Whiplash", "genres": ["Drama", "Music"], "year": 2014, "rating": 8.5, "rank": 44},
	{"id": "0110357", "title": "The Lion King", "genres": ["Animation", "Adventure", "Drama", "Family", "Musical"], "year": 1994, "rating": 8.5, "rank": 45},
	{"id": "0047396", "title": "Rear Window", "genres": ["Mystery", "Thriller"], "year": 1954, "rating": 8.5, "rank": 46},
	{"id": "0082971", "title": "Raiders of the Lost Ark", "genres": ["Action", "Adventure"], "year": 1981, "rating": 8.5, "rank": 47},
	{"id": "0172495", "title": "Gladiator", "genres": ["Action", "Adventure", "Drama"], "year": 2000, "rating": 8.5, "rank": 48},
	{"id": "0482571", "title": "The Prestige", "genres": ["Drama", "Mystery", "Sci-Fi", "Thriller"], "year": 2006, "rating": 8.5, "rank": 49},
	{"id": "0078788", "title": "Apocalypse Now", "genres": ["Drama", "War"], "year": 1979, "rating": 8.4, "rank": 50}
])
```

После выполнения мультивставки можем убедиться, что в нашей коллекции `movies` на самом деле имеется 50 фильмов.

```javascript
> db.movies.find().count()
50 
```
 
Теперь, когда у нас есть данные,  можем освоить селекторы. `{field: value}` используется для поиска любых документов, где поле равно значению. `{field1: value1, field2: value2}` — это то, как мы можем объединить их с семантикой **and**.
Специальные `$lt`, `$lte`, `$gt`, `$gte` и `$ne` используются для операций меньше, меньше или равно, больше, больше или равно и не равно.

Чтобы получить все Family фильмы, можем выполнить

```javascript
db.movies.find({"genres": "Family"})
```

Если  хотим получить все фильмы, которые были опубликованы в 2010 году и позже, мы можем сделать следующее:

```javascript
db.movies.find({"genres":"Action", "year": { $gte :  2010 } })
```

Чтобы найти все фильмы, которые **not** относятся к жанру **Drama**

```javascript
db.movies.find({"genres": { $ne: "Drama"} })
```

Оператор `$exists` может использоваться для проверки наличия или отсутствия поля.

```javascript
db.movies.find({ "plotOutline": { $exists: true} })
```

мы видим, что только два фильма имеют установленное свойство `plotOutline`.

Оператор `$in` можно использовать для сопоставления одного из нескольких значений, которые мы передаем как массив.

```javascript
db.movies.find({ "genres": { $in: ['Family', 'Mistery']} })
```

который возвращает все фильмы в жанре `Family` или `Mistery`.

Если  хотим использовать логическое ИЛИ (OR) вместо И (AND) для нескольких условий на разных полях, мы используем оператор $or, которому передаем массив селекторов, которые нужно объединить через ИЛИ.

 Чтобы найти все фильмы жанра *Music* **OR** которые были выпущены в *2012* году или позже

```javascript
db.movies.find({ $or: [ { "genres":"Music" },  { "year": { $gte :  2012 } } ] })
```

Чтобы найти все фильмы жанра *Action* **AND** которые были выпущены в *2010* году или позже **OR** имеют рейтинг выше *8.8*

```javascript
db.movies.find({ "genres":"Action", $or: [ { "year": { $gte :  2010 } },  { "rating": { $gt :  8.8 } } ] })
```

В наших последних двух примерах есть что-то довольно интересное. Возможно, вы уже заметили, но поле `genres` является массивом. MongoDB поддерживает массивы как объекты первого класса. Это невероятно удобная функция. Когда вы начинаете ее использовать, вы задаетесь вопросом, как вы жили без нее. Что еще интереснее, так это то, насколько просто выполнять выборку на основе значения массива: `{ genres: 'Action' }` вернет любой документ, где в genres есть значение `Action`.

Существует больше доступных операторов, чем мы видели до сих пор. Все они описаны в разделе [Query Selectors](https://docs.mongodb.com/manual/reference/operator/query/index.html) руководства MongoDB. То, что мы рассмотрели до сих пор - это основы, которые вам понадобятся для начала работы. Это также то, что вы будете использовать чаще всего.

Мы видели, как эти селекторы можно использовать с командой `find`. Но их также можно использовать с командой `remove`, командой `count` и командой `update`, которым мы уделим больше внимания позже.

`ObjectId`, который MongoDB сгенерировал для нашего поля `_id`, можно выбрать следующим образом:

```javascript
db.movies.find( {_id: ObjectId("<the-object-id>")})
```

Убедитесь, что вы заменили `<the-object-id>` на фактическое значение одного из фильмов, которые вы вставили ранее.

 ## Обновление документов

В своей простейшей форме `updateOne()` принимает два параметра: селектор (where) для использования и обновления, которые нужно применить к полям. Допустим, мы хотим изменить рейтинг фильма `Fight Club` на `9`

```javascript
db.movies.updateOne ( {title: 'Fight Club'} , { $set: {rating: 9} } )
```

Помимо `$set`, мы можем использовать другие операторы для выполнения некоторых полезных операций. Все операторы обновления работают с полями - поэтому ваш весь документ не будет стерт. Например, оператор `$inc` используется для увеличения поля на определенное положительное или отрицательное значение.

Если мы хотим увеличить количество голосов для фильма "The Matrix", которое в настоящее время установлено на `1496538`, как мы можем легко увидеть с помощью find

```javascript
db.movies.find( {title: 'The Matrix'}, {"votes":1})
```

*Примечание:* второй параметр в find указывает, что вместо полного документа мы хотим вернуть только свойство `votes`, как мы можем видеть в результате (_id всегда возвращается по умолчанию и может быть удален путем явного указания `{ _id:0}` во втором параметре).

```javascript
> db.movies.find( {title: 'The Matrix'}, {"votes":1})
{ "_id" : ObjectId("5ccffa52aff86ec587e35faa"), "votes" : 1496538 }
```

мы можем выполнить следующее обновление

```javascript
db.movies.updateOne( {title: 'The Matrix'} , { $inc: {votes: 1} } )
```
 Давайте разберем каждое поле в результате выполнения команды `updateOne`:

```json
{
  acknowledged: true,      // Подтверждение, что операция была принята сервером
  insertedId: null,       // null, так как это обновление, а не вставка
  matchedCount: 1,        // Найден 1 документ, соответствующий условию {title: 'The Matrix'}
  modifiedCount: 1,       // 1 документ был фактически изменен
  upsertedCount: 0        // 0 документов было создано (upsert = update + insert)
}
```

Подробнее о каждом поле:

1. `acknowledged: true` - MongoDB подтверждает, что операция была успешно получена и обработана сервером

2. `insertedId: null` - Поскольку это операция обновления, а не вставки, идентификатор нового документа отсутствует 

3. `matchedCount: 1` - Показывает, что был найден один документ, соответствующий условию поиска `{title: 'The Matrix'}`

4. `modifiedCount: 1` - Показывает, что один документ был фактически изменен (увеличено значение поля votes)

5. `upsertedCount: 0` - Показывает, что новые документы не создавались. Это имеет значение при использовании опции upsert, которая создает новый документ, если совпадений не найдено

В данном случае результат говорит нам, что операция успешно обновила один документ с названием "The Matrix", увеличив значение его поля votes на 1.

проверить новый результат, используя тот же find второй раз

```javascript
db.movies.find( {title: 'The Matrix'}, {"votes":1})
```

 ## Оптимизация производительности с помощью индексов

Индексы в MongoDB работают во многом как индексы в реляционной базе данных: они помогают улучшить производительность запросов и сортировки. Индексы создаются с помощью команды `createIndex`. Давайте добавим индекс по названию фильмов. Для возрастающего индекса по полю укажите значение `1`; для убывающего индекса укажите значение `-1`.

```javascript
db.movies.createIndex( {title: 1} );
```

если мы теперь выполним запрос по названию, будет использован индекс

```javascript
db.movies.find ( {title: "The Matrix"} );
```

Если бы у нас было гораздо больше данных в коллекции фильмов, мы могли бы увидеть визуальную разницу. Но с всего 50 фильмами это не так. Однако мы можем использовать метод `explain()` для просмотра плана выполнения оптимизатора.

Добавление метода `explain` в конце оператора find вернет следующий результат

```javascript
> db.movies.find ( {title: "The Matrix"} ).explain();
{
  explainVersion: '1',
  queryPlanner: {
    namespace: 'filmdb.movies',
    indexFilterSet: false,
    parsedQuery: { title: { '$eq': 'The Matrix' } },
    queryHash: '2495AF30',
    planCacheKey: 'D2B6550E',
    maxIndexedOrSolutionsReached: false,
    maxIndexedAndSolutionsReached: false,
    maxScansToExplodeReached: false,
    winningPlan: {
      stage: 'FETCH',
      inputStage: {
        stage: 'IXSCAN',
        keyPattern: { title: 1 },
        indexName: 'title_1',
        isMultiKey: false,
        multiKeyPaths: { title: [] },
        isUnique: false,
        isSparse: false,
        isPartial: false,
        indexVersion: 2,
        direction: 'forward',
        indexBounds: { title: [ '["The Matrix", "The Matrix"]' ] }
      }
    },
    rejectedPlans: []
  },
  command: { find: 'movies', filter: { title: 'The Matrix' }, '$db': 'filmdb' },
  serverInfo: {
    host: 'mongo-1',
    port: 27017,
    version: '7.0.12',
    gitVersion: 'b6513ce0781db6818e24619e8a461eae90bc94fc'
  },
  serverParameters: {
    internalQueryFacetBufferSizeBytes: 104857600,
    internalQueryFacetMaxOutputDocSizeBytes: 104857600,
    internalLookupStageIntermediateDocumentMaxSizeBytes: 104857600,
    internalDocumentSourceGroupMaxMemoryBytes: 104857600,
    internalQueryMaxBlockingSortMemoryUsageBytes: 104857600,
    internalQueryProhibitBlockingMergeOnMongoS: 0,
    internalQueryMaxAddToSetBytes: 104857600,
    internalDocumentSourceSetWindowFieldsMaxMemoryBytes: 104857600,
    internalQueryFrameworkControl: 'trySbeRestricted'
  },
  ok: 1
}
```

Мы можем видеть, что `winningPlan` использует индекс `title_1`.

Уникальный индекс может быть создан путем передачи второго параметра и установки `unique` в true. Давайте добавим индекс по полю `id`, чтобы убедиться, что оно уникально.

```javascript
db.movies.createIndex( {id: 1}, {unique: true} );
```

Если мы теперь попытаемся добавить один из фильмов второй раз, мы получим ошибку:

```javascript
> db.movies.insertOne( {"id": "0111161", "title": "The Shawshank Redemption", "genres": ["Drama"], "year": 1994, "rating": 9.2, "rank": 1} )
MongoServerError: E11000 duplicate key error collection: filmdb.movies index: id_1 dup key: { id: "0111161" }
```

Мы можем просмотреть индексы, которые у нас есть в настоящее время в коллекции `movies`, используя `db.movies.getIndexes()`:

```javascript
> db.movies.getIndexes()
[
  { v: 2, key: { _id: 1 }, name: '_id_' },
  { v: 2, key: { title: 1 }, name: 'title_1' },
  { v: 2, key: { id: 1 }, name: 'id_1', unique: true }
]
```

Мы можем видеть всего 3 индекса: два, которые мы только что добавили, и третий по полю `_id`, который был создан автоматически MongoDB.

Индекс может быть удален с помощью команды `dropIndex`.

```javascript
db.movies.dropIndex( {title: 1} );
```

Мы также можем создать **Составной** индекс, охватывающий несколько полей, создать **Многоключевой** индекс для индексации содержимого поля массива и создать **Геопространственные**, **Текстовые** и **Хэшированные** индексы.

Обратитесь к [документации MongoDB](https://docs.mongodb.com/manual/indexes/) для получения дополнительной информации об индексах.

 ## Текстовый поиск

MongoDB поддерживает операции запросов, которые выполняют текстовый поиск по строковому содержимому. Для выполнения текстового поиска MongoDB использует **текстовый индекс** и оператор `$text`.

Для выполнения запросов текстового поиска у вас должен быть текстовый индекс в вашей коллекции. Коллекция может иметь только один индекс текстового поиска, но этот индекс может охватывать несколько полей.

Например, вы можете выполнить следующее в оболочке mongo, чтобы разрешить текстовый поиск по полям `title` и `plotOutline`:

```javascript
db.movies.createIndex ( { title: "text", plotOutline: "text" } )
```

Теперь давайте выполним текстовый поиск по термину "fight"

```javascript
db.movies.find( { $text: { $search: "fight" } } )
```

Оператор запроса `$text` будет токенизировать строку поиска, используя пробелы и большинство знаков препинания в качестве разделителей, и выполнит логическое ИЛИ всех таких токенов в строке поиска.
Мы должны получить результат с двумя фильмами, один Fight Club, где термин можно найти в названии, и другой, где термин используется в `plotOutline`.

```javascript
db.movies.find( { $text: { $search: "fight" } } )
[
  {
    _id: ObjectId('66cb7a728137d3ecf9c76a9b'),
    rating: 9,
    genres: [ 'Drama' ],
    rank: 10,
    title: 'Fight Club',
    year: 1999
  },
  {
    _id: ObjectId('66cb796c8137d3ecf9c76a8d'),
    id: '0110912',
    title: 'Pulp Fiction',
    year: 1994,
    runtime: 154,
    languages: [ 'en', 'es', 'fr' ],
    rating: 8.9,
    votes: 2084331,
    genres: [ 'Crime', 'Drama' ],
    plotOutline: 'Jules Winnfield (Samuel L. Jackson) and Vincent Vega (John Travolta) are two hit men who are out to retrieve a suitcase stolen from their employer, mob boss Marsellus Wallace (Ving Rhames). Wallace has also asked Vincent to take his wife Mia (Uma Thurman) out a few days later when Wallace himself will be out of town. Butch Coolidge (Bruce Willis) is an aging boxer who is paid by Wallace to lose his fight. The lives of these seemingly unrelated people are woven together comprising of a series of funny, bizarre and uncalled-for incidents.',
    coverUrl: 'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY150_CR1,0,101,150_.jpg',
    actors: [
      { actorID: '0000619', name: 'Tim Roth' },
      { actorID: '0001625', name: 'Amanda Plummer' },
      { actorID: '0522503', name: 'Laura Lovelace' },
      { actorID: '0000237', name: 'John Travolta' },
      { actorID: '0000168', name: 'Samuel L. Jackson' },
      { actorID: '0482851', name: 'Phil LaMarr' },
      { actorID: '0001844', name: 'Frank Whaley' },
      { actorID: '0824882', name: 'Burr Steers' },
      { actorID: '0000246', name: 'Bruce Willis' },
      { actorID: '0000609', name: 'Ving Rahmes' },
      { actorID: '0000235', name: 'Uma Thurman' },
      { actorID: '0000233', name: 'Quentin Tarantino' }
    ],
    directors: [ { directorID: '0000233', name: 'Quentin Tarantino' } ],
    producers: [
      { producerID: '0004744', name: 'Lawrence Bender' },
      { producerID: '0000362', name: 'Danny DeVito' },
      { producerID: '0321621', name: 'Richard N. Gladstein' },
      { producerID: '0787834', name: 'Michael Shamberg' },
      { producerID: '0792049', name: 'Stacey Sher' },
      { producerID: '0918424', name: 'Bob Weinstein' },
      { producerID: '0005544', name: 'Harvey Weinstein' }
    ]
  }
]
```

Если мы изменим термин на `fight terrorist`, мы увидим, что строка поиска будет разбита на токены `fight` и `terrorist`, и будут возвращены все фильмы, соответствующие любому из этих двух терминов в поле `title` или `plotOutline`.

```javascript
db.movies.find( { $text: { $search: "fight terrorist" } } )
```

Поэтому мы также получим третий фильм, фильм "The Matrix", в описании сюжета которого используется слово Terrorist.

 ## Агрегация данных

Конвейер агрегации дает вам возможность преобразовывать и комбинировать документы в вашей коллекции. Вы делаете это, пропуская документы через конвейер, который аналогичен Unix "pipe", где вы передаете вывод от одной команды к другой, к третьей и т.д.

Простейшая агрегация, с которой вы, вероятно, уже знакомы - это выражение SQL group by. Мы уже видели простые методы `countDocuments()` и `count()`, но что если мы хотим увидеть, сколько фильмов у нас есть для разных рейтингов?

```javascript
db.movies.aggregate( [{$group:{_id:'$rating', total: { $sum:1 }}}]) 
```

В оболочке у нас есть помощник агрегации, который принимает массив операторов конвейера. Для простого подсчета, сгруппированного по чему-либо, нам нужен только один такой оператор, называемый `$group`. Это точный аналог GROUP BY в SQL, где мы создаем новый документ с полем `_id`, указывающим, по какому полю мы группируем (здесь это rating), и другими полями, обычно получающими результаты некоторой агрегации, в данном случае мы используем `$sum 1` для каждого документа, соответствующего определенному рейтингу. Вы, вероятно, заметили, что полю `_id` было присвоено `$rating`, а не просто `rating` - `$` перед именем поля указывает, что будет подставлено значение этого поля из входящего документа.

Какие еще операторы конвейера мы можем использовать?

Наиболее часто используемый до (и часто после) `$group` - это `$match` - это точно как метод find, и он позволяет нам агрегировать только соответствующее подмножество наших документов или исключить некоторые документы из нашего результата.

В следующем примере мы группируем по `genres` и подсчитываем количество фильмов для каждого жанра. Поскольку поле `genres` является массивом, сначала мы должны использовать `$unwind` для разворачивания массива. Мы также возвращаем минимальный, максимальный и средний рейтинг для каждой группы. Результат сортируется по количеству фильмов в жанре в порядке убывания.

```javascript
db.movies.aggregate([
                    {$match: {year:{$gt:2000}}}, 
                    {$unwind: "$genres" }, 
                    {$group: {_id:'$genres',
                        number :{ $sum:1 },
                        minRating:{$min:'$rating'}, 
                        maxRating:{$max:'$rating'}, 
                        avgRating:{$avg:'$rating'}
                    }}, 
                    {$sort:{number:-1}} ])
```

Выполнение должно вернуть следующий результат

[результат опущен для краткости]

Есть еще один мощный оператор конвейера, называемый `$project` (аналогичный проекции, которую мы можем указать для команды find), который позволяет не только включать определенные поля, но и создавать или вычислять новые поля на основе значений в существующих полях. Например, вы можете использовать математические операторы для сложения значений нескольких полей перед нахождением среднего, или вы можете использовать строковые операторы для создания нового поля, которое является конкатенацией некоторых существующих полей.

Это лишь слегка затрагивает поверхность того, что вы можете делать с агрегациями. Обратитесь к [документации MongoDB](https://docs.mongodb.com/manual/core/aggregation-pipeline/index.html) для получения дополнительной информации о конвейерах агрегации.

## Удаление документов

Для удаления одного или нескольких документов просто используйте то, что мы узнали о селекторах запросов, но в качестве параметра команды `deleteOne` вместо команды `find`.

Если мы хотим удалить конкретный документ, например фильм "Fight Club", мы можем выполнить

```javascript
db.movies.deleteOne( { "title": "Fight Club" } )
```

Результат покажет, сколько документов было удалено:

```javascript
> db.movies.deleteOne( { "title": "Fight Club" } )
{ acknowledged: true, deletedCount: 1 }
```

Мы видим, что, как и ожидалось, один фильм был удален.

Мы также можем легко удалить остальные дополнительные фильмы, которые мы добавили ранее, следующей командой, указав удалить все документы, где нет поля `plotOutline`.

```javascript
db.movies.deleteMany( { "plotOutline": { $exists: false} } )
```
