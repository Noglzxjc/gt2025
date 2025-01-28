def perform_dfs(node, graph, visited_nodes):
    stack = [node]
    component = set()

    while stack:
        current_node = stack.pop()
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)
            component.add(current_node + 1)
            neighbors = [index for index, is_connected in enumerate(graph[current_node]) if is_connected and index not in visited_nodes]
            stack.extend(neighbors)

    return component

def get_connected_components(graph):
    visited_nodes = set()
    components = []

    for node in range(len(graph)):
        if node not in visited_nodes:
            component = perform_dfs(node, graph, visited_nodes)
            components.append(component)

    return components

def convert_to_undirected(graph):
    return [[1 if graph[i][j] == 1 or graph[j][i] == 1 else 0 for j in range(len(graph))] for i in range(len(graph))]

def count_components(directed_graph):
    undirected_graph = convert_to_undirected(directed_graph)
    directed_components = get_connected_components(directed_graph)
    undirected_components = get_connected_components(undirected_graph)

    return {"strong": directed_components, "weak": undirected_components}

if __name__ == '__main__':
    graph = [
        [0, 1, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    result = count_components(graph)

    print("Strong Components:")
    for component in result["strong"]:
        print(f"Component: {component}")

    print("\nWeak Components:")
    for component in result["weak"]:
        print(f"Component: {component}")
