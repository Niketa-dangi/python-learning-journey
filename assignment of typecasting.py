# A python program to Generate an Employee Salary Slip
name = input("Employee Name:")
Basic_Salary = float(input("Enter Basic_Salary:"))
Bonus_Amount = float(input("Enter Bonus Amount:"))
Tax_Percentage = float(input("Enter Tax % age:"))
 

 #Program should calculate:
Gross_Salary = Basic_Salary+Bonus_Amount,
Tax_Amount = Gross_Salary*(Tax_Percentage/100),
net_Salary = Gross_Salary-Tax_Amount,


print("\n...Employee Salary Slip:...")
print("Employee Name:",name)
print("Gross_Salary:",Gross_Salary)
print("Tax_Amount:",Tax_Amount)
print("net_Salary:",net_Salary)               