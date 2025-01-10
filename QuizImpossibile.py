import random
# Dobbiamo fare 3 o 5 domande, ciascuna con 4 opzioni di risposta, le domande le salviamo in una tupla,
# le opzioni le salviamo in un dizionario
# per ogni domanda la macchina sceglie a caso una risposta giusta e salva la risposta giusta in una lista
# per ogni domanda viene richiesto all'utente di scegliere una risposta e quella risposta viene salvata in una lista
# per ogni domanda facciamo il confronto tra le due risposte comunicando giusto o sbagliato
# alla fine vogliamo il punteggio

def quiz(domanda):
    risposta_giusta = random.randint(0, 3)
    global punteggio
    print(domanda + "\n")
    #print(scelte_pc[risposta_giusta])
    risposta = input("cosa rispondi? ").strip().upper()
    if risposta == scelte_pc[risposta_giusta]:
        print("pazzesco hai indovinato!!")
        punteggio += 1
    else:
        print(f"Hai sbagliato!! la risposta giusta era {scelte_pc[risposta_giusta]}")
    print(f" il tuo punteggio è {punteggio} \n\n")


punteggio = 0

scelte_pc = ("A", "B", "C", "D")

domanda1 = """a quale coloRe Ora Sto penSandO? 
scegli: 
A: Magenta
B: Vinaccia
C: Bordeaux
D: Cremisi
"""

domanda2 = """con quale stagione armocromatica mi riconosco? 
scegli: 
A: Inverno glittarato
B: Primavera lorenzo
C: Estate gayosa
D: Autunno bionico 
"""

domanda3 = """con quale orientamento mi riconosco? 
scegli: 
A: Lorenzo
B: B
C: G
D: Demisessuale 
"""

domanda4 = """Come faccio la pipi? 
scegli: 
A: Cecchino
B: Spiderman
C: Il pensatore
D: Lorenzo 
"""


quiz(domanda1)

quiz(domanda2)

quiz(domanda3)

quiz(domanda4)

























