#this is for comprehensions

def list_comprehension():
    print('List comprehension for integers:\n')
    l = [1, 2, 3]
    new_list = [x*2 for x in l]
    print(f'This is coded in list comprehension: {new_list}')

    '''The list comprehension above is similar to the code below'''
    numbers = [1,2,3]
    new_numbers = []
    for num in numbers:
        new_number = num * 2
        new_numbers.append(new_number)
    print(f'This is coded in non list comprehension logic: {new_numbers}')

    print('\nList comprehension for strings:\n')
    name = 'marjorie'
    new_name = [char.upper() for char in name]
    print(f'Print all characters in capital letters: {new_name}')

    friends = ['ashley', 'matt', 'michael']
    new_friends = [friend[0].upper() for friend in friends]
    print(f'print the first character and convert to upper case: {new_friends}')

    new_list_friends = [friend[0].capitalize() + friend[1:] for friend in friends]
    print(f'capitalize the names: {new_list_friends}')

    ranges = [num*10 for num in range(1,6)]
    print(f'Range: {ranges}')

    boolean = [bool(val) for val in [1, [], '']]
    print(f'Boolean: {boolean}')

    num = [1,2,3,4,5]
    string_list = [str(num) for num in numbers]
    print(f'Numbers converted to string: {string_list}')

    evens = [n for n in num if n % 2 == 0]
    print(f'Even number: {evens}')

    odd = [n for n in num if n % 2 != 0]
    print(f'Odd number: {odd}')

    st = [25, 91, 22, -7, -20]
    new_st = [str(x) for x in st if x % 5 == 0]
    print(new_st)

    vowels = 'mathematics'
    new_vowel = list(set([str(char) for char in vowels if char in 'aeiou']))
    print(new_vowel)

    rem_vowel = 'the quick brown fox jumps over the lazy dog'
    new_list = ''.join(char for char in rem_vowel if char not in 'aieou')
    print(new_list)

    words_not_the = "the quick brown fox jumps over the lazy dog"
    split_words = words_not_the.split()

    new_words = ' '.join(word for word in split_words if word not in "the" )
    print(split_words[0:])
    print(new_words)
    wiggle = [72, 26, 79, 70, 20, 68, 43, -71, 71, -2]
    new_even = [x*2 if x % 2 == 0 else x*-1 for x in wiggle ]
    print(new_even)




list_comprehension()