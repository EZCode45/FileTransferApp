from model.services.discovery import Discovery
from model.services.transfer import Transfer

class MainModel():
    '''
    Provides an encapsulation of application services
    '''
    def __init__(self, selected_ip: None, file_path: None, ftp_instance):
        self.discovery_service = Discovery(ftp_instance)
        self.transfer_service = Transfer(ftp_instance)
        self.selected_ip = selected_ip
        self.file_path = file_path
        self.local_ip = self.discovery_service.get_local_ip()

        #Get own IP address and listen to broadcast messages on daemonic thread
        self.local_ip = self.discovery_service.get_local_ip()
        self.discovery_service.find_devices()
        print("Device Discovery Service initialized and running.")

    def get_discovered_devices(self):
        self.discovery_service.find_devices()
        return self.discovery_service.devices
    def connect_to_device(self, device):
        if self.discovery_service.connect_to_device(device):
            self.selected_ip = device
            return True
        else:
            return False
    def disconnect(self):
        self.discovery_service.disconnect()
        self.selected_ip = None
    def set_file_path(self, new_file_path):
        self.file_path = new_file_path
        self.transfer_service.set_file_path(new_file_path)
    def set_selected_ip(self, new_selected_ip):
        self.selected_ip = self.discovery_service.connect_to_device(new_selected_ip)