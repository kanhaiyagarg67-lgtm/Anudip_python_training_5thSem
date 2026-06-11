#program to calculate corresponding seconds into hour minutes and seconds
second=int(input("enter the time in seconds(in seconds)"))
if (second<0):
    exit("Time cannot be negative")
#-------------------------------------
print("-------------------------------------------------------------")

hour=0
minute=0
if (second>=3600):    
    hour= second//3600
    second=second%3600
#converting into minute
if(second>= 60):

    minute=second//60
    second=second%60
print("Equivalent time is",hour,":",minute,":",second)
