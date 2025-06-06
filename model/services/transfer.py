from ftplib import FTP as ftp
class Transfer:
    def __init__(self, instance):
        self.ftp = instance
        self.file_path = None
        self.transfer_ip = None

    def set_file_path(self, file_path):
        self.file_path = file_path

    def set_transfer_ip(self, transfer_ip):
        self.transfer_ip = transfer_ip

    def send_file(self, file_path, alias):
        pass