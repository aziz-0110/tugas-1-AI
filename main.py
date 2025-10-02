import heapq

def astar_search(graph, heuristics, start, goal):
    frontier = [(heuristics[start], 0, start, [start])]  # (f, g, node, path)
    explored = set()

    while frontier:
        f, g, node, path = heapq.heappop(frontier)

        if node in explored:
            continue
        explored.add(node)

        if node == goal:
            return path, g

        for neighbor, cost in graph[node].items():
            if neighbor not in explored:
                g_new = g + cost
                f_new = g_new + heuristics[neighbor]
                heapq.heappush(frontier, (f_new, g_new, neighbor, path + [neighbor]))

    return None, float("inf")


graph = {
    'S': {'A': 1, 'D': 2},
    'A': {'B': 1},
    'D': {'B': 1, 'E': 4},
    'B': {'C': 2, 'E': 1},
    'C': {},
    'E': {'G': 3},
    'G': {}
}

heuristics = {
    'S': 7,
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'G': 0
}

path, cost = astar_search(graph, heuristics, 'S', 'G')
print("Path:", path)
print("Cost:", cost)
