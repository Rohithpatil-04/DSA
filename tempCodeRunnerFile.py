 def dequeue(self):

        if len(self.queue) == 0:
            print("Queue is Empty!")
        else:
            process = self.queue.pop(0)
            print("Executed Process:", process)