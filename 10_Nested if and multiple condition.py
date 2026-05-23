# 9- python - nested if and multiple condition

print("Check your Elligibility")

age=int(input("Enter your age :"))
if age>=18:
    id_no=int(input("Enter your id number:"))
    if id_no == 1722:
        print("You can enter")
    else:
        print("Wrong id number")
else:
    print("you are underage")



 # Multiple condition (and)
age=int(input("Enter your age:"))
residence=input("Are you indian?:")

if age>=18 and residence=="yes":
    print("Eligible to drive")
else:
    print("Not Eligible to drive")
        
    


