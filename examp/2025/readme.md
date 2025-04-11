
=======
## Cassandra
=======

### **Подключение и настройка Cassandra**

1. Какая команда используется для подключения к контейнеру Cassandra через SSH?
   - `docker exec cassandra-1 cqlsh`
   - `sudo docker exec -ti cassandra-1 cqlsh`
   - `ssh cassandra-1`
   - `docker connect cassandra-1`  


2. Какой порт по умолчанию используется для подключения к Cassandra?
   - `9042`
   - `8080`
   - `27017`
   - `3306`  


3. Какая команда отображает существующие пространства ключей в Cassandra?
   - `DESCRIBE keyspaces;`
   - `SELECT * FROM system_schema.keyspaces;`
   - `SHOW keyspaces;`
   - `LIST keyspaces;`  


4. Какой интерпретатор используется в Apache Zeppelin для работы с Cassandra?
   - `cassandra`
   - `python`
   - `sql`
   - `scala`  


5. Какое значение нужно указать для `cassandra.credentials.username` при настройке интерпретатора в Zeppelin?
   - `root`
   - `admin`
   - `cassandra`
   - `zeppelin`  


---

### **Работа с пространствами ключей (Keyspaces)**

6. Как создать пространство ключей в Cassandra?
   - `CREATE KEYSPACE movies WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};`
   - `CREATE DATABASE movies;`
   - `USE movies;`
   - `ALTER KEYSPACE movies;`  


7. Что означает параметр `replication_factor` при создании пространства ключей?
   - Количество реплик данных
   - Размер таблицы
   - Скорость записи
   - Тип данных  


8. Как переключиться на созданное пространство ключей?
   - `USE movies;`
   - `SWITCH movies;`
   - `SELECT movies;`
   - `DESCRIBE movies;`  


9. Как проверить текущие настройки пространства ключей?
   - `DESCRIBE KEYSPACE movies;`
   - `SHOW movies;`
   - `LIST movies;`
   - `SELECT movies;`  


10. Какой стратегии репликации обычно используют в производственной среде?
    - `LocalStrategy`
    - `SimpleStrategy`
    - `NetworkTopologyStrategy`
    - `GlobalStrategy`  


---

### **Создание и управление таблицами**

11. Как создать таблицу в Cassandra?
    - `CREATE TABLE movies.movie (movie_id int, title text, PRIMARY KEY (movie_id));`
    - `INSERT INTO movies.movie (movie_id, title);`
    - `UPDATE TABLE movies.movie;`
    - `ALTER TABLE movies.movie;`  


12. Что такое первичный ключ в Cassandra?
    - Уникальный идентификатор строки
    - Название таблицы
    - Тип данных
    - Размер таблицы  

13. Как удалить таблицу в Cassandra?
    - `DROP TABLE movies.movie;`
    - `DELETE TABLE movies.movie;`
    - `REMOVE TABLE movies.movie;`
    - `CLEAR TABLE movies.movie;`  

14. Как добавить новый столбец в существующую таблицу?
    - `ALTER TABLE movies.movie ADD new_column text;`
    - `UPDATE TABLE movies.movie ADD new_column text;`
    - `INSERT INTO movies.movie (new_column);`
    - `MODIFY TABLE movies.movie ADD new_column text;`  


15. Как получить метаданные таблицы?
    - `DESCRIBE TABLE movies.movie;`
    - `SHOW TABLE movies.movie;`
    - `LIST TABLE movies.movie;`
    - `SELECT TABLE movies.movie;`  

---

### **Вставка, обновление и удаление данных**

16. Как вставить данные в таблицу?
    - `INSERT INTO movies.movie (movie_id, title) VALUES (1, 'The Matrix');`
    - `ADD INTO movies.movie (movie_id, title) VALUES (1, 'The Matrix');`
    - `PUT INTO movies.movie (movie_id, title) VALUES (1, 'The Matrix');`
    - `SET INTO movies.movie (movie_id, title) VALUES (1, 'The Matrix');`  


17. Что происходит при использовании операции `INSERT` для существующего первичного ключа?
    - Добавляется новая строка
    - Обновляются значения
    - Происходит ошибка
    - Ничего не происходит  


18. Как обновить данные в таблице?
    - `UPDATE movies.movie SET title = 'New Title' WHERE movie_id = 1;`
    - `MODIFY movies.movie SET title = 'New Title' WHERE movie_id = 1;`
    - `CHANGE movies.movie SET title = 'New Title' WHERE movie_id = 1;`
    - `REPLACE movies.movie SET title = 'New Title' WHERE movie_id = 1;`  


19. Как удалить конкретную строку из таблицы?
    - `DELETE FROM movies.movie WHERE movie_id = 1;`
    - `REMOVE FROM movies.movie WHERE movie_id = 1;`
    - `CLEAR FROM movies.movie WHERE movie_id = 1;`
    - `DROP FROM movies.movie WHERE movie_id = 1;`  


20. Как очистить все данные из таблицы?
    - `TRUNCATE movies.movie;`
    - `CLEAR movies.movie;`
    - `DELETE ALL FROM movies.movie;`
    - `DROP DATA FROM movies.movie;`  


---

### **Запросы и фильтрация**

21. Как выбрать все данные из таблицы?
    - `SELECT * FROM movies.movie;`
    - `GET * FROM movies.movie;`
    - `FETCH * FROM movies.movie;`
    - `READ * FROM movies.movie;`  


22. Можно ли использовать фильтрацию по любому столбцу без использования ALLOW FILTERING?
    - Да
    - Нет
    - Только для числовых столбцов
    - Только для текстовых столбцов  


23. Как применить фильтрацию по неосновному столбцу?
    - `SELECT * FROM movies.movie WHERE title = 'The Matrix';`
    - `SELECT * FROM movies.movie WHERE title = 'The Matrix' ALLOW FILTERING;`
    - `SELECT * FROM movies.movie WHERE movie_id = 1;`
    - `SELECT * FROM movies.movie WHERE title = 'The Matrix' WITHOUT FILTERING;`  


24. Как работает функция TTL в Cassandra?
    - Устанавливает время жизни данных
    - Ограничивает размер таблицы
    - Определяет тип данных
    - Задаёт порядок сортировки  


25. Как проверить оставшееся время жизни данных?
    - `SELECT TTL(column_name) FROM table_name;`
    - `CHECK TTL(column_name) FROM table_name;`
    - `GET TTL(column_name) FROM table_name;`
    - `SHOW TTL(column_name) FROM table_name;`  

---

### **Динамические таблицы и связи**

