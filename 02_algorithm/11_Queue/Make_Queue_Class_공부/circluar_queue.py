class Queue:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return (self.rear + 1) % self.size == self.front

    def q_peek(self):
        if self.is_empty():
            print('Queue is Empty')
        else:
            return self.items[self.front+1]

    def en_queue(self, item):
        if self.is_full():
            print('Queue is Full')
        else:
            self.rear = (self.rear + 1) % self.size
            self.items[self.rear] = item
	
    def de_queue(self):
        if self.is_empty():
            print('Queue is Empty')
        else:
            self.front = (self.front + 1) % self.size
            return self.items[self.front]

    def __str__(self):
        return f'{self.items}'


queue = Queue(10)
print(queue)
print(queue.is_empty())
print(queue.is_full())
print(queue.size)
queue.de_queue()
queue.en_queue(10)
print(queue)
print(queue.q_peek())
print(queue.front)
print(queue.rear)
for i in range(3, 7):
    queue.en_queue(i)
print(queue.de_queue())
print(queue.de_queue())
print(queue.de_queue())
print(queue)
print(queue.front)
print(queue.rear)
print(queue.q_peek())
for i in range(10, 16):
    queue.en_queue(i)
print(queue)
print(queue.is_full())
print(queue.front)
print(queue.rear)
print(queue.q_peek())
queue.en_queue(345)
queue.en_queue(346)
print(queue)