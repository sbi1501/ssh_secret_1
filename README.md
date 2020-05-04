# ssh_secret

## Запуск контейнеров:

```
docker-compose up -d --build
```

## Остановка контейнеров:

```
docker-compose down -v
```

## Запуск миграций

```
docker-compose exec web python manage.py migrate --noinput
```

## Логи

```
docker-compose logs -f
```

## База данных

```
docker-compose exec db psql --username=username --dbname=dbname
```

## Статические файлы

```
docker-compose exec web python manage.py collectstatic --no-input --clear
```
