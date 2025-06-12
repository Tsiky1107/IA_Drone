import threading
import tkinter as tk

from App.app import DroneDashboard

if __name__ == "__main__":
    root = tk.Tk()
    app = DroneDashboard(root)
    threading.Thread(target=app.show_video_feed).start()
    root.mainloop()