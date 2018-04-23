from python:3-alpine
# For immediate output to stdout
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt

ADD manage.py genenv.py startserver.sh example.env /app/
ADD quotes /app/quotes
ADD stocks /app/stocks

CMD sh startserver.sh