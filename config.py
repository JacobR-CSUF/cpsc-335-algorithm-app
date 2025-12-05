# config.py
import tkinter as tk
from tkinter import ttk

# Application Settings
APP_TITLE = "TitanCampus Algorithmic Assistant (CPSC 335)"
WINDOW_SIZE = "1000x700"

# Graph Data (Adjacency List based on your screenshot)
# Format: {Node: {Neighbor: Weight, ...}}
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


def setup_styles():
    """Configures a modern look for the UI."""
    style = ttk.Style()
    style.theme_use('clam')  # 'clam' usually looks cleaner than default

    # General Frame Background
    style.configure("TFrame", background="#f0f0f0")
    style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 11))
    style.configure("TButton", font=("Helvetica", 10, "bold"), padding=6)

    # Header Style
    style.configure("Header.TLabel", font=("Helvetica", 16, "bold"), foreground="#333")