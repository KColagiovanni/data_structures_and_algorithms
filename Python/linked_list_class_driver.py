from data_structures_and_algorithms import LinkedList
import csv

csv_filename = '../random_numbers.csv'

def linked_list_example_test():

    ll = LinkedList()

    ll.insert(40)
    ll.insert(10)
    ll.insert(30)
    ll.insert(5)
    ll.insert(15)
    ll.insert(25)
    ll.insert(20)
    ll.insert(35)

    ll.traverse()

    ll.search(25)
    ll.search(22)

    ll.delete(15)

    ll.traverse()

    ll.insert(45)

    ll.delete(22)

    ll.traverse()

    print(f'Linked List size: {ll.size()}')

    ll.is_empty()

def read_from_csv():

    ll = LinkedList()

    with open(csv_filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                ll.insert(int(item))

    ll.traverse()

#linked_list_example_test()
read_from_csv()