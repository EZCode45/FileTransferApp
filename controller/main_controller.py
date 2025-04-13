from view.main_view import MainView
from model.main_model import MainModel


class MainController():
    def __init__(self, model : MainModel, view : MainView):
        self.model = model
        self.view = view
        self.local_ip  = self.model.local_ip
        self.file_path = None
        if self.local_ip:
            print("Local IP: ", self.local_ip)
            self.view.update_alias_label(self.local_ip)

        #Add callbacks through controller
        self.view.add_callbacks("refresh", self.refresh)
        self.view.add_callbacks("upload", self.upload)

        #Bind the registered callback methods to their respective MainView widgets
        self.model.set_selected_ip(self.view.get_selected_ip())
        self.view.bind_commands()

    def refresh(self):
        devices = self.model.get_discovered_devices()
        print("Discovered devices: ", devices)
        self.view.update_ip_list(devices)

    def upload(self):
        self.file_path = self.view.request_file()

