# Работа с GraphDB

В этом практическом занятии мы узнаем, как использовать базу данных `Ontotext GraphDB NoSQL`.

Предполагается, что платформа, описанная [здесь](../01-environment/README.md), запущена и доступна.

На этом занятии вы узнаете, как загружать данные в формате `RDF` в `GraphDB`, а затем использовать язык запросов `SPARQL` для выполнения запросов к данным.

## Загрузка RDF данных

Мы будем использовать данные о фильмах, взятые из учебного пособия, предоставленного GraphDB. Данные доступны в синтаксисе Turtle, распространённом формате для хранения RDF данных, в проекте на GitHub по ссылке <https://raw.githubusercontent.com/gschmutz/nosql-workshop/master/07-working-with-graphdb/data/movies.ttl>. Если вы нажмёте на ссылку, увидите данные, представленные ниже.

![](./images/graphdb-movies-data.png)

Мы будем использовать GraphDB Workbench для загрузки данных. В браузере перейдите по адресу <http://localhost:17200>, чтобы открыть GraphDB Workbench.

![](./images/graphdb-workbench-1.png)

Нажмите на **Create new repository** и выберите **GraphDB Repository**.

![](./images/graphdb-workbench-2.png)

Введите `Movies` в поле **Repository** 

![](./images/graphdb-workbench-3.png)

и нажмите **Create**.

В меню слева нажмите на **Import**.

![](./images/graphdb-import-1.png)

Нажмите на **Movies** и выберите второй вариант **Get RDF data from a URL**.

![](./images/graphdb-import-2.png)

