FROM python:3.12-slim

WORKDIR /code

COPY ./requirements.txt /code/

RUN pip install -r /code/requirements.txt

COPY . .

LABEL authors="lukashermadini"

ENTRYPOINT ["Bash", "entrypoint.sh"]

CMD ["python", "manage.py", "runserver"]