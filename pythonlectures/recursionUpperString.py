#Given a string, find the uppercase character

input1 = 'lucidProgramming'
input2 = 'LucidProgramming'
input3 = 'lucidprogramming'

def find_uppercase_iterative(input_str):
    for i in range(len(input_str)):
        if input_str[i].isupper():
            return input_str[i]
    return 'No upprcase character found'

def find_uppercase_recursive(input_str, idx = 0):
    if input_str[idx].isupper():
        return input_str[idx]
    if idx == len(input_str) - 1:
        return 'No Upprcase character found'
    return find_uppercase_recursive(input_str, idx + 1)

print(find_uppercase_iterative(input1))
print(find_uppercase_iterative(input2))
print(find_uppercase_iterative(input3))


print(find_uppercase_recursive(input1))
print(find_uppercase_recursive(input2))
print(find_uppercase_recursive(input3))