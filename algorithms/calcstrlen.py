# given a string, calculate the length of the string

input_str = input('Enter a string and calculate the length removing spaces:\n')

print(len(input_str))

# when solving iteratively, loop thru the character and keep running a count of number of characters
def iterative_str_length(input_str):
    count=0
    input_str = input_str.replace(" ", "")
    for i in range(len(input_str)):
        count +=1
    return count # this is the cumulative count

def recursive_str_len(input_str):
    input_str = input_str.replace(" ", "")
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])

print(iterative_str_length(input_str))
print(recursive_str_len(input_str))