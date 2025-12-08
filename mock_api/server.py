from flask import Flask, request, jsonify
import base64  # not really needed here, but shows how you might extend later

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


TOXIC_KEYWORDS = ["idiot", "stupid", "hate", "trash", "dumb"]


@app.route("/classify", methods=["POST"])
def classify():
    data = request.get_json(silent=True)

    # Missing or empty payload -> 400
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400

    text = data.get("text")
    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Text must be a non-empty string"}), 400

    text_lower = text.lower()

    is_toxic = any(word in text_lower for word in TOXIC_KEYWORDS)

    if is_toxic:
        label = "toxic"
        confidence = 0.92
    else:
        label = "non_toxic"
        confidence = 0.10

    return jsonify({"label": label, "confidence": confidence}), 200


if __name__ == "__main__":
    # Use port 5002 so it doesn't clash with your image project on 5001
    app.run(host="0.0.0.0", port=5002)

