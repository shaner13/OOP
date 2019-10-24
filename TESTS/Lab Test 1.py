'''
Lab test 1.

Author: Shane Riedy

Date 24/10.2019
'''

def make_new_row(old_row):
    
    new_row = [1]
    
    #Special cases for old row.
    if (old_row == []):
        return [1]
    if (old_row == [1]):
        return [1, 1]
    
    #for loop to add new elements to new_row.    
    for i in range(len(old_row)):
        
        if(i==len(old_row)-1):
            new_row.append(1)
            break 
        if(i<len(old_row)-1):
            new_row.append(old_row[i]+old_row[i+1])
        
    return new_row

#Driver Program

old_row = []
master_list = []
list1 = [1,2,3,4]

#Getting User Input
while(1):
    height = input("Enter the desired height of Pascal's triangle.\n")
    height = int(height)
    if(height<=0):
        print("Please enter a height that is larger than 0.\n")
    else:
        break

#Generating The Triangle
for i in range(height):
    old_row = make_new_row(old_row)#appending master list with each row of pascal's triangle.
    master_list.append(old_row)
    
print("Printing whole list of lists:\n")
print(master_list)
print("Printing list of lists, one list at a time:\n")
for i in range(len(master_list)):
    print(master_list[i])

#Printing Pascal's triangle in a triangular format. No commas or square
#bracket will be shown.


for i in master_list:
    new_list = ' '.join(str(i))
    print(new_list.center(100))

