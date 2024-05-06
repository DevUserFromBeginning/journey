from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, Ernesto!</p>"

if __name__ == "__main__":
  # remember to change debug to False in production
  app.run(host='0.0.0.0',debug=True) 