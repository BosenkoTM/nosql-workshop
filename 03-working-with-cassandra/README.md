# Работа в Cassandra
На этом семинаре мы научимся использовать базу данных Apache Cassandra NoSQL.

Мы предполагаем, что описанная [здесь](../01-environment) платформа запущена и доступна.

## Подключение к среде Cassandra

### Использование утилиты командной строки Cassandra

Вы можете найти утилиту командной строки `cqlsh` внутри контейнера Cassandra Docker, работающего как часть платформы. Подключитесь через SSH к Docker Host и выполните следующую команду `docker exec`

```
sudo docker exec -ti cassandra-1 cqlsh -u cassandra -p cassandra
```

Это подключит вас к контейнеру `cassandra-1` и запустит `cqlsh` внутри id. Вы должны увидеть вывод, похожий на этот.

```bash
bigdata@bigdata:~$ docker exec -ti cassandra-1 cqlsh-u cassandra -p cassandra
Connected to CassandraCluster at 127.0.0.1:9042.
[cqlsh 5.0.1 | Cassandra 3.11.19 | CQL spec 3.4.4 | Native protocol v4]
Use HELP for help.
cqlsh>
```

Теперь вы находитесь в командной строке Cassandra CQL и готовы выполнять операторы CQL.

Мы также можем увидеть актуальную версию Cassandra, CQL и cqlsh, доступную нам.

Попробуйте выполнить следующий оператор CQL

```sql
SELECT * FROM system_schema.keyspaces;
```

и вы должны увидеть существующие в настоящее время пространства ключей в качестве результатов

```bash
cqlsh> SELECT * FROM system_schema.keyspaces;


 keyspace_name      | durable_writes | replication
--------------------+----------------+-------------------------------------------------------------------------------------
        system_auth |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '1'}
      system_schema |           True |                             {'class': 'org.apache.cassandra.locator.LocalStrategy'}
 system_distributed |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
             system |           True |                             {'class': 'org.apache.cassandra.locator.LocalStrategy'}
      system_traces |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '2'}

(5 rows)
```

### Использование браузерного графического интерфейса
Вместо работы через командную строку и, следовательно, необходимости подключаться к Docker Host через SSH, мы также можем использовать браузерный графический интерфейс для доступа к Cassandra. В качестве части платформы доступны две браузерные утилиты.

#### Cassandra Web

