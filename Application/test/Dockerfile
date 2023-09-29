#docker file to create build twelve factor app
FROM python:3.10-alpine

WORKDIR /sanapp-twelve-factor-app

COPY . /sanapp-twelve-factor-app/

RUN pip install -r requirements.txt --no-cache-dir

CMD python app.py