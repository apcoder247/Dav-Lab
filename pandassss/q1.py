import pandas as pd

print("Enter the daily temperatures in °C over a week:")

days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
temp = []

for d in days:
    t = int(input(f"Enter temperature for {d}: "))
    temp.append(t)

temp_series = pd.Series(temp, index=days)

print("\nTemperature Series:\n", temp_series)

mean_temp = temp_series.mean()
max_temp = temp_series.max()
min_temp = temp_series.min()

print("\nMean temperature:", mean_temp)
print("Maximum temperature:", max_temp, "on", temp_series.idxmax())
print("Minimum temperature:", min_temp, "on", temp_series.idxmin())

value = int(input("\nEnter a value to filter temperatures greater than it: "))
high_temps = temp_series[temp_series > value]
print(f"\nTemperatures greater than {value}:\n{high_temps}")

fah_series = (temp_series * 9/5) + 32
print("\nTemperatures in Fahrenheit:\n", fah_series)

days_above_avg = temp_series[temp_series > mean_temp].index.tolist()
print("\nDays having temperature greater than average:", days_above_avg)
