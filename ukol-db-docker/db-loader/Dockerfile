FROM python:3.12

WORKDIR /app

COPY ./src /app
COPY ./required.txt /app

RUN pip install -r required.txt

CMD ["python", "loader.py"]