26. Как создать динамическую таблицу для хранения фильмов по актёрам?
    - `CREATE TABLE movies.movies_by_actor (actor_id int, movie_id int, PRIMARY KEY (actor_id, movie_id));`
    - `CREATE TABLE movies.movies_by_actor (actor_id int, movie_id int);`
    - `CREATE TABLE movies.movies_by_actor (actor_id int, movie_id int, title text);`
    - `CREATE TABLE movies.movies_by_actor (actor_id int, movie_id int, title text, PRIMARY KEY (actor_id));`  

27. Как получить фильмы для конкретного актёра?
    - `SELECT title FROM movies.movies_by_actor WHERE actor_id = 1;`
    - `GET title FROM movies.movies_by_actor WHERE actor_id = 1;`
    - `FETCH title FROM movies.movies_by_actor WHERE actor_id = 1;`
    - `READ title FROM movies.movies_by_actor WHERE actor_id = 1;`  


28. Как создать таблицу для подсчёта просмотров фильмов?
    - `CREATE TABLE movies.movie_viewed_by_time (movie_id int, year int, month int, male counter, female counter, PRIMARY KEY (movie_id, year, month));`
    - `CREATE TABLE movies.movie_viewed_by_time (movie_id int, year int, month int, male int, female int, PRIMARY KEY (movie_id));`
    - `CREATE TABLE movies.movie_viewed_by_time (movie_id int, year int, month int, male int, female int);`
    - `CREATE TABLE movies.movie_viewed_by_time (movie_id int, year int, month int, male counter, female counter);`  


29. Как увеличить счётчик мужских просмотров для фильма?
    - `UPDATE movies.movie_viewed_by_time SET male = male + 1 WHERE movie_id = 1 AND year = 2023 AND month = 5;`
    - `INCREMENT movies.movie_viewed_by_time SET male = male + 1 WHERE movie_id = 1 AND year = 2023 AND month = 5;`
    - `ADD movies.movie_viewed_by_time SET male = male + 1 WHERE movie_id = 1 AND year = 2023 AND month = 5;`
    - `GROW movies.movie_viewed_by_time SET male = male + 1 WHERE movie_id = 1 AND year = 2023 AND month = 5;`  


30. Как получить статистику просмотров за определённый период?
    - `SELECT * FROM movies.movie_viewed_by_time WHERE movie_id = 1 AND year = 2023 AND month >= 1 AND month <= 6;`
    - `GET * FROM movies.movie_viewed_by_time WHERE movie_id = 1 AND year = 2023 AND month >= 1 AND month <= 6;`
    - `FETCH * FROM movies.movie_viewed_by_time WHERE movie_id = 1 AND year = 2023 AND month >= 1 AND month <= 6;`
    - `READ * FROM movies.movie_viewed_by_time WHERE movie_id = 1 AND year = 2023 AND month >= 1 AND month <= 6;`  


---

### **API и инструменты**

31. Какой язык программирования используется для API Cassandra?
    - Python
    - Java
    - C++
    - JavaScript  


32. Какой инструмент позволяет работать с Cassandra через браузер?
    - Cassandra Web
    - MySQL Workbench
    - MongoDB Compass
    - PostgreSQL Admin  


33. Какой интерфейс предоставляет Apache Zeppelin для работы с Cassandra?
    - Notebook
    - Command Line
    - GUI
    - REST API  


34. Какой интерпретатор используется в Apache Zeppelin для работы с Cassandra?
    - SQL
    - Python
    - Scala
    - Cassandra  


35. Какой пароль используется для входа в Apache Zeppelin?
    - `abc123!`
    - `admin`
    - `password`
    - `zeppelin`  


---

### **Дополнительные вопросы**

36. Какой тип данных используется для подсчёта рейтингов фильмов?
    - `counter`
    - `int`
    - `float`
    - `text`  


37. Какой порядок сортировки используется в таблице `movie_viewed_by_time`?
    - По возрастанию года и месяца
    - По убыванию года и месяца
    - Без сортировки
    - По алфавиту  

38. Какая команда используется для создания нового блокнота в Zeppelin?
    - `Create new note`
    - `New notebook`
    - `Add note`
    - `Insert notebook`  


39. Какой метод используется для выполнения запросов в Zeppelin?
    - `Ctrl + Enter`
    - `Shift + Enter`
    - `Alt + Enter`
    - `Tab + Enter`  


40. Какая команда используется для вывода версии Cassandra?
    - `SELECT * FROM system_schema.keyspaces;`
    - `DESCRIBE KEYSPACE movies;`
    - `SHOW VERSION;`
    - `cqlsh --version`  


========
## MONGODB
========

### **Подключение и настройка MongoDB**

41. Какая команда используется для подключения к контейнеру MongoDB через SSH?
   - `docker exec mongo-1 mongosh`
   - `sudo docker exec -ti mongo-1 mongosh -u "root" -p "abc123!"`
   - `ssh mongo-1`
   - `connect mongo-1`  


42. Какой порт по умолчанию используется для подключения к MongoDB?
   - `9042`
   - `8080`
   - `27017`
   - `3306`  


43. Какая команда отображает существующие коллекции в текущей базе данных?
   - `SHOW COLLECTIONS;`
   - `LIST COLLECTIONS;`
   - `db.getCollectionNames();`
   - `DESCRIBE COLLECTIONS;`  


44. Какой интерпретатор используется в MongoDB Shell для выполнения запросов?
   - `mongosh`
   - `python`
   - `sql`
   - `scala`  


45. Какое значение нужно указать для `username` при настройке подключения в MongoDB Compass?
   - `admin`
   - `root`
   - `mongo`
   - `compass`  


---

### **Работа с базами данных и коллекциями**

46. Как создать новую базу данных в MongoDB?
   - `CREATE DATABASE filmdb;`
   - `USE filmdb;`
   - `INSERT INTO filmdb;`
   - `NEW DATABASE filmdb;`  


47. Как создать новую коллекцию в MongoDB?
   - `CREATE TABLE movies;`
   - `db.createCollection("movies");`
   - `NEW COLLECTION movies;`
   - `INSERT INTO movies;`  


48. Как переключиться на созданную базу данных?
   - `SWITCH filmdb;`
   - `USE filmdb;`
   - `SELECT filmdb;`
   - `GO TO filmdb;`  


49. Как проверить текущие настройки базы данных?
   - `DESCRIBE DATABASE;`
   - `SHOW SETTINGS;`
   - `db.stats();`
   - `LIST DATABASE;`  


50. Как удалить коллекцию из базы данных?
   - `DROP TABLE movies;`
   - `DELETE COLLECTION movies;`
   - `db.movies.drop();`
   - `REMOVE movies;`  

---

### **Вставка, обновление и удаление данных**

