import tkinter as tk
from config import APP_TITLE, WINDOW_SIZE, setup_styles
from ui.main_window import MainWindow


def main():
    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry(WINDOW_SIZE)

    # Apply configuration
    setup_styles()

    # Initialize Main UI
    app = MainWindow(root)

    root.mainloop()


if __name__ == "__main__":
    main()