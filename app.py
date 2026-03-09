"""
Plant Disease Detection System — Flask Web Application
"""

import os
import uuid

from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename

from model import load_model, predict
from classes import CLASS_NAMES, DISEASE_INFO, parse_label

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


def get_sample_images():
    samples_dir = os.path.join("static", "samples")
    sample_images = []
    if os.path.isdir(samples_dir):
        for fname in sorted(os.listdir(samples_dir)):
            if fname.lower().endswith((".png", ".jpg", ".jpeg")):
                sample_images.append(fname)
    return sample_images


@app.route("/")
def index():
    return render_template("index.html", active_page="home")


@app.route("/diagnose")
def diagnose():
    return render_template(
        "diagnose.html", active_page="diagnose", sample_images=get_sample_images()
    )


@app.route("/insights")
def insights():
    # Build plant-disease mapping for the insights page
    plant_diseases = {}
    for cls in CLASS_NAMES:
        parsed = parse_label(cls)
        plant = parsed["plant"]
        disease = parsed["disease"]
        if plant not in plant_diseases:
            plant_diseases[plant] = []
        plant_diseases[plant].append(
            {
                "disease": disease,
                "class_name": cls,
                "severity": DISEASE_INFO.get(cls, {}).get("severity", "unknown"),
            }
        )
    return render_template(
        "insights.html",
        active_page="insights",
        plant_diseases=plant_diseases,
        total_classes=len(CLASS_NAMES),
    )


@app.route("/about")
def about():
    return render_template("about.html", active_page="about")


@app.route("/predict", methods=["POST"])
def predict_route():
    if "file" not in request.files:
        flash("No file selected. Please upload a leaf image.", "error")
        return redirect(url_for("diagnose"))

    file = request.files["file"]
    if file.filename == "":
        flash("No file selected. Please upload a leaf image.", "error")
        return redirect(url_for("diagnose"))

    if not allowed_file(file.filename):
        flash("Invalid file type. Please upload a PNG, JPG, or JPEG image.", "error")
        return redirect(url_for("diagnose"))

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
        return redirect(url_for("diagnose"))

    top = results[0]
    disease_info = DISEASE_INFO.get(top["class_name"], {})

    return render_template(
        "result.html",
        active_page="diagnose",
        results=results,
        top=top,
        disease_info=disease_info,
        image_path=f"uploads/{unique_name}",
    )


@app.errorhandler(413)
def file_too_large(e):
    flash("File too large. Maximum allowed size is 10 MB.", "error")
    return redirect(url_for("diagnose"))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