51. Как вставить документ в коллекцию?
   - `db.movies.insertOne({ title: "The Matrix" });`
   - `db.movies.add({ title: "The Matrix" });`
   - `db.movies.push({ title: "The Matrix" });`
   - `db.movies.put({ title: "The Matrix" });`  


52. Что происходит при использовании операции `insertOne` для существующего `_id`?
   - Добавляется новая строка
   - Происходит ошибка
   - Обновляются значения
   - Ничего не происходит  


53. Как обновить данные в коллекции?
   - `db.movies.update({ title: "The Matrix" }, { $set: { year: 1999 } });`
   - `db.movies.modify({ title: "The Matrix" }, { year: 1999 });`
   - `db.movies.change({ title: "The Matrix" }, { year: 1999 });`
   - `db.movies.replace({ title: "The Matrix" }, { year: 1999 });`  


54. Как удалить конкретный документ из коллекции?
   - `db.movies.deleteOne({ title: "The Matrix" });`
   - `db.movies.remove({ title: "The Matrix" });`
   - `db.movies.erase({ title: "The Matrix" });`
   - `db.movies.clear({ title: "The Matrix" });`  


55. Как очистить все данные из коллекции?
   - `TRUNCATE movies;`
   - `CLEAR movies;`
   - `db.movies.deleteMany({});`
   - `EMPTY movies;`  


---

### **Запросы и фильтрация**

56. Как выбрать все документы из коллекции?
   - `db.movies.find();`
   - `db.movies.selectAll();`
   - `db.movies.listAll();`
   - `db.movies.showAll();`  


57. Можно ли использовать фильтрацию по любому полю без индексации?
   - Да
   - Нет
   - Только для числовых полей
   - Только для текстовых полей  


58. Как применить фильтрацию по нескольким полям?
   - `db.movies.find({ field1: value1, field2: value2 });`
   - `db.movies.filter({ field1: value1, field2: value2 });`
   - `db.movies.select({ field1: value1, field2: value2 });`
   - `db.movies.where({ field1: value1, field2: value2 });`  


59. Как работает оператор `$in` в MongoDB?
   - Возвращает документы, где поле содержит хотя бы одно из значений массива
   - Возвращает документы, где поле равно всем значениям массива
   - Возвращает документы, где поле не содержит ни одного значения массива
   - Возвращает документы, где поле пусто  


60. Как получить документы, где поле `genres` содержит значение `Action`?
   - `db.movies.find({ genres: "Action" });`
   - `db.movies.find({ genres: [$eq: "Action"] });`
   - `db.movies.find({ genres: {$contains: "Action"} });`
   - `db.movies.find({ genres: {$like: "Action"} });`  


---

### **Индексы и производительность**

61. Как создать индекс по полю `title`?
   - `db.movies.createIndex({ title: 1 });`
   - `db.movies.addIndex({ title: 1 });`
   - `db.movies.setIndex({ title: 1 });`
   - `db.movies.makeIndex({ title: 1 });`  


62. Что делает уникальный индекс?
   - Разрешает дублирование значений
   - Запрещает дублирование значений
   - Ускоряет чтение данных
   - Ускоряет запись данных  


63. Как проверить существующие индексы коллекции  (начиная с версии 3.0)?
   - `db.movies.getIndexes();`
   - `db.movies.listIndexes();`
   - `db.movies.showIndexes();`
   - `db.movies.describeIndexes();`  


64. Как удалить индекс из коллекции?
   - `db.movies.dropIndex({ title: 1 });`
   - `db.movies.removeIndex({ title: 1 });`
   - `db.movies.deleteIndex({ title: 1 });`
   - `db.movies.clearIndex({ title: 1 });`  


65. Какой тип индекса используется для геопространственных запросов?
   - `text`
   - `hashed`
   - `2dsphere`
   - `compound`  


---

### **Текстовый поиск**

66. Как создать текстовый индекс для полей `title` и `plotOutline`?
   - `db.movies.createIndex({ title: "text", plotOutline: "text" });`
   - `db.movies.addTextIndex({ title: "text", plotOutline: "text" });`
   - `db.movies.setTextIndex({ title: "text", plotOutline: "text" });`
   - `db.movies.makeTextIndex({ title: "text", plotOutline: "text" });`  


67. Как выполнить текстовый поиск по термину `fight`?
   - `db.movies.find({ $text: { $search: "fight" } });`
   - `db.movies.search("fight");`
   - `db.movies.query("fight");`
   - `db.movies.lookup("fight");`  


68. Что делает оператор `$text`?
   - Выполняет точное совпадение
   - Выполняет текстовый поиск
   - Выполняет регулярное выражение
   - Выполняет сравнение чисел  


69. Как ограничить количество результатов текстового поиска?
   - `db.movies.find({ $text: { $search: "fight" } }).limit(10);`
   - `db.movies.find({ $text: { $search: "fight" } }).count(10);`
   - `db.movies.find({ $text: { $search: "fight" } }).max(10);`
   - `db.movies.find({ $text: { $search: "fight" } }).restrict(10);`  


70. Как получить документы, содержащие слово `fight` или `terrorist`?
   - `db.movies.find({ $text: { $search: "fight terrorist" } });`
   - `db.movies.find({ $or: ["fight", "terrorist"] });`
   - `db.movies.find({ $contains: ["fight", "terrorist"] });`
   - `db.movies.find({ $match: ["fight", "terrorist"] });`  


---

### **Агрегация данных**

71. Какой оператор агрегации используется для группировки документов?
   - `$group`
   - `$sort`
   - `$project`
   - `$match`  


72. Как подсчитать количество документов для каждого рейтинга?
   - `db.movies.aggregate([{$group:{_id:'$rating', total: { $sum:1 }}}]);`
   - `db.movies.aggregate([{$count:{_id:'$rating'}}]);`
   - `db.movies.aggregate([{$total:{_id:'$rating'}}]);`
   - `db.movies.aggregate([{$sum:{_id:'$rating'}}]);`  


73. Какой оператор агрегации используется для сортировки результатов?
   - `$sort`
   - `$order`
   - `$rank`
   - `$sequence`  


74. Как создать новое поле на основе существующих данных?
   - `$project`
   - `$create`
   - `$add`
   - `$generate`  


75. Как объединить несколько коллекций в одну агрегацию?
   - `$lookup`
   - `$join`
   - `$merge`
   - `$combine`  


---

### **Дополнительные вопросы**

76. Какой язык программирования используется для API MongoDB?
   - Python
   - Java
   - C++
   - JavaScript  


77. Какой инструмент позволяет работать с MongoDB через браузер?
   - Cassandra Web
   - MySQL Workbench
   - MongoDB Compass
   - PostgreSQL Admin  


