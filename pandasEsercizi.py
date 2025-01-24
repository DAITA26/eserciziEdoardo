import pandas as pd
# dataframes
matrice = [[1,2,3], [4,5,6], [7,8,9]]
df = pd.DataFrame(matrice)

# visualizzazione dataframe
print(df.head())
print("****************************")
# visualizza info su dataframe
print(df.info())
print("****************************")
# visualizza solo la prima riga
print(df.head(1))
