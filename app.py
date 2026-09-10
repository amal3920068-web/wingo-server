from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Server is working!"


@app.route("/test")
def test():
    return jsonify({
        "status": "success",
        "message": "Kivy app connected to server!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
