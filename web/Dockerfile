FROM python:3.5.2-alpine

RUN python -m pip install --upgrade pip

RUN apk update && apk add libpq 
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

ADD requirements.txt requirements.txt

RUN mkdir /code
WORKDIR /code
ADD . /code

RUN pip install --no-cache-dir -r requirements.txt

RUN apk del .build-deps

EXPOSE 8000

CMD ["gunicorn", "mysite.wsgi", "0:8000"]
