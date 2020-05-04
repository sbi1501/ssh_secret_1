# ssh_secret

## Development

```
docker-compose build

docker-compose up -d

docker-compose logs -f

docker-compose up -d --build

docker-compose exec web python manage.py migrate --noinput

docker-compose exec db psql --username=username --dbname=dbname

docker-compose down -v
```

## Production

```
docker-compose -f docker-compose.prod.yml up -d --build
```