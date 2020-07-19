'''Given a string, count the number of consonants
Note a consonant is a letter that is not a vowel
i.e a letter that is not a,e,i,o,u '''

input_str = input('Enter a string:\n')

vowel = "aeiou"

def iterative_count_consonant(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowel and input_str[i].isalpha():
            count += 1
    return count

def recursive_count_consonant(input_str):
