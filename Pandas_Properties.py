import pandas as pd
import numpy as np


print("=" * 50)
print("SERIES PROGRAMS")
print("=" * 50)


print("\n1. Creating a Series")
s = pd.Series([10, 20, 30, 40, 50])
print(s)


print("\n2. Series to List Conversion")
s2 = pd.Series([1, 2, 3, 4, 5])
converted = s2.tolist()
print(converted)
print(type(converted))


print("\n3. Series Arithmetic")
s3 = pd.Series([10, 20, 30, 40, 50])
s4 = pd.Series([2, 4, 6, 8, 10])
print("Addition:")
print(s3 + s4)
print("Subtraction:")
print(s3 - s4)
print("Multiplication:")
print(s3 * s4)
print("Division:")
print(s3 / s4)


print("\n4. Series Comparison")
s5 = pd.Series([1, 2, 3, 4, 5])
s6 = pd.Series([5, 4, 3, 2, 1])
print("Equal:")
print(s5 == s6)
print("Greater than:")
print(s5 > s6)
print("Less than:")
print(s5 < s6)


print("\n5. Dict to Series")
d = {"a": 100, "b": 200, "c": 300, "d": 400}
s7 = pd.Series(d)
print(s7)


print("\n6. Array to Series")
arr = np.array([10, 20, 30, 40, 50])
s8 = pd.Series(arr)
print(s8)


print("\n7. Change Series DataType")
s9 = pd.Series([1, 2, 3, 4, 5])
print("Original dtype:", s9.dtype)
s9 = s9.astype(float)
print("After converting to float:")
print(s9)
print("New dtype:", s9.dtype)


print("\n8. DF Column to Series")
df1 = pd.DataFrame({"Col1": [1, 2, 3], "Col2": [4, 5, 6], "Col3": [7, 8, 9]})
first_col = df1.iloc[:, 0]
print(first_col)
print(type(first_col))


print("\n9. Series to Array")
s10 = pd.Series([10, 20, 30, 40, 50])
arr2 = s10.to_numpy()
print(arr2)
print(type(arr2))


print("\n10. Flatten Series of Lists")
s11 = pd.Series([[1, 2], [3, 4], [5, 6, 7]])
flat = s11.explode()
print(flat.reset_index(drop=True))


print("\n11. Sort Series")
s12 = pd.Series([3, 1, 4, 1, 5, 9, 2, 6])
print("Ascending:")
print(s12.sort_values())
print("Descending:")
print(s12.sort_values(ascending=False))


print("\n12. Append Data to Series")
s13 = pd.Series([1, 2, 3])
new_data = pd.Series([4, 5, 6])
s13 = pd.concat([s13, new_data]).reset_index(drop=True)
print(s13)


print("\n13. Subset Series")
s14 = pd.Series([10, 20, 30, 40, 50, 60, 70])
subset = s14[s14 > 30]
print(subset)


print("\n14. Reorder Series Index")
s15 = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])
reordered = s15.reindex(["e", "c", "a", "b", "d"])
print(reordered)


print("\n15. Series Stats")
s16 = pd.Series([10, 20, 30, 40, 50])
print("Mean:", s16.mean())
print("Standard Deviation:", s16.std())


print("\n16. Series Difference")
s17 = pd.Series([1, 2, 3, 4, 5])
s18 = pd.Series([3, 4, 5, 6, 7])
diff = s17[~s17.isin(s18)]
print(diff)


print("\n17. Non-common Series Items")
s19 = pd.Series([1, 2, 3, 4, 5])
s20 = pd.Series([3, 4, 5, 6, 7])
non_common = pd.concat([s19[~s19.isin(s20)], s20[~s20.isin(s19)]])
print(non_common)


print("\n18. Five-Number Summary")
s21 = pd.Series([10, 20, 30, 40, 50, 60, 70, 80])
print("Minimum:", s21.min())
print("25th Percentile:", s21.quantile(0.25))
print("Median:", s21.median())
print("75th Percentile:", s21.quantile(0.75))
print("Maximum:", s21.max())


print("\n" + "=" * 50)
print("DATAFRAME PROGRAMS")
print("=" * 50)


print("\n1. Creating a DataFrame from a Dictionary")
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35], "City": ["Lahore", "Karachi", "Islamabad"]}
df = pd.DataFrame(data)
print(df)


print("\n2. DataFrame with Specified Index Labels")
data2 = {"Name": ["Alice", "Bob", "Charlie"], "Age": [25, 30, 35]}
df2 = pd.DataFrame(data2, index=["s1", "s2", "s3"])
print(df2)


print("\n3. DataFrame Basic Summary Information")
df3 = pd.DataFrame({"A": [1, 2, 3], "B": [4.0, 5.0, 6.0], "C": ["x", "y", "z"]})
print(df3.info())
print(df3.describe())


print("\n4. Selecting First 3 Rows")
df4 = pd.DataFrame({"A": range(1, 11), "B": range(11, 21)})
print(df4.head(3))


print("\n1. Display Default and Set Column as Index")
df5 = pd.DataFrame({"Name": ["Ali", "Sara", "Hamza"], "Score": [85, 90, 78]})
print("Default Index:")
print(df5)
df5 = df5.set_index("Name")
print("\nAfter Setting Name as Index:")
print(df5)


print("\n2. Create MultiIndex Frame")
arrays = [["Math", "Math", "Science", "Science"], ["Midterm", "Final", "Midterm", "Final"]]
index = pd.MultiIndex.from_arrays(arrays, names=["Subject", "Exam"])
df6 = pd.DataFrame({"Score": [80, 90, 70, 85]}, index=index)
print(df6)


print("\n3. Reset Index After Setting Column as Index")
df7 = pd.DataFrame({"Name": ["Ali", "Sara"], "Marks": [80, 90]})
df7 = df7.set_index("Name")
print("With Name as Index:")
print(df7)
df7 = df7.reset_index()
print("\nAfter Reset:")
print(df7)


print("\n4. Create 64-bit Integer and Float Index Labels")
df8 = pd.DataFrame({"Values": [10, 20, 30]}, index=pd.Index([1, 2, 3], dtype="int64"))
print("Int64 Index:")
print(df8)

df9 = pd.DataFrame({"Values": [10, 20, 30]}, index=pd.Index([1.0, 2.0, 3.0], dtype="float64"))
print("\nFloat64 Index:")
print(df9)


print("\n1. Select Rows Based on Column A Value")
df10 = pd.DataFrame({"A": [2, 5, 3, 7, 1, 4, 6], "B": [10, 20, 30, 40, 50, 60, 70]})
print(df10[df10["A"] > 4])


print("\n2. Select Specific Columns X and Y")
df11 = pd.DataFrame({"X": [1, 2, 3], "Y": [4, 5, 6], "Z": [7, 8, 9]})
print(df11[["X", "Y"]])


print("\n3. Set MultiIndex and Access Data")
df12 = pd.DataFrame(
    {"Score": [88, 92, 75, 85]},
    index=pd.MultiIndex.from_tuples(
        [("Ali", "Math"), ("Ali", "Science"), ("Sara", "Math"), ("Sara", "Science")],
        names=["Student", "Subject"]
    )
)
print(df12)
print("\nAccessing Ali's data:")
print(df12.loc["Ali"])


print("\n4. Slice DataFrame Based on MultiIndex Levels")
print(df12.loc[("Ali", "Math"):("Ali", "Science")])


print("\n5. Swap Levels of a MultiIndex DataFrame")
df13 = df12.swaplevel("Student", "Subject")
print(df13)


print("\n6. Reset Index of a MultiIndex DataFrame")
df14 = df12.reset_index()
print(df14)
