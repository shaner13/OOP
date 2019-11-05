'''Program to implement scramble using python. The program will prompt
the user for a string of words and will then scramble each word and return
a string of the scrambled words..
'''
import random
import string

letters = string.ascii_letters
result = ""

scramble_words = input("Enter some text to be scrambled.\n").split()
print(scramble_words)

for word in scramble_words:
    
    if len(word) <= 1:
        result += result + " "
        continue
    
    word = list(word)
    for ch in range(0, len(word)):
        swap_char1 = random.randrange(0, len(word) -1)
        swap_char2 = random.randrange(0, len(word) -1)
            
        if (swap_char1 != swap_char2 and word[swap_char1] in letters and word[swap_char2] in letters):
            temp = word[swap_char1]
            word[swap_char1] = word[swap_char2]
            word[swap_char2] = temp
                
    result += "".join(word) + " "
    
print(result)    
