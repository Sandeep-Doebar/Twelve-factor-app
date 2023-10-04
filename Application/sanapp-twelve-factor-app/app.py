#code for basic python app
import redis
from flask import Flask


app = Flask(__name__)
redisDb = redis.Redis(host='redis', port=6379)

@app.route('/')
def Santwelvefactorapp():
    redisDb.incr('visitorCount')
    visitCount = str(redisDb.get('visitorCount'), 'utf-8')
    return "Welcome to my twelvefactorapp! Visitor Count: " + visitCount

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) 