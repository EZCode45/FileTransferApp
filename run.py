import tkinter as tk
from model.main_model import MainModel
from view.main_view import MainView
from controller.main_controller import MainController
from ftplib import FTP as ftp
# Initialize FTP instance
from model.services.server import run  # Ensure no null bytes or encoding issues
ftp_instance = ftp()
ftp_instance.connect('localhost', 21)
ftp_instance.login('admin', 'uhvhgjbvdjbhgoefijrwpjnbheori2pjebfgvfyr98u34ijrefbgyv99rihtgy58u9rihgvy78furhvgyiufrhqgvfdysi8dgetuh3gy8fuhbvhdwiqueohjvfdijwbavhfwri3kejfbvjsdpockjbhvuiforjfbvhjxciodajhfvgtu9ri0fjvhbsdfiesojhvbhgkrfijdhbvjicojhbdkgjiofjvbdjiapofjhbgjogifjvhhsfiu9ghif0sdiuchvgfur9efhdvdicuuhguifdhvjcudfshgfiodbadfuwhbfhjdkjcbfhdjkjhvbfjdkcnabvngjlfgmbjdl;vkbejfkwnvjbghitjorfjkvbghifjkbhgrjbghrfjvbhgfjhbghrjfbhjfvhfjvbh')
print(ftp_instance)
# ftp_instance.connect()
selected_ip = None
file_path = None
if __name__ == "__main__":
    root = tk.Tk()
    controller = MainController(MainModel(selected_ip=selected_ip, file_path=file_path, ftp_instance=ftp_instance), MainView(root))
    root.mainloop()
