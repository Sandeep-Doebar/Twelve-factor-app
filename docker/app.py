#code for basic python app
import redis
from flask import Flask
import os  
from datetime import datetime

app = Flask(__name__)
redisDb = redis.Redis(host=os.environ['HOST'], port=os.environ['PORT'])

@app.route('/')
def Santwelvefactorapp():
    date = datetime.now()    
    redisDb.incr('visitorCount')
    visitCount = str(redisDb.get('visitorCount'), 'utf-8')
    return "Welcome to my twelvefactorapp! The current date is " + date.strftime("%m/%d/%Y, %H:%M:%S") +" And the Visitor Count is: " + visitCount

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) 