import socket
# import threading
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
    def send_file(self):
        if not self.transfer_ip or not self.file_path:
            print("Transfer IP or file path is not set.")
            return

        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Connect to the server
            sock.connect((self.transfer_ip, self.TRANSFER_PORT))

            # Send the file name first
            file_name = os.path.basename(self.file_path)
            sock.sendall(file_name.encode())

            # Wait for the server to acknowledge the file name
            ack = sock.recv(1024).decode()
            if ack != "ACK":
                print("Failed to send file name.")
                return

            # Send the file content in chunks
            with open(self.file_path, 'rb') as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    sock.sendall(data)

            print("File sent successfully.")

        except Exception as e:
            print(f"Error sending file: {e}")

        finally:
            sock.close()
    def receive_file(self):
        if not self.file_path:
            print("File path is not set.")
            return

        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Bind the socket to the port
            sock.bind(('', self.TRANSFER_PORT))

            # Listen for incoming connections
            sock.listen(1)
            print(f"Listening for incoming file transfers on port {self.TRANSFER_PORT}...")

            # Accept a connection from a client
            conn, addr = sock.accept()
            print(f"Connection from {addr} established.")

            # Receive the file name first
            file_name = conn.recv(1024).decode()
            if not file_name:
                print("Failed to receive file name.")
                return

            # Send an acknowledgment for the file name
            conn.sendall("ACK".encode())

            # Receive the file content in chunks and save it to a file
            with open(os.path.join(self.file_path, file_name), 'wb') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)

            print(f"File received successfully and saved as {file_name}.")

        except Exception as e:
            print(f"Error receiving file: {e}")

        finally:
            conn.close()
            sock.close()