import tkinter as tk
from gui import AppCriptografia

def main():
    root = tk.Tk()
    app = AppCriptografia(root)
    root.mainloop()

if __name__ == "__main__":
    main()