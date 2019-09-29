#initialising variables
binary = input("Enter a number in binary please.\n")
length = len(binary) - 1
decimal=0
i=0

while(i<=length):

    decimal = decimal + int(binary[i]) * 2 ** (length-i)
    i = i + 1

#end while

#printing number in decimal.
print("Your number in decimal is:\n")
print(decimal)


