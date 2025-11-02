from data_structures_and_algorithms import Array
import csv

csv_filename = 'random_numbers.csv'

def array_example_test():

    array = Array()

    array.traverse()

    array.insert(0, 'first')  # First item inserted

    array.traverse()

    array.insert(1, 'second')  # Second item inserted

    array.traverse()

    array.insert(2, 'third')  # Third item inserted

    array.traverse()

    array.insert(5, 'fourth')  # Invalid index

    array.traverse()

    array.insert(-1, 'fourth')  # Invalid index

    array.traverse()

    print(f'array size: {array.length()}')

    array.pop(1)

    array.traverse()

    array.insert(1, 'second')

    array.traverse()

    array.pop()

    array.traverse()

    array.insert(3, 'fourth')

    array.traverse()

    array.insert(-1, 'end')

    array.traverse()

    array.pop(20)

    array.traverse()

    array.pop(-1)

    array.traverse()

    array.append('appended value')

    array.traverse()

    array.search("third")

    array.clear()

    array.traverse()

    array.append('appended value')

    array.traverse()

    array.search("unknown item")

    # array.sort()  # !!!!! Need to look into this method to see why it throws an error. !!!!!
    #
    # array.traverse()

def read_from_csv():

    array = Array()

    # Open the random_number.csv file in read mode and append the data to a list.
    with open(csv_filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                array.append(int(item))
    array.traverse()

# array_example_test()
read_from_csv()