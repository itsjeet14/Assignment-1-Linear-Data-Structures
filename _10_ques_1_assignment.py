"""Implement a queue using the stack data structure"""

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return "Queue is empty"
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

# create a new queue object
queue = Queue()

# get user input for the number of elements to enqueue
num_elements = int(input("Enter the number of elements to enqueue: "))

# enqueue elements to the queue
for i in range(num_elements):
    element = int(input("Enter the element to enqueue: "))
    queue.enqueue(element)

# dequeue all elements from the queue
print("Dequeueing all elements from the queue:")
while True:
    element = queue.dequeue()
    if element == "Queue is empty":
        break
    print(element)
