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
        with open(file_path, 'rb') as file:
            try:
                self.ftp.storbinary(f'STOR {alias}', file)
            except Exception as e:
                print(f"Failed to send file {file_path} to {self.transfer_ip}: {e}")
                