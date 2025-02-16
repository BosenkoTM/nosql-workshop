# Локальная среда Docker

Убедитесь, что Docker и Docker Compose запущены в вашей локальной среде. Для запуска docker в Windows вам понадобится Windows 10.

* Mac: <https://docs.docker.com/docker-for-mac/>
* Windows 10: <https://docs.docker.com/docker-for-windows/install/>

## Подготовка среды

В виртуальной машине запустите окно терминала и выполните следующие команды.

Сначала добавим переменные среды. Обязательно адаптируйте сетевой интерфейс (**ens33**) в соответствии с вашей средой. Вы можете получить имя интерфейса с помощью **ipconfig** в Windwos или **ifconfig* в Mac/Linux.

```
# Установите переменные среды в соответствии с IP-адресом локальной машины
export PUBLIC_IP=localhost
export DOCKER_HOST_IP=127.0.0.1
```

Теперь для правильной работы Elasticserach нам нужно увеличить параметр `vm.max_map_count`, как показано ниже.

```
# необходимо для elasticsearch
sudo sysctl -w vm.max_map_count=262144
```

Теперь давайте проверим проект NoSQL Workshop с github:

```
# Получите проект
cd
sudo rm -R nosql-workshop/
git clone https://github.com/BosenkoTM/nosql-workshop.git
cd nosql-workshop/01-environment/docker
```

## Запуск среды

И, наконец, давайте запустим среду:

```
# Убедитесь, что среда не запущена
sudo docker compose down

# Запуск среды
sudo docker compose up -d
```

Среда становится сразу доступной, так как все необходимые образы доступны в локальном реестре образов docker.

Вывод должен похож на тот, что приведен ниже.

![Alt ​​Image Text](./images/start-env-docker.png "StartDocker")

Теперь экземпляр готов к использованию. Выполните шаги после установки, описанные [здесь](README.md).

## Остановить среду

Чтобы остановить среду, выполните следующую команду:

```
sudo docker compose stop
```

после этого ее можно перезапустить с помощью `sudo docker compose start`.

Чтобы остановить и удалить все запущенные контейнеры, выполните следующую команду:

```
sudo docker compose down
```
