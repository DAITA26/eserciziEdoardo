import pandas as pd

# impostazioni di visualizzazione
pd.set_option("display.max.columns", None)
pd.set_option("display.max.rows", None)
pd.set_option("display.width", None)

df = pd.read_csv(r'data/raw/flavors.csv')
print(df)
print()

# funzione aggregazione media che funziona solo su num
print(df.groupby(by="Base Flavor").mean(numeric_only= True))
print()

#funzione di aggregazione count
print(df.groupby(by='Base Flavor').count())

#funzione di aggregazione minimo
print(df.groupby(by='Base Flavor').min())

print(df.groupby(by=["Base Flavor","Liked"]).mean(numeric_only= True))

print()

print(df.groupby(by=["Base Flavor","Liked"]).describe())