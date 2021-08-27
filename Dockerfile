FROM python:3.7.3-slim

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . .
WORKDIR /.

RUN python etl.py

EXPOSE 8000

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000"]