import sys
import pandas as pd



months = {
    1 : "Jan", 2: "Feb", 3: "March", 4 : "April", 
    5: "may", 6: "June", 7: "July", 8: "Aug",
    9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}

month = int(sys.argv[1])

df = pd.DataFrame({"Day": [1, 2], "num_passengers": [3, 4]})
df['month'] = months[month]
print(df.head())

df.to_parquet(f"output_{month}.parquet")

if month in months : 
    print(f'Hello pipeline,  month = {months[month]} ')