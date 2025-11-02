from data_structures_and_algorithms import Graph
import csv
import random

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
    data_list = []

    # Open the random_graph.csv file in read mode and append the data to a list.
    with open(csv_filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for item in range(len(row)):
                data_list.append(row[item])

    # Insert vertices to make an edge.
    for item in range(50):
        g.insert_edge(random.choice(data_list), random.choice(data_list))

    # Size
    v, e = g.size()
    print(f"\nVertices: {v}, Edges: {e}")

    # Traversals
    print(f"\nDFS starting from {row[0]}:")
    g.traverse_dfs(row[0])

    print(f"\n\nBFS starting from {row[0]}:")
    g.traverse_bfs(row[0])
    print()

# graph_example_test()
read_from_csv()