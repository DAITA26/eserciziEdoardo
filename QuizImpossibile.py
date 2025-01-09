import random
# Dobbiamo fare 3 o 5 domande, ciascuna con 4 opzioni di risposta, le domande le salviamo in una tupla,
# le opzioni le salviamo in un dizionario
# per ogni domanda la macchina sceglie a caso una risposta giusta e salva la risposta giusta in una lista
# per ogni domanda viene richiesto all'utente di scegliere una risposta e quella risposta viene salvata in una lista
# per ogni domanda facciamo il confronto tra le due risposte comunicando giusto o sbagliato
# alla fine vogliamo il punteggio


print("""a quale coloRe Ora Sto penSandO? 
scegli un colore: 
A: Magenta
B: Vinaccia
C: Bordeaux
D: Cremisi""")

risposta = input("cosa rispondi? ").strip().upper()
risposta_giusta = random.randint(0,3)

scelte_pc = ("A", "B", "C", "D")
#scelta C bordeaux
print(scelte_pc[risposta_giusta])


if risposta == scelte_pc[risposta_giusta]:
    print("pazzesco hai indovinato!!")
else:
    print(f"Hai sbagliato!! la risposta giusta era {scelte_pc[risposta_giusta]}")



