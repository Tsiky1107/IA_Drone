from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model.train(data='datasets/data.yaml', imgsz=640, batch=64, epochs=10, name='modele drone agri v2')

print(model.val())