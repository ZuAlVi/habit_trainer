FROM python:3

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

COPY . .

# Команда для запуска приложения при старте контейнера
#CMD ["python", "manage.py", "runserver"]