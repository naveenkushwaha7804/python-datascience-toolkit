import numpy as np
import pandas as pd

#         Attributes

A1=[78,56,98,78,56,87,55]
A2=["A","B","C","D","E","F","G"]
Result=pd.Series(A1,index=A2,name="Results")
print(Result)
print(Result.index)#only indexes
print(Result.values)#only values
print(Result.is_unique)# values unique hai ya nahi
print(Result.name)# Series ka name
print(Result.size)# Number of Values
print(Result.dtype)# Data type ke liye