from view.main_view import MainView


class MainController():
    def __init__(self, view: MainView):
        self.view = view
        devices = ["0.0.0.0", "192.10.0.2"]
        MainView.update_ip_list(self.view, devices)