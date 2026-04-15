def has_cycle(graph):
    # colors: WHITE (unvisited), GRAY (visiting), BLACK (done)
    color = {}

    for node in graph.graph:
        color[node] = "WHITE"

    def dfs(node):
        if color[node] == "GRAY":
            return True  # cycle found

        if color[node] == "BLACK":
            return False  # already processed

        color[node] = "GRAY"

        for neighbor, _ in graph.graph[node]:
            if dfs(neighbor):
                return True

        color[node] = "BLACK"
        return False

    for node in graph.graph:
        if color[node] == "WHITE":
            if dfs(node):
                return True

    return False
