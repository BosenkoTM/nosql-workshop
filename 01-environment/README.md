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
| Neo4J | Neo4J | http://localhost:7474 |
| Jupyter | Jupyter | http://localhost:28888 |


## Семинар на основе IMDb

Для семинара будем использовать данные из [IMDb](https://www.imdb.com/).

На следующей диаграмме показана концептуальная модель IMDb.

![Alt ​​Image Text](./images/IMDB-domain-and-context-data-model.png "Lightsail Homepage")

Данные были загружены с помощью следующего блокнота Jupyter (ссылка будет добавлена).
