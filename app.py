from flask import Flask

app = Flask(__name__)

print("由Zengtudor开发")


@app.route('/')
def hello_world():  # put application's code here
    return "Hello world!"


if __name__ == '__main__':
    app.run()
