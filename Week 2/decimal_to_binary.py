#intiialising variables

decimal_num = 0
correct = 0
i = 0
binary = ''


while(correct==0):

    decimal_num = int(input("Enter a number to be converted to binary.\n"))

    if(decimal_num>=0):

        correct = correct + 1

     #end if

    else:

        print("Enter a positive integer please.")

    #end else
#end while.

while(decimal_num>0):

    if(decimal_num % 2 == 0):

        binary = binary + '0'
    #end if

    else:

        binary = binary + '1'

    #end else

    decimal_num = decimal_num // 2

#end while

print("Your number in binary is:\n")

print(binary[::-1])

#end for
