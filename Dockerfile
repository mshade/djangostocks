from python:3-alpine
ENV PYTHONBUFFERED 1
RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip install -r requirements.txt
ADD manage.py startserver.sh /app/
ADD quotes /app/quotes
ADD stocks /app/stocks

CMD sh startserver.sh
