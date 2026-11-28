
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create / Insert at end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        print("Node inserted successfully")

    # 2. Display / Traversal
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # 3. Insert at beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print("Node inserted at beginning")

    # 4. Insert at specific position (1-based)
    def insert_position(self, data, position):
        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node
        print("Node inserted successfully")

    # 5. Delete from beginning
    def delete_beginning(self):
        if self.head is None:
            print("Linked List is empty")
            return

        self.head = self.head.next
        print("First node deleted")

    # 6. Delete from end
    def delete_end(self):
        if self.head is None:
            print("Linked List is empty")
            return

        if self.head.next is None:
            self.head = None
            print("Last node deleted")
            return

        temp = self.head
        while temp.next.next:
            temp = temp.next

        temp.next = None
        print("Last node deleted")

    # 7. Delete from specific position
    def delete_position(self, position):
        if self.head is None:
            print("Linked List is empty")
            return

        if position < 1:
            print("Invalid position")
            return

        if position == 1:
            self.delete_beginning()
            return

        temp = self.head

        for i in range(position - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None or temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next
        print("Node deleted successfully")

    # 8. Search an element
    def search(self, key):
        temp = self.head
        position = 1

        while temp:
            if temp.data == key:
                print("Element found at position:", position)
                return
            temp = temp.next
            position += 1

        print("Element not found")

    # 9. Count nodes
    def count(self):
        temp = self.head
        total = 0

        while temp:
            total += 1
            temp = temp.next

        print("Total nodes:", total)

    # 10. Reverse linked list
    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        print("Linked List reversed")

    # 11. Find middle element
    def middle(self):
        if self.head is None:
            print("Linked List is empty")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle element:", slow.data)

    # 12. Find maximum and minimum
    def maximum_minimum(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head
        maximum = minimum = temp.data

        while temp:
            maximum = max(maximum, temp.data)
            minimum = min(minimum, temp.data)
            temp = temp.next

        print("Maximum:", maximum)
        print("Minimum:", minimum)

    # 13. Sort linked list
    def sort(self):
        if self.head is None:
            print("Linked List is empty")
            return

        current = self.head

        while current:
            index = current.next

            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next

            current = current.next

        print("Linked List sorted")


# Main Menu
ll = SinglyLinkedList()

while True:
    print("\n------ SINGLY LINKED LIST MENU ------")
    print("1. Insert at End")
    print("2. Display")
    print("3. Insert at Beginning")
    print("4. Insert at Position")
    print("5. Delete from Beginning")
    print("6. Delete from End")
    print("7. Delete from Position")
    print("8. Search Element")
    print("9. Count Nodes")
    print("10. Reverse Linked List")
    print("11. Find Middle Element")
    print("12. Maximum and Minimum")
    print("13. Sort Linked List")
    print("14. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        data = int(input("Enter data: "))
        ll.insert_end(data)

    elif choice == 2:
        ll.display()

    elif choice == 3:
        data = int(input("Enter data: "))
        ll.insert_beginning(data)

    elif choice == 4:
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))
        ll.insert_position(data, pos)

    elif choice == 5:
        ll.delete_beginning()

    elif choice == 6:
        ll.delete_end()

    elif choice == 7:
        pos = int(input("Enter position: "))
        ll.delete_position(pos)

    elif choice == 8:
        key = int(input("Enter element to search: "))
        ll.search(key)

    elif choice == 9:
        ll.count()

    elif choice == 10:
        ll.reverse()

    elif choice == 11:
        ll.middle()

    elif choice == 12:
        ll.maximum_minimum()

    elif choice == 13:
        ll.sort()

    elif choice == 14:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