78. Какой метод используется для подсчёта документов в коллекции?
   - `db.movies.countDocuments();`
   - `db.movies.total();`
   - `db.movies.sum();`
   - `db.movies.quantity();`  


79. Какой метод используется для проверки наличия документа?
   - `db.movies.exists();`
   - `db.movies.isPresent();`
   - `db.movies.findOne();`
   - `db.movies.isAvailable();`  


80. Какой метод используется для получения предполагаемого количества документов?
   - `db.movies.estimatedDocumentCount();`
   - `db.movies.guessCount();`
   - `db.movies.approximate();`
   - `db.movies.predict();`  

---
=========
## Neo4J
=========

### **Подключение и настройка Neo4j**

81. Какая команда используется для подключения к контейнеру Neo4j через SSH?
   - `docker exec neo4j-1 cypher-shell`
   - `sudo docker exec -ti neo4j-1 ./bin/cypher-shell -u neo4j -p abc123abc123`
   - `ssh neo4j-1`
   - `connect neo4j-1`  


82. Какой порт по умолчанию используется для подключения к Neo4j через HTTP?
   - `7687`
   - `8080`
   - `7474`
   - `3306`  


83. Какой порт по умолчанию используется для подключения к Neo4j через Bolt Protocol?
   - `7474`
   - `8080`
   - `7687`
   - `3306`  


84. Какая команда используется для входа в интерфейс Cypher Shell?
   - `cypher-shell`
   - `neo4j-shell`
   - `connect neo4j`
   - `login neo4j`  


85. Какой пользователь и пароль используются для входа в Neo4j Browser по умолчанию?
   - `admin / admin`
   - `root / root`
   - `neo4j / abc123abc123`
   - `user / password`  

---

### **Основные компоненты графовой модели**

86. Что представляют собой узлы (Nodes) в графовой базе данных Neo4j?
   - Связи между сущностями
   - Сущности или объекты
   - Типы данных
   - Запросы  


87. Как называются метки, которые можно присвоить узлам в Neo4j?
   - Labels
   - Tags
   - Categories
   - Types  


88. Как создать новый узел в Neo4j?
   - `CREATE (n:Person {name: 'John', age: 30});`
   - `INSERT INTO Person (name, age) VALUES ('John', 30);`
   - `NEW NODE Person (name: 'John', age: 30);`
   - `ADD NODE Person (name: 'John', age: 30);`  


89. Какое свойство содержит **Направление** в отношениях между узлами?
   - Type
   - Name
   - Label
   - Direction 


90. Как создать новое отношение между двумя узлами в Neo4j?
   - `CREATE (a:Person)-[r:KNOWS {since: 2020}]->(b:Person);`
   - `INSERT RELATIONSHIP a TO b WITH TYPE KNOWS;`
   - `CONNECT a TO b AS KNOWS;`
   - `LINK a TO b WITH KNOWS;`  


---

### **Запросы и фильтрация**

91. Выбрать запрос, который найдет актёра с именем Tom Hanks в Neo4j?
   - `SELECT * FROM Person WHERE name = 'Tom Hanks';`
   - `MATCH (tom {name: "Tom Hanks"}) RETURN tom;`
   - `FIND (Person) WHERE name = 'Tom Hanks';`
   - `GET Person WHERE name = 'Tom Hanks';`  


92. Выбрать запрос, который выведет фильм с названием Cloud Atlas в Neo4j?
   - `SELECT * FROM Movie WHERE title = 'Cloud Atlas';`
   - `MATCH (cloudAtlas {title: "Cloud Atlas"}) RETURN cloudAtlas;`
   - `FIND (Movie) WHERE title = 'Cloud Atlas';`
   - `GET Movie WHERE title = 'Cloud Atlas';`  


93. Как найти всех актеров, которые участвовали в съёмках вместе с Tom Hanks?
   - `SELECT coActors.name FROM Person WHERE name = 'Tom Hanks';`
   - `MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors) RETURN coActors.name;`
   - `FIND (Person) WHERE acted_with = 'Tom Hanks';`
   - `GET Partners WHERE actor = 'Tom Hanks';`  


94. Как найти самый короткий путь между Kevin Bacon и Meg Ryan?
   - `SELECT shortestPath('Kevin Bacon', 'Meg Ryan');`
   - `MATCH p=shortestPath((bacon:Person {name:"Kevin Bacon"})-[*]-(meg:Person {name:"Meg Ryan"})) RETURN p;`
   - `FIND SHORTEST_PATH FROM 'Kevin Bacon' TO 'Meg Ryan';`
   - `GET PATH WHERE start = 'Kevin Bacon' AND end = 'Meg Ryan';`  


95. Как вывести все свойства узла?
   - `SELECT * FROM Node;`
   - `MATCH (n) RETURN n;`
   - `LIST ALL PROPERTIES OF Node;`
   - `SHOW Node PROPERTIES;`  


---

### **Импорт и загрузка данных**

96. Какой инструмент используется для импорта данных из CSV/JSON в Neo4j?
   - `Neo4j Data Importer`
   - `Neo4j Bloom`
   - `Neo4j Browser`
   - `Cypher Shell`  


97. Какая команда используется для создания компании в графовой базе данных?
   - `CREATE (:Company {id: 1, name: "ABC Corp", industry: "IT"});`
   - `INSERT INTO Company (id, name, industry) VALUES (1, "ABC Corp", "IT");`
   - `NEW COMPANY (id: 1, name: "ABC Corp", industry: "IT");`
   - `ADD COMPANY (id: 1, name: "ABC Corp", industry: "IT");`  


98. Как создать отношение WORKS_AT между сотрудником и компанией?
   - `CREATE (e:Employee)-[:WORKS_AT]->(c:Company);`
   - `INSERT RELATIONSHIP e TO c AS WORKS_AT;`
   - `CONNECT e TO c WITH WORKS_AT;`
   - `LINK e TO c USING WORKS_AT;`  


99. Как загрузить данные о проектах в Neo4j?
   - `CREATE (:Project {id: 1, name: "Project X", start_date: "2023-01-01", end_date: "2023-06-01", company_id: 1});`
   - `INSERT INTO Project (id, name, start_date, end_date, company_id) VALUES (1, "Project X", "2023-01-01", "2023-06-01", 1);`
   - `NEW PROJECT (id: 1, name: "Project X", start_date: "2023-01-01", end_date: "2023-06-01", company_id: 1);`
   - `ADD PROJECT (id: 1, name: "Project X", start_date: "2023-01-01", end_date: "2023-06-01", company_id: 1);`  


