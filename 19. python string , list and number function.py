#DAY 19 -STRING,LIST,AND NUMBER FUNTION IN PYTHON

#STRING FUNCTIONS
text = "banana"
print(text.count("a"))

print ("hello.py" .endswith(".py"))

print("Sales_Report.csv" .startswith("Sales"))

print("123".isdigit())

print("ABC".isalpha())

print("A1B2".isalnum())

print("Line1\nLine2".splitlines())

# List functions
nums = [5, 2, 7, 1]

nums.sort()
print(nums)

fruits = ["Banana","Apple","Mango"]
print(sorted(fruits))

marks = [1, 2, 1, 3, 1 ]
print(min(marks), max(marks), sum(marks))

mylist = [1, 2, 1, 3, 1, 4, 1, 5, ]
print(mylist.count(5))
print(mylist.index(4))

a = [1, 2]
b = [3, 4]
a.extend(b)
print(a)

#Number functions
print(round(3.678, 0))
print(abs(-50))
print(pow(25, 2))
print(divmod(10, 2))
print(sum([5,5,5],5))

# Practical examples
products = [" mobile ", "Laptop", " TABLET"]
clean = [p.strip().title()for p in products]
clean.sort()
print(clean)

emails = ("rohit@gmail.com","mohit@yahoo.com")
domains = [mail[mail.find("g")+1:]for mail in emails]
print(domains)

mobiles = ["9876543210","123456789","123456"] 
valid = [m for m in mobiles if m.isdigit() and len(m)==10]
print(valid)


