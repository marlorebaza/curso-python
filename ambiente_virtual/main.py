from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hola Marlo"


if __name__ == '__main__':
    # Levantará un servidor web en localhost
    app.run()