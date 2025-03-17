import tkinter as Tk
from view.main_view import MainView
from controller.main_controller import MainController

if __name__ == "__main__":
    root = Tk.Tk()
    view = MainView(root)
    controller = MainController(view)
    root.mainloop()