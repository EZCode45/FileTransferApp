from view.main_view import MainView
from model.main_model import MainModel
import random


class MainController():
    def __init__(self, model: MainModel, view: MainView): 
        self.model = model
        self.view = view
        self.local_ip  = self.model.local_ip
        self.file_path = None
        # self.used_aliases = []
        # self.alias = f"FTPUSER_{random.randint(0, 9999999999)}"
        # self.used_aliases.append(self.alias)
        # if self.alias in self.used_aliases:
        #     self.used_aliases.remove(self.alias)
        #     self.alias = f"FTPUSER_{random.randint(0, 9999999999)}"
        #     self.used_aliases.append(self.alias)
        # self.view.update_alias_label(self.alias)
    def transfer(self):
        self.file_path = self.view.request_file()
        if self.file_path:
            self.model.set_file_path(self.file_path)
            selected_ip = self.view.get_selected_ip()
            if selected_ip:
                if self.model.connect_to_device(selected_ip):
                    self.model.transfer_service.send_file(self.file_path, self.alias)
                else:
                    print("Failed to connect to device.")
            else:
                print("No device selected.")
        else:
            print("No file selected.")
        