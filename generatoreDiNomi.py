#decidiamo il nome da castello
#imput: segno zodiacale, giorno di nascita, anno di nascita, colore della maglietta che stai indossando

def domanda(richiesta, dizionario):
    inputGiusto = False
    while not inputGiusto:
        risp = input(f"inserisci {richiesta} ").strip().capitalize()
        for indice in dizionario:
            if indice == risp:
                inputGiusto = True


segno = {"Capricorno": "Sir", "Acquario": "Pricipessa", "Pesci" : "Giullare", "Ariete" : "Dragone", "Toro" : "Cavallo",
         "Gemelli" : "Stregone", "Cancro" : "Balia", "Leone" : "Re", "Vergine" : "Fanciulla", "Bilancia" : "Lady",
         "Scorpione" : "Guerriera", "Sagittario" : "Arciere"}

giorno = {"1": "Mario Merlo","2": "Giorgio Vanni","3": "Cristina D'Avena","4": "Hagrid","5": "Ascanio",
          "6": "Lupo Lucio","7" :"Gargamella","8": "Lorenzo","9": "Fedez","10": "Alessandra Amoroso","11": "Tony Effe",
          "12": "Chiara Ferragni","13": "Taylor Mega","14": "Shrek II","15": "Pinocchio",
          "16": "Lupo sessualmente confuso","17": "Rosario Muniz","18": "Dario Moccia","19": "Giuseppe Simone",
          "20": "Peppe Fetish","21": "Diprè","22": "Sandokan","23": "Papa Francesco","24": "Favij","25": "PewdiePie",
          "26": "St3pny","27": "Surry","28": "Il Masseo","29": "Lollo Lacustre",
          "30": "Ciccio Gamer89","31": "Il Cornetto"}

anno = {"2007" : "il fannullone", "2006" : "la baddie", "2005" : "la disonesta", "2004" : "il gerarca",
        "2003" : "il santo", "2002" : "il villano", "2001" : "il fresco di zona", "2000" : "il generale",
        "1999" : "lo scorpione", "1998" : "lo stronzo", "1997" : "l'anti-panico", "1996": "il messia",
        "1995" : "il bomber", "1983" : "la migliore prof del mondo!!!!111!!"}

maglietta = {"Bianco" : "da Biancavilla", "Nero" : "da Predappio", "Rosso" : "da Bologna", "Verde" : "da Catanzaro",
             "Grigio" : "da Londra", "Giallo" : "da Busto Arsizio", "Rosa" : "da Torino",
             "Blu" : "da fuori il Raccordo Anulare", "Viola" : "da Firenze", "Multicolore" : "da Oz",
             "Altro" : "da Altrove"}

print("""Benvenuti nel castello di Lorenzo!! Qui tutti i desideri diventano realtà.
Prego, inserisci i dati seguenti per rivendicare il titolo che ti spetta. 
""")

inputGiusto = False
while not inputGiusto:
    risp1 = input("Inserisci il tuo segno zodiacale: ").strip().capitalize()
    for indice in segno:
        if indice == risp1:
            inputGiusto = True


inputGiusto = False
while not inputGiusto:
    risp2 = input("Inserisci il tuo giorno di nascita (solo il numero): ").strip().capitalize()
    for indice in giorno:
        if indice == risp2:
            inputGiusto = True


inputGiusto = False
while not inputGiusto:
    risp3 = input("In quale anno sei nato/a? ").strip()
    for indice in anno:
        if indice == risp3:
            inputGiusto = True


inputGiusto = False
while not inputGiusto:
    risp4 = input("Scrivi il colore della maglietta che stai indossando: ").strip().capitalize()
    for indice in maglietta:
        if indice == risp4:
            inputGiusto = True

domanda("segno",segno)
domanda("giorno di nascita",giorno)
domanda("anno di nascita", anno)
domanda("colore della maglietta", maglietta)

print(segno[risp1] + " " + giorno[risp2] + " " + anno[risp3] + " " + maglietta[risp4])


































