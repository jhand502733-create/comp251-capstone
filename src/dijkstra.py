def dijkstra(graph, start):
    distances = {}
    previous = {}

    for node in graph.graph:
        distances[node] = float('inf')
        previous[node] = None

    distances[start] = 0
    visited = []

    while len(visited) < len(graph.graph):
        current_node = None
        current_distance = float('inf')

        for node in graph.graph:
            if node not in visited and distances[node] < current_distance:
                current_distance = distances[node]
                current_node = node

        if current_node is None:
            break

        visited.append(current_node)

        for neighbor, weight in graph.graph[current_node]:
            new_distance = distances[current_node] + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node

    return distances, previous


def get_path(previous, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    if path[0] == start:
        return path
    else:
        return []
