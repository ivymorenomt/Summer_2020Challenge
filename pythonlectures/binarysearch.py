#https://www.techiedelight.com/binary-search/

def linear(data, target):
    for i in range(len(data)):
        if data[i] == target:
            print(f'Found the number {target} at index {i}')
            return True
    print('Number not found')
    return False
data = [2,3,84,90,20,100,19,25,33,37]
target = 25

print('Linear Search performed:')
linear(data, target)

#iterative binary search
'''when searching, If the target is greater than the middle, it should ignore the first half/the lesser half of the middle
'''
def binary_search_iterative(data, target):
    #divide and conquer. Split the list in half. Look at the middle. is the middle greater than or less than?
    low = 0 #first element of the list
    high = len(data) - 1 #last element of the list
    #data = sorted(data)

    while low <= high:
        mid = (low + high) //2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1

    print('Number not found')
    return False

#recursive Binary search
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) //2 #to get the mid point
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1) #look at the high and mid of search iterative
        else:
            return binary_search_recursive(data, target, mid+1 , high)

print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data)-1))