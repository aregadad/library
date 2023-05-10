# Личная библиотека
Отображает личную библиотеку в браузере. Работает без интернета.

Протестировать онлайн версию можно по [ссылке](https://aregadad.github.io/library/)

![library main page animation](https://dvmn.org/media/filer_public/11/9f/119fc7d8-216e-4bd1-9c18-b0d54e7c0fdc/ezgifcom-gif-maker_2.gif)

## Простой вариант использования
Скачайте [текущий репозиторий](https://github.com/aregadad/library/archive/refs/heads/main.zip) и откройте `index.html`. Файлы должны быть разархивированы

## Использование через локальный сервер
### Зависимости
Python3 должен быть установлен. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```bash
pip install -r requirements.txt
```

### Как запустить
Запуск на Linux(Python 3) или Windows:

```bash
$ python render_website.py runserver
```

Вы увидите:

```
Site rebuilt
Serving on http://127.0.0.1:5500
Start watching changes
Start detecting changes
...
```
Перейдите по адресу: [localhost:5500](http://localhost:5500/pages/index1.html)

## Где взять книги
Несколько книг уже есть в репозитории. Но можно воспользоваться скриптами из [другого репозитория](https://github.com/aregadad/books), чтобы скачать больше. 
### Расположение файлов
* книги – `./media/books/`
* обложки – `./media/images/`
* books.json – `./media/`

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
