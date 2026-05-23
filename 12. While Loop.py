# DAY - 12 WHILE LOOP

# 1. Basic while loop

i=1
while i<=5:
    print(i)
    i+=1

# countdown

n=5
while n>0:
    print(n)
    n-=1


# Ask user until valid input
num=""
while not num.isnumeric():
    num = input("Enter any value: ")
    print("Please enter only number")
print("Number acerpted:", num) 

20
# Loop through list using while
items = ["Apple", "Banana", "Grapes"]
i = 0
while i < len(items):
    print(items[i])
    i += 1

#Using Break
x = 1
while x <= 10:
    break
print(x)
x += 1


# using continue
y = 0 
while y<10:
    y+=1
    if y%2 == 0:
        continue
    print(y)

#Password system (Advanced)
password = ""
attempts = 0

while password != "admin123" and attempts < 3:
    password = input("Enter your password: ")
    attempts += 1
    if password == "admin123":
        print("Login Successful")
    else:
        print("Wrong Password Try again, Attempt count :",attempts)
    if attempts==3:
        print("3 attempt expired ")





   



   

