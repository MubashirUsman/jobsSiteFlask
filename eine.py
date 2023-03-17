from flask import Flask

app = Flask(__name__)


@app.route("/")
def helloWorld():
  return "<h1>Hello, Mubashir</h1>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)