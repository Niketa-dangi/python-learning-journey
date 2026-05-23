#DAY - 14 TUPLES

#create table
fruits = ("Apple","Banana","Mango")
print(fruits)

#Indexing
print(fruits[0])
print(fruits[-1])

#Slicing
nums = (10, 20, 30, 40, 50,)
print(nums[3:])

#Looping
colors = ("Red", "blue", "Green",)
for c in colors:
    print(c)

#Tuple length
print(len(colors))


#Concatenation
a = (1, 2)
b = (3, 4)
print(a + b)

#Packing and Unpacking
data = ("Laptop",45000,"Black")
product,price,color = data
print(f"Product : (product)Price : (price) and color : (color)")

# Nested tuple inside list
employees = [("E101","Rohit", "Pune") , ("E102","Mohit","Mumbai")]
for eid, name, city in employees:
    print(eid, name, city)
