
class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    # Insert element
    def enqueue(self, value):
        if self.is_full():
            print("Queue is Full")
        else:
            self.queue.append(value)
            print(value, "inserted")

    # Delete element
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            print("Deleted element:", self.queue.pop(0))

    # Display front element
    def peek(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            print("Front element:", self.queue[0])

    # Display all elements
    def display(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            print("Queue:", self.queue)

    # Get front
    def get_front(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            print("Front:", self.queue[0])

    # Get rear
    def get_rear(self):
        if self.is_empty():
            print("Queue is Empty")
        else:
            print("Rear:", self.queue[-1])

    # Check empty
    def is_empty(self):
        return len(self.queue) == 0

    # Check full
    def is_full(self):
        return len(self.queue) == self.size

    # Count elements
    def get_size(self):
        print("Size:", len(self.queue))

    # Search element
    def search(self, value):
        if value in self.queue:
            print(value, "found at position",
                  self.queue.index(value) + 1)
        else:
            print(value, "not found")


# Main program
n = int(input("Enter queue size: "))
q = Queue(n)

while True:
    print("\n----- QUEUE MENU -----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Get Front")
    print("6. Get Rear")
    print("7. Is Empty")
    print("8. Is Full")
    print("9. Size")
    print("10. Search")
    print("11. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter element: "))
        q.enqueue(value)

    elif choice == 2:
        q.dequeue()

    elif choice == 3:
        q.peek()

    elif choice == 4:
        q.display()

    elif choice == 5:
        q.get_front()

    elif choice == 6:
        q.get_rear()

    elif choice == 7:
        print("Queue is Empty" if q.is_empty()
              else "Queue is Not Empty")

    elif choice == 8:
        print("Queue is Full" if q.is_full()
              else "Queue is Not Full")

    elif choice == 9:
        q.get_size()

    elif choice == 10:
        value = int(input("Enter element to search: "))
        q.search(value)

    elif choice == 11:
        print("Program Exited")
        break

    else:
        print("Invalid Choice")
