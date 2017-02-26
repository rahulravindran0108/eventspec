FROM python:2.7

ADD requirements.txt /config/requirements.txt
RUN pip install -r /config/requirements.txt

COPY . /eventspec

WORKDIR eventspec

CMD ["python", "manage.py", "runserver"]

