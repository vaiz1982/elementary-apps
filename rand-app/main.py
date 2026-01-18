from flask import Flask, jsonify
import random

app = Flask(__name__)


@app.route("/random", methods=["GET"])
def random_number():
    value = random.randint(1, 100)
    return jsonify({"value": value})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8003)
