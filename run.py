import tkinter as tk
from model.main_model import MainModel
from view.main_view import MainView
from controller.main_controller import MainController

selected_ip = None
file_path = None
if __name__ == "__main__":
    root = tk.Tk()
    controller = MainController(MainModel(selected_ip, file_path), MainView(root))
    root.mainloop()
