import tkinter as tk
from tkinter import filedialog
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
        self.callbacks = dict()
        self.title = tk.Label(root,
                          text="File Sharing APP",
                          fg="Blue", bg="white",
                          font=("Arial", 20))
        self.title.pack(padx="2")
        self.ip_list = tk.Listbox(root,
                            bg="#137fad",
                            fg = "white",
                            font=("Bookman Old Style", 15, "bold"),
                            height=5, width=50,
                            relief=tk.FLAT)
        self.ip_list.pack(pady="10")
        self.upload =  tk.Button(root,
                            text="Upload",
                            fg="white",
                            bg="#137fad",
                            font=("Bookman Old Style", 15, "bold"),
                            relief=tk.FLAT)
        self.upload.pack(pady="100")
        self.refresh = tk.Button(root,
                            text="Refresh",
                            fg="white",
                            bg="#137fad",
                            font=("Bookman Old Style", 15, "bold"),
                            relief=tk.FLAT,
                            width=7,
                            height=1)
        self.alias_label = tk.Label(self.root,
                                text=f"UNKNOWN",
                                fg="white",
                                bg="#137fad",
                                font=("Bookman Old Style", 15, "bold"),
                                relief=tk.FLAT,
                                width=7,
                                height=1)
        self.alias_label.pack(pady="5")
        self.refresh.pack(pady="5")
    def update_ip_list(self, devices):
        # update device ip list  with the new devices
        self.ip_list.delete(0, tk.END)
        self.ip_list
        for device in devices:
            self.ip_list.insert(tk.END, device)
    def request_file(self):
        return filedialog.askopenfilename() # type: ignore
    def add_callbacks(self, key, method):
        self.callbacks[key] = method
    def bind_commands(self):
        # bind the commands to the buttons
        self.upload.config(command=self.callbacks["upload"])
        self.refresh.config(command=self.callbacks["refresh"])
    def update_alias_label(self, alias):
        self.alias_label.config(text=f"Others will see you as {alias}")