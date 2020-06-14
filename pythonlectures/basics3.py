from functools import reduce

my_list = [1,2,3]
your_list = [10, 20, 30]
def multiply(item):
    #map will create a list for you without affecting the original list
    return item*2

def only_odd(item):
    return item % 2 != 0


print(list(map(multiply, my_list)))
print(my_list)
print(list(filter(only_odd, my_list)))
print(my_list)
#zip adds items together and creates a tuple
print(list(zip(my_list, your_list)))

#import reduce function to use in our code
#we reduce the list by accumulating the items and add them

def accumulator(acc, item):
    #acc + item = will add the items
    print(acc, item) # so here it would be (0, 1) - 0 + 1 will return 1, and so on (1, 1) (1,2)
    return acc + item
print('\nThe reduced value is: \n')
print(reduce(accumulator, my_list, 0)) # 0 will be the default number if there is no value in accumulator