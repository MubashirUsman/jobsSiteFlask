from flask import Flask, render_template

app = Flask(__name__)

COMMAND= [
  {
    'id': 1,
    'Name': "lsblk",
    'used': 'list block devices'
  },
    {
    'id': 2,
    'Name': "fdisk",
    'used': 'show detailed information about block devices'
  },
    {
    'id': 3,
    'Name': "mount",
    'used': 'mount a partition'
  },
    {
    'id': 4,
    'Name': "uname -r",
    'used': 'kernal version'
  }
]
@app.route("/")
def helloWorld():
  return render_template('home.html', command=COMMAND)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)