def construct_adjacency_matrix(edges, n):
    adj_matrix = [[0] * n for _ in range(n)]
    for u, v in edges:
        adj_matrix[u-1][v-1] = 1
    return adj_matrix

def inorder_traversal(tree, node):
    if node not in tree or not tree[node]:
        return []

    left = inorder_traversal(tree, tree[node][0]) if len(tree[node]) > 0 else []
    right = inorder_traversal(tree, tree[node][1]) if len(tree[node]) > 1 else []

    return left + [node] + right

def main():
    edges = [(1, 2), (1, 3), (2, 5), (2, 6), (3, 4), (4, 8), (5, 7)]
    n = 8 

    adj_matrix = construct_adjacency_matrix(edges, n)
    print("Adjacency Matrix:")
    for row in adj_matrix:
        print(row)

    tree_structure = {
        1: [3, 2], 
        2: [6, 5], 
        3: [4], 
        4: [8], 
        5: [7],          
        6: [],       
        7: [],           
        8: []    
    }

    try:
        x = int(input("Enter the node label to print subtree in Inorder: "))
        if x not in tree_structure:
            raise ValueError("Node not found")

        inorder_result = inorder_traversal(tree_structure, x)
        print(f"Inorder Traversal of subtree rooted at node {x}: {inorder_result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()