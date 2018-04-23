# Django Quotes
A simple app that reads and presents stock data from JSON

## Data
Data for the application is found in [./quotes/static/quotes_data.json](./quotes/static/quotes_data.json). It's called via HTTP to mimic the spirit of an external API request.
The URL can be defined via settings in .env.

## Running Locally with manage.py runserver
Requirements:
- Python 3 (tested and written on 3.6.5)
- pip
- Virtualenv recommended

Check out the repository, then:
```
$ cd djangostocks
# Create and activate virtualenv
$ virtualenv .
$ source bin/activate

$ pip install -r requirements.txt
$ ./startserver.sh
```
The app is available at http://localhost:8000/


## Running Locally with docker
[Install docker for your platform](https://docs.docker.com/install/), then clone the repository and build the container:

```
$ cd djangostocks
$ docker build -t djangostocks .
$ docker run -d -p 8000:8000 djangostocks
```

The app is available at http://localhost:8000/

If you want to work interactively and let django runserver restart when it detects code changes, mount your working directory to the application like so:
```
$ docker run -it -p 8000:8000 -v $(pwd):/app djangostocks
```

You may also customize .env settings via --env:
```
docker run -it -p 8000:8000 --env QUOTES_URL=http://example.com/other_file.json djangostocks
```

## Running locally with docker-compose
Install docker and the [docker-compose](https://docs.docker.com/compose/install/) tool.
The docker-compose.yml file sets up a two container stack to handle static files via, as an example of a "production" style deployment.

```
docker-compose up
```

The app is available at http://localhost:8000/