import csv
import random

vertices = []
csv_filename = 'random_graph.csv'
number_of_vertices = 100

for counter in range(number_of_vertices):
    vertices.append(f'vertex_{counter}')

with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    print(f'vertices are: {vertices}')
    writer.writerow(vertices)

print(f"CSV file '{csv_filename}' created successfully.")