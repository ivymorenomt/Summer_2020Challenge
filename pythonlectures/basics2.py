#conditional logic
def if_else():
    is_old = True
    is_licensed = True
    if is_old and is_licensed:
        print('You are Legal to drive')
    else:
        print('You are not legal to drive')

#ternary operator - conditional expressions
def ternary_lecture():
    #condition_is_true if condition else condition_if_else - if condition is true, then condition would get triggered, else execute the second statement
    is_allowed = False
    can_message = 'You are allowed to send me a friend request' if is_allowed else 'You are not allowed to send me a friend request'
    print(can_message)


def equality():
    
    print(True == 1)
    print('' == 1)
    print([] == 1)
    print(10 == 10.0)
    print([] == [])
    
    # is would check if the location and memory where the value is stored is the same
    print(True is True)


#loops
def for_loop():
    for item in (1,2,3,4,5):
        for x in ['a', 'b', 'c']:
            print(item, x)

#iterable - list, dictionary - check one by one in a collection - looping over something
def iterable_lec():
    user = {
        'name': 'gollum',
        'age' : 100,
        'can_swim': False
    }
    for item in user.items():
        print(item)

    for values in user.values():
        print(values)

    #tuple unpacking
    for key, value in user.items():
        print('\n', key, value)

#range, enums
def range_lec():
    print(range(100))
    for x in range(10):
        print(x)

    #the underscore does not care about a variable, it only cares about the range
    print('This will print from 1 to 20\n') 
    for _ in range(1, 21):
        print(_) 
    
    print('This will print in reverse\n')
    for _ in range(10, 0, -1):
        print(_)
    
    print("This will print in 2s\n")
    for _ in range(0,5,2):
        print(_)

def enum_lec():
    for i, char in enumerate(list(range(100))):
        print(i, char)
        if char == 50:
            print(f'The index of 50 is: {i}')

#While loops - while a condition is happening, do something
def while_lec():
    i = 0
    while i < 50:
        print(i)
        i += 1
   # else:
    print('Done with all the work')

#when to use while and for loop?
    list_no = [1,2,3]

    for i in list_no:
        print(i)
    #the same can be done with while loop
    i=0
    while i < len(list_no):
        print(list_no[i])
        i += 1
    #for iterating simple collections or if you know the size of a list, then use for loop, while would be for iterable objects that you ar not sure of the size

    while True:
        input('Say something: ') 
        break

if __name__ == "__main__":
    while_lec()