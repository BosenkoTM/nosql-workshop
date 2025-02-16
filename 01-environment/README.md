# NoSQL Platform on Docker

## Среда разработки
Среда для этого курса полностью основана на контейнерах Docker.

Для упрощения предоставления используется одна конфигурация docker-compose. Все необходимое программное обеспечение будет предоставлено с помощью Docker.

У вас есть следующие варианты запуска среды:

* [**Виртуальная машина облака на Ubuntu с Init Script**](./CloudVM.md) — используйте облачную виртуальную машину, работающую на Ubuntu, и предоставьте Init Script.
* [**Среда AWS Lightsail**](./Lightsail.md) — AWS Lightsail — это сервис в Amazon Web Services (AWS), с помощью которого мы можем легко запустить среду и предоставить всю необходимую начальную загрузку в виде скрипта.
* [**Среда локальной виртуальной машины**](./LocalVirtualMachine.md) — виртуальная машина с предустановленными Docker и Docker Compose будет распространяться инфраструктурой курса. Вам понадобится 50 ГБ свободного места на диске.
* [**Локальная среда Docker**](./LocalDocker.md) — у вас есть локальная настройка Docker и Docker Compose, которую вы хотите использовать

## Сервисы, доступные на платформе NoSQL
Следующие сервисы доступны как часть платформы:

Продукт | Тип | Услуга | URL
------|------| --------| ----
Redis | Разработка | Redis Commander | <http://localhost:28119>
Cassandra | Разработка | Cassandra-Web | <http://localhost:28200>
MongoDB | Управление | Администрирование Mongo | <http://localhost:28204>
MongoDB | Разработка | Mongo-Express | <http://localhost:28203>
Elasticsearch | Разработка | Dejavu | <http://localhost:28205>
Elasticsearch | Разработка | cerebro | <http://localhost:28206>
Elasticsearch | Разработка | Kibana | <http://localhost:5601>
Elasticsearch | Разработка | ElasticHQ | <http://localhost:28207>
Neo4J | Разработка | Neo4J | <http://localhost:7474>
Grafana | Разработка | Grafana | <http://localhost:3000>
Zepplin | Разработка | Zeppelin | <http://localhost:28080>
Jupyter | Разработка | Jupyter | <http://localhost:28888>
Influx DB | Разработка | Chronograf | <http://localhost:28209>
Influx DB | Разработка | Influx UI | <http://localhost:28208>
Администратор | Разработка | PostgreSQL | <http://localhost:28210>
CAdvisor | Управление | Docker | <http://localhost:28217>

## Семинар на основе IMDb

Для семинара будем использовать данные из [IMDb](https://www.imdb.com/).

На следующей диаграмме показана концептуальная модель IMDb.

![Alt ​​Image Text](./images/IMDB-domain-and-context-data-model.png "Lightsail Homepage")

Данные были загружены с помощью следующего блокнота Jupyter (ссылка будет добавлена).
