from data_structures_and_algorithms import HashTable

def hash_table_example_test():
    ht = HashTable(size=5)

    # Insert items
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("cherry", 30)
    ht.insert("banana", 25)  # updates existing key

    # Search
    print("Search 'banana':", ht.search("banana"))  # → 25
    print("Search 'grape':", ht.search("grape"))    # → None

    # Traverse
    print("\nTraversing hash table:")
    ht.traverse()

    # Count
    print("\nTotal items:", ht.count())  # → 3

    # Delete
    ht.delete("apple")
    print("\nAfter deleting 'apple':")

    ht.traverse()
    print("Total items:", ht.count())

hash_table_example_test()