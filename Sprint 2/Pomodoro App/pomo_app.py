import tkinter as tk
from pomo_controller import PomoController

def main():
    root = tk.Tk()
    root.title("PomoPython")
    root.resizable(False, False)
    app = PomoController(root)
    root.mainloop()

if __name__ == '__main__':
    main()