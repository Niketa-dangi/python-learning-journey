text1="     hello python learners       "

#Remove Spaces
print("Original text:",text1)

print("Remove spaces",text1.strip())


#Convert to capital letters
print("Capital Letters :",text1.upper().strip())

#Convert to proper case
print("Proper letters :",text1.title().strip())

#Convert to lower letters
print("lower letters :",text1.lower().strip())

#Replace
print("Repalce python word with SQL",text1.replace("python","SQL"))

#Coutn occurences of a letter of word
print("Count of o:",text1.count("o"))

#Check if text start with something
print("start with hello?",text1.strip().startswith("hello"))

#Check if only numbers are present in data
mobile="9876543210"



msg="Welcome to python course"

#Split string into list of words
words=msg.split()
print("Word list :", words)

#Join back with hyphen
joined_text="..".join(words)
print("Joined text:",joined_text)

#find position of letter
print("Index of p :",msg.find("P"))
      


#Extract domain
email="student@example.com"
domain = email[email.find("@")+1:]
print("Domain:",domain)


#Advanced Example: Clean price (Remove Sprcial Character)
#Example:"Price: $3500/-".."3500"
price_text =" Price: $3500/-"
clean_price = price_text.replace("price","") \
                         .replace("$", "") \
                         .replace("/-","") \
                         
print("Clean Price:",clean_price )      
                  
