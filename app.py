
from flask import Flask, render_template, request, jsonify
from ocr import scan_document
import os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scan", methods=["POST"])
def scan():
    file = request.files["document"]

    os.makedirs("uploads", exist_ok=True)

    path = os.path.join("uploads", file.filename)
    file.save(path)

    text = scan_document(path)

    os.remove(path)

    return jsonify({"text": text})


if __name__ == "__main__":
    app.run(debug=True, port=5050)