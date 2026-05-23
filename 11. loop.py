# DAY 11- FOR LOOP


#BASIC LOOP
for i in range(1,11):
    print(i)

# print characters
word="Python"

for alphabet in word:  
    print(alphabet)

word2 = "SQL"
for j in range(1,11):
   print(word2)


#  LOOP THROUGH LIST
items = ["Pen", "Book", "Laptop"]
for item in items:
    print(item)

 # EVEN NUMBERS
print("Print even numbers")
for n in range(0,20,2):
 print(n)

#Total calculation
marks = [78,89,90]
total = 0
for n in marks:
 total += n
print("total",total)


# CLEAN CITY NAMES

cities=["Mumbai" , "pune" , "CHENNAI"]
cleaned = []
for c in cities:
    cleaned.append(c.strip().title())
print(cleaned)


# LOOP WITH IF CONDITION
nums = [5, 12, 3, 18, 7]
for n in nums:
    if n>10:
        print(n, "is greater then 10")
    else:
        print(n,"is not grater then 10")



# 89 extract last four IDs
ids = ["EMP-001122","EMP-889900"]
for last4 in ids:
    print(last4[-5:])








