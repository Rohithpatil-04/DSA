# class node:
#     def __init__(self,value):
#         self.data=value
#         self.next=None
#         pass
# class scll:
#     def __init__(self):
#         self.head=None
#     def append(self,new_node):
#         if(self.head==None):
#             self.head=new_node
#         else:
#             temp=self.head
#             while(temp.next !=self.head):
#                 temp=temp.next
#             temp.next=new_node
#         new_node.next=self.head
#     def insert(self,new_node,pos):
#         if pos==1:
#             self.head=new_node
#             temp=self.head
#         else:
#             p=1
#             temp=self.head
#             while(p!=pos-1):
#                 temp=temp.next
#                 p+=1
#             new_node.next=temp.next
#             temp.next=new_node
#     def delete(self,value):
#         temp=self.head
#         pre=None
#         if temp is None:
#             print("List is empty")
#             return
#         if temp.data==value:
#             self.head=self.head.next
#         else:
#             while temp and temp.data!=value:
#                 pre=temp
#                 temp=temp.next
#             if temp==None:
#                 print("value is not present ")
#                 return
#             pre.next=temp.next
#             temp=None
#     def print(self):
#             print()
#             print("list elements: ")
#             temp=self.head
#             while(True):
#                 print(temp.data,end=" ")
#                 temp=temp.next
#                 if temp==self.head:
#                     break
# list1=scll()
# n1=node(10) 
# n2=node(20)  
# list1.append(n1)
# list1.append(n2)
# list1.append(node(30))
# list1.append(node(40))
# list1.print()

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class SinglyCircularLinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            if self.head == None:
                new_node = Node(data)
                self.head  = new_node
                new_node.next = self.head
                return

            new_node = Node(data)
            t = self.head

            while t.next != self.head:
                t = t.next

            t.next = new_node
            new_node.next = self.head

        def traverse(self):
            if self.head == None:
                print("Linked list is empty!")
                return

            t = self.head
            if t.next == self.head:
                print(t.data," ->",self.head)
                return
            while True:
                print(f"{t.data} -> ",end="")
                t=t.next
                if t == self.head:
                    break
            print(self.head.data)

        # def insert(self, posi, data):
        #     new_node = Node(data)
        #     if posi == 1:
        #         if self.head == None:
        #             self.head = new_node
        #             return
        #         new_node.next = self.head
        #         self.head = new_node
        #         return
        #     count = 1
        #     t = self.head
        #
        #     while count != (posi - 1):
        #         t = t.next
        #         count += 1
        #     new_node.next = t.next
        #     t.next = new_node

        def insert(self,data,posi):
            new_node = Node(data)
            if self.head == None:
                self.head = new_node
                new_node.next = self.head
                return

            if posi == 1:
                new_node.next = self.head
                t = self.head
                while t.next != self.head:
                    t=t.next
                t.next = new_node
                self.head = new_node
                return

            count  = 1
            t = self.head
            while count != posi -1:
                t=t.next
                count+=1

            if t.next == self.head:
                new_node.next = t.next
                t.next = new_node
                return

            new_node.next = t.next
            t.next = new_node
            return



if __name__ == "__main__":
    list = SinglyCircularLinkedList()
    list.append(22)
    list.append(32)
    list.append(42)
    list.traverse()
    list.insert(10,1)
    list.traverse()
    list.insert(60,5)
    list.traverse()