import tkinter as tk
from model.main_model import MainModel
from view.main_view import MainView
from controller.main_controller import MainController
from ftplib import FTP as ftp
# Initialize FTP instance
ftp_instance = ftp()
from model.services import server
ftp_server = server.run()

selected_ip = None
file_path = None
if __name__ == "__main__":
    root = tk.Tk()
    controller = MainController(MainModel(ftp_instance), MainView(root))
    root.mainloop()
