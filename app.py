from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!12323213213213213213213'
    return 'Hello World!12323213213213213213213'

#123123132131132

if __name__ == '__main__':
    app.run()
