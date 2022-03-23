# What is Pandas
# Pandas is a Python library used for working with data sets.

# It has functions for analyzing, cleaning, exploring, and manipulating data.

# The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

# Why use Pandas
# Pandas allows us to analyze big data and make conclusions based on statistical theories.

# Pandas can clean messy data sets, and make them readable and relevant.

# Relevant data is very important in data science.

# WHAT CAN PANDAS USED ?
# Pandas gives you answers about the data. Like:

#     Is there a correlation between two or more columns?
#     What is average value?
#     Max value?
#     Min value?

# Pandas are also able to delete rows that are not relevant, or contains wrong values, like empty or NULL values. This is called cleaning the data

# pip install pandas
from dataclasses import dataclass
import os
import pandas as pd

# mydataset = {
#     'cars': ["Maruti", "Audi", "Lexas"],
#     'price': [200000, 10000000, 7500000]
# }

# myvar = pd.DataFrame(mydataset)

# print(myvar)

# print(pd.__version__)

# # WHAT IS A SERIES IN PYTHON
# # A Pandas Series is like a column in a table
# # It is a one dimensional array holding data of any type

# a = [1, "Ron", 3.45]

# mySeries = pd.Series(a)

# print(mySeries)

# # Index in a series
# # If nothing is specified then by default the index is set to be numbers
# #  However we can specify user defined indexes

# mySeries = pd.Series(a, index=["x", "y", "z"])

# print(mySeries)


# # Key-Value Objects as Series

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories)

# print(myvar)

# calories = {"day1": 420, "day2": 380, "day3": 390}

# myvar = pd.Series(calories, index=["day1", "day2"])

# print("******day1*******")
# print(myvar["day1"])
# print("*****************")

# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data)

# print(myvar)


# # WHAT IS A DATAFARME IN PYTHON
# # A pandas dataframe is a 2 dimensional data structure, like a 2 dimensional
# # array, or a table with rows and columns
# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }

# # load data into a DataFrame object:
# df = pd.DataFrame(data)

# print(df)
# print(df.loc[[0, 1]])


# # NAMED INDEX IN A DATAFRAME
# data = {
#     "calories": [420, 380, 390],
#     "duration": [50, 40, 45]
# }

# df = pd.DataFrame(data, index=["day1", "day2", "day3"])

# print(df)

# print(df.loc[["day1", "day2"]])


# data = {
#     "Duration": {
#         "0": 60,
#         "1": 60,
#         "2": 60,
#         "3": 45,
#         "4": 45,
#         "5": 60
#     },
#     "Pulse": {
#         "0": 110,
#         "1": 117,
#         "2": 103,
#         "3": 109,
#         "4": 117,
#         "5": 102
#     },
#     "Maxpulse": {
#         "0": 130,
#         "1": 145,
#         "2": 135,
#         "3": 175,
#         "4": 148,
#         "5": 127
#     },
#     "Calories": {
#         "0": 409,
#         "1": 479,
#         "2": 340,
#         "3": 282,
#         "4": 406,
#         "5": 300
#     }
# }

# df = pd.DataFrame(data)

# print(df)

# print(df.corr())


fileloc1 = '\\Dataset\\DirtyData.csv'

location = os.getcwd() + fileloc1


print(location)
dirtyData = pd.read_csv(location)

print(dirtyData.describe())
print(dirtyData)

# CLEANING DATA
# BAD DATA:
#   Empty cells
#   Data in wrong format
#   Wrong data
#   Duplicates

# newData = dirtyData.dropna()

# print(newData)

# dirtyData.dropna(inplace=True)

print(dirtyData)
print("***************************")
# dirtyData.fillna(130, inplace=True)

# print(dirtyData)
# dirtyData["Calories"].fillna(130, inplace=True)

# print(dirtyData)

print("#######################")
# mean = dirtyData["Calories"].mean()
# median = dirtyData["Calories"].median()
mode = dirtyData["Calories"].mode()[0]
dirtyData["Calories"].fillna(mode, inplace=True)

print(dirtyData)

dirtyData["Date"] = pd.to_datetime(dirtyData["Date"])

print("--------------TIME-----------------")
print(dirtyData)

dirtyData.dropna(subset=["Date"], inplace=True)

print(dirtyData)

# REMOVING DUPLICATES
print(dirtyData.duplicated())

dirtyData.drop_duplicates(inplace=True)

print(dirtyData)
