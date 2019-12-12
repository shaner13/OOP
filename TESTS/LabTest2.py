'''

Program to implement a 3D vector class in python.
The Vector class will also encapsulate a lot of 
basic math operators, such as 
Adding
Subtracting,
Multiplying (by an integer (returns scalar product) and another vector.)
There is also a constructor and __str__ function available in the class.
The class also has __radd__ __rmul__ and __rsub__.
Lastly a driver program is added at the end which will test out these functions
and show the output.

Author: Shane Riedy

Date: 12/12/2019

'''
import string 
import math

#Creating the Vector class.
class Vector:
    #init method, where all values will be defined.
    #default values for x,y,z are all 0.
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z 

    def __str__(self):
        return "({:.6f},{:.6f},{:.6f})".format(float(self.x),float(self.y),float(self.z))
    
    def __repr__(self):
        return self.__str__
    
    def __add__(self, other_vector):
        if type(other_vector) == int or type(other_vector) == float:
            other_vector = Vector(other_vector.x,other_vector.y,other_vector.z)
                
        if type(other_vector) == Vector:
            return Vector(other_vector.x+self.x,other_vector.y+self.y,other_vector.z+self.z)
                
        else:
            print("Invalid types. Unable to add.\n")
            
        return self    
            
            
    def __sub__(self, other_vector):
        if type(other_vector) == int or type(other_vector) == float:
            other_vector = Vector(other_vector.x,other_vector.y,other_vector.z)
                
        if type(other_vector) == Vector:
            return Vector(other_vector.x-self.x,other_vector.y-self.y,other_vector.z-self.z)
                
        else:
            print("Invalid types. Unable to subtract.\n")
        
        return self    
        
    #this method will multiply the vector coordinates by another vector's coorindates.
    #E.g (x*a,y*b,z*c)
    def __mul__(self, multiplier):
        if type(multiplier) == int:
            return Vector(self.x*multiplier,self.y*multiplier,self.z*multiplier)
        
        #If the other object passed is not an integer, implying it is another vector 
        #to be multiplied by it will convert it. Then return the scalar product.
        #Introspection is performed either way, just to ensure that it is a Vector object.
        if type(multiplier) == int or type(multiplier) == float: 
            multiplier = Vector(multiplier.x,multiplier.y,multiplier.z)
                
        if type(multiplier) == Vector:
            temp = Vector(multiplier.x*self.x,multiplier.y*self.y,multiplier.z*self.z)
            scalar = temp.x + temp.y + temp.z
            scalar = float(scalar)
            return scalar
    
        else:
            print("Invalid types. Unable to multiply.\n")
        
        return self      
        
    def magnitude(self):
        magnitude = math.sqrt((self.x**2+self.y**2+self.z**2))
        
        return magnitude
        
    def __radd__(self, other_vector):
        return self.__add__(other_vector)
    
    def __rsub__(self, other_vector):
        return self.__sub__(other_vector)
        
    def __rmul__(self, other_vector):
        return self.__mul__(other_vector)
        
#Main program to test run the class.
def main():
    v1 = Vector(1, 2, 3)
    v2 = Vector(5, 5, 5)
    print ("Printing v1")
    print ("v1 = ", v1)
    print ("Printing v2")
    print ("v2 = ", v2)
    v3 = v1 + v2
    print ("Printing addition")
    print("v1 + v2 = ", v3)
    v4 = v1 - v2
    print ("Printing subtraction")
    print("v1 - v2 = ", v4)
    print ("Printing dot product")
    v5 = v1 * v2
    print("v1 * v2 = ", v5)
    print ("Printing integer multiplication")
    v6 = v1 * 2
    print("v1 * 2.5 = ", v6)
    print("v1 magnitude is ", v1.magnitude())
    
#function call to main
main()
            
            
