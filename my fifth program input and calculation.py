# Input and Typecasting

name=input("Enter your name:")
print("Welcome", name)

age=int(input("Enter your age:"))
print(type(age))
age=age+5
print("Your age is :",age)


temperature=float(input("enter today's temperature:"))
print(type(temperature))

#convert number into string
sales=500000
text="total sales:" + str(sales)
print(text)

#Total sales calculator
product = input("Product name:")
quantity = int(input("Enter quantity sold:"))
price_per_unit = float(input("Enter price per unit:"))

total_sales = quantity*price_per_unit

print(".................")
print("product:",product)
print("total_sales_amount = ", total_sales)


fnum=int(input("Enter first num:"))
snum=int(input("Enter second num:"))

sum=fnum+snum
print(sum)
