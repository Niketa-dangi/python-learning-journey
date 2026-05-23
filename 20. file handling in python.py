# DAY 20 - FILE HANDLING IN PYTHON

# 1) Reading full file
with open ("D:\\30 days python course\\sample.txt","r")as f:
    print(f.read())

# 2) Reading line by line
with open ("D:\\30 days python course\\sample.txt","r")as f:
    for line in f:
        print(line.strip().title())

# 3)Writing(overwriting)
with open("notes.txt","w")as f:
    f.write("day 20- file handling\n")
    f.write("Learning read and write.\n")   

# 4) Appending    
with open("notes.txt","a")as f:
    f.write("Append the line.\n")         