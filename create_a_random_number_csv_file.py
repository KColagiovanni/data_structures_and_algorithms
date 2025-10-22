import csv
import random

data = []
csv_filename = 'random_numbers.csv'
array_length = 100
min_num = 0
max_num = 10

for random_number in range(array_length):
    data.append(random.randint(min_num, max_num))

with open(csv_filename, 'w', newline='') as file:
    writer = csv.writer(file)
    print(f'data is: {data}')
    writer.writerow(data)

print(f"CSV file '{csv_filename}' created successfully.")