100. Как связать клиента с проектом?
   - `CREATE (c:Client)-[:IS_CLIENT_OF]->(p:Project);`
   - `INSERT RELATIONSHIP c TO p AS IS_CLIENT_OF;`
   - `CONNECT c TO p WITH IS_CLIENT_OF;`
   - `LINK c TO p USING IS_CLIENT_OF;`  


---

### **Агрегация и анализ данных**

101. Как найти всех сотрудников компании "ABC Corp"?
   - `SELECT * FROM Employee WHERE company = 'ABC Corp';`
   - `MATCH (e:Employee)-[:WORKS_AT]->(c:Company {name: "ABC Corp"}) RETURN e.name AS EmployeeName;`
   - `FIND (Employee) WHERE company = 'ABC Corp';`
   - `GET Employees WHERE company = 'ABC Corp';`  


102. Как получить список всех компаний и их отраслей?
   - `SELECT * FROM Company;`
   - `MATCH (c:Company) RETURN c.name, c.industry;`
   - `LIST ALL Companies;`
   - `SHOW Companies;`  


103. Как найти все проекты, связанные с компанией "XYZ Inc"?
   - `SELECT * FROM Project WHERE company = 'XYZ Inc';`
   - `MATCH (c:Company {name: "XYZ Inc"})-[:HAS_PROJECT]->(p:Project) RETURN p.name;`
   - `FIND Projects WHERE company = 'XYZ Inc';`
   - `GET Projects FOR 'XYZ Inc';`  


104. Как найти всех клиентов проекта "Project X"?
   - `SELECT * FROM Client WHERE project = 'Project X';`
   - `MATCH (c:Client)-[:IS_CLIENT_OF]->(p:Project {name: "Project X"}) RETURN c.name;`
   - `FIND Clients WHERE project = 'Project X';`
   - `GET Clients FOR 'Project X';`  


105. Как получить количество проектов каждой компании?
   - `SELECT COUNT(*) FROM Project GROUP BY company;`
   - `MATCH (c:Company)-[:HAS_PROJECT]->(p:Project) RETURN c.name, COUNT(p) AS ProjectCount;`
   - `AGGREGATE Projects BY Company;`
   - `SUMMARIZE Projects PER Company;`  


---

### **Визуализация и инструменты**

106. Какой инструмент используется для визуализации графовых данных в Neo4j?
   - `Neo4j Bloom`
   - `Neo4j Browser`
   - `Cypher Shell`
   - `Neo4j Desktop`  


107. Какой инструмент предоставляет веб-интерфейс для выполнения запросов?
   - `Neo4j Browser`
   - `Neo4j Bloom`
   - `Cypher Shell`
   - `Neo4j Desktop`  


108. Какой инструмент используется для управления базами данных локально?
   - `Neo4j Desktop`
   - `Neo4j Browser`
   - `Neo4j Bloom`
   - `Cypher Shell`  


109. Какой язык запросов используется в Neo4j?
   - SQL
   - Cypher
   - Python
   - JavaScript  


110. Какая команда используется для выхода из Cypher Shell?
   - `EXIT`
   - `QUIT`
   - `DISCONNECT`
   - `:exit`  


---

### **Типы данных и свойства**

111. Какие типы данных поддерживаются в свойствах узлов и отношений?
   - Числовые, строковые, логические, списки, временные метки
   - Только числовые и строковые
   - Только строковые
   - Только числовые  


112. Как добавить новое свойство к существующему узлу?
   - `UPDATE (n) SET n.newProperty = 'value';`
   - `ALTER NODE (n) ADD PROPERTY newProperty = 'value';`
   - `MODIFY (n) WITH newProperty = 'value';`
   - `SET (n) PROPERTY newProperty = 'value';`  


113. Как удалить свойство из узла?
   - `REMOVE (n).property;`
   - `DELETE (n).property;`
   - `DROP (n).property;`
   - `CLEAR (n).property;`  


114. Как изменить значение свойства узла?
   - `UPDATE (n) SET n.property = 'newValue';`
   - `ALTER (n) SET n.property = 'newValue';`
   - `MODIFY (n) SET n.property = 'newValue';`
   - `CHANGE (n) SET n.property = 'newValue';`  


115. Как проверить наличие свойства у узла?
   - `EXISTS (n.property);`
   - `CHECK (n.property);`
   - `VALIDATE (n.property);`
   - `TEST (n.property);`  


---

### **Индексы и производительность**

116. Как создать индекс для часто запрашиваемых свойств?
   - `CREATE INDEX ON :Label(property);`
   - `BUILD INDEX FOR Label(property);`
   - `GENERATE INDEX FOR Label(property);`
   - `SET INDEX FOR Label(property);`  


117. Какой оператор используется для предотвращения дубликатов при создании узлов?
   - `MERGE`
   - `CREATE`
   - `INSERT`
   - `UPDATE`  

118. Как оптимизировать производительность запросов?
   - Использовать параметризованные запросы
   - Увеличить размер базы данных
   - Удалить все индексы
   - Добавить больше узлов  


119. Какой оператор используется для группировки данных?
   - `$group`
   - `GROUP BY`
   - `$aggregate`
   - `COLLECT`  


120. Как проверить план выполнения запроса?
   - `EXPLAIN query;`
   - `PLAN query;`
   - `DESCRIBE query;`
   - `ANALYZE query;`  


---

### **Работа с отношениями**

121. Как создать отношение между двумя узлами?
   - `CREATE (a)-[:RELATIONSHIP_TYPE]->(b);`
   - `CONNECT (a) TO (b) AS RELATIONSHIP_TYPE;`
   - `LINK (a) TO (b) USING RELATIONSHIP_TYPE;`
   - `JOIN (a) WITH (b) AS RELATIONSHIP_TYPE;`  


122. Как удалить отношение между двумя узлами?
   - `DELETE (a)-[r:RELATIONSHIP_TYPE]->(b);`
   - `REMOVE (a)-[r:RELATIONSHIP_TYPE]->(b);`
   - `ERASE (a)-[r:RELATIONSHIP_TYPE]->(b);`
   - `CLEAR (a)-[r:RELATIONSHIP_TYPE]->(b);`  


123. Как найти все отношения заданного типа?
   - `MATCH ()-[r:RELATIONSHIP_TYPE]-() RETURN r;`
   - `FIND ALL RELATIONSHIPS WHERE type = 'RELATIONSHIP_TYPE';`
   - `SELECT * FROM RELATIONSHIP WHERE type = 'RELATIONSHIP_TYPE';`
   - `LIST RELATIONSHIPS WHERE type = 'RELATIONSHIP_TYPE';`  


