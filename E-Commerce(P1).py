import pandas as pd

df = pd.read_csv(r"C:\Users\Dell\OneDrive\New folder\AIML(all basics)\Ecommerce Purchases.csv")
print(df)

#Display top 10 rows of Dataset
print(df.head(10))

#Display last 10 rows of Dataset
print(df.tail(10))

#Check datatype of each column
print(df.dtypes)

#Check null values in the Dataset
print(df.isnull())

#How many rows and cols are there in our dataset
print(df.info())

#Highest and Lowest purchase prices
print(df["Purchase Price"].max())
print(df["Purchase Price"].min())

#Average Purchase Price
print(df["Purchase Price"].mean())

#How many people have French "fr" as their language
print(df[df["Language"] == "fr"])

#Job title contains Engineer
print (df[df["Job"].str.contains("engineer" , case=False)])

#Find email of the person with the following IP address 132.207.160.22
print(df[df["IP Address"] == "132.207.160.22"])

#How many people have a mastercard as their credit card provider and made a purchase above 50
print(df[(df["CC Provider"] == "Mastercard" )] & (df["Purchase Price"] >50))



