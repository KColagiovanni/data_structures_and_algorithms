class Record:

    def __init__(self):
        self.record = {}

    def insert(self, key, value):
        """
        Insert a value into the record.
        :param key: (str) The key for the new entry.
        :param value: (str) The value for the new entry.
        :return: (bool) True if the insertion was successful, else False.
        """
        if key in self.record:
            print(f'Insert failed!! {key} already exists!!')
            return False
        else:
            self.record[key] = value
            print(f'Record inserted successfully')
            return True

    def delete(self, key):
        """
        Delete a value from the record.
        :param key: (str) The key for the new entry.
        :return: (bool) True if the deletion was successful, else False.
        """
        if key in self.record:
            del self.record[key]
            print(f'{key} was deleted successfully!')
            return True
        else:
            print(f'Delete failed!! {key} does not exist!!')
            return False

    def search(self, key):
        """
        Search for a value in the record.
        :param key: (str) The key for the new entry.
        :return: (bool) True if the search was successful, else False.
        """
        if key in self.record:
            print(f'{key} has been found! The value is {self.record[key]}')
            return True
        else:
            print(f'{key} was not found, because it does not exist!!')
            return False

    def update(self, key, new_value):
        """
        Update a value in the record.
        :param key: (str) The key for the new entry.
        :param new_value: (str) The new value for the updated record.
        :return: (bool) True if the update was successful, else False.
        """
        if key in self.record:
            old_value = self.record[key]
            self.record[key] = new_value
            print(f'Update successful! The {key} value has changed from {old_value} to {self.record[key]}')
            return True
        else:
            print(f'Update failed!! Key: {key} was not found!!')
            return False

    def clear_record(self):
        """
        Delete all data in the record.
        :return: (bool) True if the clearing of the record was successful, else False.
        """
        if self.isEmpty():
            print('Record is already empty.')
            return False
        else:
            self.record.clear()
            print('Record has been fully deleted!')
            return True

    def traverse(self):
        """
        Traverse the record and print out each key and value, line by line.
        :return: (bool) False if the record is empty, else True.
        """
        if self.isEmpty():
            print('Record is empty.')
            return False
        else:
            count = 1
            for key, value in self.record.items():
                print(f'Entry {count}) - {key}: {value}')
                count += 1
            return False

    def isEmpty(self):
        """
        Check if the record is empty.
        :return: (bool) True if the record is empty, else False.
        """
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        """
        Return the size of the record.
        :return: (int) The size of the record.
        """
        return len(self.record)
    
    def print_record(self):
        """
        Print the record to the console.
        :return: None.
        """
        print(self.record)


class Array:

    def insert(self):
        return

    def delete(self):
        return

    def search(self):
        return

    def update(self):
        return

    def traverse(self):
        return

    def isEmpty(self):
        return

    def size(self):
        return

class LinkedList:

    def insert(self):
        return

    def delete(self):
        return

    def search(self):
        return

    def update(self):
        return

    def traverse(self):
        return

    def isEmpty(self):
        return

    def size(self):
        return


class BinaryTree:

    def insert(self):
        return

    def delete(self):
        return

    def search(self):
        return

    def update(self):
        return

    def traverse(self):
        return

    def isEmpty(self):
        return

    def size(self):
        return


class HashTable:

    def insert(self):
        return

    def delete(self):
        return

    def search(self):
        return

    def update(self):
        return

    def traverse(self):
        return

    def isEmpty(self):
        return

    def size(self):
        return


class Heap:

    def insert(self):
        return

    def delete(self):
        return

    def search(self):
        return

    def update(self):
        return

    def traverse(self):
        return

    def isEmpty(self):
        return

    def size(self):
        return


class Graph:

    def insert(self):
        return

    def delete(self):
        return

    def search(self):
        return

    def update(self):
        return

    def traverse(self):
        return

    def isEmpty(self):
        return

    def size(self):
        return


class SortingAlgorithms:

    def bubble_sort(self):
        return

    def selection_sort(self):
        return

    def insertion_sort(self):
        return

    def merge_sort(self):
        return

    def quick_sort(self):
        return

    def heap_sort(self):
        return

    def counting_sort(self):
        return

    def radix_sort(self):
        return

    def bucket_sort(self):
        return

class SearchAlgorithms:

    def linear_search(self):
        return

    def binary_search(self):
        return

    def hash_table_search(self):
        return

    def breadth_first_search(self):
        return

    def depth_first_search(self):
        return