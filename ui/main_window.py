import tkinter as tk
from tkinter import ttk
from ui.navigator_tab import NavigatorTab
from ui.planner_tab import PlannerTab
from ui.search_tab import SearchTab
from ui.info_tab import InfoTab


class MainWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True)

        # Title Label
        title = ttk.Label(self, text="TitanCampus Algorithmic Assistant", style="Header.TLabel")
        title.pack(pady=10)

        # Tabs
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)

        # Add Modules
        self.notebook.add(NavigatorTab(self.notebook), text="Campus Navigator")
        self.notebook.add(PlannerTab(self.notebook), text="Study Planner")
        self.notebook.add(SearchTab(self.notebook), text="Notes Search")
        self.notebook.add(InfoTab(self.notebook), text="Algorithm Info")