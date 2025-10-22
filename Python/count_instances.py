import csv

csv_filename = 'random_numbers.csv'
num_dict = {}

def insert_number(num):

    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1


with open(csv_filename, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        for item in row:
            insert_number(int(item))

    print(num_dict)
