from data_structures_and_algorithms import Graph
import csv

csv_filename = 'random_graph.csv'

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

def read_from_csv():

    g = Graph()

    with open(csv_filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for item in range(1, len(row)):
                print(row[item])
                g.insert_edge(row[0], row[item])
    # Size
    v, e = g.size()
    print(f"\nVertices: {v}, Edges: {e}")

    # Traversals
    print("\nDFS starting from {row[0]}:")
    g.traverse_dfs(row[0])

    print("\n\nBFS starting from A:")
    g.traverse_bfs(row[0])

# graph_example_test()
read_from_csv()