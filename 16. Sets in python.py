#DAY 16 - SETS IN Python


#CREATE TABLE  
fruits = {"Apple","Banana","Apple"}
print(fruits)

#Add items
fruits.add("Orange")
print(fruits)

#Remove items
fruits.discard("Banana")
print(fruits)

#Set Operation
a = {1, 2, 3, }
b = {3, 4, 5, }
print("union",a|b)
print("Intersection:",a&b)
print("Difference:",a - b)
print("Symmetic Difference:", a ^ b)

#Remove Duplicates
cities = ["Mumbai","Pune","Delhi","Mumbai"]
unique = set(cities)
print("unique Cities:",unique)

#Missing values
list1 = {"SQL","Excel","Power BI"}
list2 = {"SQL","Power BI"}
missing = list1 - list2
print("Missing:",missing)

#Common skills
dept1 = {"SQL", "Excel", "Power BI"}
dept2 = {"SQL","Power BI","python"}
print("common sets:", dept1 & dept2)


