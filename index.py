from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/goodbye")
def goodbye():
    return "Goodbye World!"

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello {}".format(name)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
