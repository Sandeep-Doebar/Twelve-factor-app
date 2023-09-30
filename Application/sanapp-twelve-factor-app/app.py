#code for basic python app
from flask import Flask
from redis import Redis

app = Flask(__name__)
redisDb = Redis(host=os.getenv('HOST'), port=os.getenv('PORT'))

@app.route('/')
def Santwelvefactorapp():
    redisDb.incr('visitorCount')
    visitCount = str(redisDb.get('visitorCount'), 'utf-8')
    global visitCount
    visitCount+=1
    return "Welcome to my twelvefactorapp! Visitor Count: " + str(visitCount)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True) 