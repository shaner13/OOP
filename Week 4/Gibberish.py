#Program to implement 'Gibberish' game using Python.
#The game will first tell the user the rules.
#Then it will prompt the user for two 'Gibberish' infixes to be used,
#also allowing the user to make use of the '*' wildcard.
#Finally it will prompt the user for a word to be translated into 'Gibberish'.
#This will be accomplished using the two infixes they provided, which will be inserted,
#into every syllable, (each new vowel will be considered a syllable).
#Before the program exits the user will be asked if they would like to play again.

import string

#Initialising Variables

vowels = "aeiouAEIOU"
gibberish_string = ''

first_vowel_complete = False
second_vowel_complete = False

#Getting user input and explaining rules.

print("Hello! Welcome to the Gibberish game!\n You will be asked for two gibberish infixes\n"
      "then you will be asked for a word to be translated to gibberish using your vowels.\n"
      "The infix will be inserted after each vowel, but not for consecutive vowels.\n"
      "If you would like you may use the '*' wildcard at the start of your syllable to add the vowel"
      "to your gibberish\n"
      "syllable. If your word is longer than two syllables it will repeatedly add the second\n"
      "gibberish infix you provided before each vowel.\n Lastly you will asked if you would"
      "like to play again or exit the game once your word has been translated.\n Enjoy!\n")

user_syllable_1 = input("Please enter a syllable.\n")
user_syllable_2 = input("Please enter another syllable.\n")
user_word = input("Finally, please enter a word to be translated into gibberish.\n")

#Converting Word to gibberish.

#ib ob
#shaners
#sh ib a n ob e rs

for i,char in enumerate(user_word):
    if char in vowels:
        if first_vowel_complete == False:
            gibberish_string = user_word[i-1] + user_syllable_1 + char
            first_vowel_complete = True

print(gibberish_string)






