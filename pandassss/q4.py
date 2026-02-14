import pandas as pd
import numpy as np

df = pd.read_csv("cereals.csv")

num_df = df.select_dtypes(include=np.number)

print("Five-number summary before cleaning:\n")
print(num_df.describe())

df_missing = num_df.replace(-1, np.nan)
df_missing = df_missing.fillna(df_missing.mean())

Q1 = df_missing.quantile(0.25)
Q3 = df_missing.quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

df_clean = df_missing.copy()

for col in df_clean.columns:
    median_val = df_clean[col].median()
    df_clean.loc[df_clean[col] < lower[col], col] = median_val
    df_clean.loc[df_clean[col] > upper[col], col] = median_val

print("\nFive-number summary after cleaning:\n")
print(df_clean.describe())




"""
Name,Protein,Fat,Sodium,Fiber,Carbo,Vitamins
Corn Flakes,3,1,130,2,15,25
Choco Crunch,2,-1,140,1,14,25
Oats Delight,4,2,180,3,12,25
Honey Rings,-1,1,150,2,13,25
Wheat Bites,3,2,170,-1,11,25
Nutri Mix,2,1,160,2,12,25
Rice Pops,4,2,190,3,10,25
Fiber Plus,3,1,200,2,9,25
Golden Grain,2,1,140,1,13,25
Energy Balls,3,2,180,2,12,-1


"""