124. Как найти все узлы, связанные с конкретным узлом?
   - `MATCH (n)-[]->() RETURN n;`
   - `FIND ALL NODES CONNECTED TO (n);`
   - `SELECT * FROM Nodes WHERE connected_to = (n);`
   - `LIST NODES RELATED TO (n);`  


125. Как найти всех сотрудников, участвующих в проекте "Project X"?
   - `MATCH (e:Employee)-[:PARTICIPATES_IN]->(p:Project {name: "Project X"}) RETURN e.name;`
   - `FIND Employees IN Project WHERE name = 'Project X';`
   - `SELECT Employees FROM Project WHERE name = 'Project X';`
   - `GET Employees FOR 'Project X';`  



===========
## GraphDB
===========

### **Подключение и настройка GraphDB**

126. Какая команда используется для остановки контейнера GraphDB?
   - `sudo docker compose stop`
   - `sudo docker stop graphdb`
   - `sudo docker kill graphdb`
   - `sudo docker pause graphdb`  


127. Какая команда используется для запуска контейнера GraphDB?
   - `sudo docker start graphdb`
   - `sudo docker run graphdb`
   - `sudo docker compose start`
   - `sudo docker resume graphdb`  


128. Какой порт по умолчанию используется для доступа к GraphDB Workbench?
   - `17200`
   - `8080`
   - `7474`
   - `9042`  


129. Какая ссылка содержит данные о фильмах в формате Turtle для загрузки в GraphDB?
   - `https://raw.githubusercontent.com/BosenkoTM/nosql-workshop/refs/heads/main/07-working-with-graphdb/data/movies.ttl`
   - `http://localhost:17200/import`
   - `http://graphdb.com/data/movies.ttl`
   - `https://github.com/graphdb/movies.ttl`  


130. Как называется инструмент для управления базами данных в GraphDB?
   - GraphDB Workbench
   - Neo4j Browser
   - MongoDB Compass
   - Cassandra Web  


---

### **Загрузка RDF данных**

131. Какое действие выполняется для создания нового репозитория в GraphDB?
   - CREATE TABLE
   - Create Keyspace
   - Create Сollection
   - Create Repository 


132. Какой префикс используется для сокращения IRI в SPARQL-запросах?
   - `PREFIX`
   - `BASE`
   - `DEFINE`
   - `SET`  


133. Какая команда используется для импорта RDF-данных из URL?
   - `Import from file`
   - `Get RDF data from a URL`
   - `Upload RDF data`
   - `Load RDF data`  


134. Какой формат данных используется для хранения фильмов в лекции по теме  GraphDB?
   - JSON
   - CSV
   - Turtle (TTL)
   - XML  


135. Какой класс используется для представления цветных фильмов в графе?
   - `imdb:BlackAndWhiteMovie`
   - `schema:ColorMovie`
   - `imdb:ColorMovie`
   - `schema:Movie`  


---

### **Основы SPARQL**

136. Какой оператор SPARQL выбирает все триплеты из графа?
   - `SELECT * WHERE { ?s ?p ?o }`
   - `FIND ALL TRIPLES`
   - `LIST TRIPLES`
   - `SHOW TRIPLES`  


137. Как ограничить результаты запроса до первых 100 записей?
   - `LIMIT 100`
   - `TOP 100`
   - `MAX 100`
   - `COUNT 100`  


138. Что делает оператор `a` в SPARQL?
   - Выбирает конкретный объект
   - Задаёт тип сущности
   - Фильтрует результаты
   - Сортирует записи  


139. Какой префикс используется для работы с данными IMDB в SPARQL?
   - `PREFIX imdb: <http://academy.ontotext.com/imdb/>`
   - `PREFIX dbpedia: <http://dbpedia.org/resource/>`
   - `PREFIX schema: <http://schema.org/>`
   - `PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>`  


140. Как выбрать все фильмы, которые являются цветными?
   - `SELECT * WHERE { ?movie a imdb:ColorMovie }`
   - `FIND ALL WHERE { ?movie a imdb:ColorMovie }`
   - `LIST WHERE { ?movie a imdb:ColorMovie }`
   - `GET WHERE { ?movie a imdb:ColorMovie }`  


---

### **Работа с данными**

141. Как найти режиссёра фильма "Pirates of the Caribbean: At World's End"?
   - `SELECT * WHERE { imdb:title/PiratesoftheCaribbeanAtWorldsEnd schema:director ?person }`
   - `FIND director WHERE { movie = "Pirates of the Caribbean: At World's End" }`
   - `GET director FROM movie WHERE name = "Pirates of the Caribbean: At World's End"`
   - `LIST director FOR movie WHERE title = "Pirates of the Caribbean: At World's End"`  


142. Как выбрать название фильма и количество комментариев?
   - `SELECT ?movie ?name ?commentCount WHERE { ?movie schema:name ?name ; schema:commentCount ?commentCount }`
   - `FIND ?movie ?name ?commentCount WHERE { ?movie schema:name ?name ; schema:commentCount ?commentCount }`
   - `GET ?movie ?name ?commentCount WHERE { ?movie schema:name ?name ; schema:commentCount ?commentCount }`
   - `LIST ?movie ?name ?commentCount WHERE { ?movie schema:name ?name ; schema:commentCount ?commentCount }`  

143. Как отсортировать результаты по убыванию количество комментариев?
   - `ORDER BY DESC(?commentCount)`
   - `SORT BY DESC(?commentCount)`
   - `GROUP BY DESC(?commentCount)`
   - `RANK BY DESC(?commentCount)`  


144. Как выбрать фильмы, где один человек является как режиссёром, так и главным актёром?
   - `SELECT * WHERE { ?movie schema:director ?person ; imdb:leadActor ?person }`
   - `FIND movies WHERE { ?movie schema:director ?person ; imdb:leadActor ?person }`
   - `GET movies WHERE { ?movie schema:director ?person ; imdb:leadActor ?person }`
   - `LIST movies WHERE { ?movie schema:director ?person ; imdb:leadActor ?person }`  


145. Как подсчитать количество фильмов для каждого человека, который является как режиссёром, так и главным актёром?
   - `SELECT ?person (COUNT(?movie) AS ?numMovies) WHERE { ?movie schema:director ?person ; imdb:leadActor ?person } GROUP BY ?person`
   - `COUNT ?person WHERE { ?movie schema:director ?person ; imdb:leadActor ?person }`
   - `SUM ?person WHERE { ?movie schema:director ?person ; imdb:leadActor ?person }`
   - `TOTAL ?person WHERE { ?movie schema:director ?person ; imdb:leadActor ?person }`  


---

### **Визуализация графа**

146. Какой инструмент позволяет визуализировать графовые данные в GraphDB?
   - Visual Graph
   - Neo4j Bloom
   - MongoDB Compass
   - Cassandra Web  


