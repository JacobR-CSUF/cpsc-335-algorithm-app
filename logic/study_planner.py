class StudyPlannerAlgorithms:
    def greedy_schedule(self, tasks, max_time):
        """
        Greedy strategy: Sort by Value/Time ratio (density).
        If ratios equal, pick shorter task. [cite: 50]
        """
        # Sort desc by value/time
        sorted_tasks = sorted(tasks, key=lambda x: (x['value'] / x['time']), reverse=True)

        selected = []
        current_time = 0
        total_value = 0

        for task in sorted_tasks:
            if current_time + task['time'] <= max_time:
                selected.append(task)
                current_time += task['time']
                total_value += task['value']

        return selected, total_value, current_time

    def dp_knapsack(self, tasks, max_time):
        """
        0/1 Knapsack Dynamic Programming approach. [cite: 51]
        Rows = tasks, Cols = time capacity.
        """
        n = len(tasks)
        W = int(max_time)  # Ensure integer for array indexing

        # DP Table initialization
        K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

        for i in range(n + 1):
            for w in range(W + 1):
                if i == 0 or w == 0:
                    K[i][w] = 0
                else:
                    wt = int(tasks[i - 1]['time'])
                    val = tasks[i - 1]['value']

                    if wt <= w:
                        K[i][w] = max(val + K[i - 1][w - wt], K[i - 1][w])
                    else:
                        K[i][w] = K[i - 1][w]

        # Backtrack to find selected items
        res = K[n][W]
        total_value = res
        w = W
        selected = []

        for i in range(n, 0, -1):
            if res <= 0:
                break
            if res == K[i - 1][w]:
                continue
            else:
                selected.append(tasks[i - 1])
                res -= tasks[i - 1]['value']
                w -= int(tasks[i - 1]['time'])

        selected.reverse()  # Optional, just to keep order

        # Calculate used time
        total_time = sum(t['time'] for t in selected)

        return selected, total_value, total_time