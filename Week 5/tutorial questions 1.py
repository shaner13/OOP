'''
Program to implement various functions in python.

'''
import string 

def energy_equivalent(mass):
    
    c = 3.00 * 10 ** 8
    E = mass * (c ** 2)
    return E

def letter_counter(user_string):
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowel_counter = 0
    consonant_counter = 0
    for ch in user_string.lower():
        if ch in vowels:
            vowel_counter += 1
        if ch in consonants: 
            consonant_counter += 1
            
    print("Your string has:(",consonant_counter,") consonants, and (",vowel_counter,") vowels.\n")        

def display_menu():
    
    while(1):
        print("What would you like to do?\n")
        print("1) Add Numbers\n"
        "2) Subtract Numbers\n"
        "3) Multiply Numbers\n"
        "4) Divide Numbers\n"
        "5) Exit Menu\n")
        
        choice = int(input())
        if choice == 1:
            print("You have selected Add Numbers.\n")
            #make call to add numbers function.
        elif choice == 2:
            print("You have selected Subtract Numbers.\n")
            #make call to subtract numbers function.    
        elif choice == 3:
            print("You have selected Multiply Numbers.\n")
            #make call to multiply numbers function.    
        elif choice == 4:
            print("You have selected Divide Numbers.\n")
            #make call to divide numbers function.    
        elif choice == 5:
            print("You have selected Exit Menu. Bye.\n")
            return
        else:
            print("Please enter a valid choice.\n")
            
def fibonacci_sequence_nth_term(n):
    
    if n<0: 
        print("Please enter a valid input.\n")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else: 
        return fibonacci_sequence_nth_term(n-1)+fibonacci_sequence_nth_term(n-2)


def fibonacci_sequence_list(n):   
    a = 0 
    b = 1
    
    print("The first n",n," numbers of the fibonacci sequence are:")
    
    print(a)
    
    if n == 0:
        return
    
    print(b)
    
    if n == 1:
        return
    
    
    if n>1:
        for num in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)

    
    
def date_and_time(user_string):
    replacements = ['/',':']
    for ch in user_string:
        if ch in replacements:
            user_string = user_string.replace(ch, ' ')
    list1 = user_string.split()
    if(len(list1)<6):
        print("Please enter in all values asked for.\n")
        return
    
    day = int(list1[0])
    month = int(list1[1])
    year = int(list1[2])
    hours = int(list1[3])
    minutes = int(list1[4])
    seconds = int(list1[5])
    
    if (day <= 0 or day > 30 or month <= 0 or month > 12 or hours < 0 or hours > 24 or minutes < 0 or minutes > 60 or seconds < 0 or seconds > 60):
        print("You did not enter a valid day/month/hours/minutes/seconds.\n")
        return
    
    print(day,"/",month,"/",year)
    print(hours,"/",minutes,"/",seconds)
    print(month,"/",year)
    
    if(hours<12):
        print("The time is A.M\n")
    else:
        print("The time is P.M\n")


user_string = input("Enter a string of the following format 'MM/DD/YYYY HR:MIN:SEC' please.\n")
date_and_time(user_string)
    
n = int(input("Please select the first n numbers of the fibonacci sequence you would like to see.\n"))    
print(fibonacci_sequence_nth_term(n))
fibonacci_sequence_list(n)

display_menu()            
            
user_string = input("Enter a string please.\n")
letter_counter(user_string)

mass = int(input("Enter a value for mass in Kg please.\n"))
print(energy_equivalent(mass))    


