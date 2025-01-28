# import della libreria
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

# visualizzazione di righe, colonne e troncamento
# togliere numero massimo di colonne visualizzate
pd.set_option("display.max.columns", None)
# togliere troncamento della visualizzazione
pd.set_option("display.width", None)

# visualizzare la versione di pandas installata
print("versione pandas " + pd.__version__)

# serie: array monodimensionale che contiene dei dati - lista o tupla
a = [1, 5, 3, 42]
b = ("uno", "cinque", "tre")

df1 = pd.Series(a)
print(df1)
print()

df2 = pd.Series(b)
print(df2)
print()

# visualizza primo elemento della serie
print(df1[0])
print(df2[0])
print()

# cambiare gli indici in etichette
df1 = pd.Series(a, index=["primo", 42, "terzo", "quarto"])
print(df1)
print()

# visualizza elemento della serie usando etichetta
print(f"L'elemento della serie con etichetta 'terzo' è {df1['terzo']}")
print()

# creare una serie a partire da un dizionario
week_days = {
    1 : "lunedì",
    2 : "martedì",
    3 : "mercoledì",
    4 : "giovedì",
    5 : "venerdì",
    6 : "sabato",
    7 : "domenica"
}
df3 = pd.Series(week_days)
print(df3)
print()

df3a = pd.Series(week_days, index=[1, 3, 5])
print(df3a)
print()

# di solito, i dataset in pandas sono array multidimensionali, ovvero DataFrame
# i dataframe sono tabelle con righe e colonne
temperatures = {
    "month" : [1,2,3,4,5,6,7,8,9,10,11,12],
    "name" : ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"],
    "season" : ["Inverno", "Inverno", "Primavera", "Primavera", "Primavera", "Estate", "Estate", "Estate", "Autunno", "Autunno", "Autunno", "Inverno"],
    "temp" : [6.2, 6.8, 10.3, 13.8, 18.4, 22.5, 25.8, 25.2, 21.0, 15.4, 10.1, 5.4]
}

df = pd.DataFrame(temperatures)
print(df)
print()

# visualizza informazioni sul dataframe
print(df.info())
print()

# visualizza informazioni sui dati
print(df.describe())
print()

# visualizza quante righe e colonne
print(df.shape)
print()

# visualizza quantità dati
print(df.size)
print()

# visualizza dati unici
print(df.nunique())
print()

# visualizza nomi delle colonne
print(df.columns.tolist())
print()

# visualizza nomi delle righe
print(df.index.tolist())
print()

# visualizza prima parte del dataframe
print(df.head())
print()

# visualizza l'ultima parte del dataframe
print(df.tail())
print()

# visualizza una riga a caso
print(df.sample())
print()

# visualizza prima riga
print(df.head(1))
print()

# visualizza ultime 2 righe
print(df.tail(2))
print()

# utilizzo di loc
# visualizza la riga di INDICE 0
print(df.loc[0])
print()

# visualizza alcune righe in base a una lista di indici
print(df.loc[[11, 0, 1]])
print()

# visualizza righe in un intervallo
print(df.loc[2 : 7])
print()

# visualizza righe in un intervallo ma solo la colonna name
print(df.loc[2 : 7, "name"])
print()

# visualizza righe in un intervallo solo la colonna name e la colonna temp
print(df.loc[2 : 7, ["name", "temp"]])
print()

print("************** conversione del dataset in matrice **************")
print()

# converto i dati in matrice - lista di liste
temperatures = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"],
    ["Inverno", "Inverno", "Primavera", "Primavera", "Primavera", "Estate", "Estate", "Estate", "Autunno", "Autunno", "Autunno", "Inverno"],
    [6.2, 6.8, 10.3, 13.8, 18.4, 22.5, 25.8, 25.2, 21.0, 15.4, 10.1, 5.4]
]

# togliere numero massimo di colonne visualizzate
pd.set_option("display.max.columns", None)
# togliere troncamento della visualizzazione
pd.set_option("display.width", None)

df = pd.DataFrame(temperatures)
print(df)
print()

df = pd.DataFrame(
    temperatures,
    index = ["mese", "nome", "stagione", "temperatura media"],
    columns = ["gen01","feb02","mar03","apr04", "mag05","giu06","lug07","ago08", "set09","ott10","nov11","dic12"])

print(df)
print()

# iloc funziona come loc ma si basa sull'indice
# visualizza riga di indice 1
print(df.iloc[1])
print()

# visualizza singolo elemento in base all'indice di riga e colonna
print(df.iloc[1, 0])
print()

# modifica di un singolo dato
df.iloc[1, 0] = "pippo"
print(df)
print()

# modifica di un dato in un intervallo di colonne
df.iloc[1, 1 : 3] = "pluto"
print(df)
print()

# modifica di un dato in un intervallo di righe
df.iloc[1 : 3, 11] = None
print(df)
print()

