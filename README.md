# TitanCampus Algorithmic Assistant (TCAA)

A fully interactive Python GUI application designed to demonstrate major algorithmic techniques including Graph Traversal, Greedy Algorithms, Dynamic Programming, and String Pattern Matching.

## 📋 Features

1.  **Campus Navigator:**
    * Visualizes a campus graph with buildings and weighted paths.
    * Algorithms: BFS (Fewest Hops), DFS (Connectivity), Dijkstra (Shortest Path), Prim's MST .
2.  **Study Planner:**
    * Task scheduler allowing users to input tasks with time and value.
    * Algorithms: Greedy Scheduling vs. Dynamic Programming (0/1 Knapsack).
3.  **Notes Search:**
    * Document search engine supporting `.txt`, `.pdf`, and `.docx`.
    * Algorithms: Naive Search, Rabin-Karp, KMP.
4.  **Algorithm Info:**
    * Overview of Big-O complexities and reflection on P vs NP.

## ⚙️ Prerequisites & Dependencies

This project is built using **Python 3.x** and **Tkinter**.

### Required External Libraries
You must install the following libraries to support file reading (PDF/DOCX)

```bash
pip install PyPDF2 python-docx
````

*Note: `NetworkX` and `Pandas` are **not** used in this project, as per requirements .*

## 📂 Project Structure

Ensure your files are organized exactly as follows to prevent import errors:

```text
TitanCampus/
├── main.py                  # Entry point
├── config.py                # Configuration, Styles, & Graph Data
├── logic/                   # Algorithm Implementations
│   ├── __init__.py          # (Create an empty file here)
│   ├── graph_algos.py       # BFS, DFS, Dijkstra, Prim
│   ├── study_planner.py     # Greedy, DP Knapsack
│   └── string_search.py     # Naive, Rabin-Karp, KMP
└── ui/                      # GUI Components
    ├── __init__.py          # (Create an empty file here)
    ├── main_window.py       # Main Container (Sidebar + Content)
    ├── navigator_tab.py     # Tab 1: Campus Graph
    ├── planner_tab.py       # Tab 2: Study Scheduler
    ├── search_tab.py        # Tab 3: Document Search
    └── info_tab.py          # Tab 4: Big O Info
```

**Important:** You must create empty files named `__init__.py` inside both the `logic/` and `ui/` folders to allow Python to treat them as packages.

## 🚀 How to Run

1.  Open your terminal or command prompt.
2.  Navigate to the `TitanCampus` directory.
3.  Run the application:

<!-- end list -->

```bash
python main.py
```

## 🎮 Usage Guide

  * **Navigation:** Use the **Hamburger Menu (☰)** in the top-left corner to toggle the sidebar and switch between modules.
  * **Navigator:** Select a Start and End building, then click an algorithm button to see the path in the console.
  * **Planner:** Add tasks (Name, Time, Value), set your total available time, and compare the results of Greedy vs. DP.
  * **Search:** Load a file, type a pattern (e.g., "Apple"), and select an algorithm to see match indices and execution time.

<!-- end list -->
