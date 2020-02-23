FROM tiangolo/uwsgi-nginx-flask:python3.7

RUN pip install -U pip
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

COPY . /app

CMD ["python", "/app/run.py"]