import tkinter as tk
from tkinter import ttk, filedialog
import PyPDF2
import docx
from logic.string_search import StringSearchAlgorithms


class SearchTab(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.algo = StringSearchAlgorithms()
        self.loaded_text = ""
        self.filename = ""
        self.create_widgets()

    def create_widgets(self):
        # File Loading
        top_frame = ttk.Frame(self, padding=10)
        top_frame.pack(fill="x")

        self.file_label = ttk.Label(top_frame, text="No file loaded")
        self.file_label.pack(side="left")

        ttk.Button(top_frame, text="Load Document...", command=self.load_file).pack(side="left", padx=10)

        ttk.Label(top_frame, text="Pattern:").pack(side="left", padx=5)
        self.pattern_entry = tk.Entry(top_frame, width=20)
        self.pattern_entry.pack(side="left")

        # Algo Selection
        algo_frame = ttk.Frame(self, padding=10)
        algo_frame.pack(fill="x")

        self.algo_var = tk.StringVar(value="all")
        ttk.Label(algo_frame, text="Algorithm: ").pack(side="left")
        ttk.Radiobutton(algo_frame, text="Naive", variable=self.algo_var, value="naive").pack(side="left")
        ttk.Radiobutton(algo_frame, text="Rabin-Karp", variable=self.algo_var, value="rk").pack(side="left")
        ttk.Radiobutton(algo_frame, text="KMP", variable=self.algo_var, value="kmp").pack(side="left")
        ttk.Radiobutton(algo_frame, text="All (compare)", variable=self.algo_var, value="all").pack(side="left")

        ttk.Button(algo_frame, text="Search", command=self.run_search).pack(side="right", padx=10)

        # Content Viewer (Top box)
        # We let this inherit system defaults (likely black bg/white text in dark mode)
        self.text_display = tk.Text(self, height=15)
        self.text_display.pack(fill="both", expand=True, padx=10)

        # Results Viewer (Bottom box)
        # FIX: Explicitly set fg="black" to ensure text is visible on the #e6e6e6 background
        self.result_display = tk.Text(self, height=10, bg="#e6e6e6", fg="black")
        self.result_display.pack(fill="x", padx=10, pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Documents", "*.pdf *.docx *.txt")])
        if not file_path:
            return

        self.filename = file_path.split("/")[-1]
        self.file_label.config(text=f"Document: {self.filename}")

        text = ""
        try:
            if file_path.endswith(".pdf"):
                with open(file_path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        text += page.extract_text() + "\n"
            elif file_path.endswith(".docx"):
                doc = docx.Document(file_path)
                for para in doc.paragraphs:
                    text += para.text + "\n"
            else:  # txt
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()

            self.loaded_text = text
            self.text_display.delete("1.0", "end")
            self.text_display.insert("1.0", text)
        except Exception as e:
            self.result_display.delete("1.0", "end")
            self.result_display.insert("end", f"Error reading file: {e}\n")

    def run_search(self):
        pat = self.pattern_entry.get()
        if not pat or not self.loaded_text:
            return

        choice = self.algo_var.get()
        results = []

        # Helper to format output
        def format_res(name, indices, time_taken):
            # Limit indices display to first 20 to avoid freezing GUI on massive matches
            idx_str = ", ".join(map(str, indices[:20]))
            if len(indices) > 20: idx_str += "..."
            return f"[{name}]\nMatches ({len(indices)}): {idx_str}\nTime: {time_taken:.6f} s\n\n"

        self.result_display.delete("1.0", "end")
        self.result_display.insert("end", f"Searching for '{pat}' in '{self.filename}'...\n\n")

        if choice == "naive" or choice == "all":
            idx, t = self.algo.naive_search(self.loaded_text, pat)
            self.result_display.insert("end", format_res("Naive", idx, t))

        if choice == "rk" or choice == "all":
            idx, t = self.algo.rabin_karp(self.loaded_text, pat)
            self.result_display.insert("end", format_res("Rabin-Karp", idx, t))

        if choice == "kmp" or choice == "all":
            idx, t = self.algo.kmp_search(self.loaded_text, pat)
            self.result_display.insert("end", format_res("KMP", idx, t))