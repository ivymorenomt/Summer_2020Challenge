'''True if a string is palindrome, if not, then it should display False'''

class Deque:

    def __init__(self):
        self.items = []
    def add_front(self, item):
        self.items.insert(0, item)

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if self.items:
            return self.items.pop(0)
        return None

    def remove_rear(self):
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

def check_palindrome(input_str):
    my_d = Deque()
    for char in input_str:
        my_d.add_rear(char)

    while my_d.size() >=2:
        front = my_d.remove_front()
        rear = my_d.remove_rear()

        if front != rear:
            return False
    return True

print(check_palindrome('racecar'))
print(check_palindrome('oranges'))