from data_structures_and_algorithms import HashTable
import csv

csv_filename = 'random_record.csv'

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

def read_from_csv():

    ht = HashTable()

    with open(csv_filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            ht.insert(
                row[0],
                {
                    'name':row[1],
                    'age':row[2],
                    'gender':row[3]
                }
            )
    ht.traverse()

# hash_table_example_test()
read_from_csv()