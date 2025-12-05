import tkinter as tk
from tkinter import ttk
from config import BUILDINGS, CAMPUS_GRAPH
from logic.graph_algos import GraphAlgorithms


class NavigatorTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.algo = GraphAlgorithms(CAMPUS_GRAPH)
        self.create_widgets()

    def create_widgets(self):
        # Top Controls
        control_frame = ttk.Frame(self, padding=10)
        control_frame.pack(fill="x")

        ttk.Label(control_frame, text="Start:").pack(side="left")
        self.start_var = tk.StringVar(value="ECS")
        ttk.Combobox(control_frame, textvariable=self.start_var, values=BUILDINGS, width=15).pack(side="left", padx=5)

        ttk.Label(control_frame, text="End:").pack(side="left", padx=5)
        self.end_var = tk.StringVar(value="Gym")
        ttk.Combobox(control_frame, textvariable=self.end_var, values=BUILDINGS, width=15).pack(side="left", padx=5)

        # Buttons
        btn_frame = ttk.Frame(self, padding=10)
        btn_frame.pack(fill="x")

        ttk.Button(btn_frame, text="BFS (Fewest Hops)", command=self.run_bfs).pack(side="left", padx=2)
        ttk.Button(btn_frame, text="Dijkstra (Shortest Path)", command=self.run_dijkstra).pack(side="left", padx=2)
        ttk.Button(btn_frame, text="DFS / Connectivity", command=self.run_dfs).pack(side="left", padx=2)
        ttk.Button(btn_frame, text="MST (Prim)", command=self.run_mst).pack(side="left", padx=2)

        # Output Areas
        content_frame = ttk.Frame(self, padding=10)
        content_frame.pack(fill="both", expand=True)

        # Left: Results
        self.result_text = tk.Text(content_frame, height=20, width=40)
        self.result_text.pack(side="left", fill="both", expand=True, padx=5)

        # Right: Graph Info (Static Adjacency List)
        self.graph_text = tk.Text(content_frame, height=20, width=40)
        self.graph_text.pack(side="right", fill="both", expand=True, padx=5)

        self.populate_graph_text()

    def populate_graph_text(self):
        self.graph_text.insert("end", "Graph (adjacency list):\n\n")
        for node, neighbors in CAMPUS_GRAPH.items():
            line = f"{node}: " + ", ".join([f"{k}({v})" for k, v in neighbors.items()])
            self.graph_text.insert("end", line + "\n")
        self.graph_text.config(state="disabled")

    def log(self, text):
        self.result_text.delete("1.0", "end")
        self.result_text.insert("end", text)

    def run_bfs(self):
        s, e = self.start_var.get(), self.end_var.get()
        path = self.algo.bfs(s, e)
        if path:
            self.log(f"BFS Path (Fewest Hops) from {s} to {e}:\n\n{' -> '.join(path)}\n\nHops: {len(path) - 1}")
        else:
            self.log("No path found.")

    def run_dfs(self):
        s, e = self.start_var.get(), self.end_var.get()
        path = self.algo.dfs(s, e)
        if path:
            self.log(f"DFS Path from {s} to {e}:\n\n{' -> '.join(path)}")
        else:
            self.log("No path found.")

    def run_dijkstra(self):
        s, e = self.start_var.get(), self.end_var.get()
        path, cost = self.algo.dijkstra(s, e)
        if path:
            self.log(f"Dijkstra Shortest Path:\n\n{' -> '.join(path)}\n\nTotal Distance: {cost}")
        else:
            self.log("No path found.")

    def run_mst(self):
        s = self.start_var.get()
        edges, cost = self.algo.prim_mst(s)

        output = f"Minimum Spanning Tree (Prim's Algorithm) starting at {s}:\n\n"
        for u, v, w in edges:
            output += f"{u} -- {v} (weight={w})\n"
        output += f"\nTotal MST cost: {cost}"
        self.log(output)