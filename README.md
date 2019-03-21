# Morphological Analysis API Server on docker
## on local
### set up
```
$ cp .env.example .env
$ vim .env
$ pip install pipenv
$ pipenv install --dev
```

### run app
```
$ cp .env.example .env
$ vim .env
$ pipenv shell
$ cd source
$ python app.py
```

## on docker container
### set up
```
$ docker-compose build
```

### run app
```
$ docker-compose up
```

## API
`GET /parse` with `q` param
```
$ curl "http://localhost:8080/parse?q=きゃりーぱみゅぱみゅ"
```

## lint
```
$ pipenv run pylint
$ pipenv run flake
```
