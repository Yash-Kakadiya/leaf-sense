"""
Plant Disease Detection System - Flask Web Application
"""

import os
import uuid

from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

from model import load_model, predict
from classes import DISEASE_INFO

app = Flask(__name__)
app.secret_key = os.urandom(24)

UPLOAD_FOLDER = os.path.join("static", "uploads")
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load model once at startup
model = load_model()


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    # Gather sample images for gallery
    samples_dir = os.path.join("static", "samples")
    sample_images = []
    if os.path.isdir(samples_dir):
        for fname in sorted(os.listdir(samples_dir)):
            if fname.lower().endswith((".png", ".jpg", ".jpeg")):
                sample_images.append(fname)
    return render_template("index.html", sample_images=sample_images)


@app.route("/predict", methods=["POST"])
def predict_route():
    # Check if file was provided
    if "file" not in request.files:
        flash("No file selected. Please upload a leaf image.", "error")
        return redirect(url_for("index"))

    file = request.files["file"]
    if file.filename == "":
        flash("No file selected. Please upload a leaf image.", "error")
        return redirect(url_for("index"))

    if not allowed_file(file.filename):
        flash("Invalid file type. Please upload a PNG, JPG, or JPEG image.", "error")
        return redirect(url_for("index"))

    # Save uploaded file with unique name
    filename = secure_filename(file.filename)
    unique_name = f"{uuid.uuid4().hex}_{filename}"
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], unique_name)
    file.save(filepath)

    try:
        results = predict(model, filepath)
    except Exception:
        flash(
            "An error occurred during prediction. Please try again with a valid leaf image.",
            "error",
        )
        return redirect(url_for("index"))

    top = results[0]
    disease_info = DISEASE_INFO.get(top["class_name"], {})

    return render_template(
        "result.html",
        results=results,
        top=top,
        disease_info=disease_info,
        image_path=f"uploads/{unique_name}",
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
