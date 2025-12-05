import tkinter as tk
from tkinter import ttk

# Application Settings
APP_TITLE = "TitanCampus Algorithmic Assistant (CPSC 335)"
WINDOW_SIZE = "1100x750"

# Graph Data (Adjacency List)
CAMPUS_GRAPH = {
    "ECS": {"Library": 5, "TSU": 7},
    "Gym": {"LH": 8, "Parking P1": 7},
    "LH": {"MH": 5, "Gym": 8},
    "Library": {"ECS": 5, "TSU": 3, "MH": 4},
    "MH": {"Library": 4, "LH": 5},
    "Parking P1": {"TSU": 6, "Gym": 7},
    "TSU": {"ECS": 7, "Library": 3, "Parking P1": 6}
}

BUILDINGS = sorted(list(CAMPUS_GRAPH.keys()))

# Color Palette
COLORS = {
    "primary": "#007AFF",
    "primary_dark": "#0056b3",
    "bg_main": "#F5F7FA",
    "bg_sec": "#FFFFFF",
    "text": "#333333",
    "text_light": "#FFFFFF",
    "accent": "#E1E8F0",
    "sidebar": "#2C3E50",  # Dark Blue-Grey for Sidebar
    "sidebar_hover": "#34495E"
}


def setup_styles():
    style = ttk.Style()
    style.theme_use('clam')

    # Global Defaults
    style.configure(".", background=COLORS["bg_main"], foreground=COLORS["text"], font=("Segoe UI", 10))

    # --- Sidebar Styling ---
    style.configure("Sidebar.TFrame", background=COLORS["sidebar"])

    # Sidebar Buttons (Flat, White Text)
    style.configure("Sidebar.TButton",
                    font=("Segoe UI", 11),
                    background=COLORS["sidebar"],
                    foreground=COLORS["text_light"],
                    borderwidth=0,
                    anchor="w",  # Left align text
                    padding=10
                    )
    style.map("Sidebar.TButton",
              background=[("active", COLORS["sidebar_hover"]), ("pressed", COLORS["primary"])],
              foreground=[("active", "#FFFFFF")]
              )

    # --- Main Content Styling ---
    style.configure("TFrame", background=COLORS["bg_main"])
    style.configure("TLabel", background=COLORS["bg_main"], foreground=COLORS["text"])

    # Standard Buttons
    style.configure("TButton",
                    font=("Segoe UI", 10, "bold"),
                    background=COLORS["primary"],
                    foreground=COLORS["text_light"],
                    borderwidth=0,
                    focuscolor="none",
                    padding=8
                    )
    style.map("TButton",
              background=[("active", COLORS["primary_dark"])],
              relief=[("pressed", "flat")]
              )

    # Header
    style.configure("Header.TLabel",
                    font=("Segoe UI", 18, "bold"),
                    foreground=COLORS["primary"],
                    background=COLORS["bg_main"],
                    padding=[0, 10, 0, 10]
                    )

    # Inputs & Lists
    style.configure("TEntry", fieldbackground=COLORS["bg_sec"], padding=5)
    style.configure("TCombobox", fieldbackground=COLORS["bg_sec"], padding=5)
    style.configure("Treeview", background=COLORS["bg_sec"], fieldbackground=COLORS["bg_sec"],
                    foreground=COLORS["text"], borderwidth=0)
    style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"), background=COLORS["accent"],
                    foreground=COLORS["text"], relief="flat")