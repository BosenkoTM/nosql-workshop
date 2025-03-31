# NoSQL Platform on Docker

## Среда разработки
Среда для этого курса полностью основана на контейнерах Docker.

Для упрощения предоставления используется одна конфигурация docker-compose. Все необходимое программное обеспечение будет предоставлено с помощью Docker.

У вас есть следующие варианты запуска среды:

* [**Среда локальной виртуальной машины**](./LocalVirtualMachine.md) — виртуальная машина с предустановленными Docker и Docker Compose будет распространяться инфраструктурой курса. Вам понадобится 50 ГБ свободного места на диске.
* [**Локальная среда Docker**](./LocalDocker.md) — у вас есть локальная настройка Docker и Docker Compose, которую вы хотите использовать

## Сервисы, доступные на платформе NoSQL
Следующие сервисы доступны как часть платформы:

 | Продукт | Сервис | URL |
|---------|---------|-------|
| Redis | Redis Commander | http://localhost:28119 |
| Cassandra | Cassandra-Web | http://localhost:28200 |
| MongoDB | Администрирование Mongo | http://localhost:28204 |
| MongoDB | Mongo-Express | http://localhost:28203 |
| MongoDB | MongoDB Compass | Установлен локально в Ubuntu 22.04 |
| Jupyter | Jupyter | Установлен локально в Ubuntu 22.04 |
| Neo4J | Neo4J | http://localhost:7474 |
| GraphDB | GraphDB | http://localhost:17200 |

Примечание: MongoDB Compass - это графический интерфейс для работы с MongoDB, установленный непосредственно в виртуальной машине Ubuntu 22.04. Для подключения используйте:
- URI: mongodb://root:abc123!@localhost:27017
- или заполните поля отдельно:
  * Hostname: localhost
  * Port: 27017
  * Authentication: Username/Password
  * Username: root
  * Password: abc123!


## Семинар на основе IMDb

Для семинара будем использовать данные из [IMDb](https://www.imdb.com/).

На следующей диаграмме показана концептуальная модель IMDb.

![Alt ​​Image Text](./images/IMDB-domain-and-context-data-model.png "Lightsail Homepage")

Данные были загружены с помощью следующего блокнота Jupyter (ссылка будет добавлена).

если не запустился контейнер docker:


Остановить все контейнеры и удалить

```
sudo docker stop $(sudo docker ps -aq) && sudo docker rm $(sudo docker ps -aq)
```

Удаление всех образов

```
sudo docker rmi $(sudo docker images -q)
```

Очистка всех сетей

```
sudo  docker system prune -a
```

Выполнить запуск  

```
sudo  docker compose up -d
```
