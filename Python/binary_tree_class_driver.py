from data_structures_and_algorithms import BinaryTree
import csv

csv_filename = 'random_numbers.csv'

def binary_tree_example_test():

    bt = BinaryTree()

    bt.delete(2)

    print('\n########## Insert ##########')
    bt.insert(50)
    bt.insert(30)
    bt.insert(70)
    bt.insert(20)
    bt.insert(40)
    bt.insert(60)
    bt.insert(80)

    """
    Inorder = [20, 30, 40, 50, 60, 70, 80]
    
    Visual Tree:
              50
            /    \
          30      70
         /  \    /  \
        20  40  60  80
    """
    print('\n########## Pre-delete Traversal ##########')
    print("Inorder:", bt.inorder())          # [20, 30, 40, 50, 60, 70, 80]
    print("Preorder:", bt.preorder())        # [50, 30, 20, 40, 70, 60, 80]
    print("Postorder:", bt.postorder())      # [20, 40, 30, 60, 80, 70, 50]
    print("Height:", bt.height())            # 2 (levels: 50 -> 30 -> 20)
    print("Node count:", bt.count_nodes())   # 7

    print('\n########## Delete ##########')
    bt.delete(2)
    bt.delete(30)

    print('\n########## Post-delete Traversal ##########')
    print("Inorder after delete:", bt.inorder())   # [20, 40, 50, 60, 70, 80]
    print("Node count after delete:", bt.count_nodes())  # 6

def read_from_csv():

    bt = BinaryTree()

    # Open the random_numbers.csv file in read mode and append the data to a list.
    with open(csv_filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            for item in row:
                bt.insert(int(item))

    print('\n########## Pre-delete Traversal ##########')
    print("Inorder:", bt.inorder())
    print()
    print("Preorder:", bt.preorder())
    print()
    print("Postorder:", bt.postorder())
    print()
    print("Height:", bt.height())
    print()
    print("Node count:", bt.count_nodes())


# binary_tree_example_test()
read_from_csv()