import numpy as np
import pandas as pd


# a = pd.read_csv("car_type - car_type.csv")
# a

# s = pd.Series(a["Car"])
# print(s)
# s

# s[0] = None

# print(s.size)  # None value ko bhi count karega
# print(s.count())  # None ko count nahi karega


# s.head(10)  # Upar se values dega, by default 5 values
# s.tail(10)  # Niche se values dega, by default 5 values
# s.sample()  # Random data dega, by default 1 value


# s.value_counts()  # Frequencies dega

# s.sort_values()  # Ascending order me values dega
# s.sort_values(ascending=False)  # Descending order me dega

# s.sort_index()

# s.sort_values().head(5)  # Chaining method

# s.count()

# a["Weight"].describe()  # Values ki statistics dega

# a["Weight"].std()  # Standard deviation


# a = pd.read_csv("car_type - car_type.csv")

# a

# s = pd.Series(a["Car"])

# b = a.head()
# c = b["Car"]
# d = a["Model"]

# print(d)

# c[0] = "ram"

# c[[0, 1, 2, 3]] = "SUPRA"
# Fancy indexing - multiple index ki values change karne ke liye

# c


# import pandas as pd

# data1 = pd.DataFrame({
#     "faculty": ["a", "b", "c", "d"],
#     "subject": ["excel", "azure", "mysql", "python"],
#     "marks": [78, 84, 65, 96],
#     "rno": [101, 102, 103, 104]
# })

# print(data1)

# data1.set_index("rno", inplace=True)

# data1


# import numpy as np
# import pandas as pd
# import seaborn as sns


# sns.get_dataset_names()


# dataframe = sns.load_dataset("tips")

# dataframe.isnull()
# Null values ko True aur non-null values ko False karega

# dataframe.isnull().sum()


# dataframe["city"] = np.nan

# dataframe.isnull().sum().sum()


# dataframe.shape[0] * dataframe.shape[1]


# dataframe.isnull().sum().sum() / (
#     dataframe.shape[0] * dataframe.shape[1]
# ) * 100


# dataframe.isnull()

# dataframe.notnull()

# dataframe["city"].hasnans
# Single boolean value return karega


# d = pd.Series([3, 4, 10, 10, 4, 6])

# d

# print(d.unique())  # Unique values return karega

# print(d.nunique())  # Unique values ke numbers dega

# print(len(d))  # Total values ka number return karega

# dir(d)


# d = [1, 3, 4, 5, 6]

# t = tuple(d)

# s = set(t)  # Type conversion

# print(s)
# print(t)
# print(d)


# list1 = [12.3, 2.3, 4.5, 6.7]

# print(type(list1))


# j = pd.Series(list1)

# print(j)

# g = j.astype(int)

# g


# Membership Operator

# list2 = [1, 2, 3, 5]

# st = pd.Series(list2)

# st

# print(5 in st)
# Series me indexing par check karega

# print(5 in st.values)
# Value par check karega

# print(5 in list2)
# List me value se access ho jata hai


# Loop

# list3 = [5, 6, 7, 8, 9, 9]

# data3 = pd.Series(list3)

# print(data3)


# For loop me indexing automatically increase nahi hoti,
# isliye manually index variable use kiya hai

# a = 0

# for i in data3:
#     print(i)
#     i = i + 1
#     data3[a] = i
#     a = a + 1

# print(data3)


# list3 = [5, 6, 7, 8, 9, 9]

# data3 = pd.Series(list3)

# While loop me indexing increment karna zaruri hai

# w = 0

# while w < len(data3):
#     data3[w] = data3[w] + 1
#     w = w + 1

# print(data3)


# list3 = [5, 6, 7, 8, 9, 9]

# data3 = pd.Series(list3)

# data3 = data3 + 200

# print(data3)

# print(data3[data3 > 202])


# data = pd.Series([20, 35, 67, 10])

# print(data.plot(kind="bar"))
# Used to create a chart

# print(data.plot(kind="pie"))