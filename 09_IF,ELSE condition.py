# # IF ELSE CONDITIONS

age=int(input("Enter Your age:"))

if age>=18:
   print("Qualified for voting")
else:
    print("Not Qualified for voting")  


# Discount Checker
amount = 1500
if amount>=1000:
  print("You get a discount")
else:
   print("No discount")

# if-elif-else (Multiple Condition)
marks =int(input("Enter your marks:"))   
if marks >=90:
   print("Grade A")
elif marks >=75:
   print("Grade B")
else:
   print("Fail")

 # # Sales Performance (Data Analyst Use Case)
sales = 65000
if sales >= 10000:
    print("High performer") 
elif sales >= 50000:
    print("Medium performer") 
else:
    print("Lower performer")


#String comparison Example
city = "Delhi"
if city.lower()=="delhi":
    print("City matched")
else:
    print("City not matched")

# Email Validation
email = "user@example.com"
if "@" in email and "."in email:
    print("Valid Email")
else:
    print("Invalid Email") 
               

#Advanced Missind Data check
value = "sdf"
if value == " ":
    print("Missing Data Found")
else:
    print("Data found")
        
   


    
