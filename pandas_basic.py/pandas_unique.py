import pandas as pd

data = {
    "Name": ["Tejas", "Rahul", "Anu", "Kiran", "Tejas"],
    "Course": ["Python", "Java", "Python", "Java", "Python"]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nUnique Courses:")
print(df["Course"].unique())

print("\nNumber of Unique Courses:")
print(df["Course"].nunique())