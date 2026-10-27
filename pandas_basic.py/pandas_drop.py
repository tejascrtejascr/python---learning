import pandas as pd

data = {
    "Name": ["Tejas", "Rahul", "Anu"],
    "Age": [20, 21, 19],
    "Marks": [85, 75, 90]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Remove the Age column
df = df.drop(columns=["Age"])

print("\nAfter Removing Age Column:")
print(df)

# Remove the first row
df = df.drop(index=0)

print("\nAfter Removing First Row:")
print(df)
