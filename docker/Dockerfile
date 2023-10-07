#docker file to create build twelve factor app
FROM python:3.7-alpine
WORKDIR /usr/app
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD [ "redis-server", "/usr/app/local/etc/redis/redis.conf" ]
CMD [ "python", "app.py" ]