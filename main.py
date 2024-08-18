import tkinter as tk
from interfaces.MainScreen import MainScreen as MS

def main():
    root = tk.Tk()
    app = MS(root)
    root.mainloop()

if __name__ == "__main__":
    main()