def saluta(testo):
    print(f'Ciao {testo}')

saluta("pippo")

def somma(a, b):
    addizione = a + b
    print(f" il valore della tua addizione è {addizione}")

somma(12,43)

def divisione(a,b):
    div = a / b
    print(f"il valore della tua divisione è {div}")

divisione(4,12)

#funzione lambda

quadrato = lambda x: (x / 2)* 3 - 5
print(quadrato(4))
print(quadrato(5))