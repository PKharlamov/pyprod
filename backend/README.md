# PyProd backend


### Работа с миграциями
* Перейти в директорию /backend
* Создать новую миграцию: `alembic revision --autogenerate -m "migration description"`
* Создать пустую миграцию: `alembic revision -m "migration description"`
* Выполнить все миграции: `alembic upgrade head`
* Откатить одну миграцию: `alembic downgrade -1`
* Выполнить миграции до конкретной версии: `alembic upgrade <target-revision>`
* Откатить миграции до конкретной версии: `alembic downgrade <target-revision>`
* Посмотреть историю миграций: `alembic history`

Нужно учитывать, что autodetect в Alembic не обнаруживает все виды изменений в моделях, 
поэтому миграции перед выполнением надо проверять руками. [Подробнее](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect)

