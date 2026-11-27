
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    # 1. Insert
    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)

        elif data > root.data:
            root.right = self.insert(root.right, data)

        else:
            print("Duplicate value not allowed")

        return root

    # 2. Search
    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # 3. Inorder (Left Root Right)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # 4. Preorder (Root Left Right)
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # 5. Postorder (Left Right Root)
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # 6. Minimum value
    def minimum(self, root):
        if root is None:
            return None

        while root.left:
            root = root.left

        return root.data

    # 7. Maximum value
    def maximum(self, root):
        if root is None:
            return None

        while root.right:
            root = root.right

        return root.data

    # 8. Delete node
    def delete(self, root, key):
        if root is None:
            return None

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            # No child
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            # Two children
            successor = self.minimum(root.right)
            root.data = successor
            root.right = self.delete(root.right, successor)

        return root

    # 9. Count total nodes
    def count_nodes(self, root):
        if root is None:
            return 0

        return (1 + self.count_nodes(root.left)
                + self.count_nodes(root.right))

    # 10. Count leaf nodes
    def count_leaf(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        return (self.count_leaf(root.left)
                + self.count_leaf(root.right))

    # 11. Height of tree
    def height(self, root):
        if root is None:
            return 0

        return 1 + max(self.height(root.left),
                       self.height(root.right))

    # 12. Find parent
    def find_parent(self, root, key):
        parent = None

        while root:
            if root.data == key:
                return parent

            parent = root

            if key < root.data:
                root = root.left
            else:
                root = root.right

        return None

    # 13. Display tree
    def display(self, root, level=0):
        if root:
            self.display(root.right, level + 1)
            print("   " * level, root.data)
            self.display(root.left, level + 1)


# Main program
tree = BST()

while True:

    print("\n------ BST MENU ------")
    print("1. Insert")
    print("2. Search")
    print("3. Inorder")
    print("4. Preorder")
    print("5. Postorder")
    print("6. Minimum")
    print("7. Maximum")
    print("8. Delete")
    print("9. Count Nodes")
    print("10. Count Leaf Nodes")
    print("11. Height")
    print("12. Find Parent")
    print("13. Display Tree")
    print("14. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        tree.root = tree.insert(tree.root, value)

    elif choice == 2:
        value = int(input("Enter value to search: "))

        if tree.search(tree.root, value):
            print("Element Found")
        else:
            print("Element Not Found")

    elif choice == 3:
        tree.inorder(tree.root)
        print()

    elif choice == 4:
        tree.preorder(tree.root)
        print()

    elif choice == 5:
        tree.postorder(tree.root)
        print()

    elif choice == 6:
        print("Minimum:", tree.minimum(tree.root))

    elif choice == 7:
        print("Maximum:", tree.maximum(tree.root))

    elif choice == 8:
        value = int(input("Enter value to delete: "))

        if tree.search(tree.root, value):
            tree.root = tree.delete(tree.root, value)
            print("Node Deleted")
        else:
            print("Element Not Found")

    elif choice == 9:
        print("Total Nodes:", tree.count_nodes(tree.root))

    elif choice == 10:
        print("Leaf Nodes:", tree.count_leaf(tree.root))

    elif choice == 11:
        print("Height:", tree.height(tree.root))

    elif choice == 12:
        value = int(input("Enter node value: "))
        parent = tree.find_parent(tree.root, value)

        if not tree.search(tree.root, value):
            print("Node Not Found")
        elif parent is None:
            print("Root node has no parent")
        else:
            print("Parent:", parent)

    elif choice == 13:
        if tree.root is None:
            print("Tree is Empty")
        else:
            tree.display(tree.root)

    elif choice == 14:
        print("Program Exited")
        break

    else:
        print("Invalid Choice")
