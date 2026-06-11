#program to check three angles form triangle or not
angle1= float(input("Enter first angle"))
#validate angle
if(angle1<=0):
    exit("angle must be positive")
#----------------------------------
angle2 = float(input("entee second angle"))
if(angle2<=0):
    exit("angle must be positive")
#----------------------------------
angle3= float(input("enter third angle"))
if(angle3<=0):
    exit("angle must be positive")
#----------------------------------
if(angle1+angle2+angle3 == 180):
    print("Above angles form a triangle")
else:
    print("Above angles do not form a triangle")
