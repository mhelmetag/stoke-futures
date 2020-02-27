FROM python:3.8

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt

COPY . /app

EXPOSE 8000

CMD uvicorn web:app --host 0.0.0.0 --port $PORT