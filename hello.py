from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

@app.route("/works")
def works():
    return "It Works!"

if __name__=='__main__':
    app.run(debug=True, port=8000)