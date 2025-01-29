import pandas as pd

# impostazioni di visualizzazione
pd.set_option("display.max.columns", None)
pd.set_option("display.max.rows", None)
pd.set_option("display.width", None)

df = pd.read_csv(r"data/raw/world_population.csv")


#filtro 10 paesi più popolati
#print(df[df['Rank'] <= 10])

#riordinare
#print(df[df['Rank'] <= 10].sort_values(by='Rank'))

#ordine discendente
#print(df[df['Rank'] <= 10].sort_values(by='Rank', ascending=False))

#ordine alfabetico
print(df[df['Rank'] <= 10].sort_values(by=['Continent', 'Capital']))


