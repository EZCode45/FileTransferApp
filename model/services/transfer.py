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

    def connect(self):
        try:
            self.ftp.connect(self.transfer_ip)
            self.ftp.login()
            return True
        except Exception as e:
            print(f"Failed to connect to {self.transfer_ip}: {e}")
            return False

    def disconnect(self):
        try:
            self.ftp.quit()
        except Exception as e:
            print(f"Failed to disconnect: {e}")
