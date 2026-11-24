#bst using linked list 
class node:
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data= value

class BST:
    def __init__(self):
        self.root=None

    def insert(self,new_node):
        if self.root is None:
            self.root = new_node

        else:
            temp=self.root
            while True:

             if new_node.data<temp.data:

                if temp.left is None:
                    temp.left=new_node
                    return
                else:

                     temp=temp.left

             else:
                 if temp.right is None:
                     temp.right=new_node
                     return
                 else:
                     temp=temp.right

    def inorder(self,rt):
        if rt is None:
           return
        else:
            self.inorder(rt.left)
            print(rt.data,end= " ")
            self.inorder(rt.right)


    def preorder(self,rt):
        if rt is None:
            return
        else:
            print(rt.data , end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)


    def postorder(self,rt):
            if rt is None:
                return
            else:

                print(rt.data , end=" ")
                self.postorder(rt.left)
                self.postorder(rt.right)

    def findminmax(self,rt):
                temp=rt
                while temp.left:
                    temp=temp.left

                print("\nmin: ",temp.data)
                temp=rt
                while temp.right:
                    temp=temp.right

                print("\nmax:",temp.data)

b1=BST()
b1.insert(node(100))
b1.insert(node(10))
b1.insert(node(450))
b1.insert(node(0))
b1.insert(node(300))
b1.insert(node(65))
print("\ninorder")
b1.inorder(b1.root)
print("\npreorder")

b1.preorder(b1.root)

print("\npostorder")

b1.postorder(b1.root)