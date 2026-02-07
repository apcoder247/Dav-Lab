import pandas as pd

data = {
    "Roll": [1,2,3,4,5,6,7,8,9,10],
    "Name": ["A","B","C","D","E","F","G","H","I","J"],
    "Gender": ["M","F","M","F","M","F","M","F","M","F"],
    "Marks1": [45,67,23,89,56,78,34,90,66,40],
    "Marks2": [55,70,35,60,49,80,20,75,68,30],
    "Marks3": [65,72,40,70,60,85,25,88,69,50]
}

df = pd.DataFrame(data)

df["Total"] = df["Marks1"] + df["Marks2"] + df["Marks3"]
df["Average"] = df[["Marks1","Marks2","Marks3"]].mean(axis=1)

print("Student DataFrame:\n", df)

print("\nLowest in Marks1:", df["Marks1"].min())
print("Highest in Marks2:", df["Marks2"].max())
print("Average in Marks3:", df["Marks3"].mean())

print("Student with highest average:", df.loc[df["Average"].idxmax(), "Name"])

print("Number of students failed in Marks2:", (df["Marks2"] < 40).sum())
