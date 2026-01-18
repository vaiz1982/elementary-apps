from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(silent=True) or {}
    return jsonify({"echo": data})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8004)
