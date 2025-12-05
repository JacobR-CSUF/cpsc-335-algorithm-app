import heapq


class GraphAlgorithms:
    def __init__(self, graph_data):
        self.graph = graph_data

    def bfs(self, start, end):
        """Breadth-First Search for fewest hops."""
        queue = [(start, [start])]
        visited = set()

        while queue:
            (vertex, path) = queue.pop(0)
            if vertex in visited:
                continue
            visited.add(vertex)

            if vertex == end:
                return path

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        return None

    def dfs(self, start, end):
        """Depth-First Search for connectivity."""
        stack = [(start, [start])]
        visited = set()

        while stack:
            (vertex, path) = stack.pop()
            if vertex in visited:
                continue
            visited.add(vertex)

            if vertex == end:
                return path

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
        return None

    def dijkstra(self, start, end):
        """Dijkstra's Shortest Path using Min-Heap."""
        # Priority Queue stores (current_dist, current_node, path)
        pq = [(0, start, [start])]
        visited = set()

        while pq:
            (cost, node, path) = heapq.heappop(pq)

            if node in visited:
                continue
            visited.add(node)

            if node == end:
                return path, cost

            for neighbor, weight in self.graph[node].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
        return None, float('inf')

    def prim_mst(self, start_node):
        """Prim's Minimum Spanning Tree."""
        mst_edges = []
        visited = {start_node}
        # Heap edges: (weight, from_node, to_node)
        edges = [
            (weight, start_node, to_node)
            for to_node, weight in self.graph[start_node].items()
        ]
        heapq.heapify(edges)
        total_cost = 0

        while edges:
            weight, u, v = heapq.heappop(edges)
            if v not in visited:
                visited.add(v)
                mst_edges.append((u, v, weight))
                total_cost += weight

                for next_node, next_weight in self.graph[v].items():
                    if next_node not in visited:
                        heapq.heappush(edges, (next_weight, v, next_node))

        return mst_edges, total_cost