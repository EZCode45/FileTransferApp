import tkinter as tk
from model.main_model import MainModel
from view.main_view import MainView
from controller.main_controller import MainController
from ftplib import FTP
# Initialize FTP instance
server_ip = '127.0.0.1'
server_port = 21
from model.services.server import run  # Ensure no null bytes or encoding issues
run()
ftp = FTP(server_ip, server_port)
ftp.connect(server_ip, server_port)
ftp.retrlines('LIST')  # List files in the FTP server root directory
selected_ip = None
file_path = None
if __name__ == "__main__":
    with open('HELLO' ,'wb') as fp:
        ftp.retrbinary('RETR HELLO', fp.write)
    root = tk.Tk()
    controller = MainController(MainModel(selected_ip, file_path, ftp), MainView(root))
    root.mainloop()
    ftp.quit()  # Ensure the FTP connection is closed when the application exits
