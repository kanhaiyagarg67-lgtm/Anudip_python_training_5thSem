#program to calculate area and perimeter of rectangle
l=int(input("enter the length"))
#condition for non-negative length
if (l<0):
    exit("length cannot be negative")
b=int(input("enter the breadth"))
#condition for non-negative breadth
if(b<0):
    exit("breadth cannot be  negative")
else:
    #area calculation
    print("area is :", l*b)
    #parameter calculation
    print("perimeter is:", 2*(l+b))
