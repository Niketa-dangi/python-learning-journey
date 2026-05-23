# Day 15 - Dictionary in python

student = {"name": "Rohit", "age":21, "city": "Pune"}
print(student)

#Accessing values
print(student["name"])
print(student["city"])


#Adding and Updating
student["marks"] = 85
student["city"] = "Mumbai"
print(student)

#Removing
student.pop("age")
print(student)

#Dictionary methods
print(student.keys())
print(student.values())
print(student.items())
print(student.get("name"))

#Looping
for k in student:
    print(k, student[k])

#Nested dictionary
employees = {
    "E101":{"name":"Rohit","city": "pune"},
    "E102":{"name":"Sneha","city":"Delhi"}
}    
print(employees["E101"]["name"])

#mapping wrong - correct
mapper = {
    "mombai": "Mumbai",
    "kolkatta": "kolkata"

}
print(mapper["mombai"])