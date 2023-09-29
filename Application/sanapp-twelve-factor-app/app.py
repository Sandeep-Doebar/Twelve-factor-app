#code for basic python app
from flask import Flask
app = Flask(__name__)

@app.route('/')
def welcomeToSanApp():
    return "Welcome to SanApp!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)