from pandas import DataFrame
from my_mod import enlarge


print("HELLO")

df = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
print(df.head())

x = 11
print(enlarge(x))
