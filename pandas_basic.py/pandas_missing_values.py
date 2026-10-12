import pandas as pd

data = {
    "Name": ["Tejas", "Rahul", "Anu", "Kiran"],
    "Marks": [85, None, 90, None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull())

df["Marks"] = df["Marks"].fillna(0)

print("\nAfter Replacing Missing Values:")
print(df)