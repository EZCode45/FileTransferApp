from ftplib import FTP as ftp
class Discovery:
    def __init__(self, instance):
        self.ftp = instance
        self.ftp.connect()
        self.ftp.login()
    def find_devices(self):
        devices = []
        self.ftp.retrlines('LIST', devices.append)
        return devices
    def connect_to_device(self, device):
        try:
            self.ftp.connect(device)
            self.ftp.login()
            return True
        except Exception as e:
            print(f"Failed to connect to {device}: {e}")
            return False
    def disconnect(self):
        try:
            self.ftp.quit()
        except Exception as e:
            print(f"Failed to disconnect: {e}")