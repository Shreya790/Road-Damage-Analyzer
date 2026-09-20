from model.predict import predict_damage

image_path = "test.jpg"

detections = predict_damage(image_path)

print("\nDetected Damage:")

if not detections:
    print("No damage detected.")

else:
    for detection in detections:
        print("Damage:", detection["type"])
        print("Confidence:", round(detection["confidence"] * 100, 2), "%")
        print()