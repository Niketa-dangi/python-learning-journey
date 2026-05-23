#learning data types in python
# 7 data types

# 1.Text data type
# string
customer_name="Rohit"
print("customer name is",customer_name)
print("customer data type is", type(customer_name))

# 2. Numeric data type
# 2.1  Integer complete number 
rating = 4
order_quantity = 3
print("Rating data type", type(rating))
print("order_quantity data type", type(order_quantity))

# 2.2. float: decimal number
order_amount = 8599.90
print("order_amount data type :",type(order_amount))

# 2,3 . Complex Number
a=3+4j
print(type(a))


# 3. Boolean- True/False
is_paid = True
print(is_paid,type(is_paid))

# 4.Sequence data type
# 4.1 . List Sequence data type
cities = ["Mumbai","Delhi","Pune","Chennai"]
print(cities)
print(type(cities))

# 4.2 . Tuple
dimensions = (1930,2000)
print(dimensions)
print(type(dimensions))


#4.3. Range
num = range(5)
print(list(num))
#[0,1,2,3,4]
print(type(num))


days = range(1,31) #1 to 30 days
print(list(days))

# 5. Mapping data type
# 5.1 dictionary (dict.)
student = {
    "name": "Avni",
    "age" : 5,
    "city": "Mumbai"
}
print(student)
print(type(student))

# 6. set data type 
number = {0,1,2,3,4,5}
print(number)
print(type(number))


#7. None data type
remarks = "None"
print(remarks,type(None))




