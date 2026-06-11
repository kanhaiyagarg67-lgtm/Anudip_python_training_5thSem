
#program to cheeck the type of  triangle on basis of sides if triangle is vakid
#Accept the three sides of the triangle from the user
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

# Check whether the given sides can form a valid triangle
# Sum of any two sides must be greater than the third side
if (b + c > a and c + a > b and a + b > c):

    # Check if all three sides are different
    if (a != b and b != c and a != c):
        print("Scalene Triangle")

    # Check if all three sides are equal
    elif a == b and b == c:
        print("Equilateral Triangle")

    # If neither scalene nor equilateral, it must be isosceles
    else:
        print("Isosceles Triangle")

# If triangle inequality condition fails
else:
    print("Triangle not valid")
