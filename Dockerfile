 FROM python:3.10

ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt

WORKDIR /src

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]