from data_structures_and_algorithms import MinHeap
import csv

csv_filename = 'random_numbers.csv'

def heap_example_test():
    h = MinHeap()

    # Insert items
    h.insert(20)
    h.insert(15)
    h.insert(30)
    h.insert(5)
    h.insert(10)

    # Traverse
    h.traverse()  # Heap elements: [5, 10, 30, 20, 15]

    # Count
    print("Count:", h.count())  # → 5

    # Search
    print("Search 15:", h.search(15))  # True
    print("Search 40:", h.search(40))  # False

    # Delete (root each time)
    print("Deleted:", h.delete())  # → 5
    h.traverse()
    print("Deleted:", h.delete())  # → 10
    h.traverse()

def read_from_csv():

    h = MinHeap()

    # Open the random_numbers.csv file in read mode and insert the data to the heap.
    with open(csv_filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                h.insert(int(item))
    h.traverse()

# heap_example_test()
read_from_csv()
