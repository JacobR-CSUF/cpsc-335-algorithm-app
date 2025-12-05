import tkinter as tk
from tkinter import ttk

# Application Settings
APP_TITLE = "TitanCampus Algorithmic Assistant (CPSC 335)"
WINDOW_SIZE = "1100x750"  # Slightly larger for better spacing

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

# Color Palette (Modern "Aqua-like" Blue & Clean Grays)
COLORS = {
    "primary": "#007AFF",  # Titan/Aqua Blue
    "primary_dark": "#0056b3",  # Darker Blue for active states
    "bg_main": "#F5F7FA",  # Very light blue-grey background
    "bg_sec": "#FFFFFF",  # White for content areas
    "text": "#333333",  # Dark charcoal for text
    "text_light": "#FFFFFF",  # White text
    "accent": "#E1E8F0"  # Light accent for headers
}


def setup_styles():
    """Configures a sophisticated, modern look using standard ttk."""
    style = ttk.Style()

    # 'clam' is the most flexible engine for custom coloring across OS
    style.theme_use('clam')

    # 1. Global defaults
    style.configure(".",
                    background=COLORS["bg_main"],
                    foreground=COLORS["text"],
                    font=("Segoe UI", 10)  # Segoe UI is standard Windows modern font; falls back gracefully
                    )

    # 2. Tabs (TNotebook) - The "Folder" look
    style.configure("TNotebook",
                    background=COLORS["bg_main"],
                    tabposition='n',
                    borderwidth=0
                    )
    style.configure("TNotebook.Tab",
                    padding=[15, 8],
                    font=("Segoe UI", 11, "bold"),
                    foreground="#555555",
                    background=COLORS["accent"],
                    borderwidth=0
                    )
    style.map("TNotebook.Tab",
              background=[("selected", COLORS["primary"])],
              foreground=[("selected", COLORS["text_light"])],
              expand=[("selected", [0, 0, 0, 0])]  # Removes weird shifting
              )

    # 3. Buttons (Modern Flat Blue)
    style.configure("TButton",
                    font=("Segoe UI", 10, "bold"),
                    background=COLORS["primary"],
                    foreground=COLORS["text_light"],
                    borderwidth=0,
                    focuscolor="none",
                    padding=8
                    )
    style.map("TButton",
              background=[("active", COLORS["primary_dark"]), ("pressed", COLORS["primary_dark"])],
              relief=[("pressed", "flat")]
              )

    # 4. Frames & Labels
    style.configure("TFrame", background=COLORS["bg_main"])
    style.configure("TLabel", background=COLORS["bg_main"], foreground=COLORS["text"])

    # 5. Header Label Style
    style.configure("Header.TLabel",
                    font=("Segoe UI", 18, "bold"),
                    foreground=COLORS["primary"],
                    background=COLORS["bg_main"],
                    padding=[0, 10, 0, 10]
                    )

    # 6. Inputs (Entry, Combobox)
    style.configure("TEntry", fieldbackground=COLORS["bg_sec"], padding=5)
    style.configure("TCombobox", fieldbackground=COLORS["bg_sec"], padding=5)

    # 7. Treeview (Task List) - Clean white look with blue selection
    style.configure("Treeview",
                    background=COLORS["bg_sec"],
                    fieldbackground=COLORS["bg_sec"],
                    foreground=COLORS["text"],
                    font=("Segoe UI", 10),
                    rowheight=25,
                    borderwidth=0
                    )
    style.configure("Treeview.Heading",
                    font=("Segoe UI", 10, "bold"),
                    background=COLORS["accent"],
                    foreground=COLORS["text"],
                    relief="flat"
                    )
    style.map("Treeview",
              background=[("selected", COLORS["primary"])],
              foreground=[("selected", COLORS["text_light"])]
              )