Первый — [Cassandra Web](http://avalanche123.com/cassandra-web/).
В окне браузера перейдите по адресу <http://localhost:28120/>, и вы сразу попадете на главный экран, как показано ниже.

![Alt Image Text](./images/cassandra-web.png "Cassandra Web GUI")

Если нажать кнопку **Execute CQL** в правом верхнем углу, появится всплывающее окно, в котором можно ввести операторы CQL и выполнить их.

#### Apache Zeppelin

Другой универсальный инструмент «данных» — [Apache Zeppelin](http://zeppelin.apache.org). В окне браузера перейдите на <http://localhost:28080/>, и вы сразу же попадете на главный экран, как показано ниже.
![Alt Image Text](./images/apache-zeppelin.png "Apache Zeppelin")

Click on **Login** in the top right corner and enter `admin` into the **User Name** and `abc123!` into the **Password** field. Click **Login** and the home screen should refresh to show some preinstalled notebooks.
Нажмите **Войти** в правом верхнем углу и введите `admin` в поле **User Name** и `abc123!` в поле **Password**. Нажмите **Login**.
![Alt Image Text](./images/apache-zeppelin-2.png "Apache Zeppelin")

Apache Zeppelin использует так называемую модель на основе «Notebook», которая позволяет выполнять интерактивную аналитику данных и совместную работу с документами на основе SQL, Scala и т. д.

Zeppelin использует концепцию интерпретаторов. Каждый интерпретатор может «общаться» с заданными системами данных. При создании Notebook вы можете указать интерпретатор «по умолчанию», все остальные интерпретаторы также могут использоваться, но тогда в каждой ячейке должна использоваться директива `%<interpreter-name>`.

Zeppelin подключил интерпретатор Cassandra, который мы будем здесь использовать. Но прежде чем мы сможем его использовать, его нужно настроить. Щелкните раскрывающийся список **anonymous** или **User Name** вверху справа  и выберите **Interpreter**, как показано на изображении ниже.

![Alt Image Text](./images/apache-zeppelin-navigate-interpreter.png "Apache Zeppelin Interpreter")

Выбрать **Cassandra** Interpreter, выполнив поиск или прокрутив страницу вниз, чтобы добраться до него. Нажмите **edit** и измените **cassandra.credentials.username** на `cassandra`, **cassandra.credentials.password** на `cassandra` и свойство **cassandra.host** на `cassandra-1` (имя службы нашего узла Cassandra в конфигурации docker-compose).

![Alt Image Text](./images/apache-zeppelin-interpreter-cassandra.png "Apache Zeppelin Cassandra Interpreter")

Прокрутите вниз до конца настроек интерпретатора и нажмите **Save**. Подтвердите, чтобы Zeppelin перезапустил интерпретатор с новыми настройками.

Нажмите **Zeppelin** в верхнем левом углу, чтобы вернуться на главный экран.

Создадим новый блокнот, нажав на ссылку **Create new note**. Во всплывающем окне введите `Cassandra` в поле **Note Nam** и выберите **cassandra** для **Default Interpreter** и нажмите **Create**.


![Alt Image Text](./images/apache-zeppelin-create-notebook.png "Apache Zeppelin Cassandra Create Notebook")

Появится пустой блокнот с одной ячейкой. Теперь эта ячейка готова к использованию и имеет назначенную интерпретацию Cassandra. Введите каждую команду в отдельную ячейку и либо щелкните значок **play** справа, либо нажмите **Ctrl-Enter**, чтобы выполнить ячейку. Новая ячейка автоматически появится при выполнении текущей.

Выполните скрипт

```sql
SELECT * FROM system_schema.keyspaces;
```
выполните скрипт, должны увидеть существующие на данный момент пространства ключей

![Alt Image Text](./images/apache-zeppelin-cassandra.png "Apache Zeppelin Cassandra Create Notebook")

Для всех команд, которые следуют сейчас в этом семинаре, вы можете использовать один из 3 различных вариантов, показанных выше.

## Create a Keyspace for the Movie sample

Keyspace в Cassandra является эквивалентом database/schema в реляционных базах данных. При создании keyspace необходимо указать настройки репликации:

```
CREATE KEYSPACE movies WITH replication =
  {'class':'SimpleStrategy','replication_factor':1};
```
Мы будем использовать SimpleStrategy для простоты, поскольку наша настройка Cassandra — это всего лишь один узел.

В производственной среде, где обычно имеется несколько центров обработки данных, обычно используется `NetworkTopologyStrategy`, поскольку она лучше распределяет данные по центрам обработки данных.

Коэффициент репликации = 1 означает, что на определенном узле будет одна копия строки. Более высокие коэффициенты репликации устанавливаются в реальных системах для создания нескольких реплик, что обеспечивает доступность данных в случае сбоев диска.

Чтобы иметь возможность работать с таблицами, вам необходимо использовать свое пространство ключей, как показано в следующем операторе:


```
USE movies;
```
Другой вариант — добавлять к имени таблицы префикс имени пространства ключей во всех запросах, аналогично тому, что вы можете сделать при ссылке на схему.

В любое время вы можете `DESCRIBE` пространство ключей, для этого используйте следующую команду:

```
DESCRIBE KEYSPACE movies;
```

получим

```
CREATE KEYSPACE movies WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;
```

Если вы хотите перечислить все пространства ключей, имеющиеся в базе данных, резервное пространство ключей Cassandra с именем system будет вам полезно. Оно содержит множество системных таблиц для определения объектов базы данных и конфигурации кластера. Давайте перечислим все записи из таблицы `schema_keyspaces`, которая содержит записи для каждого пространства ключей.

Введите следующую команду:

```
SELECT * FROM system_schema.keyspaces;
```

получим

```
 keyspace_name      | durable_writes | replication
--------------------+----------------+-------------------------------------------------------------------------------------
        system_auth |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '1'}
      system_schema |           True |                             {'class': 'org.apache.cassandra.locator.LocalStrategy'}
             movies |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '1'}
 system_distributed |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '3'}
             system |           True |                             {'class': 'org.apache.cassandra.locator.LocalStrategy'}
      system_traces |           True | {'class': 'org.apache.cassandra.locator.SimpleStrategy', 'replication_factor': '2'}
```

## Использование "Static" таблиц (skinny row)

### Создайте таблицы Movie и Actor 

Выполните следующую инструкцию для создания таблицы с именем user. Для тех, кто знаком с SQL, следующий синтаксис должен показаться очень знакомым и почти идентичным. Даже некоторые соглашения об именовании, а также правила форматирования можно использовать повторно.

```sql
DROP TABLE IF EXISTS movies.movie;
CREATE TABLE movies.movie (movie_id int,
	title text,				// title
	release_year int,		// year
	running_time int, 		// runtimes
	languages set<text>, 	// language codes
	genres set<text>,      	// genres
	plot_outline text,    	// plot outline
   cover_url text, 			// cover url
   top250_rank int,			// top 250 rank
   PRIMARY KEY (movie_id)
);
```

Это создает первое статическое семейство столбцов (таблицу) в Cassandra. Теперь сделайте то же самое для таблицы Actor.

```sql
DROP TABLE IF EXISTS movies.actor;
CREATE TABLE movies.actor (actor_id int,
  name text,					// name
  headshot_url text,		// headshot
  mini_biography text,		// mini biography
  birth_date text,			// birth date
  trade_mark list<text>,	// trade mark
  PRIMARY KEY (actor_id)
);
```

Вы можете просмотреть метаданные таблицы с помощью команды `DESCRIBE`, как показано в следующем операторе.

```
DESCRIBE TABLE movie;
DESCRIBE TABLE actor;
```

### Вставка данных в Movie b Actor

В Cassandra операция INSERT на самом деле является "Upsert" (UPDATE или INSERT), что означает, что столбцы обновляются в случае, если строка для данного первичного ключа уже существует, в противном случае все столбцы вставляются заново.

Сначала добавим фильмы "Матрица" и "Криминальное чтиво"

```sql
// insert "The Matrix" - 0133093
INSERT INTO movies.movie (movie_id, title, release_year, running_time, languages,
                   genres, plot_outline, cover_url, top250_rank)
VALUES (0133093,
        'The Matrix',
 		1999,
 		136,
      {'en'},
      {'Action', 'Sci-Fi'},
      $$Thomas A. Anderson is a man living two lives. By day he is an average computer programmer and by night a hacker known as Neo. Neo has always questioned his reality, but the truth is far beyond his imagination. Neo finds himself targeted by the police when he is contacted by Morpheus, a legendary computer hacker branded a terrorist by the government. Morpheus awakens Neo to the real world, a ravaged wasteland where most of humanity have been captured by a race of machines that live off of the humans' body heat and electrochemical energy and who imprison their minds within an artificial reality known as the Matrix. As a rebel against the machines, Neo must return to the Matrix and confront the agents: super-powerful computer programs devoted to snuffing out Neo and the entire human rebellion$$,
      'https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX101_CR0,0,101,150_.jpg',
      19);

// insert "Pulp Fiction" - 0110912
INSERT INTO movies.movie (movie_id, title, release_year, running_time, languages,
                   genres, plot_outline, cover_url, top250_rank)
VALUES (0110912,
 		'Pulp Fiction',
 		1994,
 		154,
 		{'en', 'es', 'fr'},
 		{'Crime', 'Drama'},
 		$$Jules Winnfield (Samuel L. Jackson) and Vincent Vega (John Travolta) are two hit men who are out to retrieve a suitcase stolen from their employer, mob boss Marsellus Wallace (Ving Rhames). Wallace has also asked Vincent to take his wife Mia (Uma Thurman) out a few days later when Wallace himself will be out of town. Butch Coolidge (Bruce Willis) is an aging boxer who is paid by Wallace to lose his fight. The lives of these seemingly unrelated people are woven together comprising of a series of funny, bizarre and uncalled-for incidents.$$,
 		'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY150_CR1,0,101,150_.jpg',
 		8);

// insert "Speed" - 0111257
INSERT INTO movies.movie (movie_id, title, release_year, running_time, languages,
                   genres, plot_outline, cover_url, top250_rank)
VALUES (0111257,
		 'Speed',
		 1994,
		 116,
		 {'en'},
		 {'Action', 'Adventure', 'Crime', 'Thriller'},
		 $$Bomber extortionist's elevator plan backfires, so he rigs a bomb to a LA city bus. The stipulation is: once armed, the bus must stay above 50 mph to keep from exploding. Also if LAPD Officer tries to unload any passengers off, Payne will detonate it. Joe Morton co-stars as Jack's superior, and Jeff Daniels supports Jack helping him try to defuse the bomb.$$,
		 'https://m.media-amazon.com/images/M/MV5BYjc0MjYyN2EtZGRhMy00NzJiLWI2Y2QtYzhiYTU3NzAxNzg4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SY150_CR0,0,101,150_.jpg',
		  null); 		
```

Теперь давайте также добавим некоторых актеров, играющих в этих 2 фильмах.

Давайте добавим актеров "Bruce Willis", "John Travolta", "Sandra Bullock", "Samuel L. Jackson", "Uma Thurman" & "Quentin Tarantino"

```sql
// insert "Bruce Willis" - 0000246
INSERT INTO movies.actor (actor_id, name, headshot_url, birth_date, trade_mark)
VALUES (0000246,
 		'Bruce Willis',
 		'https://m.media-amazon.com/images/M/MV5BMjA0MjMzMTE5OF5BMl5BanBnXkFtZTcwMzQ2ODE3Mw@@._V1_UY98_CR8,0,67,98_AL_.jpg',
 		'1955-03-19',
		 ['Frequently plays a man who suffered a tragedy, had lost something or had a  crisis of confidence or conscience.',
		  'Frequently plays likeable wisecracking heroes with a moral centre',
		  'Headlines action-adventures, often playing a policeman, hitman or someone in the military',
		  'Often plays men who get caught up in situations far beyond their control',
		  'Sardonic one-liners',
		  'Shaven head',
		  'Distinctive, gravelly voice',
		  'Smirky grin.',
		  'Known for playing cynical anti-heroes with unhappy personal lives']);

// insert "John Travolta" - 0000237
INSERT INTO movies.actor (actor_id, name, headshot_url, birth_date, trade_mark)
VALUES (0000237,
		 'John Travolta',
		 'https://m.media-amazon.com/images/M/MV5BMTUwNjQ0ODkxN15BMl5BanBnXkFtZTcwMDc5NjQwNw@@._V1_UY98_CR3,0,67,98_AL_.jpg',
		 '1954-02-18',
		 ['Cleft chin and razor-sharp cheekbones',
		  'Often works some sort of dance into his roles',
		  'New Jersey accent',
		  'Black hair and blue eyes']);


// insert "Sandra Bullock" - 0000113
INSERT INTO movies.actor (actor_id, name, headshot_url, birth_date, trade_mark)
VALUES (0000113,
		'Sandra Bullock',
        'https://m.media-amazon.com/images/M/MV5BMTI5NDY5NjU3NF5BMl5BanBnXkFtZTcwMzQ0MTMyMw@@._V1_UX67_CR0,0,67,98_AL_.jpg',
        '1964-07-26',
        null);

// insert "Samuel L. Jackson" - 0000168
INSERT INTO movies.actor (actor_id, name, headshot_url, birth_date, trade_mark)
VALUES (0000168,
		 'Samuel L. Jackson',
		 'https://m.media-amazon.com/images/M/MV5BMTQ1NTQwMTYxNl5BMl5BanBnXkFtZTYwMjA1MzY1._V1_UX67_CR0,0,67,98_AL_.jpg',
		 '1948-12-21',
		 ['Deep authoritative voice',
		  'Rebellious characters who are disliked or considered strange by others in the story',
		  'Often plays police officers or government officials. Both prone to intimidation or violence',
		  'Often plays very wise and intelligent characters with great capacities for violence',
		  'Frequently plays tough characters who swear a lot',
		  'Frequent swearing',
		  'Often sports a moustache or goatee in his films',
		  'Shaven head',
		  'Kangol hats',
		  'Often plays hotheaded characters with a fiery temper',
		  'Often shouts the word "motherf*****" at some point in a film',
		  'Frequently cast by Quentin Tarantino']);

// insert "Uma Thurman" - 0000235
INSERT INTO movies.actor (actor_id, name, headshot_url, birth_date, trade_mark)
VALUES (0000235,
		 'Uma Thurman',
		 'https://m.media-amazon.com/images/M/MV5BMjMxNzk1MTQyMl5BMl5BanBnXkFtZTgwMDIzMDEyMTE@._V1_UX67_CR0,0,67,98_AL_.jpg',
		 '1970-04-29',
		 ['Long blond hair and blue eyes', 'Statuesque, model-like figure']);

// insert "Keanu Reeves" - 0000206
INSERT INTO movies.actor (actor_id, name, headshot_url, birth_date, trade_mark)
VALUES (0000206,
		 'Keanu Reeves',
 		 'https://m.media-amazon.com/images/M/MV5BNjUxNDcwMTg4Ml5BMl5BanBnXkFtZTcwMjU4NDYyOA@@._V1_UY98_CR4,0,67,98_AL_.jpg',
 		 '1964-09-02',
		 ['Intense contemplative gaze',
		  'Deep husky voice',
		  'Known for playing stoic reserved characters']);

// insert "Quentin Tarantino" - 0000233
INSERT INTO movies.actor (actor_id, name, headshot_url, birth_date, trade_mark)
VALUES (0000233,
         'Quentin Tarantino',
         'https://m.media-amazon.com/images/M/MV5BMTgyMjI3ODA3Nl5BMl5BanBnXkFtZTcwNzY2MDYxOQ@@._V1_UX67_CR0,0,67,98_AL_.jpg',
         '1963-03-27',
         ['Lead characters usually drive General Motors vehicles, particularly Chevrolet and Cadillac, such as Jules 1974 Nova and Vincents 1960s Malibu.',
          'Briefcases and suitcases play an important role in Pulp Fiction (1994), Reservoir Dogs (1992), Jackie Brown (1997), True Romance (1993) and Kill Bill: Vol. 2 (2004).',
          'Makes references to cult movies and television',
          'Frequently works with Harvey Keitel, Tim Roth, Michael Madsen, Uma Thurman, Michael Bowen, Samuel L. Jackson, Michael Parks and Christoph Waltz.',
          'His films usually have a shot from inside an automobile trunk',
          'He always has a Dutch element in his films: The opening tune, Little Green Bag, in Reservoir Dogs (1992) was performed by George Baker Selection and written by Jan Gerbrand Visser and Benjamino Bouwens who are all Dutch. The character Freddy Newandyke, played by Tim Roth is a direct translation to a typical Dutch last name, Nieuwendijk. The code name of Tim Roth is Mr. Orange, the royal color of Holland and the last name of the royal family. The Amsterdam conversation in Pulp Fiction (1994), Vincent Vega smokes from a Dutch tobacco shag (Drum), the mentioning of Rutger Hauer in Jackie Brown (1997), the brides name is Beatrix, the name of the Royal Dutch Queen.',
		  '[The Mexican Standoff] All his movies (including True Romance (1993), which he only wrote and did not direct) feature a scene in which three or more characters are pointing guns at each other at the same time.',
         'Often uses an unconventional storytelling device in his films, such as retrospect (Reservoir Dogs (1992)), non-linear (Pulp Fiction (1994)), or "chapter" format (Kill Bill: Vol. 1 (2003)).',
         'His films will often include one long, unbroken take where a character is  followed around somewhere.']);
```

### Отображение данных

Команда SELECT выводит список содержимого таблицы; фильтр можно применить с помощью предложения WHERE:

```sql
SELECT movie_id, title
FROM movies.movie;
```

Мы также можем выбрать все столбцы, как показано здесь для таблицы «Актёр»:

```sql
SELECT *
FROM movies.actor;
```

Результат предыдущих запросов SELECT может заставить вас задуматься, ведь они похожи на таблицы в РСУБД, неужели данные хранятся в таблицах в Cassandra?

Ответ  таков: хотя CQL предоставляет вам удобный интерфейс, похожий на привычную РСУБД, данные хранятся в Cassandra в соответствии с ее собственной моделью данных.

Что произойдет, если поставить фильтр, например на `name` актера.


```
SELECT *
FROM movies.actor
WHERE name = 'Bruce Willis';
```

You can see that you get an error

```
com.datastax.driver.core.exceptions.InvalidQueryException:
Cannot execute this query as it might involve data filtering and thus may have unpredictable performance.
If you want to execute this query despite the performance unpredictability, use ALLOW FILTERING
```

Cassandra does not allow to restrict on another column than the primary key. Let's see if that is true. When we use the `actor_id` instead the query will work.

```
SELECT *
FROM movies.actor
WHERE actor_id = 0000246;
```

As hinted in the exception, you can force Cassandra to execute a restriction on a non-primary column by adding the `ALLOW FILTERING` clause.

```
SELECT *
FROM movies.actor
WHERE name = 'Bruce Willis'
ALLOW FILTERING;
```

Be careful with this all though. This is **very inefficient** for Cassandra to do and there is a good reason `ALLOW FILTERING` is not enabled by default.

### Updating data
You can use `UPDATE` to change data. As said previously, it will have the same effect as an `INSERT`.

Let's update the actor Bruce Willis and add his middle name.

```
UPDATE movies.actor
SET name = 'Bruce Walter Willis'
WHERE actor_id = 0000246;
```

Check the result with a `SELECT`.

```
SELECT *
FROM movies.actor
WHERE actor_id = 0000246;
```

The same could have been achieved with the following insert, just updating the email to a different value to be able to see the result.

```
INSERT INTO movies.actor (actor_id, name)
VALUES (0000246, 'Bruce Willis');
```

Check the result again with a `SELECT`. You can see that the `name` has been updated.

Now let's show that with an `UPDATE` we can even create a new record:

```
UPDATE movies.actor
SET name = 'Cool Actor'
WHERE actor_id = 99999999;
```

You can clearly see that an `INSERT` will not complain if a row already exists under a given primary key (row key). It will even update that row. A huge difference compared to RDBMS!

Be careful to always pass the right primary key value, otherwise some unexpected results might occur.


### Deleting data

Of course we can also delete data.

Data can be deleted using CQL in one of the following ways

1.	As used before - it deletes column(s) or entire row(s)
2.	`TRUNCATE`: It deletes all rows from the table
3.	`USING TTL`: It sets time to live on column(s) within a row; after expiration of specified period, columns are automatically deleted by Cassandra.


Let's remove the actor with ID 99999999 we have just inserted before with a `DELETE`:

```
DELETE FROM movies.actor
WHERE actor_id = 99999999;
```

Let's see  

```
INSERT INTO movies.actor (actor_id, name)
VALUES (99999998, 'An other actor')
USING TTL 120;
```

So, this test user will automatically be deleted after 120 seconds.

You can check the remaining TTL by using the function TTL on a column

```
SELECT TTL(name), actor_id, name
FROM movies.actor;
```

You can see that all the rows without a TTL return NULL, and the row we have added before returns the number of seconds left until the record is removed.

If you repeatedly execute that statement, you will see the TTL going down until the record is gone.

That finishes our work with static tables. In the next section we will see how we can use dynamic tables, which are much more interesting and important capability of Cassandra.

So far we have only stored information which static in a way that the number of columns we wanted to store by Movie and Actor are static during runtime. Of course we might from time to time extend the data model and might add new columns to an existing table. But this is a development task and can be done using an `ALTER TABLE xxxx ADD COLUMN ...` statement, as we know it from RDBMS.

## Using "Dynamic" Tables (wide row)

Dynamic Tables allow also growing to the side, so the number of columns are basically dynamic at runtime and ever row can have a different number of columns stored in the table / database.

So far our Movies and Actors which we have stored in the so-named static Cassandra table have no "relationships" to each-other. But of course an actor has played in many movies and a movie has many actors playing in it.

For storing this information, wide-row tables are the tool to use in Casandra.

### Create the "Movies by Actor" and "Actors by Movie" tables

Let's start with the Actor and the movies he has played in, which we call `movies_by_actor`.

```
DROP TABLE IF EXISTS movies.movies_by_actor;
CREATE TABLE movies.movies_by_actor (actor_id int,
				movie_id int,  
				title text,
				PRIMARY KEY (actor_id, movie_id)
);
```

We use a name which reflects the query we can resolve using that table.

Now let's continue with the table to get the actors who have played in a given movie, which we call `actors_by_movie`

```
DROP TABLE IF EXISTS movies.actors_by_movie;
CREATE TABLE movies.actors_by_movie (movie_id int,
             title text STATIC,
				actor_id int,  
				name text,
				PRIMARY KEY (movie_id, actor_id)
);
```

### Inserting data to the two tables

Let's add some movies for given actors. Of course in real world they have played in much more movies, this is just a sample of movies for some of the actors which we have in the `actor` table. But not all of the movies we add here to the `movies_by_actor` table are in fact stored in the `movie` table. We can see, there are no foreign keys and nobody can stop us to add movies to that table which are not "known" to us / not stored also in the `movie` table.

```
// Movies for actor "Bruce Willis"

INSERT INTO movies.movies_by_actor (actor_id, movie_id, title)
VALUES (0000246, 0110912, 'Pulp Fiction');

INSERT INTO movies.movies_by_actor (actor_id, movie_id, title)
VALUES (0000246, 1606378, 'A Good Day to Die Hard');

INSERT INTO movies.movies_by_actor (actor_id, movie_id, title)
VALUES (0000246, 0217869, 'Unbreakable');

INSERT INTO movies.movies_by_actor (actor_id, movie_id, title)
VALUES (0000246, 0377917, 'The Fifth Element');

INSERT INTO movies.movies_by_actor (actor_id, movie_id, title)
VALUES (0000246, 0112864, 'Die Hard: With a Vengeance');

// Movies for actor "Keanu Reeves"

INSERT INTO movies.movies_by_actor (actor_id, movie_id, title)
VALUES (0000206, 0133093, 'The Matrix');

INSERT INTO movies.movies_by_actor (actor_id, movie_id, title)
VALUES (0000206, 0234215, 'The Matrix Reloaded');

INSERT INTO movies.movies_by_actor (actor_id, movie_id, title)
VALUES (0000206, 0111257, 'Speed');


// Movies for actor "Sandra Bullock"

INSERT INTO movies.movies_by_actor (actor_id, movie_id, title)
VALUES (0000113, 0111257, 'Speed');
```

Now let's also add some data to the `actors_by_movie` table. Again, not all of the actors we add here are also stored in the `movie` table. In real-world of course they would have to be in sync and when inserting the data this would have been taken care off.

```
// Actors for movie "The Matrix"

INSERT INTO movies.actors_by_movie (movie_id, title, actor_id, name)
VALUES (0133093, 'The Matrix', 0000206, 'Keanu Reeves');

INSERT INTO movies.actors_by_movie (movie_id, title, actor_id, name)
VALUES (0133093, 'The Matrix', 0000401, 'Laurence Fishburne');

INSERT INTO movies.actors_by_movie (movie_id, title, actor_id, name)
VALUES (0133093, 'The Matrix', 0005251, 'Carrie-Anne Moss');

INSERT INTO movies.actors_by_movie (movie_id, title, actor_id, name)
VALUES (0133093, 'The Matrix', 0915989, 'Hugo Weaving');


// Actors for movie "Pulp Fiction"

INSERT INTO movies.actors_by_movie (movie_id, title, actor_id, name)
VALUES (0110912, 'Pulp Fiction', 0000237, 'John Travolta');

INSERT INTO movies.actors_by_movie (movie_id, title, actor_id, name)
VALUES (0110912, 'Pulp Fiction', 0000168, 'Samuel L. Jackson');

INSERT INTO movies.actors_by_movie (movie_id, title, actor_id, name)
VALUES (0110912, 'Pulp Fiction', 0000246, 'Bruce Willis');
```

Now let's see these table in Action. First let's see all the movies "Bruce Willis" has played in.

```
SELECT title
FROM movies.movies_by_actor
WHERE actor_id = 0000246;
```

And now let's see the actors which played in the movie "Pulp Fiction"

```
SELECT name, title
FROM movies.actors_by_movie
WHERE movie_id = 0110912;
```

## Using Counter Columns

For the movie ratings table, we will be using a static table with some columns of type `COUNTER` so that we can easily count the number of stars we gave to each movie.  

Columns of type COUNTER cannot be mixed with other data types and therefore we have to create a new table cannot add these columns to the existing `movie` table.

```
DROP TABLE IF EXISTS movies.rating_by_movie;
CREATE TABLE movies.rating_by_movie (movie_id int,
             one_star counter,  
             two_star counter,  
             three_star counter,  
             four_star counter,  
             five_star counter,
				PRIMARY KEY (movie_id)
);
```

Let's add some ratings for the movie "Pulp Fiction". With columns of type counter you have to use the `UPDATE` command and you can't use an `INSERT`.

```
UPDATE movies.rating_by_movie
SET five_star = five_star + 1
WHERE movie_id = 0110912;

UPDATE movies.rating_by_movie
SET four_star = four_star + 1
WHERE movie_id = 0110912;

UPDATE movies.rating_by_movie
SET five_star = five_star + 1
WHERE movie_id = 0110912;

UPDATE movies.rating_by_movie
SET five_star = five_star + 1
WHERE movie_id = 0110912;

UPDATE movies.rating_by_movie
SET two_star = two_star + 1
WHERE movie_id = 0110912;
```

Check the current ratings for movie "Pulp Fiction"

```
SELECT * FROM movies.rating_by_movie WHERE movie_id = 0110912;
```

Let's also create a table which counts the number of views per movie, separated by male and female viewers and per month.
In this case we create a wide-row table, with `movie_id` for the partition key and `year` and `month` as the clustering key. Additionally we decided to store the clustering columns in descending order by year and month, so that the latest view counts can be retrieved efficiently.

```
DROP TABLE IF EXISTS movies.movie_viewed_by_time;
CREATE TABLE movies.movie_viewed_by_time (movie_id int,
			   year int,
			   month int,
             male counter,
             female counter,
				PRIMARY KEY (movie_id, year, month)
) WITH CLUSTERING ORDER BY (year DESC, month DESC);
```

Add some sample values to the new table

```
// Pulp Fiction Views 2019/03
UPDATE movies.movie_viewed_by_time
SET male = male + 1
WHERE movie_id = 0110912 AND year = 2019 and month = 03;

UPDATE movies.movie_viewed_by_time
SET male = male + 1
WHERE movie_id = 0110912 AND year = 2019 and month = 03;

UPDATE movies.movie_viewed_by_time
SET female = female + 1
WHERE movie_id = 0110912 AND year = 2019 and month = 03;

// Pulp Fiction Views 2019/04
UPDATE movies.movie_viewed_by_time
SET female = female + 1
WHERE movie_id = 0110912 AND year = 2019 and month = 04;

UPDATE movies.movie_viewed_by_time
SET male = male + 1
WHERE movie_id = 0110912 AND year = 2019 and month = 04;

UPDATE movies.movie_viewed_by_time
SET female = female + 1
WHERE movie_id = 0110912 AND year = 2019 and month = 04;

UPDATE movies.movie_viewed_by_time
SET female = female + 1
WHERE movie_id = 0110912 AND year = 2019 and month = 04;

// Pulp Fiction Views 2019/05
UPDATE movies.movie_viewed_by_time
SET male = male + 1
WHERE movie_id = 0110912 AND year = 2019 and month = 05;

UPDATE movies.movie_viewed_by_time
SET male = male + 1
WHERE movie_id = 0110912 AND year = 2019 and month = 05;

UPDATE movies.movie_viewed_by_time
SET female = female + 1
WHERE movie_id = 0110912 AND year = 2019 and month = 05;

UPDATE movies.movie_viewed_by_time
SET female = female + 1
WHERE movie_id = 0110912 AND year = 2019 and month = 05;
```

and see the views for the movie "Pulp Fiction" for all the time

```
SELECT *
FROM movies.movie_viewed_by_time
WHERE movie_id = 0110912;
```

for just one month

```
SELECT *
FROM movies.movie_viewed_by_time
WHERE movie_id = 0110912 AND year = 2019 AND month = 05;
```

or for the month January to May

```
SELECT *
FROM movies.movie_viewed_by_time
WHERE movie_id = 0110912 AND year = 2019 AND month >= 01 AND month <= 5;
```


## Using the Python API with Cassandra

to be done ....


This finishes the workshop for Cassandra.
