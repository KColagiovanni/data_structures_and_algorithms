"""
Uses a dict to count the number of instances of each number in the random_numbers.csv file.
"""
import csv
from data_structures_and_algorithms import BinaryTree

csv_filename = 'random_numbers.csv'
num_dict = {}

def insert_number(num):
    """
    Takes a number and adds it to a dictionary as a key, if the key exists, and one to the number of instances, else set
    the number of instances to 1.
    :param num: (int) A number from the random_numbers.csv.
    :return: None
    """
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1

bt = BinaryTree()

# Open the random_number.csv file in read mode and insert the data to a Binary tree so it's sorted.
with open(csv_filename, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        for item in row:
            bt.insert(int(item))

    for item in bt.inorder():
        insert_number(item)

    print(num_dict)
