#import module numeric calculations
from numericcalculation import *
#----------------------------------
#main program
num1 = float(input("Enter the first number : "))
num2 = float(input("Enter the second number : "))
#to calculate addition
print("Addition : ",add(num1, num2))
#to calculate subtraction
print("Difference between",num1," and ",num2,"is : ",subtract(num1, num2))
#to calculate multiplication
print("Product : ",multiply(num1, num2))
#to calculate division
print("Quotient : ",divide(num1, num2))
#to calculate modulus
print("Modulus : ",modulus(num1, num2))
#to calculate floor division
print("Floor Division : ",floor_division(num1, num2))
#----------------------------------------------------
'''Output:
Enter the first number : 10
Enter the second number : 3
Addition :  13.0
Difference between 10.0  and  3.0 is :  7.
Product :  30.0
Quotient :  3.3333333333333335
Modulus :  1.0
Floor Division :  3.0
    '''
