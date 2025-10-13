from data_structures_and_algorithms import WeightedGraph

def weighted_graph_example_test():
    starting_vertex = 'A'
    ending_vertex = 'E'
    g = WeightedGraph()

    # Insert edges with weights
    g.insert_edge('A', 'B', 4)
    g.insert_edge('A', 'C', 2)
    g.insert_edge('C', 'D', 3)
    g.insert_edge('B', 'D', 10)
    g.insert_edge('D', 'E', 1)
    g.insert_edge('C', 'E', 6)

    print("Weighted Graph adjacency list:")
    g.display()

    print(f"\nShortest paths from {starting_vertex}:")
    distances, previous = g.dijkstra(starting_vertex)
    print(f'distances is: {distances}')
    for vertex, dist in distances.items():
        print(f"{starting_vertex} → {vertex}: {dist}")

    print(f'\nShortest path from {starting_vertex} to {ending_vertex}:')
    path, distance = g.get_shortest_path(starting_vertex, ending_vertex)
    print(f"Path: {' → '.join(path)} (Total cost: {distance})")

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