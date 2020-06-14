# only add items to and remove from the top of the stack
#LIFO - last in first out
#Python list is the best to use
#right side would be the top - which is the end of the list. it is for operating time
# a stack can be empty

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        ''''Accepts an item as a paramenter and appends to the end of the list
        it returns nothing
        The runtime for the method is o(1) or constant time, because appending to the end
        of a list happens in constant time
        '''
        return self.items.append(item)

    def pop(self):
        ''''#we don't need to specify an index since pop is built in
        removes and returns the last item from the list which is also
        the top item of the stack
        The runtime is constant time,because all it does is index to the last item of the list
        '''
        if self.items: #if there is something in the items, return the item
            print(f'Item popped: {item[-1]}')
            return self.items.pop()
        return None

    def peek(self):
        ''''This method returns the last item in the list which is also the top item of the stack.
        This method runs in constant time because  all it does is index to the last item of the list'''
        if self.items:
            print(f"Last item in the stack: {self.items[-1]}")
            return self.items[-1]
        return None

    def size(self):
        print(f'Size of the stack: {len(self.items)}')
        return len(self.items)

    def is_empty(self):
        return self.items == []

if __name__ == '__main__':

    item = ['Apple', 'Banana', 'Orange', 'Pineapple']
    my_item = Stack()
    print(my_item.is_empty())
    for i in item:
        my_item.push(i)
    print(my_item.is_empty())
    print('Current items: ', my_item.items)
    my_item.peek()
    my_item.size()
    my_item.pop()
    print('Updated items: ', my_item.items)
    my_item.peek()
