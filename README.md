## Полезная информация

В репозиторий добавлен **Makefile** с полезными командами.
Команды вызываются в консоли вот таким образом:

```shell
make linters

make install_reqs
```

## Структура проекта

Для удобства и соблюдения принципов чистой архитектуры проект разделен на следующие пакеты:

- `configurations` — слой для хранения конфигураций, констант, параметров и настроек проекта.

- `models` — слой для хранения моделей (ORM или Data Classes).

- `routers` — слой для настроек урлов для различных эндпоинтов.

- `schemas` — слой содержащий схемы pydantic, отвечает за сериализацию и валидацию.

## Полезные ссылки (в основном на английском)

#### По Fastapi:

1. [Официальная документация](https://fastapi.tiangolo.com/)

2. [Лучшие практики](https://github.com/zhanymkanov/fastapi-best-practices)

3. [Собрание полезных библиотек и пакетов](https://github.com/mjhea0/awesome-fastapi)

4. [Полезная статья по структуре проекта](https://camillovisini.com/coding/abstracting-fastapi-services)

#### По принципам REST архитектуры:

5. [Полезные рекомендации по правильному написанию REST API](<https://github.com/stickfigure/blog/wiki/How-to-(and-how-not-to)-design-REST-APIs>)

#### По SQLAlchemy:

6. [Хороший бесплатный видеокурс на YouTube. На русском языке](https://youtube.com/playlist?list=PLeLN0qH0-mCXARD_K-USF2wHctxzEVp40&si=V7rZGqu1KVJvidLz)

7. [Видеокурс построенный по официальной доке SQLAlchemy. На русском языке](https://youtube.com/playlist?list=PLN0sMOjX-lm5Pz5EeX1rb3yilzMNT6qLM&si=ShZ41fEfSR0s0op4)
# mts_shad_fastapi_project
