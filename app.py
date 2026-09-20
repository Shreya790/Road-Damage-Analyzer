from flask import Flask, render_template, request
import os
import cv2

from model.predict import predict_damage
from severity.severity import calculate_severity


app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "image" not in request.files:
        return "No image selected"

    image = request.files["image"]

    if image.filename == "":
        return "No image selected"


    # Save image

    image_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        image.filename
    )

    image.save(image_path)


    # Get GPS from form

    latitude = request.form.get("latitude")

    longitude = request.form.get("longitude")


    if latitude and longitude:

        location = (
            f"{float(latitude):.6f}, "
            f"{float(longitude):.6f}"
        )

    else:

        location = "Location not provided"


    # AI detection

    detections = predict_damage(image_path)


    # Read image

    img = cv2.imread(image_path)

    if img is None:
        return "Invalid image file"


    image_height, image_width = img.shape[:2]

    total_area = image_width * image_height


    # Damage area

    damage_area = 0


    for detection in detections:

        width = (
            detection["x2"]
            - detection["x1"]
        )

        height = (
            detection["y2"]
            - detection["y1"]
        )

        damage_area += width * height


    if total_area > 0:

        damage_percentage = (
            damage_area / total_area
        ) * 100

    else:

        damage_percentage = 0


    # Severity

    score, severity = calculate_severity(
        damage_percentage
    )


    # Damage information

    if detections:

        damage_type = detections[0]["type"]

        confidence = (
            detections[0]["confidence"] * 100
        )

    else:

        damage_type = "No damage detected"

        confidence = 0


    # Result page

    return render_template(

        "result.html",

        image=image.filename,

        damage_type=damage_type,

        confidence=round(confidence, 2),

        damage=round(damage_percentage, 2),

        score=score,

        severity=severity,

        location=location

    )


if __name__ == "__main__":

    app.run(debug=True)