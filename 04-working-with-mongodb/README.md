# Работа с MongoDB

В этом семинаре мы научимся использовать базу данных MongoDB NoSQL.

Мы предполагаем, что платформа, описанная [здесь](../01-environment), запущена и доступна.

## Подключение к среде MongoDB

### Использование утилиты командной строки MongoDB

Вы можете найти утилиту командной строки `mongo` внутри контейнера Docker MongoDB, работающего как часть платформы. Подключитесь по SSH к хосту Docker и выполните следующую команду `docker exec`

```
docker exec -ti mongo-1 mongosh -u "root" -p "abc123!"
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

------
Включите бесплатную облачную службу мониторинга MongoDB, которая затем будет получать и отображать
метрики о вашем развертывании (использование диска, ЦП, статистика операций и т. д.).

Данные мониторинга будут доступны на веб-сайте MongoDB с уникальным URL-адресом, доступным вам
и всем, с кем вы поделитесь URL-адресом. MongoDB может использовать эту информацию для внесения
улучшений в продукт и для предложения вам продуктов MongoDB и вариантов развертывания.

Чтобы включить бесплатный мониторинг, выполните следующую команду: db.enableFreeMonitoring()
Чтобы навсегда отключить это напоминание, выполните следующую команду: db.disableFreeMonitoring()
------

test>
```

Теперь вы находитесь в командной строке MongoDB, готовой к выполнению любых операторов MongoDB. Мы также можем увидеть версию сервера MongoDB, а также оболочки MongoDB.

Оболочка запускает JavaScript. Есть несколько глобальных команд, которые вы можете выполнить, например help или exit. Команды, которые вы выполняете для текущей базы данных, выполняются для объекта db, например `db.help()` или `db.stats()`.

Команды, которые вы выполняете для определенной коллекции, что мы будем делать много раз, выполняются для объекта `db.COLLECTION_NAME`, например `db.movies.help()` или `db.movies.countDocuments()`.

Продолжайте и введите `db.help()`, вы получите список команд, которые вы можете выполнить для объекта db.

**Небольшое примечание:** Поскольку это оболочка JavaScript, если вы выполните метод и опустите скобки (), вы увидите тело метода, а не выполнение метода. Я упоминаю об этом только для того, чтобы в первый раз, когда вы сделаете это и получите ответ, начинающийся с function (...){, вы не были удивлены. Например, если вы введете db.help (без скобок), вы увидите внутреннюю реализацию метода help.

### Использование браузерного графического интерфейса

Вместо работы в командной строке и, следовательно, необходимости подключаться к Docker Host через SSH, мы также можем использовать браузерный графический интерфейс для доступа к MongoDB. В рамках платформы доступны две браузерные утилиты.

#### Mongo Express

Первый — [Mongo Express](https://github.com/mongo-express/mongo-express), веб-интерфейс администратора MongoDB, написанный с помощью Node.js, Express и Bootstrap3.

В окне браузера перейдите на <http://localhost:28203/>, и вы должны сразу попасть на главный экран, как показано ниже.

![Alt ​​Image Text](./images/mongo-express-home.png "Mongo Express")

#### Admin Mongo
Второй — [Admin Mongo](https://github.com/adicom-systems/adminMongo), открытый исходный интерфейс администратора для MongoDB.

В окне браузера перейдите на <http://localhost:28204/> и войдите с именем пользователя `admin` и паролем `pass`, и вы должны увидеть главный экран, как показано ниже.

![Alt ​​Image Text](./images/admin-mongo-home.png "Admin Mongo")

Чтобы подключиться к экземпляру MongoDB, добавьте новое подключение к Admin Mongo. Введите `Data Platform` в поле **Имя подключения** и `mongodb://mongo-1:27017` в поле **Строка подключения** и нажмите **Добавить подключение**. Должно появиться сообщение о том, что подключение было успешно добавлено.

![Alt ​​Image Text](./images/admin-mongo-connection.png "Admin Mongo Connection")

Нажатие кнопки **Подключить** открывает страницу сведений об администрировании Mongo для подключения.

### Использование настольных приложений

Существуют также различные настольные приложения для управления и администрирования MongoDB, которые можно загрузить и установить на рабочем столе. Оттуда вы можете подключиться как к локальному, так и к удаленному экземпляру Mongo.

#### Studio 3T (ранее известная как Robo 3T или Robomongo)

Тот, который мы здесь показываем, — это [Studio 3T](https://
