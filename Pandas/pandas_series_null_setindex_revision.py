import pandas as pd
import numpy as np
import seaborn as sns

# ==================== Part 1: Series methods on CSV column ====================
A = pd.read_csv('car_type - car_type.csv')
print(A)

s = pd.Series(A["Car"])
print(s)

print(s.head())       # by default top 5 data dega, nahi to instruction v de sakte hai
print(s.head(10))

print(s.tail())        # by default lower 5 data dega, nahi to instruction v de sakte hai
print(s.tail(10))

print(s.sample())      # by default random 1 data dega, nahi to instruction v de sakte hai
print(s.sample(10))

print(s.value_counts())    # frequency batayega

print(s.sort_values())               # ascending sort kar dega data ko
print(s.sort_values(ascending=False))  # descending sort kar dega data ko
print(s.sort_index())                # index number of data will be arranged in ascending

s[0] = None    # value assign karne ke liye
print(s)

print(s.count())
print(s.size)

# ---- Nesting ----
print(s.sort_values().head(5))
print(s.sort_values().head(5).values)   # sirf values dega

# ---- Numerical data pr operation perform karega ----
print(A.describe())
print(A['Weight'].describe())

Collection = A.head()
print(Collection)

D = Collection["Car"]
print(D)

# ---- Fancy Indexing ----
D[[0, 1, 2]] = 'nav'
print(D)


# ==================== Part 2: Null value handling (seaborn tips) ====================
df = sns.load_dataset('tips')
print(df)

# Null value hai ya nahi dekhne ke liye
print(df.isnull().sum())

# true ko false or false ko true, yahi difference hai
print(df.notnull())

# Column add karne ke liye
df['city'] = np.nan

# Total number of Null values
print(df.isnull().sum().sum())

# percentage nikalne ke liye
print(df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100)

# hasnans sirf series pe work karega or yah batayega null value hai ya nahi
print(df["city"].hasnans)

N = pd.Series([12, 23, 45, 12, 34])
# bas unique values return karega
print(N.unique())
# number of unique values kitni hai ye batayega
print(N.nunique())


# ==================== Part 3: set_index practice ====================
Data1 = pd.DataFrame({
    "Roll No": [101, 102, 103, 104, 105],
    "Name": ["Naveen", "Rahul", "Aman", "Priya", "Sneha"],
    "Subject": ["Math", "Science", "English", "Math", "Science"],
    "Marks": [85, 90, 78, 88, 92]
})
print(Data1)

Data1.set_index("Roll No", inplace=True)   # inplace for changing data in original dataframe
print(Data1)

Data1.reset_index(inplace=True)   # Roll No wapas column bana do, taaki Name ko index bana sakein
Data1.set_index('Name', inplace=True)
print(Data1)