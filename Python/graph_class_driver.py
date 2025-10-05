from data_structures_and_algorithms import Graph

def graph_example_test():
    g = Graph()

    # Insert vertices and edges
    g.insert_edge('A', 'B')
    g.insert_edge('A', 'C')
    g.insert_edge('B', 'D')
    g.insert_edge('C', 'D')

    print("Graph adjacency list:")
    g.display()

    # Size
    v, e = g.size()
    print(f"\nVertices: {v}, Edges: {e}")

    # Traversals
    print("\nDFS starting from A:")
    g.traverse_dfs('A')

    print("\n\nBFS starting from A:")
    g.traverse_bfs('A')

    # Delete
    print("\n\nDeleting edge A-C and vertex D:")
    g.delete_edge('A', 'C')
    g.delete_vertex('D')
    g.display()

    # Count again
    v, e = g.size()
    print(f"\nVertices: {v}, Edges: {e}")

graph_example_test()