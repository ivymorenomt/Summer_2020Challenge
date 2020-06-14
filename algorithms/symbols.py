''''create a function that takes in string of symbol pairs as a parameter
Function should return True if the symbol string is balanced or False if it is not
For symbols to be balanced, symbols must also have a closing symbol and the symbols must be
properly nested
'''
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        return None

    def is_empty(self):
        return self.items == []

def match_symbol(symbol_str):
        sym_pairs={
            '(': ')',
            '[': ']',
            '{': '}',
        }

        openers = sym_pairs.keys()
        my_stack = Stack()

        index = 0 #to use for while loop to loop thru the symbol string
        while index < len(symbol_str):
            symbol = symbol_str[index]

            if symbol in openers:
                my_stack.push(symbol)
            else:
                if my_stack.is_empty():
                    return False

                else:
                    top_item = my_stack.pop()
                    if symbol != sym_pairs[top_item]:
                        return False
            index += 1
        if my_stack.is_empty():
            return True

        return False
print(match_symbol('([{}])'))
print(match_symbol('(([{}]])'))

