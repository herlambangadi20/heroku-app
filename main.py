from flask import Flask
from module.user.route import user_bp
app = Flask(__name__)
app.register_blueprint(user_bp, url_prefix='/user')

@app.route("/")
def hello():
    return 'hello'


# if __name__=='__main__':
#     app.run(debug=True, port=8000)