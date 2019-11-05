'''
Program to implement many fraction functions that support the "tuple" data type.
and do other things.
'''

def gcd(a,b):
    if a == 0:
        return b
        
    return gcd(b%a, a) 
    
def lcm(a,b):
    lcm = a * b // gcd(a, b)
    return lcm

def addFrac(frac1,frac2):
    denominator = lcm(frac1[1],frac2[1])
    frac1_numerator = frac1[0] * frac2[1]
    frac2_numerator = frac2[0] * frac1[1]
    frac3 = [frac1_numerator + frac2_numerator, denominator]
    return frac3
    
def subFrac(frac1,frac2):
    denominator = lcm(frac1[1],frac2[1])
    frac1_numerator = frac1[0] * frac2[1]
    frac2_numerator = frac2[0] * frac1[1]
    frac3 = [frac1_numerator - frac2_numerator, denominator]
    return frac3    
    
def reduceFrac(frac1):
    divisor = gcd(frac1[0],frac1[1])
    frac3 = [frac1[0]//divisor, frac1[1]//divisor]
    return frac3    
    
a = int(input("Enter a number.\n"))
b = int(input("Enter a number.\n"))
c = int(input("Enter a number.\n"))
d = int(input("Enter a number.\n"))

fraction1 = a,b
fraction2 = c,d

print("GCD of:(", a ,",", b ,") is - ", gcd(fraction1[0],fraction2[0]))
print("LCM of:(", a ,",", b ,") is - ", lcm(fraction1[0],fraction2[0]))
print(addFrac(fraction1,fraction2))
print(subFrac(fraction1,fraction2))
print(reduceFrac(fraction1))

