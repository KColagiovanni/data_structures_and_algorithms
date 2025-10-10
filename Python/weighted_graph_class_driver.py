from data_structures_and_algorithms import WeightedGraph

def weighted_graph_example_test():
    g = WeightedGraph()

    # Insert edges with weights
    g.insert_edge('A', 'B', 4)
    g.insert_edge('A', 'C', 2)
    g.insert_edge('B', 'C', 5)
    g.insert_edge('B', 'D', 10)
    g.insert_edge('C', 'D', 3)

    print("Weighted Graph adjacency list:")
    g.display()

    print("\nShortest paths from A:")
    distances = g.dijkstra('A')
    for vertex, dist in distances.items():
        print(f"A → {vertex}: {dist}")

    # Size
    v, e = g.size()
    print(f"\nVertices: {v}, Edges: {e}")

    # Traversals
    print("\nDFS from A:")
    g.traverse_dfs('A')

    print("\n\nBFS from A:")
    g.traverse_bfs('A')

    # Delete
    print("\n\nDeleting edge B-C and vertex D:")
    g.delete_edge('B', 'C')
    g.delete_vertex('D')
    g.display()

    # Count again
    v, e = g.size()
    print(f"\nVertices: {v}, Edges: {e}")

weighted_graph_example_test()