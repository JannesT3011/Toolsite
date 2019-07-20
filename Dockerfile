FROM python:3

LABEL maintainer="Bmbus"

WORKDIR /usr/Toolsite

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]