# Quizzer

### Стек:
![Python](https://img.shields.io/badge/Python-171515?style=flat-square&logo=Python)![3.12.0](https://img.shields.io/badge/3.12.0-blue?style=flat-square&logo=3.12.0)
![Django](https://img.shields.io/badge/Django-171515?style=flat-square&logo=Django)![4.2.14](https://img.shields.io/badge/4.2.14-blue?style=flat-square&logo=4.2.14)
![SQLite](https://img.shields.io/badge/SQLite-171515?style=flat-square&logo=SQLite)![3.46.0](https://img.shields.io/badge/3.46.0-blue?style=flat-square&logo=3.46.0)
![Pytest](https://img.shields.io/badge/Pytest-171515?style=flat-square&logo=Pytest)

### Описание
**_Quizzer_** - сервис, позволяющий окунуться в мир увлекательных тестов-квизов и вывести свою эрудицию на принципиально новый уровень! Проходите квизы, получайте и копите за это баллы, которые затем можно потратить на невероятные цвета для рамки своего профиля и многое другое.

#### *Правила*
Проходить квизы могут только авторизованные пользователи и каждый квиз можно пройти только один раз. В каждом вопросе может быть только один правильный вариант ответа*. Вариант ответа можно не указывать, в таком случае ответ будет засчитан как неверный. У каждого вопроса есть стоимость - количество очков, которое начисляется за правильный ответ. Эта стоимость отражает сложность вопроса и показывается рядом с ним на станице квиза. После прохождения квиза будет показан результат с правильными ответами. Результат прохождения теста - сумма очков за правильные ответы. За прохождение квиза начисляется валюта в пропорции одна условная единица за каждый балл. Эту валюту можно тратить на покупку цветов в специальном магазине, которыми можно менять стилизацию своего логина*. Рейтинг пользователя - сумма всех очков/баллов за все пройденные им квизы (не за баланс валюты). Рейтинг пользователей можно посмотреть на отдельной странице.  
**Планируется добавить возможность нескольких правильных ответов в будущем*  
**Это поведение планируется расширить*  

### Запуск проекта (локально)
**На сервере проект пока не тестировался*  
**Команды проверялись на Windows (PowerShell 7.4.2), но большая часть должна работать и на Unix*

На машине должен быть установлен Python версии 3.12 или совместимый с ним. Скачать и установить можно отсода: https://www.python.org/downloads/. Проверить, установлен ли Python, можно командой `python --version`
```bash
python --version
Python 3.12.0
```

Чтобы клонировать репозиторий, должен быть установлен git, но это не обязательно, исходный код можно скачать с GitHub архивом (кнопка для скачивания находится в верхнем правом углу страницы репозитория: <>Code -> Download ZIP). Скачать и установить git можно отсюда: https://git-scm.com/downloads. Проверить, установлен ли git, можно командой `git version`:
```bash
git version
git version 2.43.0.windows.1
```

В командной строке переходим в каталог (команда `cd`), где будет хранится проект, клонируем репозиторий и переходим в него:
```bash
cd <ИМЯ КАТАЛОГА>
git clone https://github.com/vitsmirnov/quizzer
cd quizzer
```
**Создать каталог можно командой* `mkdir <ИМЯ КАТАЛОГА>`

Создаём и активируем виртуальное окружение командой `python -m venv <ИМЯ КАТАЛОГА>` (имя каталога, где будет располагаться окружение, в данном случае `.venv`):
```bash
python -m venv .venv
./.venv/Scripts/Activate.ps1
```
**Команда для активации окружения на Unix:* `source venv/bin/activate`  
**Если виртуальное окружение успешно установлено и активировано, в командной строке должна появится соответствующая надпись* `(.venv)` *(справедливо для PowerShell)*  
**Деактивировать виртуальное окружение можно командой* `deactivate`  
**Если команда python не работает, можно попробовать команду* `python3`  

Обновляем pip до последней версии:
```bash
python -m pip install --upgrade pip
```

Устанавливаем зависимости (виртуальное окружение должно быть активировано):
```bash
python -m pip install -r requirements.txt
```

На момент написания этих строк проект зависит только от Django (помимо Python), а зависимости, необходимые для работы Django, он установит самостоятельно. Поэтому requirements.txt содержит только Django, но после установки должны появится следующие приложения, что можно проверить командой `pip list`:
```bash
pip list
asgiref  3.8.1
Django   4.2.14
pip      24.1.2
sqlparse 0.5.1
tzdata   2024.1
```
**Если команда* `pip list` *не работает, можно попробовать команду* `python -m pip list`

Вместе с проектом в репозитории уже находится тестовая база данных SQLite (файл с именем db.sqlite3), к ней применены миграции и в ней находятся тестовые данные. Подробнее о ней далее.
Если вам не нужна база данных, то нужно удалить или переместить файл db.sqlite3, после чего нужно создать и применить миграции, а затем создать суперюзера для входа в портал администрации Django для редактирования базы данных.
Создать миграции можно командой `python manage.py makemigrations`, а применить миграции командой `python manage.py migrate`:
```bash
python manage.py makemigrations
...
python manage.py migrate
...
```
**Для того, чтобы эти инструкции работали, нужно находиться в каталоге репозитория, где расположен файл manage.py. Это файл, который Django создаёт автоматически при создании проекта и находится в корне репозитория. Подробнее узнать можно здесь:* https://docs.djangoproject.com/en/4.2/ref/django-admin/.

Создать суперюзера можно командой `python manage.py createsuperuser`, где необходимо будет ввести имя, пароль и адрес почты.
```bash
python manage.py createsuperuser
...
```

После того, как суперюзер создан, можно запустить локальный сервер командой `python manage.py runserver`:
```bash
python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
December 31, 1999 - 23:59:59
Django version 4.2.14, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
**Остановить работу локального сервера можно сочетанием клавиш Ctrl+C (для Windows)*

После успешного запуска сервера можно перейти в браузере по адресу http://127.0.0.1:8000/admin, авторизоваться под созданным именем и паролем, и вносить изменения в базу данных.

По адресу http://127.0.0.1:8000/ будет доступно само приложение Quizzer.

Чтобы упростить процесс запуска приложения, в корневом каталоге репозитория находятся скрипты для PowerShell (*.ps1), которые содержат в себе все перечисленные выше команды:
`start.ps1` `cloneandstart.ps1`. Для запуска команды перед ней нужно добавить `./`:
```bash
./start.ps1
...
```
**Скрипты написаны для Windows, но, если заменить команду активации виртуального окружения на* `source venv/bin/activate` *и, возможно, команду* `python` *на* `python3` *, то должны работать и в Unix.*

Эти скрипты не включают в себя команды создания и применения миграций, и создания суперюзера для новой базы данных. Для этого нужно применить команды, описанные выше. Также нужно самостоятельно установить Python и git (см. выше). Если команды не работают, можно попробовать заменить в скриптах команду `python` на `python3`.
Если вы уже клонировали репозиторий с GitHub, то просто запустите скрипт *start.ps1*. Или скачайте/скопируйте скрипт *cloneandstart.ps1* и *start.ps1* в каталог, где будет располагаться проект и запустите его.

Приятного использования!

*Виталий Смирнов, 2024*  
*https://github.com/vitsmirnov*  
*mrmaybelately@gmail.com*  
