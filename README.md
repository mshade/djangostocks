# Django Quotes
A simple app that reads and presents stock data from JSON

## Data
Data for the application is found in [./quotes/static/quotes_data.json](./quotes/static/quotes_data.json). It's called via HTTP to mimic the spirit of an external API request.

## Running Locally with manage.py runserver
Requirements:
- Python 3 (tested and written on 3.6.5)
- pip
- Virtualenv recommended

```
$ git clone https://github.com/mshade/djangostocks
$ cd djangostocks
$ virtualenv .
$ source bin/activate
$ pip install -r requirements.txt
$ cp example.env .env
# Copy example.env to .env and edit as necessary
# A fresh secret key may be generated with the following command:
$ python manage.py shell -c 'from django.core.management import utils; print(utils.get_random_secret_key())'
$ cp example.env .env
$ ./startserver.sh
```
The app is available at http://localhost:8000/


## Running Locally with docker
[Install docker for your platform](https://docs.docker.com/install/), then clone the repository and build the container:

```
$ git clone https://github.com/mshade/djangostocks
$ cd djangostocks
# Copy example.env to .env, and edit as necessary
$ cp example.env .env
$ docker build -t djangostocks .
$ docker run -d -p 8000:8000 --env-file=.env djangostocks
```

The app is available at http://localhost:8000/

