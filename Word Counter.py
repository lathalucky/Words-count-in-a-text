# 4. Character Counter
# • Create a function count_characters that takes a string as input.
# • The function should return a dictionary where keys are characters and values are
# the number of occurrences of each character in the string.

def count_characters(lst):
    char_count = {}
    for char in lst:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count

user_input=input("Enter you string:")
result=count_characters(user_input)
print(result)