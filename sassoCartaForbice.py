import random
numero_casuale = random.randint(1, 3)

if numero_casuale == 1:
    print("il tuo avversario ha scelto sasso\n")
elif numero_casuale == 2:
    print("il tuo avversario ha scelto carta\n")
else:
    print("il tuo avversario ha scelto forbice\n")

print("Sfida all'ultimo byte contro Mr.Python a sasso carta forbice!!!\n\n")

nome_giocatore = input("inserisci nome giocatore: ")

scelta_giocatore= input(f"scegli la tua mossa {nome_giocatore} (sasso, carta, forbice): ")

if scelta_giocatore == "sasso":
    scelta_giocatore = 1
elif scelta_giocatore == "carta":
    scelta_giocatore = 2
elif scelta_giocatore == "forbice":
    scelta_giocatore = 3


if scelta_giocatore == numero_casuale:
    print("Bin bum ba le... giu!!!")
    print(f"{nome_giocatore} hai pareggiato con MrPython")
elif scelta_giocatore != numero_casuale:
    print("Bin bum ba le... giu!!!")
    if [scelta_giocatore == 2 and numero_casuale == 1] or [scelta_giocatore == 3 and numero_casuale == 2] or[scelta_giocatore == 1 and numero_casuale == 3]:
        print(f"{nome_giocatore} hai vinto!!")
    else:
        print(f"Mi dispiace {nome_giocatore} ha vinto MrPython")











"""while numero_casuale == scelta_giocatore:
    print(f"{nome_giocatore} la partita è patta riprova")
else:
    print(f"forza {nome_giocatore} la partita comincia a farsi interessante")"""
