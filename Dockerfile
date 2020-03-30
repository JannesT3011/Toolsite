FROM python:3

WORKDIR /toolsite

ADD . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD python app.py