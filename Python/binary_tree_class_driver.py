from data_structures_and_algorithms import BinaryTree

def binary_tree_example_test():

    bt = BinaryTree()

    bt.delete(2)

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

    print("Inorder:", bt.inorder())          # [20, 30, 40, 50, 60, 70, 80]
    print("Height:", bt.height())            # 2 (levels: 50 -> 30 -> 20)
    print("Node count:", bt.count_nodes())   # 7

    bt.delete(2)
    bt.delete(30)
    print("Inorder after delete:", bt.inorder())   # [20, 40, 50, 60, 70, 80]
    print("Node count after delete:", bt.count_nodes())  # 6

binary_tree_example_test()