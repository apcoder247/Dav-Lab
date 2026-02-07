import pandas as pd
import numpy as np

df = pd.read_csv("cereals.csv")

num_df = df.select_dtypes(include=np.number)

print(num_df.describe())

df_mean = num_df.replace(-1, np.nan)
df_mean = df_mean.fillna(df_mean.mean())

print(df_mean.describe())

df_median = num_df.replace(-1, np.nan)
df_median = df_median.fillna(df_median.median())

print(df_median.describe())



"""
Name,Protein,Fat,Sodium,Fiber,Carbo,Vitamins
C1,3,1,130,2,15,25
C2,2,-1,140,1,14,25
C3,4,2,180,3,12,25
C4,-1,1,150,2,13,25
C5,3,2,170,-1,11,25
C6,2,1,160,2,12,25
C7,4,2,190,3,10,25
C8,3,1,200,2,9,25
C9,2,1,140,1,13,25
C10,3,2,180,2,12,-1

"""