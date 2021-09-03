import pandas as pd

import sidetable

df = pd.read_csv("crosstab.csv")
#a=pd.crosstab(df['Under 18'], df['18-24 years old'])
p=pd.pivot_table(df, index='province', columns=['gender','age'], aggfunc='sum')

print(p)

