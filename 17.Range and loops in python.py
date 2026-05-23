# DAY 17 - RANGE AND LOOPS  IN PYTHON

print("\n1)print 1 to 5")
for i in range (4,10):
    print(i)

print("\n2)Even Numbers (0-18)")    
for i in range (10, 0, -1):
    print(i)

print("\n3)countdown from 10 to 1 ")
for i in range (10, 0,-1 ):
    print(i)

print("\n4)Loop through list using Index")
items = ["Pen","Book","Laptop"]
for i in range (len(items)):
    print(i,items[i])

print("\n5) Gnerate Employee IDs")
for i in range(1, 6):
    print("EMP:",i)

print("\n6) Create Year List")
years = []
for y in range(2015,2026):
    years.append(y)
print(years)            

print("/n7)Clean City Names Using Range")
cities = ["MmMbai","DelHi","pune"]
for i in range (len(cities)):
    cities[i] = cities[i].strip().title()
print(cities)

#print(*\n8)Extract last 4 digit from IDs")
ids = ["EMP-001122", "EMP-550044","EMP-990011"]
for i in range(len(ids)):
    print(ids[i][-4:])

for i in range (1, 11) :
    for j in range(1,100):
        print(f"1 value : (1) 3 values :(1)")  


