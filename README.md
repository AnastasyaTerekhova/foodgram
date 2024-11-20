# Foodgram
Сайт, куда можно выкладывать рецепты. Есть система регистрации через JWT-токен (Djoser). Можно подписаться на другого пользователя. Система поиска по тегам. Ингредиенты и теги может добавить только админ. Можно добавить рецепт в избранное, а ингредиенты в  список покупок. Список покупок можно скачать файлом. Бэкенд часть сайта написана на Django, фронтенд - на React. Проект упакован в контейнеры, настроено CI/CD.

# Нужно доработать:
теги оттображаюстся в линию, при слишком большом колличестве все не видны.
подключить страницы "о проекте"
если нет подписок, на странице "мои подписки" это должно отбражаться

# Как подключить:
Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone https://github.com/AnastasyaTerekhova/foodgram.git
cd foodgram/backend
```

В локальной папке проекта создать и активировать виртуальное окружение:
```bash
# Команды для Windows:
python -m venv env
source env/Scripts/activate

# Команды для Linux и macOS:
python3 -m venv env
source env/bin/activate
```

Обновить пакетный менеджер:
```bash
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```

Выполнить команды:
```bash
cd infra
docker compose up -d
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /static/
```
# Документация
Можно посмотреть по ссылке после развертывания проекта
http://localhost/api/docs/