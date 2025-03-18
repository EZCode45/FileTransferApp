from view.main_view import MainView


class MainController():
    def __init__(self, view: MainView):
        self.view = view
        self.devices = ["0.0.0.0", "192.10.0.2"]
        #step 1 of button bind: add callback trough controller
        self.view.add_callbacks("upload", self.upload)
        self.view.add_callbacks("refresh", self.refresh)
        #step 2 bind commands
        self.view.bind_commands()
    def upload(self):
        self.selected_file = self.view.request_file()
    def refresh(self):
        self.view.update_ip_list(self.devices)

    