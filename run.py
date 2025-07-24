import tkinter as tk
from model.main_model import MainModel
from view.main_view import MainView
from controller.main_controller import MainController
from ftplib import FTP
from model.services.server import run
# Initialize FTP instance
server_ip = '10.1.10.109'
server_port = 21
run()
ftp = FTP(server_ip, server_port)
# ftp.connect(server_ip, server_port)
# ftp.retrlines('LIST')  # List files in the FTP server root directory
selected_ip = None
file_path = None
if __name__ == "__main__":
    root = tk.Tk()
    controller = MainController(MainModel(selected_ip, file_path, ftp), MainView(root))
    # with open('HELLO' ,'wb') as fp:
    #     ftp.retrbinary('RETR HELLO', fp.write)
    root.mainloop()
    ftp.quit()  # Ensure the FTP connection is closed when the application exits
