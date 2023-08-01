from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!llddddlddddll"


if __name__ == "__main___":
    app.run(host='0.0.0.0', port=81, debug = True)