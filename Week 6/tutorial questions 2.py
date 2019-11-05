'''

tutorial questions 2

'''
import math

def Kaprekar_Number_Checker(num):
    square_num = int(num) ** 2
    digits = len(str(square_num))
    for i in range(1, digits):
        part1 = str(square_num)[:i]
        part2 = str(square_num)[i:]
        sum_num = int(part1) + int(part2)
        if(sum_num == int(num)):
            return sum_num
    return ''    
            
def Kaprekar_Number_Printer(n):
    print("The list of Kaprekar numbers between 10 and",n,"is: \n")
    for i in range(10,int(n)):
        print(Kaprekar_Number_Checker(i))


n = input("Enter a value please.\n")        
Kaprekar_Number_Printer(n)
