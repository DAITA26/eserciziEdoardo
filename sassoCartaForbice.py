import random
print("Sfida all'ultimo byte contro Mr.Python a sasso carta forbice!!!\n\n")
nome_giocatore = input("inserisci il tuo nome sfidante: ")
risposta_giocatore = input(f"{nome_giocatore} Pronto per la sfida? (si/no): ")

while risposta_giocatore == "si":
    scelta_giocatore = 0
    numero_casuale = random.randint(1, 3)
    print(numero_casuale)
    if numero_casuale == 1:
        print("il tuo avversario ha scelto sasso\n")
    elif numero_casuale == 2:
        print("il tuo avversario ha scelto carta\n")
    else:
        print("il tuo avversario ha scelto forbice\n")

    while not 1 <= scelta_giocatore <= 3:
        scelta_giocatore= input(f"scegli la tua mossa {nome_giocatore} (sasso, carta, forbice): ")
        if scelta_giocatore == "sasso":
            scelta_giocatore = 1
        elif scelta_giocatore == "carta":
            scelta_giocatore = 2
        elif scelta_giocatore == "forbice":
            scelta_giocatore = 3
        else:
            print("Mossa non riconosciuta!")
            scelta_giocatore = 0



    if scelta_giocatore == numero_casuale:
        print(f"{nome_giocatore}, hai pareggiato con Mr. Python!")

    elif (scelta_giocatore == 1 and numero_casuale == 3) or (scelta_giocatore == 2 and numero_casuale == 1) or (scelta_giocatore == 3 and numero_casuale == 2):
        print(f"{nome_giocatore} hai vinto!!")
    else:
        print(f"Mi dispiace {nome_giocatore}, ha vinto Mr. Python!")
    risposta_giocatore = input(f"{nome_giocatore} Vuoi giocare ancora? (si/no): ")
else:
    print(f"{nome_giocatore} grazie di aver partecipato!! ")


















