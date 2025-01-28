import pandas as pd
print(pd.__version__)

# serie: array che contengono dati
a = [1, 5, 3, 42]
b = ["uno", "cinque", "tre"]

df1 = pd.Series(a)
print(df1)

df2 = pd.Series(b)
print(df2)

#cambiare indici etichette
df1 = pd.Series(a, index=["primo", "secondo", "terzo", "quarto"])
print(df1)

print(f"L'elemento della serie con etichetta terzo è {df1['terzo']}")

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

df3a = pd.Series(week_days, index= [1, 3, 5])
print(df3a)

temperatures = {
    "month" : [1,2,3,4,5,6,7,8,9,10,11,12],
    "name" : ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"],
    "season" : ["Inverno", "Inverno", "Primavera", "Primavera", "Primavera", "Estate", "Estate", "Estate", "Autunno", "Autunno", "Autunno", "Inverno"],
    "temp" : [6.2, 6.8, 10.3, 13.8, 18.4, 22.5, 25.8, 25.2, 21.0, 15.4, 10.1, 5.4]
}

df = pd.DataFrame(temperatures)
print(df)

print(df.info())
print()


print(df.describe())




