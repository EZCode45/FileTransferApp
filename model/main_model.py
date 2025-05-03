from model.services.discovery import Discovery
from model.services.transfer import Transfer

class MainModel():
    '''
    Provides an encapsulation of application services
    '''
    def __init__(self, selected_ip: None, file_path: None):
        self.discovery_service = Discovery()
        self.transfer_service = Transfer()
        self.selected_ip = selected_ip
        self.file_path = file_path

        #Get own IP address and listen to broadcast messages on daemonic thread
        self.local_ip = self.discovery_service.get_local_ip()
        self.discovery_service.listen_async()
        print("Device Discovery Service initialized and running.")

    def get_discovered_devices(self):
        #Send broadcast message and update list of received signals
        self.discovery_service.broadcast_discovery()
        return self.discovery_service.discovered_devices
    def set_file_path(self, new_file_path):
        self.file_path = new_file_path
        self.transfer_service.set_file_path(new_file_path)
    def set_selected_ip(self, new_selected_ip):
        self.selected_ip = new_selected_ip
        self.transfer_service.set_transfer_ip(new_selected_ip)
        self.transfer_service.set_file_path(self.file_path)