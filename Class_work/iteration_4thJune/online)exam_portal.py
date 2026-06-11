#Program of Online Exam Portal

marks=int(input("Enter your marks: "))  #enter your marks
while(marks<40):     #runs loop until marks come more than 40 or equal then 40
    print("Result : Fail")
    marks=int(input("Enter your marks:"))   ##again take input of marks
if marks>=40: 
    print("Result : PASS")   
    print("Congratulations! You have Cleared the assessment")