В появившемся окне введите [`https://raw.githubusercontent.com/BosenkoTM/nosql-workshop/refs/heads/main/07-working-with-graphdb/data/movies.ttl`](https://raw.githubusercontent.com/BosenkoTM/nosql-workshop/refs/heads/main/07-working-with-graphdb/data/movies.ttl) в поле.

![](./images/graphdb-import-33.png)

Оставьте выбранным **Start import automatically** и нажмите **Import**. Оставьте значения по умолчанию в другом всплывающем окне и снова нажмите **Import**.

Через несколько секунд ввод должен завершиться успешным сообщением, как показано на следующем снимке экрана.

![](./images/graphdb-import-44.png)

Теперь база данных готова к использованию.

## Обзор графа

Нажмите на **Explore** и **Class hierarchy**.

![](./images/graphdb-explore-1.png)

Мы можем увидеть схему графа фильмов с базовым классом `schema:Movie` и двумя подклассами `imbd:BlackAndWhiteMovie` и `imdb:ColorMovie`.

Нажмите на более крупную внутреннюю окружность, представляющую цветные фильмы.

![](./images/graphdb-explore-2.png)

Мы можем увидеть, что в графе есть `4690` экземпляров цветных фильмов, с отображением нескольких названий фильмов справа.

Вы можете либо напрямую нажать на одно из отображённых названий, либо использовать поиск для нахождения определённого фильма. Давайте введём `matrix`.


![](./images/graphdb-explore-3.png)

Чтобы найти фильм **The Matrix**, введите `matrix`. Нажмите на него, и вы увидите перечисленные связи, которые относятся к этому фильму.

![](./images/graphdb-explore-4.png)

Нажмите **Visual Graph**, чтобы увидеть график визуально.

![](./images/graphdb-explore-5.png)

Преимущество Визуального Графа заключается в том, что вы можете дважды щёлкнуть на одном из узлов, чтобы расширить граф. Давайте попробуем это на актера **KeanuReeves**, и граф должен расшириться, как показано ниже.


![](./images/graphdb-explore-6.png)

Мы можем увидеть все другие фильмы, в которых также снялся Кейну Ривз.

Навигация по графу таким образом имеет некоторые преимущества, но сначала нам нужно найти стартовый узел в нашем графе. Для этого RDF/Triple-хранилище предлагает язык запросов SPARQL.


## Querying the graph using SPARQL

Нажмите на **SPARQL** в навигационном меню слева, и вы перейдёте в представление SPARQL, которое интегрирует [редактор запросов YASGUI](http://about.yasgui.org/) или [редактор запросов YASGUI](https://docs.triply.cc/yasgui/).

![](./images/graphdb-sparql-1.png)

Самый простой оператор выбора SPARQL предварительно заполнен в окне запроса.

```sparql
select * where {
    ?s ?p ?o .
} limit 100
```

Нажмите **Run**, чтобы выполнить запрос. Он выбирает все `триплеты` в графе, но ограничивает результат до 100 записей.

![](./images/graphdb-sparql-2.png)

Если мы хотим показывать только триплет с определённым субъектом, мы можем адаптировать запрос следующим образом:

```sparql
select * where {
    <http://academy.ontotext.com/imdb/title/PiratesoftheCaribbeanAtWorldsEnd> ?p ?o .
}
```
Запрос выбирает RDF-утверждения, чей субъект — фильм "Pirates of the Caribbean: At World's End" (идентифицируемый IRI `http://academy.ontotext.com/imdb/title/PiratesOfTheCaribbeanAtWorldsEnd`).


![](./images/graphdb-sparql-3.png)

Мы можем сократить IRI, установив префикс, как показано ниже:

```sparql
PREFIX imdb: <http://academy.ontotext.com/imdb/>

select * where {
    imdb:title\/PiratesoftheCaribbeanAtWorldsEnd ?p ?o .
}
```

Это более полезно, если один и тот же префикс используется несколько раз.

Обратите внимание, что нужно экранировать `/` в сокращённом IRI.

Переменные `?p` и `?o` соответствуют предикату и объекту RDF-утверждений. Мы видим, что режиссёр (через предикат `schema:director`) идентифицируется IRI `imdb:person/GoreVerbinski` (прокрутите вниз при необходимости).

Следующий запрос выбирает все цветные фильмы по классу (`a` является сокращённой записью для `rdf:type`), а затем выполняет два соединения для получения названия фильма (через предикат `schema:name`) и количества комментариев к фильму (через предикат `schema:commentCount`). Наконец, результат должен быть отсортирован по количеству комментариев в порядке убывания.

```sparql
PREFIX imdb: <http://academy.ontotext.com/imdb/>
PREFIX schema: <http://schema.org/>

SELECT ?movie ?name ?commentCount
WHERE {
  ?movie a imdb:ColorMovie ;
           schema:name ?name ;
           schema:commentCount ?commentCount .
}
ORDER BY DESC(?commentCount)
LIMIT 100

```sparql
PREFIX imdb: <http://academy.ontotext.com/imdb/>
PREFIX schema: <http://schema.org/>

SELECT * { 
    ?movie a imdb:ColorMovie ;
           schema:name ?movieName ;
           schema:commentCount ?commentCount .
} ORDER BY DESC(?commentCount)
```

Таблица показывает результаты выполнения запроса.

![](./images/graphdb-sparql-4.png)

Переменные `?movie`, `?name` и `?commentCount` содержат соответственно IRI фильма, название фильма и количество комментариев. Мы видим, что фильм с наибольшим количеством комментариев, "The Dark Knight Rises", находится на вершине списка.

Следующий запрос выбирает RDF-утверждения, которые имеют одинаковый субъект (`?movie`) и одинаковый объект (`?person`). 
Для любого заданного фильма и человека должны существовать RDF-утверждения, связывающие фильм и человека с использованием предикатов `schema:director` и `imdb:leadActor`.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX imdb: <http://academy.ontotext.com/imdb/>

SELECT * { 
	?movie schema:director ?person ;
           imdb:leadActor ?person .
} ORDER BY ?person
```

Таблица показывает результаты выполнения запроса.

![](./images/graphdb-sparql-5.png)

Как и в предыдущем запросе, в следующем запросе мы выбираем фильмы и людей, которые являются как главными актёрами, так и режиссёрами. В этом запросе мы также используем `GROUP BY ?person` для группировки результатов по человеку и `COUNT(?movie)` для подсчёта количества фильмов, удовлетворяющих критериям для каждого человека. Подсчитанное количество возвращается в переменной `?numMovies`.

```sparql
PREFIX schema: <http://schema.org/>
PREFIX imdb: <http://academy.ontotext.com/imdb/>

SELECT ?person (COUNT(?movie) as ?numMovies) { 
	?movie schema:director ?person ;
           imdb:leadActor ?person .
} GROUP BY ?person ORDER BY DESC(?numMovies)
```

Таблица показывает результаты выполнения запроса.

![](./images/graphdb-sparql-6.png)

Так как мы также использовали `ORDER BY DESC(?numMovies)` для сортировки результатов по количеству фильмов в порядке убывания, мы легко можем увидеть, что как Клинт Ист伍уд, так и Уоди Аллен снялись в 10 фильмах, где они были как главными актёрами, так и режиссёрами.
