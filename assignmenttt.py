# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, value):
#         self.stack.append(value)

#     def display(self):
#         print("Stack:", self.stack)


# s = Stack()

# s.push(10)
# s.push(20)
# s.push(30)

# s.display()


class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Deleted:", self.stack.pop())

    def display(self):
        print("Stack:", self.stack)


s = Stack()

s.stack = [10, 20, 30]




s.pop()
s.display()




class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def display(self):
        if len(self.stack) == 0:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in self.stack:
                print(i)


s = Stack()

s.push(10)
s.push(20)
s.push(30)

s.display()





class Stack:
    def __init__(self):
        self.stack = []

    def reverse_string(self, string):
        for i in string:
            self.stack.append(i)

        reverse = ""

        while len(self.stack) > 0:
            reverse = reverse + self.stack.pop()

        return reverse


s = Stack()

string = input("Enter a string: ")

print("Reversed string:", s.reverse_string(string))





class Stack:
    def __init__(self):
        self.stack = []

    def reverse_stack(self):
        stack2 = []

        while len(self.stack) > 0:
            stack2.append(self.stack.pop())

        self.stack = stack2

    def display(self):
        print("Stack:", self.stack)


s = Stack()

s.stack = [10, 20, 30]

print("Original Stack:", s.stack)

s.reverse_stack()

print("Reversed Stack:", end=" ")
s.display()




