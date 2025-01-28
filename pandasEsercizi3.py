import pandas as pd

# impostazioni di visualizzazione
# togliere numero massimo di colonne visualizzate
pd.set_option("display.max.columns", None)
# togliere numero massimo di righe visualizzate
pd.set_option("display.max.rows", None)
# togliere troncamento della visualizzazione
pd.set_option("display.width", None)

df = pd.read_table("data/raw/countries_of_the_world.txt")


df = pd.read_csv("data/raw/world_population.csv")


df = pd.read_json("data/raw/json_sample.json")


df = pd.read_excel("data/raw/world_population_excel.xlsx")
print(df)



