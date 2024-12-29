import random
numero_casuale = random.randint(1, 3)
print(numero_casuale)

if numero_casuale == 1:
    print("il tuo avversario ha scelto sasso\n")
elif numero_casuale == 2:
    print("il tuo avversario ha scelto carta\n")
else:
    print("il tuo avversario ha scelto forbice\n")

print("Sfida all'ultimo byte contro Mr.Python a sasso carta forbice!!!\n\n")

nome_giocatore = input("inserisci nome giocatore: ")
scelta_giocatore= input(f"scegli la tua mossa {nome_giocatore} (sasso, carta, forbice): ")

while scelta_giocatore != "sasso" and scelta_giocatore != "carta" and scelta_giocatore != "forbice":
    print("Mossa non riconosciuta!")
    scelta_giocatore = input(f"Scegli una mossa valida {nome_giocatore} (sasso, carta, forbice): ")

if scelta_giocatore == "sasso":
    scelta_giocatore = 1
elif scelta_giocatore == "carta":
    scelta_giocatore = 2
elif scelta_giocatore == "forbice":
    scelta_giocatore = 3

while scelta_giocatore == numero_casuale:
    print(f"{nome_giocatore}, hai pareggiato con Mr. Python!")
    numero_casuale = random.randint(1, 3)
    print(numero_casuale)
    scelta_giocatore = input(f'{nome_giocatore} scegli una nuova mossa: ')
#Se avviene nuovamente un pareggio il gioco non da l'input giusto da rivedere!!!

if (scelta_giocatore == 1 and numero_casuale == 3) or (scelta_giocatore == 2 and numero_casuale == 1) or (scelta_giocatore == 3 and numero_casuale == 2):
    print(f"{nome_giocatore} hai vinto!!")

else:
    print(f"Mi dispiace {nome_giocatore}, ha vinto Mr. Python!")


#Come faccio a farlo andare in loop?

"""risposta_giocatore = input(f"{nome_giocatore} Vuoi rigiocare? (si/no): ")

if risposta_giocatore == "si":
    numero_casuale = random.randint(1, 3)
    print(numero_casuale)
    scelta_giocatore = input(f'{nome_giocatore} scegli una nuova mossa: ')
else:
    print("Grazie di aver giocato!")"""
















"""while numero_casuale == scelta_giocatore:
    print(f"{nome_giocatore} la partita è patta riprova")
else:
    print(f"forza {nome_giocatore} la partita comincia a farsi interessante")"""
