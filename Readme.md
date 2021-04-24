# URL-Shortener Application

Url-Shortener is an application for creating short links for long URLs. User can provide the long URLs and get their short aliases. Upon clicking on those short urls, user will be redirected to its original URL. This application uses:
* **Web framework** - Django
* **Database** - Mongodb

## Execution

### With Docker
#### Prerequisites

```
* Docker
```

#### How to run
Run the following command
```
docker-compose up -d --build
```

Internally, the following things will be done by docker-compose:
* **Initialize a fresh instance of database** : \
When the container is created, it initialize the databse using the MONGO_INITDB_DATABASE variable in docker-compose.yml.
* **Define Mongodb storage in Host System** : \
`data_db` directory will serve as the Mongodb directory for the host system outside the container, and it will be mounted to `/data/db` directory inside the container where Mongodb will write all the files, by default.
* **Database Migration** : \
Following the docker hierarchy, the docker configuration will automatically run the data migration commands by running services `make-migrations` and `migration`.
* **Run the web service** : \
Once the database migration is finished, the docker configuration will automatically run the `web` service.
* **Web-based Mongodb Admin interface** : \
The `mongo-express` serves a web-based admin interface for Mongodb, exposed at port `8081`.

```
* web service : 0.0.0.0:8000
* mongo admin : 0.0.0.0:8081
```

### Without Docker
#### Prerequisites

```
* Python 3.9
* Mongodb
```

#### How to run
* Create and activate `virtualenv` with Python 3.9 and install mongodb. Then run the following commands to install the requirements :
```
$ git clone
$ cd urlShort
$ pip install requirements.txt
```
* Make migrations for database:
```
$ python manage.py makemigrations
```
* Migrate the models :
```
$ python manage.py migrate
```

Before running the server make the following changes in `settings.py` in urlShort directory : 
```
DATABASES = {
   'default' : {
        'ENGINE': 'djongo',
        'ENFORCE_SCHEMA': True,
        'NAME': <databasename>,
        'HOST': <host>,
        'PORT': 27017,
        'USER': <username>,
        'PASSWORD': <password>,
        'AUTH_SOURCE': 'admin',
        'AUTH_MECHANISM': 'SCRAM-SHA-1',
   }
}
```
Finally, run the server :
```
$ python manage.py runserver
```

## License


