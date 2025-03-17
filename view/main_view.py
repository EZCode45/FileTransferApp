import tkinter as tk
#fg = text color
#bg = background color
#font = font style and size
#padx = padding in x direction
#pady = padding in y direction
class MainView():
    def __init__(self, root : tk.Tk):
        self.root = root
        self.root.geometry("300x500")
        self.root.title("File Sharing APP")

        self.title = tk.Label(root,
                          text="File Sharing APP",
                          fg="Blue", bg="white",
                          font=("Arial", 20))
        self.title.pack(padx="2")
        self.ip_list = tk.Listbox(root,
                            bg="cyan",
                            fg = "white",
                            font=("Arial", 15),
                            height=5, width=50)
        self.ip_list.pack(pady="10")
        self.upload =  tk.Button(root,
                            text="Upload",
                            fg="white",
                            bg="blue",
                            font=("Arial", 15))
        self.upload.pack(pady="100")
    def update_ip_list(self, devices):
        # update device ip list  with the new devices
        self.ip_list
        for device in devices:
            self.ip_list.insert(tk.END, device)