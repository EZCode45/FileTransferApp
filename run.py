import tkinter as tk
from model.main_model import MainModel
from view.main_view import MainView
from controller.main_controller import MainController
from ftplib import FTP as ftp
# Initialize FTP instance
server_ip = '127.0.0.1'
server_port = 21
from model.services.server import run  # Ensure no null bytes or encoding issues
ftp_instance = ftp()
ftp_instance.connect('127.0.0.1', 21)
ftp_instance.login('admin', 'uhvhgjbvdjbhERTYUIO%WE&*@#%#$%^&*@#@^$#@%^&**UGCR%^&*@TRDHUYREW$^&SDFGHJ^%$#$%^*UHHJG&YGFGUTDgoefijrwpjnbheori2pjebfgvfyr98u34w5yeuwperfd6789dyft5u7398rf8yugu90v8yfght4riueoh^REW$#%^&ITYFDSRE%$^&TFGSE%&TIGFGSRE%^&*YGFSE^%&*YUGFDER*OIHGCFG^*OYIHJGCDIYJC^&@#UIHJG%^@*&UIGFDE$&%*YUHGCXDFE^&*UGHCFGR^@&*YUGHDR*YUGF%^*YUGFDRE%^YUGFHDR&*YIUGJFTYR%&^*@&UIHGYFR&4ijrefbgyv99rihtgy58u9rihgvy78furhvgyiufrhqgvfdysi8dgeSETYOIHGCFDR^T&Y*OIHGDTYR^&@#UIHJGCDRT*U@POJHFGR^@&#*POJKBVGCHT*@UOPLIJHGCDR^@*&#PIOJLHKGDR^*&UIHJVR^%&*@UIGFDRT&*UOIHKGD^*@&OUIHKGD%^&*@tuh3gy8fuhbvhdwiqueohjvfdijwbavhfwri3kejfbvjsdpockjbhvuiforjfbvhjxciodajhfvgtu9ri0fjvhbsdfiesojhvbhgkrfijdhbvjicojhbdkgjiofjvbdjiapofjhbgjogifjvhhsfiu9ghif0sdiuchvgfur9efhdvdicuuhguifdhvjcudfshgfiodbadfuwhbfhjdkjcbfhdjkjhvbfjdkcnabvngjlfgmbjdl;vkbejfkwnvjbghitjorfjkvbghifjkbhgrjbghrfjvbhgfjhbghrjfbhjfvhfjvbh')
# print(ftp_instance)
# ftp_instance.connect()
run()
selected_ip = None
file_path = None
if __name__ == "__main__":
    root = tk.Tk()
    controller = MainController(MainModel(selected_ip=selected_ip, file_path=file_path, ftp_instance=ftp_instance), MainView(root))
    root.mainloop()
