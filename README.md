# Relayer

Relayer serves as a front-end to manage and view [nginx-rtmp-module](https://github.com/arut/nginx-rtmp-module) live streams.

## Local Setup

First, [install Django](https://docs.djangoproject.com/en/1.10/intro/install/). A [virtual environment](https://virtualenv.pypa.io/en/stable/) is also recommended. 

```bash
$ git clone git@github.com:kegwen/relayer.git
$ cd relayer
$ pip install -r requirements.txt
```

Make a copy of relayer/local_settings_example.py named local_settings.py and fill in the variables appropriate to your nginx-rtmp configuration.

## Create a superuser and start the development server

```bash
$ python manage.py createsuperuser
$ python manage.py runserver
```

Navigate to localhost:8000 and log in with the superuser credentials.