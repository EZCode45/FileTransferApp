from view.main_view import MainView
from model.main_model import MainModel
import random


class MainController():
    def __init__(self, model : MainModel, view : MainView):
        self.model = model
        self.view = view
        self.local_ip  = self.model.local_ip
        self.file_path = None
        self.aliases = [
    "Solivagus", "Nyxium", "Zephyrion", "Luminex", "Aetheral", "Drakthar", "Vynoria", 
    "Oculis", "Astralith", "Quorix", "Serenith", "Obsidral", "Halythion", "Phantrix", 
    "Eclipira", "Chromith", "Thalorix", "Emberis", "Crython", "Falkara", "Velithra", 
    "Cyrenix", "Galvoro", "Harkis", "Jorenth", "Lysara", "Myrinth", "Orvyn", 
    "Pyrithor", "Quorath", "Ralith", "Silvara", "Terithra", "Umbroth", "Valtheris", 
    "Wylinth", "Xenithra", "Yaraxis", "Zorinth", "Aquenith", "Bralith", "Calvoro", 
    "Dromerix", "Elthara", "Firynth", "Goraxis", "Halvyn", "Imberon", "Jorithar", 
    "Kalorix"
]
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
    def set_alias(self):
        random_alias = random.choice(self.aliases)
        self.view.set_alias(random_alias)
    def upload(self):
        self.file_path = self.view.request_file()
        if self.file_path:
            print("File path: ", self.file_path)
            self.model.set_file_path(self.file_path)
            selected_ip = self.view.get_selected_ip()
            if selected_ip:
                print("Selected IP: ", selected_ip)
                self.model.set_selected_ip(selected_ip)
                self.model.transfer_service.send_file()
            else:
                print("No IP selected.")
        else:
            print("No file selected.")
        self.view.update_alias_label(self.local_ip)
