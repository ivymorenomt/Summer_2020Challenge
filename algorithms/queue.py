'''''The adding of the item in a queue is enqueue and removing is dequeue
Left side is the rear of the queue and right is the top
insert to the left - this is to constant time
pop to the right
we can only access the front of the queue
real world - print queue
queue is a recursive data structure
'''

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        '''''Takes in an item and inserts that item into the 0th index of the list

        the runtime is 0(n)'''
        return self.items.insert(0, item) #save the end of the list for popping

    def dequeue(self):
        '''The pop item will always pop the last item in the queue
        The runtime is constant time 0(1)
        '''
        if self.items:
            return self.items.pop()
        else:
            return None

    def peek(self):
        '''Returns the last item in the list which is the front most of the queue'''
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        print(f'Size of the queue: {len(self.items)}')
        return len(self.items)

    def is_empty(self):
        return self.items == []

if __name__ == '__main__':
    my_queue = Queue()
    my_queue.peek()
    my_queue.size()
    print(my_queue.is_empty())
    my_queue.enqueue('Apple')
    print(my_queue.items)
    my_queue.enqueue('Banana')
    print(my_queue.items)
    print(my_queue.peek())
    print(my_queue.is_empty())
    my_queue.size()