147. Как расширить граф, чтобы показать связанные узлы в GraphDB?
   - Двойной клик левой кнопкой мыши по узлу
   - Щелчок правой кнопкой мыши по узлу
   - Использование команды `EXPAND`
   - Использование фильтра `FILTER`   


148. Как найти фильм по названию "The Matrix"?
   - Ввести "matrix" в поле поиска
   - Выполнить запрос `SELECT * WHERE { ?movie schema:name "The Matrix" }`
   - Нажать на кнопку "Find Movie"
   - Использовать команду `DESCRIBE`  


149. Какие типы фильмов представлены в графе?
   - Только чёрно-белые
   - Только цветные
   - Чёрно-белые и цветные
   - Только анимационные  


150. Как получить информацию о связях между фильмом и актёрами?
   - Нажать на фильм в графе
   - Выполнить запрос `SELECT * WHERE { ?movie schema:actor ?actor }`
   - Использовать команду `DESCRIBE`
   - Применить фильтр `FILTER (?movie = "The Matrix")`  


---

### **SPARQL-запросы**

151. Как выбрать все триплеты для определённого фильма?
   - `SELECT * WHERE { imdb:title/PiratesoftheCaribbeanAtWorldsEnd ?p ?o }`
   - `FIND ALL WHERE { imdb:title/PiratesoftheCaribbeanAtWorldsEnd ?p ?o }`
   - `GET ALL WHERE { imdb:title/PiratesoftheCaribbeanAtWorldsEnd ?p ?o }`
   - `LIST ALL WHERE { imdb:title/PiratesoftheCaribbeanAtWorldsEnd ?p ?o }`  


