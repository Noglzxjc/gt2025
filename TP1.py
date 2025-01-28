def is_path_exist(graph, start, end):
    def dfs(node, visited):
        if node == end:
            return True

        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited and dfs(neighbor, visited):
                return True

        return False

    visited = set()
    return dfs(start, visited)

graph = {
    1: [2],
    2: [1, 5],
    3: [6],
    4: [6, 7],
    5: [2],
    6: [3, 4, 7],
    7: [4, 6]
}

while True:
    try:
        start_node = int(input("Enter the start node: "))
        if start_node in graph:
            break
        else:
            print("Start node does not exist")
    except ValueError:
        print("Invalid input")

while True:
    try:
        end_node = int(input("Enter the end node: "))
        if end_node in graph:
            break
        else:
            print("End node does not exist")
    except ValueError:
        print("Invalid input")

result = is_path_exist(graph, start_node, end_node)
print(result)