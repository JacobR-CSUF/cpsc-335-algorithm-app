import tkinter as tk
from tkinter import ttk


class InfoTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_content()

    def create_content(self):
        # Using a standard Text widget. It will inherit system colors (White on Black for dark mode)
        text_area = tk.Text(self, wrap="word", padx=10, pady=10, font=("Courier", 11))
        text_area.pack(fill="both", expand=True)

        info = """Algorithm Info & Complexity (CPSC 335)

Graph Algorithms:
- BFS: O(V + E)
- DFS: O(V + E)
- Dijkstra (with min-heap): O((V + E) log V)
- Prim MST (with heap): O(E log V)

Study Planner:
- Greedy schedule (value/time): O(n log n)
- DP 0/1 Knapsack: O(n * C) where C = capacity in time units

String Matching:
- Naive search: O((n - m + 1) * m) worst case
- Rabin-Karp: average O(n + m), worst O(n * m)
- KMP: O(n + m)

P vs NP (informal reflection):

1. Polynomial Time (P):
The Graph algorithms (Dijkstra, Prim) used in the Campus Navigator
run in polynomial time. We can solve them efficiently even for
large inputs.

2. NP-Complete & Pseudo-Polynomial Time:
The 0/1 Knapsack problem (Study Planner) is technically NP-Complete.
However, we solve it using Dynamic Programming in O(n * C).
This is called "Pseudo-Polynomial" time. It is efficient as long
as the time capacity C is small, but would become slow if C were
exponentially large (e.g., extremely high precision time units).

3. NP-Hard:
If we tried to find the "shortest tour visiting every building
once" (TSP), that would be NP-Hard. No polynomial-time solution
is known, implying P != NP.

Summary:
This project demonstrates that while some problems are hard (Knapsack),
practical techniques like DP can often solve them efficiently for
real-world constraints.
"""
        text_area.insert("1.0", info)
        text_area.config(state="disabled")