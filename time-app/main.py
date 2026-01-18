from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/time", methods=["GET"])
def current_time():
    now = datetime.utcnow().isoformat() + "Z"
    return jsonify({"utc_time": now})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002)
