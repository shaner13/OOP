#Program to implement 'Gibberish' game using Python.
#The game will first tell the user the rules.
#Then it will prompt the user for two 'Gibberish' infixes to be used,
#also allowing the user to make use of the '*' wildcard.
#Finally it will prompt the user for a word to be translated into 'Gibberish'.
#This will be accomplished using the two infixes they provided, which will be inserted,
#into every syllable, (each new vowel will be considered a syllable).
#Before the program exits the user will be asked if they would like to play again.

#Creating File

filename = input("Please name your file.\n")
filename = filename + '.txt'
filename_length = len(filename)
input_file = open(filename,"w")
print("Honestly, the story is complete gibberish,with only the kind of goofy logic a child would come up with.\n",file=input_file)
output_file = filename[:filename_length-4] + 'Gibberish' + '.txt'
output_file = open(output_file,"a+")

#Explaining rules

print("Hello! Welcome to the Gibberish game!\nYou will be asked for two gibberish infixes\n"
        "then you will be asked for a word to be translated to gibberish using your vowels.\n"
        "The infix will be inserted after each vowel, but not for consecutive vowels.\n"
        "If you would like you may use the '*' wildcard at the start of your syllable to add the vowel"
        "to your gibberish\n"
        "syllable. If your word is longer than two syllables it will repeatedly add the second\n"
        "gibberish infix you provided before each vowel.\nLastly you will asked if you would"
        "like to play again or exit the game once your word has been translated.\nEnjoy!\n")

play = 'y'

while(play == 'y' or play == 'yes'):

    #Initialising Variables

    vowels = "aeiouAEIOU"
    gibberish_string = ''
    first_vowel_complete = False


    #Getting user input

    user_syllable_1 = input("Please enter a syllable.\n")
    user_syllable_2 = input("Please enter another syllable.\n")
    user_word = input("Finally, please enter a word to be translated into gibberish.\n")
    length = len(user_word)

    #Converting Word to gibberish.

    for i,char in enumerate(user_word):
        if char in vowels:
            if first_vowel_complete == False:
                if user_syllable_1[0] == '*':
                    if i == length-2:
                        gibberish_string = user_word[0:i] + char + user_syllable_1[1:] + char + user_word[i+1:i+2]
                        j = i
                        first_vowel_complete = True
                    #end if
                    else:
                        gibberish_string = user_word[:i] + char + user_syllable_1[1:] + char
                        j = i
                        first_vowel_complete = True
                    #end else
                #end if
                else:
                    if i == length-2:
                        gibberish_string = user_word[0:i] + user_syllable_1 + char + user_word[i+1:i+2]
                        j = i
                        first_vowel_complete = True
                    #end if
                    else:
                        gibberish_string = user_word[:i] + user_syllable_1 + char
                        j = i
                        first_vowel_complete = True
                    #end else
                #end else
            #end if
            else:
                if user_syllable_2[0] == '*':
                    if user_word[i-1] not in vowels:
                        if user_word[length-2] not in vowels:
                            gibberish_string = gibberish_string + user_word[j:i] + char + user_syllable_2[1:] + char + user_word[i+1:length]
                            j = i
                        #end if
                        else:
                            gibberish_string = gibberish_string + user_word[j:i] + char + user_syllable_2[1:] + char
                            j= i
                        #end else
                    #end if

                else:
                    if user_word[i-1] not in vowels:
                        if user_word[length-2] not in vowels:
                            gibberish_string = gibberish_string + user_word[j:i] + user_syllable_2 + char + user_word[i+1:length]
                            j = i
                        #end if
                        else:
                            gibberish_string = gibberish_string + user_word[j:i] + user_syllable_2 + char
                            j = i
                        #end else
                    #end if
                #end else
            #end else
         #end if
    #end for

    print("Your word in gibberish is:",gibberish_string)
    print(gibberish_string,file=output_file)
    play = input("Would you like to play again? y/n\n")

#end while
