print("Hello Niketa")

#variable
product = "Milk"
sales = 500
print(product,sales)

#list
product=["Milk","Bread","Soap"]
print(product)

#loop
for item in product:
    print(item)

 
import pandas as pd

# create data
data = {
    "Product": ["Milk", "Bread", "Soap"],
    "City": ["Delhi", "Noida", "Delhi"],
    "Sales": [500, 500, 500]
}

df = pd.DataFrame(data)

print(df) 

# total sales
print(df["Sales"].sum())

# sales by city
print(df.groupby("City")["Sales"].sum())


import csv

#Read Entire CSV:
import pandas as pd

df = pd.read_csv("D:\\30 days python course\\sales_data.csv")

# max sales
print(df["Sales"].max())

# total sales
print(df["Sales"].sum())

# sales by city
print(df.groupby("City")["Sales"].sum())

# sales by product
print(df.groupby("Product")["Sales"].sum())

# sorting of data
print(df.sort_values(by="Sales", ascending=False))

#check data information
print(df.info())

#Check missing values
print(df.isnull().sum())

#Remove missing value
df = df.dropna()

import pandas as pd

# load data
df = pd.read_csv("D:\\30 days python course\\sales_data.csv")

# basic info
print("Dataset:\n", df)

# total sales
total_sales = df["Sales"].sum()
print("\nTotal Sales:", total_sales)

# sales by city
sales_by_city = df.groupby("City")["Sales"].sum()
print("\nSales by City:\n", sales_by_city)

# sales by product
sales_by_product = df.groupby("Product")["Sales"].sum()
print("\nSales by Product:\n", sales_by_product)

# top product
top_product = sales_by_product.idxmax()
print("\nTop Product:", top_product)

# top city
top_city = sales_by_city.idxmax()
print("\nTop City:", top_city)

# Delhi has highest sales
# Milk is the top product
# total sales = 1400

# save results
df.to_csv("cleaned_sales_data.csv", index=False)        


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\\30 days python course\\sales_data.csv")

#Sales by city (Bar Chart)
df.groupby("City")["Sales"].sum().plot(kind="bar")
plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")
plt.show()

#Sales by product
df.groupby("Product")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Product")
plt.show()

# Line chat (Trend)
df["Sales"].plot(kind="line")
plt.title("Sales Trend")
plt.show()

plt.show()

#sales by city (better version)

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("D:\\30 days python course\\sales_data.csv")

sales_city = df.groupby("City")["Sales"].sum()

sales_city.plot(kind="bar")

plt.title("Sales by City", fontsize=14)
plt.xlabel("City")
plt.ylabel("Total Sales")
plt.xticks(rotation=0)

plt.show()

# Add colors
sales_city.plot(kind="bar", color=["blue", "green"])

# Add values on bars
ax = sales_city.plot(kind="bar")

for i in ax.patches:
    ax.text(i.get_x() + 0.1, i.get_height() + 10, str(i.get_height()))

plt.show()

# pie chart
sales_city.plot(kind="pie", autopct='%1.1f%%')

plt.title("Sales Distribution by City")
plt.ylabel("")

plt.show()

#better layout (fixing spaces)
plt.tight_layout()

#DATA FROM SQL
import pandas as pd

df = pd.read_csv("D:\\30 days python course\\sales_data.csv")

print("Total Sales:", df["Sales"].sum())

print("\nSales by City:\n", df.groupby("City")["Sales"].sum())

print("\nSales by Product:\n", df.groupby("Product")["Sales"].sum())

#VISUALIZATION
import matplotlib.pyplot as plt

df.groupby("City")["Sales"].sum().plot(kind="bar")
plt.title("Sales by City")
plt.show()