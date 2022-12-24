# Penny Stacks: Django Postgres

Implementation using Django, Django ORM, and Postgres.

No Rest Framework.

## Migrate
```shell
python manage.py migrate
```

## Build
```shell
pip install -r requirements.txt
```

## Launch with gunicorn
```shell
gunicorn django_postgres.wsgi:application 
```