# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in,
# first-out) data structure with the following methods: enqueue, which inserts
# an element into the queue, and dequeue, which removes it.

class Queue:
    stack1 = []
    stack2 = []

    def enqueue(self, elem):
        self.stack1.append(elem)

    def dequeue(self):
        if not self.stack2:
            if not self.stack1:
                return None
            
            while self.stack1:
                self.stack2.append(self.stack1.pop())    

        return self.stack2.pop()

def main():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue.dequeue() == 1)
    
    queue.enqueue(5)
    print(queue.dequeue() == 2)
    print(queue.dequeue() == 3)
    print(queue.dequeue() == 4)
    
    queue.enqueue(6)
    print(queue.dequeue() == 5)
    print(queue.dequeue() == 6)

if __name__ == "__main__":
    main()