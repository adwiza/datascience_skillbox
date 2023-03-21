FROM python:3.10-slim-bullseye
WORKDIR /App
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD [ "python", "app.py" ]