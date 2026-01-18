from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/sum", methods=["GET"])
def sum_two():
    try:
        a = float(request.args.get("a", "0"))
        b = float(request.args.get("b", "0"))
    except ValueError:
        return jsonify({"error": "Invalid numbers"}), 400
    return jsonify({"a": a, "b": b, "sum": a + b})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8005)
