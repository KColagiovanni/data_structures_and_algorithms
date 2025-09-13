class Record:

    def __init__(self):
        self.record = {}

    def insert_record(self, record_id, value):
        """
        Insert a value into the record.

        Time Complexity: O(1)

        :param record_id: (int) The record_id for the new entry.
        :param value: (dict) The value for the new entry.
        :return: (bool) True if the insertion was successful, else False.
        """
        if record_id in self.record:
            print(f'Insert failed!! Record ID({record_id}) already exists!!')
            return False
        else:
            self.record[record_id] = value
            print(f'Record inserted successfully')
            return True

    def insert_new_item(self, record_id, key, value):
        """
        Insert a new item into an existing record.

        Time Complexity: O(1)

        :param record_id: (int) The record_id for the new entry.
        :param key: (str) The key of the value to be updated.
        :param value: (str) The new value for the updated record.
        :return: (bool) True if the update was successful, else False.
        """
        if record_id in self.record:
            self.record[record_id][key] = value
            print(f'Item insertion successful! [{key}: {value}] was added to Record ID({record_id})')
            return True
        else:
            print(f'Item insertion failed!! Record ID({record_id}) was not found!!')
            return False

    def delete_record(self, record_id):
        """
        Delete an entire record.

        Time Complexity: O(1)

        :param record_id: (int) The record_id for the new entry.
        :return: (bool) True if the deletion was successful, else False.
        """
        if record_id in self.record:
            del self.record[record_id]
            print(f'Record ID({record_id}) was deleted successfully!')
            return True
        else:
            print(f'Delete failed!! Record ID ({record_id}) does not exist!!')
            return False

    def delete_record_value(self, record_id, key):
        """
        Delete a key and value in the provided record.

        Time Complexity: O(1)

        :param record_id: (int) The record_id for the new entry.
        :param key: (str) The key of the value to be deleted.
        :return: (bool) True if the deletion was successful, else False.
        """
        if record_id in self.record:
            if key in self.record[record_id]:
                value_to_delete = self.record[record_id][key]
                del self.record[record_id][key]
                print(f'{key}: {value_to_delete} in Record ID({record_id}) was deleted successfully!')
                return True
            else:
                print(f'Delete failed!! Record ID ({record_id}) key ({key}) does not exist!!')
                return False
        else:
            print(f'Delete failed!! Record ID ({record_id}) does not exist!!')
            return False

    def search(self, record_id):
        """
        Search for a value in the record.

        Time Complexity: O(1)

        :param record_id: (int) The record_id for the new entry.
        :return: (bool) True if the search was successful, else False.
        """
        if record_id in self.record:
            print(f'Record ID({record_id}) has been found! The value is {self.record[record_id]}')
            return True
        else:
            print(f'{record_id} was not found, because it does not exist!!')
            return False

    def update(self, record_id, key, new_value):
        """
        Update a value in the record.

        Time Complexity: O(1)

        :param record_id: (int) The record_id for the new entry.
        :param key: (str) The key of the value to be updated.
        :param new_value: (str) The new value for the updated record.
        :return: (bool) True if the update was successful, else False.
        """
        if record_id in self.record:
            old_value = self.record[record_id][key]
            self.record[record_id][key] = new_value
            print(f'Update successful! The "{key}" value in Record ID({record_id}) has changed from {old_value} to {self.record[record_id][key]}')
            return True
        else:
            print(f'Update failed!! id: {record_id} was not found!!')
            return False

    def delete_all(self):
        """
        Delete all records.

        Time Complexity: O(1)

        :return: (bool) True if the clearing of the records was successful, else False.
        """
        if self.is_empty():
            print('There are no records to delete.')
            return False
        else:
            self.record.clear()
            print('All records have been deleted!')
            return True

    def traverse(self):
        """
        Traverse the record and print out each record id and value, line by line.

        Time Complexity: O(n)

        :return: (bool) False if the record is empty, else True.
        """
        if self.is_empty():
            print('Record is empty.')
            return False
        else:
            for record_id, value in self.record.items():
                print(f'Record ID: {record_id}')
                for key, entry in value.items():
                    print(f'  - {key}: {entry}')
            return False

    def is_empty(self):
        """
        Check if the record is empty.

        Time Complexity: O(n)

        :return: (bool) True if the record is empty, else False.
        """
        if self.size() > 0:
            return False
        else:
            return True

    def size(self):
        """
        Return the size of the record.

        Time Complexity: O(n)

        :return: (int) The size of the record.
        """
        return len(self.record)
    
    def print_record(self):
        """
        Print the record to the console.

        Time Complexity: O(n)

        :return: None.
        """
        print(self.record)


class Array:

    def __init__(self):
        self.capacity = 2  # The capacity of the array.
        self.size = 0  # The current size of the array.
        self.data = [None] * self.capacity

    def _resize(self, new_capacity):
        """
        Resize the underlying storage array.
        :param new_capacity: (int) The new capacity of the array.
        :return: None.
        """
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def insert(self, index, item):
        """
        Inserts the specified item at the specified index.
        :param index: (str) The index of the array where the item will be inserted.
        :param item: (any) The item that will be inserted to the list.
        :return: None.
        """
        if index < 0 or index > self.size:
            print("Insert failed: Invalid index.")
            return False

        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = item
        self.size += 1
        return True

    def append(self, item):
        """
        Adds the specified item to the end of the array.
        :param item: (any) The item to be appended to the list.
        :return: None.
        """
        return

    def clear(self):
        """
        Clears all the items from the array.
        :return: None.
        """
        return

    def search(self, item):
        """
        Preform a binary search for the specified item.
        :param item: (any) The item to be searched for.
        :return index: (int) The index of specified item, if the item is not found, -1 will be returned.
        """
        return

    def pop(self, index=-1):
        """
        Removes the item at the specified index, if an index is not given, the last item will be removed.
        :param index:
        :return: None.
        """
        return

    def length(self):
        """
        Returns the number of items in the array.
        :return size: (int) The number of items in the array.
        """
        return

    def print_array(self):
        """
        Prints out the content of the array in a less pretty way than the traverse method.
        :return: None.
        """
        print(self.data)

    def traverse(self):
        """
        Prints out the content of the array.
        :return: None.
        """
        for i in range(self.size):
            print(self.data[i], end=", ")
        print()

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

    def is_empty(self):
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

    def is_empty(self):
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

    def is_empty(self):
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

    def is_empty(self):
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

    def is_empty(self):
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