FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /app

WORKDIR /app

ADD requirements.txt /app/

RUN pip install -r requirements.txt

ADD . /app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]