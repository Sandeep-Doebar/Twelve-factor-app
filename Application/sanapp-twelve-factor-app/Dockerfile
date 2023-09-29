#docker file to create build twelve factor app
FROM python

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]