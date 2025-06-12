import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
from ultralytics import YOLO
import serial
import time
import threading

class DroneDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Drone Dashboard")
        self.root.geometry("800x600")
        self.root.configure(bg='black')
        self.colors = ((0, 255, 0), (0, 0, 255))

        self.model = YOLO("best.pt")
        self.cap = cv2.VideoCapture(1)
        
        self.ser = serial.Serial('COM5', 9600, timeout=1)
        time.sleep(2)  # Wait for Arduino to initialize

        self.video_label = tk.Label(self.root, bg='black')
        self.video_label.pack(pady=20)

        self.speedometer = ttk.Progressbar(self.root, orient='vertical', length=200, mode='determinate')
        self.speedometer.pack(side='left', padx=20)

        self.speedometer_label = tk.Label(self.root, text="Speed", bg='black', fg='white')
        self.speedometer_label.pack(side='left', padx=25)
        
        self.battery_frame = tk.Frame(self.root, bg='black')
        self.battery_frame.pack(side='right', padx=20)

        self.battery_label = tk.Label(self.battery_frame, text="Battery Level", bg='black', fg='white')
        self.battery_label.pack()
        
        self.battery_percentage = tk.Label(self.battery_frame, text="100%", bg='black', fg='blue')
        self.battery_percentage.pack()

        self.battery_bar = ttk.Progressbar(self.battery_frame, orient='horizontal', length=200, mode='determinate')
        self.battery_bar.pack()

    def update_dashboard(self):
        data = self.ser.readline().decode().strip().split()
        speed, battery = (0, 0) if len(data)<2 else (data[0], data[1])

        self.speedometer['value'] = speed
        self.battery_bar['value'] = battery
        self.battery_percentage['text'] = f"{battery}%"

    def show_video_feed(self):
        self.update_dashboard()
        ret, frame = self.cap.read()
        if ret:
            results = self.model.predict(source=frame, stream=True, conf=0.6)
            for result in results:
                boxes = result.boxes
                for box in boxes:
                    x1, y1, x2, y2 = box.xyxy[0].numpy().astype(int)
                    conf = box.conf[0].item()
                    cls = int(box.cls[0].item())
                    label = f'{result.names[cls]} {conf:.2f}'
                    cv2.rectangle(frame, (x1, y1), (x2, y2), self.colors[cls], 2)
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, self.colors[cls], 2)
                    
                    if result.names[cls] == "marquage":
                        data = result.names[cls]
                        self.ser.write(data.encode())  # Send data to Arduino
                        time.sleep(1)  # Pause before the next cycle
            
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = img
            self.video_label.configure(image=img) 

        self.video_label.after(1, self.show_video_feed)