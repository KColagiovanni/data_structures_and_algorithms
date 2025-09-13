from data_structures_and_algorithms import Array

def array_example_test():

    array = Array()

    array.traverse()

    array.insert(0, 'first')

    array.traverse()

    array.insert(1, 'second')

    array.traverse()

    array.insert(2, 'third')

    array.traverse()

    array.pop(1)

    array.traverse()

    array.insert(1, 'second')

    array.traverse()

    array.pop()

    array.traverse()

    array.insert(2, 'third')

    array.traverse()


array_example_test()