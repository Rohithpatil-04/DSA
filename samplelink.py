
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter data: "))
            self.insert_end(data)

    # Display Linked List
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")

    # Insert at Beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Insert at Position (1-based)
    def insert_position(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.insert_begin(data)
            return

        temp = self.head

        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node

    # Delete from Beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # Delete at Position (1-based)
    def delete_position(self, pos):
        if self.head is None or pos < 1:
            print("Invalid operation")
            return

        if pos == 1:
            self.delete_begin()
            return

        temp = self.head

        for i in range(pos - 2):
            if temp.next is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp.next is None:
            print("Invalid position")
            return

        temp.next = temp.next.next

    # Search Element
    def search(self, key):
        temp = self.head
        pos = 1

        while temp:
            if temp.data == key:
                print("Element found at position", pos)
                return

            temp = temp.next
            pos += 1

        print("Element not found")

    # Count Nodes
    def count(self):
        temp = self.head
        c = 0

        while temp:
            c += 1
            temp = temp.next

        print("Total nodes:", c)

    # Find Middle Element
    def middle(self):
        if self.head is None:
            print("List is empty")
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print("Middle element:", slow.data)

    # Reverse Linked List
    def reverse(self):
        prev = None
        temp = self.head

        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node

        self.head = prev

    # Sum of All Nodes
    def total_sum(self):
        temp = self.head
        total = 0

        while temp:
            total += temp.data
            temp = temp.next

        print("Sum:", total)


# Main Program
ll = LinkedList()

while True:
    print("\n--- LINKED LIST MENU ---")
    print("1. Create")
    print("2. Display")
    print("3. Insert Beginning")
    print("4. Insert End")
    print("5. Insert Position")
    print("6. Delete Beginning")
    print("7. Delete End")
    print("8. Delete Position")
    print("9. Search")
    print("10. Count")
    print("11. Middle Element")
    print("12. Reverse")
    print("13. Sum")
    print("14. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        ll.create()

    elif ch == 2:
        ll.display()

    elif ch == 3:
        data = int(input("Enter data: "))
        ll.insert_begin(data)

    elif ch == 4:
        data = int(input("Enter data: "))
        ll.insert_end(data)

    elif ch == 5:
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))
        ll.insert_position(data, pos)

    elif ch == 6:
        ll.delete_begin()

    elif ch == 7:
        ll.delete_end()

    elif ch == 8:
        pos = int(input("Enter position: "))
        ll.delete_position(pos)

    elif ch == 9:
        key = int(input("Enter element to search: "))
        ll.search(key)

    elif ch == 10:
        ll.count()

    elif ch == 11:
        ll.middle()

    elif ch == 12:
        ll.reverse()
        print("List reversed")

    elif ch == 13:
        ll.total_sum()

    elif ch == 14:
        print("Program ended")
        break

    else:
        print("Invalid choice")
