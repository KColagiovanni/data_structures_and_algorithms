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
        :param index: (int) The index of the array where the item will be inserted.
        :param item: (any) The item that will be inserted to the list.
        :return: (bool) True if the insert was successful, else False.
        """

        # If index is less than -1 return false.
        if index < -1:
            print("\nInsert failed: Invalid index.")
            return False

        # If the array size is equal to the capacity, increase the array capacity.
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        # If index provided is -1 or larger than the size of the index, insert the item at the end of the array.
        if index == -1 or index > self.size:
            self.data[self.size] = item
            self.size += 1
            print(f'\nSuccessfully inserted "{item}" at the end of the array.')

        else:
            # Make room for the newly inserted item by shifting all the items down one after the inserted item.
            for i in range(self.size, index, -1):
                self.data[i] = self.data[i - 1]

            # Insert the item.
            self.data[index] = item

            # Insert the size by 1.
            self.size += 1

            print(f'\nSuccessfully inserted "{item}" at index {index}.')

        return True

    def append(self, item):
        """
        Adds the specified item to the end of the array.
        :param item: (any) The item to be appended to the end of the list.
        :return: (bool) True if the append was successful, else False.
        """

        # Increase the size of the array.
        if self.size == self.capacity:
            self._resize(self.capacity * 2)

        # Insert the item at the end of the array.
        self.data[self.size] = item

        # Increase the array size by one.
        self.size += 1

        print(f'\nSuccessfully appended {item} to the end of the array.')

        return True

    def pop(self, index=-1):
        """
        Removes the item at the specified index, if an index is not given, the last item will be removed.
        :param index: (int) The index of the array where the item will be inserted.
        :return: (bool) True if the pop was successful, else False.
        """

        # If index is less than -1 return false.
        if index < -1:
            print("\nPop failed: Invalid index.")
            return False

        # If index is -1 or larger than the size of the array, remove the last item.
        elif index == -1 or index >= self.size:
            self.data[-2] = self.data[-1]
            print(f'\nSuccessfully removed the last item from the array.')

        # Remove the item at the specified index and move all the item after it down.
        else:
            for i in range(index, self.size - 1):
                self.data[i] = self.data[i + 1]
            print(f'\nSuccessfully removed the item at index {index}.')

        # Set the end of the array to None
        self.data[self.size - 1] = None

        # Reduce the size of the array by 1.
        self.size -= 1

        # If the array size is greater than 0 and less than array capacity divided by 4, then resize the array by half.
        if 0 < self.size < self.capacity // 4:
            self._resize(self.capacity // 2)

        return True

    def clear(self):
        """
        Clears all the items from the array.
        :return: None.
        """
        while self.size > 0:
            self.pop(0)
        print('\nThe array has been cleared!!')

    def length(self):
        """
        Returns the number of items in the array.
        :return: The number of items in the array.
        """
        return self.size

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

    def search(self, item):
        """
        Preform a linear search for the specified item.
        :param item: (any) The item to be searched for.
        :return index: (int) The index of specified item, if the item is not found, -1 will be returned.
        """
        index = 0
        for element in self.data:
            if element == item:
                print(f'\n"{element}" has been found at index {index}')
                return index
            else:
                index += 1

        print(f'\n{item} was not found in the array.')
        return -1

class LinkedListNode:
    """
    Class to keep track of the node for the LinkedList class
    """
    def __init__(self, data):
        self.data = data  # The data to be passed to the method in the LinkedList class.
        self.next = None  # Pointer to the next node.

class LinkedList:

    def __init__(self):
        self.head = None   # First node (head of the list).

    def insert(self, data):
        """
        Insert a new node at the end of the linked list.
        :param data: (any) The keyword or item to be inserted.
        :return: None.
        """
        new_node = LinkedListNode(data)
        if not self.head:  # If list is empty (self.head == None as defined in the __init__ function).
            self.head = new_node  # Add a new node as the head of the linked list.
            return  # Item has been inserted to the list, so we're done here.
        current = self.head
        while current.next:  # Traverse to the end if the linked list.
            current = current.next
        current.next = new_node  # Assign the new node(data) to the end of the list.
        print(f'{data} has been successfully inserted to the end of the linked list.')

    def delete(self, key):
        """
        Find the first occurrence of the keyword, or item, passed into the function by doingf a linear search and delete
        it. If the item is not found, nothing will be deleted.
        :param key: (any) The keyword or item to be deleted.
        :return: None.
        """
        current = self.head  # Make the head of the list the current node.

        if current and current.data == key:  # If head needs to be removed/deleted.
            self.head = current.next  # Make the head the next node.
            return

        prev = None

        while current and current.data != key:  # Traverse the linked list while current is not None and the current
            # node does not equal the key.
            prev = current  # Make the current node the previous node.
            current = current.next  # Make the next node the current node.

        if current:  # The key has been found.
            prev.next = current.next  # Make the previous value point to the current keys next value. The previous node
            # now points to the node after the current node, unlinking the current node(which is equal to the key).
            print(f'Success! {key} has been found!')
        else:  # The key has not been found.
            print(f'Delete failed!! {key} could not be found!')

    def search(self, key):
        """
        Perform a linear search on the linked list, and return True if key is in the list, else False.
        :param key: (any) The keyword or item to be searched for.
        :return: (bool) True if key has been found in the list, else False.
        """
        current = self.head  # Make the head of the list the current node.

        while current:  # Traverse the linked list while the current node is not none.
            if current.data == key:  # if the current node value is equal to the key, the key has been found.
                print(f'Success!! {key} has been found.')
                return True
            current = current.next  # Continue to the next node.
        print(f'Uh oh. {key} could not be found.')
        return False

    def traverse(self):
        """
        Print all elements to the console.
        :return: None.
        """
        current = self.head  # Make the head of the list the current node.

        while current:  # Traverse the linked list while the current node is not None.
            print(current.data, end=" -> ")
            current = current.next  # Continue to the next node.
        print("None")

    def is_empty(self):
        """
        Check to see if the list is empty (size=0) and return True if the linked list is empty, else False.
        :return: (bool) True if the linked list is empty, else False.
        """
        if self.size() == 0:
            print('The linked list is empty.')
            return True
        else:
            print('The linked list is not empty.')
            return False

    def size(self):
        """
        Return the number of elements in the linked list.
        :return count: (int) The number of elements in the linked list.
        """
        count = 0
        current = self.head  # Make the head of the list the current node.

        while current:  # Traverse the list and
            count += 1
            current = current.next
        return count


class BinaryTreeNode:

    def __init__(self, data):
        self.data = data  # The data to be passed to the method in the LinkedList class.
        self.left = None
        self.right = None

class BinaryTree:
    """
    A binary tree is a tree of data. The tree root is the median value of all the values in the tree. Items that are
    less than the root are assigned to the left of the tree and items that are greater than the root are assigned to the
    right side of the tree. The tree is adjusted as needed when new data is inserted.
    """
    def __init__(self):
        self.root = None # Start with empty tree

    # ---------------- INSERT ----------------
    def insert(self, data):
        """
        Insert data into the tree.
        :param data: (any) The keyword or item to be inserted.
        :return: None
        """
        if self.root is None:  # The tree is empty
            self.root = BinaryTreeNode(data)  # Insert the item to the tree root.
            print(f'Success!!. {data} has been inserted as the root node.')
        else:
            self._insert(self.root, data)  # Call the helper function to insert the data to the appropriate tree node.

    def _insert(self, current, data):
        """
        Helper method for the insert() method.
        :param current: (any) The tree node to insert/check the data.
        :param data: (any) The keyword or item to be inserted.
        :return: None.
        """
        print()
        if data < current.data:  # If the data to be inserted is less than the tree root.
            if current.left is None:  # If the left tree node is empty(None).
                current.left = BinaryTreeNode(data)  # Insert the data to the left tree node.
                print(f'Success!! {data} has been inserted left of the root({current.data}) because it is less than the median value.')
            else:  # Else the left node is not empty
                self._insert(current.left, data)  # Call this method recursively, and pass the left node to it as the
                # root.
        else:  # Else the data to be inserted is greater than the tree root.
            if current.right is None:  # If the right tree node is empty(None).
                current.right = BinaryTreeNode(data)  # Insert the data to the right tree node.
                print(f'Success!! {data} has been inserted right of the root({current.data}) because it is greater than the median value.')
            else:  # Else the right node is not empty
                self._insert(current.right, data)  # Call this method recursively, and pass the right node to it as the
                                                   # root.
        print(f'The root node is now: {current.data}')


    # ---------------- SEARCH ----------------
    def search(self, data):
        """
        Search for specific data in the tree.
        :param data: (any) The keyword or item to be inserted.
        :return: None
        """
        return self._search(self.root, data)  # Call the helper method, passing the root node and the data to search.

    def _search(self, current, data):
        """
        Helper method for the search() method.
        :param current: (any) The tree node to insert/check the data.
        :param data: (any) The keyword or item to be inserted.
        :return: None.
        """
        if current is None:  # If there is no data in the root node and therefore no data in the binary tree.
            return False
        if current.data == data:  # The data has been found.
            print(f'Success!! {data} has been found in the binary tree.')
            return True
        elif data < current.data:  # If the item to be searched for is less than the current leaf.
            return self._search(current.left, data)  # Recursively call the helper method again passing the left node as
                                                     # current.
        else:  # Else the item to be searched for is greater than the current leaf.
            return self._search(current.right, data)  # Recursively call the helper method again passing the left node as
                                                      # current.

    # ---------------- DELETE ----------------
    def delete(self, data):
        self.root = self._delete(self.root, data)  # Call the delete helper method to delete the data parameter passed
                                                   # to the method

    def _delete(self, current, data):
        if current is None:  # If there is no data in the root node and therefore no data in the binary tree.
            print(f'The binary tree is empty, so there is nothing to delete.')
            return current

        if data < current.data:  # If the current node is greater than the data to be deleted, recursively call this
                                 # method passing in the left(lesser) node.
            current.left = self._delete(current.left, data)
            print(f'{data} not found yet. Looking to the left')
        elif data > current.data:  # If the current node is less than the data to be deleted, recursively call this
                                   # method passing in the right(greater) node.
            current.right = self._delete(current.right, data)
            print(f'{data} not found yet. Looking to the right')
        else:  # Node found.
            if current.left is None and current.right is None:  # The node has no children.
                print(f'The {data} node has no children.')
                return None
            if current.left is None:  # The node has a right child, but has no left child.
                print(f'The {data} node has a right child.')
                return current.right
            elif current.right is None:  # The node has a left child, but has no right child.
                print(f'The {data} node has a left child.')
                return current.left

            print(f'The {data} node has two children.')

            # Find inorder successor (smallest in right subtree)
            successor = self._min_value_node(current.right)

            # Replace value
            current.data = successor.data

            # Delete the inorder successor
            current.right = self._delete(current.right, successor.data)

        return current

    @staticmethod
    def _min_value_node(node):
        """
        Find the node with the smallest value in the subtree and return it.
        :param node: The parent node.
        :return: The left(smaller) child node of the node that was passed in to the method.
        """
        current = node
        while current.left is not None:
            current = current.left
        return current

    """
    +------------------------------- Depth-First Traversals --------------------------------+
    | Inorder Traversal (Left → Root → Right).                                              |
    |     * Visit left subtree first.                                                       |
    |     * Then visit root node.                                                           |
    |     * Then visit right subtree.                                                       |
    | For Binary Search Trees (BSTs), inorder traversal always gives nodes in sorted order. |
    |---------------------------------------------------------------------------------------|
    | Preorder Traversal (Root → Left → Right)                                              |
    |     * Visit root node first.                                                          |
    |     * Then left subtree.                                                              |
    |     * Then right subtree.                                                             |
    | Useful for copying a tree or generating prefix expressions.                           |
    |---------------------------------------------------------------------------------------|
    | Postorder Traversal (Left → Right → Root)                                             |
    |     * Visit left subtree.                                                             |
    |     * Then right subtree.                                                             |
    |     * Finally root node.                                                              |
    | Useful for deleting a tree (children first, root last).                               |
    +---------------------------------------------------------------------------------------+
    """
    def inorder(self):
        """
        Print the binary tree out in order from least to greatest. Call the _inorder() helper method passing the root
        and result list. The _inorder() will traverse the list recursively, then return the list items in order(least to
        greatest).
        :return result: (list) A list of the items in the binary tree.
        """
        result = []
        print(f'self.root from inorder() is: {self.root}')
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        """
        Traverse the list in order(left to right) and append each value during traversal. Go to the left most node and
        then start moving up. Left child --> Left parent --> Right child --> Grandparent(root) --> Left child --> Right
        parent --> Right child.
        :param node: The node that is being evaluated.
        :param result: (list) The list that holds the node values.
        :return: None
        """
        print(f'\nresult list is: {result}')
        if node:
            print(f'node.left is: {node.left}')
            self._inorder(node.left, result)
            print(f'node.data({node.data}) is being appended to the result list')
            result.append(node.data)
            print(f'node.right is: {node.right}')
            self._inorder(node.right, result)

    def preorder(self):
        """
        Print the binary tree out in order from least to greatest. Call the _preorder() helper method passing the root
        and result list. The _preorder() will traverse the list recursively, then return the list items.
        :return result: (list) A list of the items in the binary tree.
        """
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        """
        Traverse the list from root, then left, then right and append each value during traversal. Start at the root and
        then go to the left. Left child --> Left parent --> Right child --> Grandparent(root) --> Left child --> Right
        parent --> Right child.
        :param node: The node that is being evaluated.
        :param result: (list) The list that holds the node values.
        :return: None
        """
        if node:
            result.append(node.data)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        """
        Print the binary tree out in order from the bottom left to the top(root). Call the _postorder() helper method
        passing the root and result list. The _postorder() will traverse the list recursively, then return the list
        items.
        :return result: (list) A list of the items in the binary tree.
        """
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        """
        Traverse the list from the bottom, left up. Start at the minimum value node, then go to the right node of the
        same level, then go up to the parent of those two nodes. Then go to the next value on the bottom of the tree,
        then again, to the right node and the same level, then their parent. Keep doing that until the root node is
        reached, which will be the last value appended to the list.
        :param node: The node that is being evaluated.
        :param result: (list) The list that holds the node values.
        :return: None
        """
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.data)

    # ---------------- HEIGHT ----------------
    def height(self):
        """
        Return the height (max depth) of the tree.
        :return: (int) The height of the Binary tree.
        """
        return self._height(self.root)

    def _height(self, node):
        """
        Traverse the binary tree, then find and return the max depth/height. If it is empty return -1.
        :param node: The node that is being evaluated.
        :return: (int) The height of the Binary tree.
        """
        if node is None:
            return -1  # define empty tree height as -1
        left_h = self._height(node.left)
        right_h = self._height(node.right)
        return 1 + max(left_h, right_h)

    # ---------------- COUNT NODES ----------------
    def count_nodes(self):
        """
        Return the total number of nodes in the tree.
        :return: (int) The number of nodes in the Binary tree.
        """
        return self._count_nodes(self.root)

    def _count_nodes(self, node):
        """
        Traverse the Binary tree and count all the nodes and return that value. If it is empty, return 0.
        :param node: The node that is being evaluated.
        :return: (int) The number of nodes in the Binary tree.
        """
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)


class HashTable:

    def __init__(self, size=10):
        """
        Initialize hash table with given size (default=10).
        :param size: (int) The number of buckets in the hash table.
        """
        self.size = size
        self.table = [[] for _ in range(size)]  # list of lists (chaining)

    def _hash(self, key):
        """
        Private method: Compute hash index for a key.
        :param key: (int) The key for the hash table index.
        :return: (int) The hash index.
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Insert or update a key-value pair.
        :param key: (int) The key for the hash table index.
        :param value: (any) The value to add to the hash table in the given key bucket.
        :return: None.
        """
        index = self._hash(key)
        # Check if key already exists → update value
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # Otherwise, append new key-value pair
        self.table[index].append([key, value])

    def search(self, key):
        """
        Search for a key and return its value, or None if not found.
        :param key: (int) The key for the hash table index.
        :return: Key-Value pair if the key is found, otherwise None.
        """
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        """
        Delete key-value pair if it exists.
        :param key: (int) The key for the hash table index.
        :return: True is the key is found, else False.
        """
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def traverse(self):
        """
        Traverse and print all key-value pairs.
        :return: None
        """
        for i, bucket in enumerate(self.table):
            if bucket:
                for key, value in bucket:
                    print(f"Index {i}: {key} -> {value}")

    def count(self):
        """
        Return the number of key-value pairs in the table.
        :return: (int) The number of items in the hash table.
        """
        return sum(len(bucket) for bucket in self.table)


class MinHeap:
    """
    A MinHeap is a complete binary tree where:
        * The root is always the smallest element.
        * Each parent is ≤ its children.
        * The tree is stored in a simple list/array.


    """

    def __init__(self):
        """
        Initialize an empty heap.
        """
        self.heap = []

    def _parent(self, index):
        """
        Get parent index.
        :param index: (int) The index of the element.
        :return: (int) The index of the parent node.
        """
        return (index - 1) // 2

    def _left(self, index):
        """
        Get left child index.
        :param index: (int) The index of the element.
        :return: (int) The index of the left child.
        """
        return 2 * index + 1

    def _right(self, index):
        """
        Get right child index.
        :param index: (int) The index of the element.
        :return: (int) The index of the right child.
        """
        return 2 * index + 2

    def insert(self, value):
        """
        Insert a new value into the heap.
        :param value: (any) The value to be inserted.
        :return: None.
        """
        self.heap.append(value)  # Add at the end
        self._heapify_up(len(self.heap) - 1)  # Fix heap property

    def _heapify_up(self, index):
        """
        Move node up until heap property is restored.
        :param index: (int) The index of the element.
        :return: None.
        """
        parent = self._parent(index)
        while index > 0 and self.heap[index] < self.heap[parent]:
            # Swap if child is smaller than parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = self._parent(index)

    def delete(self):
        """
        Remove and return the smallest element (root).
        :return:
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last element to root
        self._heapify_down(0)  # Fix heap property
        return root

    def _heapify_down(self, index):
        """
        Move node down until heap property is restored.
        :param index: (int) The index of the element.
        :return: None.
        """
        smallest = index
        left = self._left(index)
        right = self._right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def search(self, value):
        """
        Search for a value in the heap (O(n)).
        :param value:
        :return:
        """
        return value in self.heap

    def traverse(self):
        """
        Traverse and print the heap.
        :return: None.
        """
        print("Heap elements:", self.heap)

    def count(self):
        """
        Return number of elements in the heap.
        :return: (int) The number of elements in the heap.
        """
        return len(self.heap)


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