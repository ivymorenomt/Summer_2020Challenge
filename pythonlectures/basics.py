# List slicing
def list_lecture():
    li = ['notebook', 'paper', 'pencil', 'pen', 'highlighter']
    print(li[1:3]) #will print ['paper', 'pencil']
    print(li[:4]) #will print ['notebook', 'paper', 'pencil', 'pen']
    print(li[1:]) # will print ['paper', 'pencil', 'pen', 'highlighter']
    print(li[:-1]) #will print ['notebook', 'paper', 'pencil'] eliminates the last value
    print(li[-1]) #will print pencil - it traverses from the last value to the 3rd index
    print(li[:]) #will print all of the list


#Dictionary
#it is an unordered key value pair. they are not right next to each other in memory
def dictionary_lec():
    my_list = [
        {
            'list': ['a', 'b', 'c'],
            'number': 2,
            'bool': True
        }, 
        {
            'list': ['d', 'e', 'f'],
            'number': 1,
            'bool': True
        }
    ]
    print(my_list[0]['list'][2]) # this will display c  [first json object][the key you want to access][the index of the key list you want to access]
    print(my_list[1]['bool']) #this will display True - it accessed the second json object


def matrix_lecture():
    matrix = [[1, 2, 3],[4,5,6],[7,8,9]]
    print(matrix[0][2]) # this will print 3 - it accessed the first item of the matrix(1,2,3) then it accessed the second item of that item which is 3
    

#tuples are like list but you cannot modify them. it is immutable
def tuple_lecture():
    my_tuple = (1,2,3,4,5)
    print(my_tuple[3])

    x,y,z, *other = (1,2,3,4,5)
    print(other) # it will print out [4,5] the variables represent the places of each values in the tuple.

#sets are unordered collections of unique objects
def set_lecture():
    my_set = {1,2,3,4,5,5} 
    print(my_set) #this will remove the duplicate value
    my_set.add(2) #this won't add 2 anymore
    print(my_set) 

    my_list = [1,2,3,4,5,5]
    print(set(my_list)) #this will convert the list to a set and will print out unique values


#data type string - concatenation
def str_concat_lecture():
    print('hello' + ' ' + 'marj')
    name = 'marjorie'
    print(f'{name}')


if __name__ == "__main__":
    str_concat_lecture()
