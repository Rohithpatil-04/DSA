class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self, max_size=None):
        self.top = None
        self._size = 0
        self.max_size = max_size  # Set None for unlimited capacity

    def is_empty(self):
        return self.top is None

    def is_full(self):
        if self.max_size is None:
            return False
        return self._size >= self.max_size

    def size(self):
        return self._size

    def push(self, data):
        if self.is_full():
            print(f"Stack Overflow! Cannot push '{data}'.")
            return
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        print(f"Pushed '{data}' onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Stack is empty.")
            return None
        popped_data = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.top.data

    def search(self, target):
        current = self.top
        position = 1  # 1-based position from the top
        while current:
            if current.data == target:
                return position
            current = current.next
            position += 1
        return -1

    def clear(self):
        self.top = None
        self._size = 0
        print("Stack cleared.")

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
            return
        elements = []
        current = self.top
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Stack (Top -> Bottom):", " -> ".join(elements))


def main():
    stack = Stack(max_size=5)  # Use Stack() for unlimited dynamic nodes

    while True:
        print("\n--- NODE-BASED STACK MENU ---")
        print("1. Push\n2. Pop\n3. Peek (Top)\n4. Size")
        print("5. Search\n6. Display\n7. Clear\n8. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            val = input("Enter value to push: ")
            stack.push(val)
        elif choice == "2":
            popped = stack.pop()
            if popped is not None:
                print(f"Popped element: {popped}")
        elif choice == "3":
            top = stack.peek()
            if top is not None:
                print(f"Top element: {top}")
        elif choice == "4":
            limit = stack.max_size if stack.max_size else "Unlimited"
            print(f"Current size: {stack.size()} / {limit}")
        elif choice == "5":
            val = input("Enter value to search: ")
            pos = stack.search(val)
            if pos != -1:
                print(f"Found '{val}' at position {pos} from the top.")
            else:
                print(f"'{val}' not found in stack.")
        elif choice == "6":
            stack.display()
        elif choice == "7":
            stack.clear()
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
