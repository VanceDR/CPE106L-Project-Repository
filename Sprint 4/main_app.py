import tkinter as tk
from login_controller import LoginController

def main():
    root = tk.Tk()
    root.title("PomoPython")
    root.resizable(False, False)
    app = LoginController(root)
    root.mainloop()

if __name__ == '__main__':
    main()