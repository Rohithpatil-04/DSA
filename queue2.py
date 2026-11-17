class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self,data):
        node = Node(data)

        if self.top == None:
            self.top = node
            return

        node.next = self.top
        self.top = node

    def pop(self):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.next
            return data

    def print(self):
        if not self.isEmpty():
            t= self.top
            print("Stack elements: ")
            while t:
                print(f"{t.data}",end=" ")
                t=t.next

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None


    def isEmpty(self):
        if self.front == None:
            return True


    def enque(self,data):

        node = Node(data)

        if self.front ==None:
            self.front = self.rear = node
            return

        self.rear.next = node
        self.rear = node


    def deque(self):
        if self.isEmpty():
            print("Queue is empty!")
            return

        t= self.front
        self.front = self.front.next
        if self.front == None:
            self.rear = None
            print("Queue is now empty!")
        data = t.data
        t = None
        return data

    def print(self):
        if self.isEmpty():
            print("Queue is empty!")
            return

        t = self.front
        print("Queue elements: ")
        while t:
            print(t.data,end=" ")
            t=t.next
        print()

    def reverse(self):
        if self.front is None:
            print("Queue is empty!")
            return
        print("Queue elements in reverse: ")
        s = Stack()
        t = self.front
        while t:
            s.push(t.data)
            t=t.next

        s.print()

def reverseStack(s : Stack):
    if s.isEmpty():
        print("Stack underflow!")
        return

    q = Queue()

    while not s.isEmpty():
        q.enque(s.pop())

    while not q.isEmpty():
        s.push(q.deque())

    s.print()



# q = Queue()
# q.enque(10)
# q.enque(20)
# q.enque(30)
# q.print()
# q.enque(40)
# q.print()
# q.reverse()
s = Stack()
s.push(11)
s.push(21)
s.push(31)
s.push(41)
s.print()
reverseStack(s)