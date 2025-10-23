import csv
from data_structures_and_algorithms import BinaryTree

csv_filename = 'random_numbers.csv'
num_dict = {}

def insert_number(num):

    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

bt = BinaryTree()

with open(csv_filename, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        for item in row:
            bt.insert(int(item))

    for item in bt.inorder():
        insert_number(item)

    print(num_dict)
