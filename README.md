# Quizzer

### Стек:
![Python](https://img.shields.io/badge/Python-171515?style=flat-square&logo=Python)![3.12.0](https://img.shields.io/badge/3.12.0-blue?style=flat-square&logo=3.12.0)
![Django](https://img.shields.io/badge/Django-171515?style=flat-square&logo=Django)![4.2.14](https://img.shields.io/badge/4.2.14-blue?style=flat-square&logo=4.2.14)
![SQLite](https://img.shields.io/badge/SQLite-171515?style=flat-square&logo=SQLite)![3.46.0](https://img.shields.io/badge/3.46.0-blue?style=flat-square&logo=3.46.0)
![Pytest](https://img.shields.io/badge/Pytest-171515?style=flat-square&logo=Pytest)

### Описание
**_Quizzer_** - сервис для прохождения увлекателных тестов/опросов, позволяющий проходить тесты, получать за это баллы, на которые можно покупать невероятные цвета для своей рамки, и многое другое (ничего).

### Запуск проекта (локально)
**Команды проверялись на Windows, но большая часть должна работать и на Linux*
**Для проверки исользовался PowerShell 7.4.2*

На машине должен быть установлен Python версии 3.12 или совместимый с ним. Если нет, то установить можно отсода: https://www.python.org/downloads/. Проверить, установлен ли Python можно командой python --version
```bash
python --version
Python 3.12.0
```

Также для кло
```bash
git version
git version 2.43.0.windows.1
```

В командной строке переходим в каталог (команда cd), где будет хранится проект, клонируем репозиторий и переходим в него:
```bash
cd <ИМЯ КАТАЛОГА>
git clone https://github.com/vitsmirnov/quizzer
cd quizzer
```

Создаём и активируем виртуальное окружение:
```bash
python -m venv .venv
./.venv/Scripts/Activate.ps1
```
**Если виртуальное окружение успешно установлено и активировано, в командной строке должна появится соответствующая надпись* **(.venv)** *(справедливо для PowerShell)*
**Деактивировать виртуальное окружение можно командой* **deactivate**
**Если команда python не работает, можно попробовать* **python3**

Обновляем pip до последней версии:
```bash
python -m pip install --upgrade pip
```

Устанавливаем зависимости (находясь в виртуальном окружении):
```bash
python -m pip install -r requirements.txt
```

На момент написания проект зависит только от Django (помимо Python), а зависимости, необходимые для работы Django, он установит самостоятельно. Поэтому в requirements.txt только Django, но после установки должны появится следующие приложения, что можно проверить командой **pip list**
```bash
pip list
asgiref  3.8.1
Django   4.2.14
pip      24.1.2
sqlparse 0.5.1
tzdata   2024.1
```
**Если команда* **pip list** *не работает, можно попробовать команду* **python -m pip list**

//git clone https://github.com/vitsmirnov/quizzer
//cd quizzer-main

python -m pip install -r requirements.txt


//python manage.py makemigrations
//python manage.py migrate
//python manage.py createsuperuser



### Запуск на локальной машине:
#### Создаем и активируем виртуальное окружение в корневой папке task_for_kokoc, для выхода из папки введите команду ```cd ..```:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```
#### Обновиляем pip и ставим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

#### Открываем в консоли папку backend:
```bash
cd backend
```

#### Обновиляем pip и ставим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate --noinput
```

#### Создайте суперпользователя Django:
```bash
python manage.py createsuperuser
```

#### Запускаем сервер:
```bash
python manage.py runserver
```

#### Теперь сервер доступен по адресу - http://localhost:8000 админка доступна по - http://localhost:8000/admin/.

--------------------------

### Задание
#### Создать сервис прохождения опросов пользователями на Django.
#### Обязательная часть:
1. Можно зарегистрироваться и логинится. Наверху показано под каким логином ты зашел.
2. Тесты и ответы на них создаются динамически через админку.
3. Список тестов выводится в виде содержания произвольного вида (столбец, таблица, как удобно) Фронт делается с помощью шаблонизатора Django, СУБД произвольная

### Опция 1.

1. За прохождение тестов начисляется какое-то количества валюты.
2. Валюту можно потратить на перекрашивание рамки логина или бэкграунда на странице профиля.
3. Показывать список пользователей и количество пройденных тестов на отдельной странице, там же показывать цветовую дифференциацию пользователей.

### Опция 2.
1. Сделать фронт на реакте, в виде SPA или отдельных модулей.



### Маршруты
| Название | Метод | Описание | Авторизация |
|----------|-------|----------|-------------|
| /                          | GET      | Список тестов и поиск по названию | нет
| test/<<int:pk>>/           | GET/POST | Страница теста                    | Да
| ...                        |          |                                   | 
| auth/signup/               | GET/POST | Зарегестрироваться                | Да
| auth/login/                | GET/POST | Авторизоваться                    | Да
| auth/logout/               | GET/POST | Выйти                             | Да
| users/                     | GET/POST | Список пользователей и количество пройденных тестов, и их цвета | Да
| profile/                   | GET/POST | Профиль пользователя с выбором купленных цветов                 | Да
| buy/                       | GET/POST | Список цветов доступных для покупки                             | Да


### Запуск проекта
Клонируем репозиторий и переходим в него:
```bash
gh clone https://github.com/PivnoyFei/task_for_kokoc.git
cd task_for_kokoc
```

### Перед запуском сервера, необходимо создать .env файл расположенный по пути infra/.env со своими данными.
### Ниже представлены параметры по умолчанию.
```bash
SECRET_KEY='key' # Секретный ключ джанго
DEBUG='True' # Режим разработчика
ALLOWED_HOSTS='localhost' # Адрес

DB_ENGINE='django.db.backends.postgresql'
DB_NAME='postgres' # имя БД
POSTGRES_USER='postgres' # логин для подключения к БД
POSTGRES_PASSWORD='postgres' # пароль для подключения к БД
DB_HOST='db' # название контейнера
DB_PORT='5432' # порт для подключения к БД
```

#### Чтобы сгенерировать безопасный случайный секретный ключ, используйте команду:
```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### Для запуска в Docker:
#### Переходим в папку с файлом docker-compose.yaml:
```bash
cd infra
```

#### Запуск docker-compose:
```bash
docker-compose up -d --build
```

#### Примените миграции:
```bash
docker-compose exec backend python manage.py makemigrations
docker-compose exec backend python manage.py migrate --noinput
```

#### Загрузите подготовленные цвета в базу данных:
в папке data - ```colors.json```, ```tests.json```
```bash
docker-compose exec backend python manage.py load_items colors.json
```

#### Создайте суперпользователя Django:
```bash
docker-compose exec backend python manage.py createsuperuser
```

#### После успешной сборки, на сервере выполните команды (только после первого деплоя):
```bash
docker-compose exec backend python manage.py collectstatic --noinput
```

#### Теперь сервер доступен по адресу - http://localhost админка доступна по - http://localhost/admin/.

#### Останавливаем контейнеры:
```bash
docker-compose down -v
```

### Запуск на локальной машине:
#### Создаем и активируем виртуальное окружение в корневой папке task_for_kokoc, для выхода из папки введите команду ```cd ..```:
```bash
python3 -m venv venv
source venv/bin/activate
```
#### для Windows
```bash
python -m venv venv
source venv/Scripts/activate
```
#### Обновиляем pip и ставим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r backend/requirements.txt
```

#### Открываем в консоли папку backend:
```bash
cd backend
```

#### Обновиляем pip и ставим зависимости из requirements.txt:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

#### Примените миграции:
```bash
python manage.py makemigrations
python manage.py migrate --noinput
```

#### Создайте суперпользователя Django:
```bash
python manage.py createsuperuser
```

#### Запускаем сервер:
```bash
python manage.py runserver
```

#### Теперь сервер доступен по адресу - http://localhost:8000 админка доступна по - http://localhost:8000/admin/.

#### Автор
[Смелов Илья](https://github.com/PivnoyFei)

# Dillinger
## _The Last Markdown Editor, Ever_

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Dillinger is a cloud-enabled, mobile-ready, offline-storage compatible,
AngularJS-powered HTML5 Markdown editor.

- Type some Markdown on the left
- See HTML in the right
- ✨Magic ✨

## Features

- Import a HTML file and watch it magically convert to Markdown
- Drag and drop images (requires your Dropbox account be linked)
- Import and save files from GitHub, Dropbox, Google Drive and One Drive
- Drag and drop markdown and HTML files into Dillinger
- Export documents as Markdown, HTML and PDF

Markdown is a lightweight markup language based on the formatting conventions
that people naturally use in email.
As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually- written in Markdown! To get a feel
for Markdown's syntax, type some text into the left window and
watch the results in the right.

## Tech

Dillinger uses a number of open source projects to work properly:

- [AngularJS] - HTML enhanced for web apps!
- [Ace Editor] - awesome web-based text editor
- [markdown-it] - Markdown parser done right. Fast and easy to extend.
- [Twitter Bootstrap] - great UI boilerplate for modern web apps
- [node.js] - evented I/O for the backend
- [Express] - fast node.js network app framework [@tjholowaychuk]
- [Gulp] - the streaming build system
- [Breakdance](https://breakdance.github.io/breakdance/) - HTML
to Markdown converter
- [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

## Installation

Dillinger requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd dillinger
npm i
node app
```

For production environments...

```sh
npm install --production
NODE_ENV=production node app
```

## Plugins

Dillinger is currently extended with the following plugins.
Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |

## Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:

```sh
node app
```

Second Tab:

```sh
gulp watch
```

(optional) Third:

```sh
karma test
```

#### Building for source

For production release:

```sh
gulp build --prod
```

Generating pre-built zip archives for distribution:

```sh
gulp build dist --prod
```

## Docker

Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the
Dockerfile if necessary. When ready, simply use the Dockerfile to
build the image.

```sh
cd dillinger
docker build -t <youruser>/dillinger:${package.json.version} .
```

This will create the dillinger image and pull in the necessary dependencies.
Be sure to swap out `${package.json.version}` with the actual
version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on
your host. In this example, we simply map port 8000 of the host to
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <youruser>/dillinger:${package.json.version}
```

> Note: `--capt-add=SYS-ADMIN` is required for PDF rendering.

Verify the deployment by navigating to your server address in
your preferred browser.

```sh
127.0.0.1:8000
```

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
