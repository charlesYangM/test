# coding=UTF-8
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello 张添!'

if __name__ == '__main__':
    app.run()