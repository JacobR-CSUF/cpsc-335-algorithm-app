import tkinter as tk
from tkinter import ttk
from logic.study_planner import StudyPlannerAlgorithms


class PlannerTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.tasks = []
        self.algo = StudyPlannerAlgorithms()
        self.create_widgets()

    def create_widgets(self):
        # Input Frame
        input_frame = ttk.Frame(self, padding=10)
        input_frame.pack(fill="x")

        ttk.Label(input_frame, text="Task:").pack(side="left")
        self.task_name = tk.Entry(input_frame, width=15)
        self.task_name.pack(side="left", padx=5)

        ttk.Label(input_frame, text="Time (h):").pack(side="left")
        self.task_time = tk.Entry(input_frame, width=5)
        self.task_time.pack(side="left", padx=5)

        ttk.Label(input_frame, text="Value:").pack(side="left")
        self.task_val = tk.Entry(input_frame, width=5)
        self.task_val.pack(side="left", padx=5)

        ttk.Button(input_frame, text="Add", command=self.add_task).pack(side="left", padx=10)
        ttk.Button(input_frame, text="Remove Selected", command=self.remove_task).pack(side="left")

        # Task List (Treeview)
        columns = ("task", "time", "value")
        self.tree = ttk.Treeview(self, columns=columns, show="headings", height=8)
        self.tree.heading("task", text="Task")
        self.tree.heading("time", text="Time (h)")
        self.tree.heading("value", text="Value")
        self.tree.pack(fill="x", padx=10, pady=5)

        # Execution Frame
        exec_frame = ttk.Frame(self, padding=10)
        exec_frame.pack(fill="x")

        ttk.Label(exec_frame, text="Available Time (h):").pack(side="left")
        self.max_time_entry = tk.Entry(exec_frame, width=8)
        self.max_time_entry.pack(side="left", padx=5)

        ttk.Button(exec_frame, text="Run Greedy", command=self.run_greedy).pack(side="left", padx=5)
        ttk.Button(exec_frame, text="Run DP (Knapsack)", command=self.run_dp).pack(side="left", padx=5)

        # Output Area
        self.output_text = tk.Text(self, height=10)
        self.output_text.pack(fill="both", expand=True, padx=10, pady=10)
        self.output_text.insert("end", "Study Planner:\nAdd tasks, set available time, then compare Greedy vs DP.\n")

    def add_task(self):
        name = self.task_name.get()
        try:
            time_cost = int(self.task_time.get())
            val = int(self.task_val.get())
            if name and time_cost > 0:
                self.tasks.append({'name': name, 'time': time_cost, 'value': val})
                self.refresh_list()
                self.task_name.delete(0, 'end')
                self.task_time.delete(0, 'end')
                self.task_val.delete(0, 'end')
        except ValueError:
            pass  # Ignore invalid inputs

    def remove_task(self):
        selected = self.tree.selection()
        if selected:
            # Simple approach: clear all and rebuild excluding selection logic requires ID tracking
            # For simplicity in this assignment, we will pop the last one or clear list
            # Better approach:
            for item in selected:
                vals = self.tree.item(item)['values']
                # Remove first matching dict
                for t in self.tasks:
                    if t['name'] == vals[0] and t['time'] == vals[1] and t['value'] == vals[2]:
                        self.tasks.remove(t)
                        break
            self.refresh_list()

    def refresh_list(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        for t in self.tasks:
            self.tree.insert("", "end", values=(t['name'], t['time'], t['value']))

    def run_greedy(self):
        try:
            limit = int(self.max_time_entry.get())
            sel, val, t = self.algo.greedy_schedule(self.tasks, limit)

            out = f"--- Greedy Result ---\nTotal Value: {val} | Time Used: {t}/{limit}\nTasks Chosen:\n"
            for s in sel:
                out += f" - {s['name']} (v={s['value']}, t={s['time']})\n"

            self.output_text.delete("1.0", "end")
            self.output_text.insert("end", out)
        except ValueError:
            self.output_text.insert("end", "\nError: Invalid Max Time")

    def run_dp(self):
        try:
            limit = int(self.max_time_entry.get())
            sel, val, t = self.algo.dp_knapsack(self.tasks, limit)

            out = f"--- DP (Knapsack) Result ---\nTotal Value: {val} | Time Used: {t}/{limit}\nTasks Chosen:\n"
            for s in sel:
                out += f" - {s['name']} (v={s['value']}, t={s['time']})\n"

            self.output_text.delete("1.0", "end")
            self.output_text.insert("end", out)
        except ValueError:
            self.output_text.insert("end", "\nError: Invalid Max Time")