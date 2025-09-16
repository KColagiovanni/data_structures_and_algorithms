from data_structures_and_algorithms import Array

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

array_example_test()