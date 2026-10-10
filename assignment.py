
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def create(self):
        n = int(input("Enter number of nodes: "))
        temp = None

        for i in range(n):
            value = int(input("Enter node value: "))
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
                temp = new_node
            else:
                temp.next = new_node
                temp = new_node

        print("Created Linked List:")
        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


    
    def traverse(self):
        temp = self.head

        if temp is None:
            print("Linked List is empty")
            return

        print("Linked List:")
        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


    
    def insert(self):
        value = int(input("Enter value to insert: "))
        pos = int(input("Enter position: "))

        new_node = Node(value)

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
        else:
            temp = self.head

            for i in range(pos - 2):
                if temp is None:
                    print("Invalid position")
                    return
                temp = temp.next

            if temp is None:
                print("Invalid position")
                return

            new_node.next = temp.next
            temp.next = new_node

        print("Node inserted successfully!")



    
    def middle(self):
        if self.head is None:
            print("Linked List is empty")
            return

        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        print("Middle node:", slow.data)


    
    def delete(self):
        value = int(input("Enter value to delete: "))

        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            print("Node deleted successfully!")
            return

        temp = self.head

        while temp.next is not None:
            if temp.next.data == value:
                temp.next = temp.next.next
                print("Node deleted successfully!")
                return

            temp = temp.next

        print("Value not found")


    
    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

        print("Linked List reversed successfully!")


    
    def consecutive_sum(self):
        temp = self.head

        if temp is None or temp.next is None:
            print("Need at least two nodes")
            return

        while temp.next is not None:
            total = temp.data + temp.next.data

            print(temp.data, "+", temp.next.data, "=", total)

            temp = temp.next





ll = LinkedList()

ll.create()
ll.traverse()

ll.insert()
ll.traverse()

ll.middle()

ll.delete()
ll.traverse()

ll.reverse()
ll.traverse()

ll.consecutive_sum()

