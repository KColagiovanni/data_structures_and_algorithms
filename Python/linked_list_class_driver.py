from data_structures_and_algorithms import LinkedList

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

linked_list_example_test()