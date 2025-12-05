import tkinter as tk
from tkinter import ttk
from config import APP_TITLE
from ui.navigator_tab import NavigatorTab
from ui.planner_tab import PlannerTab
from ui.search_tab import SearchTab
from ui.info_tab import InfoTab


class MainWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(style="TFrame")
        self.pack(fill="both", expand=True)

        self.sidebar_expanded = False  # expand hamburger menu
        self.views = {}

        self.create_layout()
        self.init_pages()
        self.show_view("Navigator")  # Default page
        self.toggle_sidebar()

    def create_layout(self):
        # 1. Top Header Bar
        header_frame = ttk.Frame(self, style="TFrame")
        header_frame.pack(side="top", fill="x", padx=10, pady=5)

        # Hamburger Button (Using simple text '☰')
        self.menu_btn = tk.Button(header_frame, text="☰", font=("Segoe UI", 18),
                                  bg="#F5F7FA", fg="#333", bd=0,
                                  activebackground="#E1E8F0", cursor="hand2",
                                  command=self.toggle_sidebar)
        self.menu_btn.pack(side="left", padx=(0, 15))

        # App Title
        title = ttk.Label(header_frame, text="TitanCampus Algorithmic Assistant", style="Header.TLabel")
        title.pack(side="left")

        # 2. Main Body Container
        self.body_frame = ttk.Frame(self)
        self.body_frame.pack(side="top", fill="both", expand=True)

        # 3. Sidebar
        self.sidebar = ttk.Frame(self.body_frame, style="Sidebar.TFrame", width=200)

        # 4. Content Area
        self.content_area = ttk.Frame(self.body_frame, style="TFrame")
        self.content_area.pack(side="left", fill="both", expand=True, padx=20, pady=10)

        # 5. Sidebar Navigation Buttons
        self.add_sidebar_btn("Campus Navigator", "Navigator")
        self.add_sidebar_btn("Study Planner", "Planner")
        self.add_sidebar_btn("Notes Search", "Search")
        self.add_sidebar_btn("Algorithm Info", "Info")

    def add_sidebar_btn(self, text, view_key):
        btn = ttk.Button(self.sidebar, text=text, style="Sidebar.TButton",
                         command=lambda: self.show_view(view_key))
        btn.pack(fill="x", pady=2, padx=5)

    def init_pages(self):
        # Instantiate all views once and keep them in memory
        # This preserves data (like graph selections) when switching tabs
        self.views["Navigator"] = NavigatorTab(self.content_area)
        self.views["Planner"] = PlannerTab(self.content_area)
        self.views["Search"] = SearchTab(self.content_area)
        self.views["Info"] = InfoTab(self.content_area)

    def toggle_sidebar(self):
        if self.sidebar_expanded:
            self.sidebar.pack_forget()
            self.sidebar_expanded = False
        else:
            self.sidebar.pack(side="left", fill="y", before=self.content_area)
            self.sidebar_expanded = True

    def show_view(self, view_name):
        # Hide all views
        for view in self.views.values():
            view.pack_forget()

        # Show selected view
        self.views[view_name].pack(fill="both", expand=True)
