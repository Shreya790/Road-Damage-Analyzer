from ultralytics import YOLO

# Load a small pretrained YOLO model
model = YOLO("yolo11n.pt")

# Train the model using our road damage dataset
model.train(
    data="dataset/data.yaml",
    epochs=10,
    imgsz=640,
    batch=8
)