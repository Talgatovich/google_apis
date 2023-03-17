### Google Sheets API 

#### Получение данных с документа при помощи Google API. Данные должны добавляться в БД

##### Подготовка и запуск проекта

Склонировать репозиторий на локальную машину:

```
git clone git@github.com:Talgatovich/google_apis.git
```
### Перейти в директорию с файлом "docker-compose.yml" 
### Создать файл ".env" и добавить в него
``` 
DJANGO_SECRET_KEY=<Секретный ключ Django>
DB_ENGINE=django.db.backends.postgresql
DB_NAME=<Название базы данных>
POSTGRES_USER=<Имя пользователя>
POSTGRES_PASSWORD=<Пароль пользователя>
DB_HOST=db
DB_PORT=5432


CHAT_ID=<ID вашего профиля в telegram>

```
### Чтобы узнать ID вашего профиля в telegram напишите [боту](https://t.me/userinfobot)


### Создать и запустить контейнеры
```
docker-compose up -d
```
#### Применить миграции

```
docker-compose exec web python manage.py migrate --noinput
```

### Чтобы получать уведомления найдите [бота](https://t.me/google_sheets_notification_bot) и нажмите "Start". 
После перехода на главную страницу приложения,
он пришлет вам сообщение с 
количеством просроченных заказов и их список

##### Введите в адресную строку браузера localhost:8000 : приложение запущено и работает!



Автор: [Ибятов Раиль](https://github.com/Talgatovich)