152. Как экранировать символ `/` в сокращённом IRI?
   - Использовать обратную косую черту `\`
   - Использовать двойные кавычки `""`
   - Использовать точку `.`
   - Использовать звёздочку `*`  


153. Как выбрать фильмы и их количество комментариев, отсортированные по убыванию?
   - `SELECT ?movie ?commentCount WHERE { ?movie schema:commentCount ?commentCount } ORDER BY DESC(?commentCount)`
   - `FIND ?movie ?commentCount WHERE { ?movie schema:commentCount ?commentCount } SORT BY DESC(?commentCount)`
   - `GET ?movie ?commentCount WHERE { ?movie schema:commentCount ?commentCount } RANK BY DESC(?commentCount)`
   - `LIST ?movie ?commentCount WHERE { ?movie schema:commentCount ?commentCount } GROUP BY DESC(?commentCount)`  


154. Как выбрать людей, которые являются как режиссёрами, так и главными актёрами?
   - `SELECT ?person WHERE { ?movie schema:director ?person ; imdb:leadActor ?person }`
   - `FIND ?person WHERE { ?movie schema:director ?person ; imdb:leadActor ?person }`
   - `GET ?person WHERE { ?movie schema:director ?person ; imdb:leadActor ?person }`
   - `LIST ?person WHERE { ?movie schema:director ?person ; imdb:leadActor ?person }`  


155. Как подсчитать количество фильмов для каждого режиссёра?
   - `SELECT ?director (COUNT(?movie) AS ?numMovies) WHERE { ?movie schema:director ?director } GROUP BY ?director`
   - `COUNT ?director WHERE { ?movie schema:director ?director }`
   - `SUM ?director WHERE { ?movie schema:director ?director }`
   - `TOTAL ?director WHERE { ?movie schema:director ?director }`  


---

### **Агрегация данных**

156. Как выбрать фильмы и их режиссёров?
   - `SELECT ?movie ?director WHERE { ?movie schema:director ?director }`
   - `FIND ?movie ?director WHERE { ?movie schema:director ?director }`
   - `GET ?movie ?director WHERE { ?movie schema:director ?director }`
   - `LIST ?movie ?director WHERE { ?movie schema:director ?director }`  


157. Как отсортировать результаты по имени режиссёра?
   - `ORDER BY ?director`
   - `SORT BY ?director`
   - `GROUP BY ?director`
   - `RANK BY ?director`  


158. Как выбрать фильмы с наибольшим количеством комментариев?
   - `SELECT ?movie ?commentCount WHERE { ?movie schema:commentCount ?commentCount } ORDER BY DESC(?commentCount)`
   - `FIND ?movie ?commentCount WHERE { ?movie schema:commentCount ?commentCount } SORT BY DESC(?commentCount)`
   - `GET ?movie ?commentCount WHERE { ?movie schema:commentCount ?commentCount } RANK BY DESC(?commentCount)`
   - `LIST ?movie ?commentCount WHERE { ?movie schema:commentCount ?commentCount } GROUP BY DESC(?commentCount)`  


159. Как выбрать фильмы и их жанры?
   - `SELECT ?movie ?genre WHERE { ?movie schema:genre ?genre }`
   - `FIND ?movie ?genre WHERE { ?movie schema:genre ?genre }`
   - `GET ?movie ?genre WHERE { ?movie schema:genre ?genre }`
   - `LIST ?movie ?genre WHERE { ?movie schema:genre ?genre }`  


160. Как выбрать фильмы и их актёров?
   - `SELECT ?movie ?actor WHERE { ?movie schema:actor ?actor }`
   - `FIND ?movie ?actor WHERE { ?movie schema:actor ?actor }`
   - `GET ?movie ?actor WHERE { ?movie schema:actor ?actor }`
   - `LIST ?movie ?actor WHERE { ?movie schema:actor ?actor }`  


---

### **Фильтрация и группировка**

161. Как выбрать фильмы, выпущенные после 2000 года?
   - `SELECT ?movie WHERE { ?movie schema:releaseDate ?date . FILTER (?date > "2000"^^xsd:integer) }`
   - `FIND ?movie WHERE { ?movie schema:releaseDate ?date . FILTER (?date > "2000"^^xsd:integer) }`
   - `GET ?movie WHERE { ?movie schema:releaseDate ?date . FILTER (?date > "2000"^^xsd:integer) }`
   - `LIST ?movie WHERE { ?movie schema:releaseDate ?date . FILTER (?date > "2000"^^xsd:integer) }`  


162. Как сгруппировать фильмы по режиссёру?
   - `GROUP BY ?director`
   - `SORT BY ?director`
   - `RANK BY ?director`
   - `FILTER BY ?director`  


163. Как выбрать режиссёров и количество фильмов, которые они сняли?
   - `SELECT ?director (COUNT(?movie) AS ?numMovies) WHERE { ?movie schema:director ?director } GROUP BY ?director`
   - `COUNT ?director WHERE { ?movie schema:director ?director }`
   - `SUM ?director WHERE { ?movie schema:director ?director }`
   - `TOTAL ?director WHERE { ?movie schema:director ?director }`  


164. Как выбрать фильмы с комментариями больше 1000?
   - `SELECT ?movie WHERE { ?movie schema:commentCount ?count . FILTER (?count > 1000) }`
   - `FIND ?movie WHERE { ?movie schema:commentCount ?count . FILTER (?count > 1000) }`
   - `GET ?movie WHERE { ?movie schema:commentCount ?count . FILTER (?count > 1000) }`
   - `LIST ?movie WHERE { ?movie schema:commentCount ?count . FILTER (?count > 1000) }`  


165. Как выбрать фильмы, выпущенные в определённом году?
   - `SELECT ?movie WHERE { ?movie schema:releaseDate "2000"^^xsd:integer }`
   - `FIND ?movie WHERE { ?movie schema:releaseDate "2000"^^xsd:integer }`
   - `GET ?movie WHERE { ?movie schema:releaseDate "2000"^^xsd:integer }`
   - `LIST ?movie WHERE { ?movie schema:releaseDate "2000"^^xsd:integer }`  


---

### **Продвинутые запросы**

166. Как выбрать фильмы и их рейтинг?
   - `SELECT ?movie ?rating WHERE { ?movie schema:rating ?rating }`
   - `FIND ?movie ?rating WHERE { ?movie schema:rating ?rating }`
   - `GET ?movie ?rating WHERE { ?movie schema:rating ?rating }`
   - `LIST ?movie ?rating WHERE { ?movie schema:rating ?rating }`  


167. Как выбрать фильмы и их актёров, сгруппированные по актёрам?
   - `SELECT ?actor (COUNT(?movie) AS ?numMovies) WHERE { ?movie schema:actor ?actor } GROUP BY ?actor`
   - `COUNT ?actor WHERE { ?movie schema:actor ?actor }`
   - `SUM ?actor WHERE { ?movie schema:actor ?actor }`
   - `TOTAL ?actor WHERE { ?movie schema:actor ?actor }`  


168. Как выбрать фильмы и их продюсеров?
   - `SELECT ?movie ?producer WHERE { ?movie schema:producer ?producer }`
   - `FIND ?movie ?producer WHERE { ?movie schema:producer ?producer }`
   - `GET ?movie ?producer WHERE { ?movie schema:producer ?producer }`
   - `LIST ?movie ?producer WHERE { ?movie schema:producer ?producer }`  


169. Как выбрать фильмы и их жанры, отсортированные по алфавиту?
   - `SELECT ?movie ?genre WHERE { ?movie schema:genre ?genre } ORDER BY ?genre`
   - `FIND ?movie ?genre WHERE { ?movie schema:genre ?genre } SORT BY ?genre`
   - `GET ?movie ?genre WHERE { ?movie schema:genre ?genre } RANK BY ?genre`
   - `LIST ?movie ?genre WHERE { ?movie schema:genre ?genre } GROUP BY ?genre`  


170. Как выбрать фильмы и их продолжительность?
   - `SELECT ?movie ?runtime WHERE { ?movie schema:runtime ?runtime }`
   - `FIND ?movie ?runtime WHERE { ?movie schema:runtime ?runtime }`
   - `GET ?movie ?runtime WHERE { ?movie schema:runtime ?runtime }`
   - `LIST ?movie ?runtime WHERE { ?movie schema:runtime ?runtime }`  


---

### **Интерпретация результатов**

171. Как интерпретировать результаты запроса в GraphDB Workbench?
   - Использовать вкладку "Results"
   - Использовать вкладку "Query"
   - Использовать вкладку "Logs"
   - Использовать вкладку "Settings"  


172. Какой инструмент используется для выполнения SPARQL-запросов в GraphDB?
   - YASGUI
   - Cypher Shell
   - Mongo Express
   - Cassandra Query Builder  


173. Какой оператор используется для объединения нескольких условий в SPARQL?
   - `UNION`
   - `JOIN`
   - `MERGE`
   - `LINK`  


174. Как выбрать фильмы и их актёров, отсортированные по алфавиту?
   - `SELECT ?movie ?actor WHERE { ?movie schema:actor ?actor } ORDER BY ?actor`
   - `FIND ?movie ?actor WHERE { ?movie schema:actor ?actor } SORT BY ?actor`
   - `GET ?movie ?actor WHERE { ?movie schema:actor ?actor } RANK BY ?actor`
   - `LIST ?movie ?actor WHERE { ?movie schema:actor ?actor } GROUP BY ?actor`  


175. Как выбрать фильмы и их продюсеров, выпущенные после 2010 года?
   - `SELECT ?movie ?producer WHERE { ?movie schema:producer ?producer ; schema:releaseDate ?date . FILTER (?date > "2010"^^xsd:integer) }`
   - `FIND ?movie ?producer WHERE { ?movie schema:producer ?producer ; schema:releaseDate ?date . FILTER (?date > "2010"^^xsd:integer) }`
   - `GET ?movie ?producer WHERE { ?movie schema:producer ?producer ; schema:releaseDate ?date . FILTER (?date > "2010"^^xsd:integer) }`
   - `LIST ?movie ?producer WHERE { ?movie schema:producer ?producer ; schema:releaseDate ?date . FILTER (?date > "2010"^^xsd:integer) }`  


---

### **Дополнительные вопросы**

176. Какой язык программирования используется для API GraphDB?
   - Python
   - Java
   - JavaScript
   - SPARQL  


177. Какой инструмент используется для загрузки RDF-данных в GraphDB?
   - Import Tool
   - Export Tool
   - Backup Tool
   - Restore Tool  


178. Какой формат данных чаще всего используется для хранения RDF-данных?
   - Turtle (TTL)
   - JSON
   - XML
   - CSV  


179. Какой оператор используется для сортировки результатов по возрастанию?
   - `ORDER BY ASC(?variable)`
   - `SORT BY ASC(?variable)`
   - `RANK BY ASC(?variable)`
   - `GROUP BY ASC(?variable)`  


180. Как выбрать фильмы и их режиссёров, выпущенные в определённом году?
   - `SELECT ?movie ?director WHERE { ?movie schema:director ?director ; schema:releaseDate "2000"^^xsd:integer }`
   - `FIND ?movie ?director WHERE { ?movie schema:director ?director ; schema:releaseDate "2000"^^xsd:integer }`
   - `GET ?movie ?director WHERE { ?movie schema:director ?director ; schema:releaseDate "2000"^^xsd:integer }`
   - `LIST ?movie ?director WHERE { ?movie schema:director ?director ; schema:releaseDate "2000"^^xsd:integer }`  


---



