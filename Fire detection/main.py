from ultralytics import YOLO


if __name__ == "__main__":
    model = YOLO("yolov8n.yaml")
    results = model.train(data="config.yaml", epochs=300, device=0)