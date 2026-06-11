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
    if(angle1<90 and angle2<90 and angle3<90):
        print("Above angles form a acute angled triangle")
    elif(angle1==90 or angle2==90 or angle3==90):
        print("Above angles form a right angled triangle")
    else:
        print("Above angles form a obtuse triangle")

else:
    print("Above angles do not form a triangle")
