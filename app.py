from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Work Hard and Build Your Dream!</h1><p>My project is officially deployed!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
