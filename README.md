# Проект «API для Yatube»
## Описание

Данное API позволяет использовать следующий функционал:

1. Публикации

- Получать список всех публикаций
- Создавать новую публикацию
- Полностью или частично редактировать публикацию
- Удалять публикацию

2. Сообщества

- Получение списка доступных сообществ
- Получение информации о сообществе

3. Комментарии

- Получение всех комментариев к публикации
- Получение конкретного комментария к публикации
- Добавление нового комментария к публикации

4. Подписка

- Получение списка своих подписчиков
- Подписка на публикации других пользователей


## Как установить и запустить

Чтобы запустить это приложение, вам потребуeтся установленный на вашем компьютере:
1) [Интерпритатор Python 3.9](https://www.python.org/downloads/release/python-390/)
2) [Visual Studio Code](https://code.visualstudio.com/download)
3) [Git](https://code.visualstudio.com/download)

- Клонировать репозиторий:

```sh
git clone git@github.com:Mangekos/yatube_api.git
```

- Перейти в него в командной строке:

```sh
cd api_final_yatube
```

- Cоздать и активировать виртуальное окружение:

```sh
python -m venv venv
source venv/Script/activate
```

- Установить зависимости из файла requirements.txt:

``` sh
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- Выполнить миграции:

```sh
python manage.py migrate
```

- Запустить проект:

```sh
python manage.py runserver
```

- Перейти:

```sh
http://127.0.0.1:8000/
```

## Как использовать

- Это приложение простое в использовании.
- Для аутентификации используются JWT-токены.
- Информация доступна как для незарегистрированных пользователей (доступ к API только на чтение), так и для зарегистрированных.
- Исключение — эндпоинт /follow/: доступ к нему возможен только аутентифицированным пользователям.
- Аутентифицированным пользователям разрешено изменение и удаление своего контента; в остальных случаях доступ предоставляется только для чтения.

Более подробное описание API можно получить по адресу:

http://localhost:8000/redoc/
