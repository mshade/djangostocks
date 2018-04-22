# Django Quotes
A simple app that reads and presents stock data from JSON

## Data
Data for the application is found in quotes/static/quotes_data.json

## Running Locally with manage.py runserver
Requirements:
- Python 3 (tested and written on 3.6.5)
- pip
- Virtualenv recommended

```
$ git clone https://github.com/mshade/djangostocks
$ cd djangostocks
$ virtualenv .
$ pip install -r requirements.txt
$ ./startserver.sh
```


## Running Locally with docker
Install docker for your platform, then:

```
docker build -t djangostocks .
docker run -d -p 8000:8000 djangostocks
```