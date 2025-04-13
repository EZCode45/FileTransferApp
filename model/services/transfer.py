import socket
import threading
import os


class FileTransferService():
    TRANSFER_PORT = 5001
    def __init__(self, transfer_ip: None, file_path: None):
        self.transfer_ip = transfer_ip
        self.file_path = file_path
    def set_transfer_ip(self, new_transfer_ip):
        self.transfer_ip = new_transfer_ip
    def set_file_path(self, new_file_path):
        self.file_path = new_file_path