'''Double ended queue
it resembles both stack and queue
you can add both to the front and back and remove front and back

let's use a list
bisect the list; reight hand would add and remove on the right side
on the left you could also add and remove

add to deque - front and rear
remove - front and rear
FIFO model and LIFO
'''

class Deque:

    def __init__(self):
        self.items = []
    def add_front(self, item):
        '''Takes an item as a parameter and inserts into the 0th index of the list
        Runtime is linear or O(n)
        '''
        self.items.insert(0, item)

    def add_rear(self, item):
        '''Takes in an item as a parameter and appends to the end of the list
        Runtime is constant
        '''
        self.items.append(item)

    def remove_front(self):
        '''Removes and returns the item in the 0th index of the list, which is the front
        of the Deque
        Runtime is linear or O(n) because when we remove an item from the 0th index, all the
        items will shift one index to the left
        '''
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
        '''Removes and returns the last item of the list which is the rear
        Runtime is constant because we're just removing the last index'''
        if self.items:
            return self.items.pop()
        return None

    def peek_front(self):
        if self.items:
            return self.items[0]
        return None

    def peek_rear(self):
        if self.items:
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

if __name__ == '__main__':
    my_deque = Deque()
    print(my_deque.peek_front())
    print(my_deque.peek_rear())
    my_deque.add_front('apple')
    my_deque.add_front('banana')
    my_deque.add_rear('carrot')
    my_deque.add_front('celery')
    print(my_deque.peek_front())
    print(my_deque.peek_rear())
    print(my_deque.items)
    print(my_deque.remove_front())
    print(my_deque.items)
    print(my_deque.remove_rear())
    print(my_deque.items)
    print(my_deque.peek_front())
    print(my_deque.peek_rear())