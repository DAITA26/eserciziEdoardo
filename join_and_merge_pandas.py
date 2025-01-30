import pandas as pd

# impostazioni di visualizzazione
pd.set_option("display.max.columns", None)
pd.set_option("display.max.rows", None)
pd.set_option("display.width", None)

df1 = pd.read_csv(r'data/raw/LOTR.csv')
print(df1)
print()
df2 = pd.read_csv(r'data/raw/LOTR 2.csv')
print(df2)
print()

#print(df1.merge(df2))

print(df1.merge(df2, how="outer"))
print()

#print(df1.merge(df2, how="left"))
print()
#print(df2.merge(df1, how="left")) #come fosse un how = "right", si usa cosi

df1 = df1.set_index("FellowshipID")
df2 = df2.set_index("FellowshipID")

df3 = df1.join(df2, how= "outer", lsuffix="_primo", rsuffix="_secondo")

print(df3)


