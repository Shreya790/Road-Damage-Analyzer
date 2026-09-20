from ultralytics import YOLO

# Load trained model
model = YOLO("model/best.pt")


def predict_damage(image_path):

    results = model(image_path)

    detections = []

    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            class_name = result.names[class_id]

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            # Calculate center of detected damage
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2

            detections.append({

                "type": class_name,

                "confidence": confidence,

                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,

                "center_x": center_x,
                "center_y": center_y
            })

    return detections