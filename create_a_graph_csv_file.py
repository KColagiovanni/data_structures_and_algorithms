import csv

vertices = []
csv_filename = 'random_graph.csv'
number_of_vertices = 100

# Creating a list of vertices
for counter in range(number_of_vertices):
    vertices.append(f'vertex_{counter}')

# Open a file and write the vertices to a CSV file.
with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    print(f'vertices are: {vertices}')
    writer.writerow(vertices)

print(f"CSV file '{csv_filename}' created successfully.")