from codici_catastali import codicicatastali
from dizionario_carattere_dicontrollo import dicpari, dicdispari, tupresto

# Nome e cognome (primi 6 caratteri)
class StringaDiTesto:
    vocali = ("A", "E", "I", "O", "U")
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
    def check_caratteri(self, is_a_name):
        temp_vocali= []
        temp_consonanti = []
        if is_a_name:
            caratteri = self.name
        else:
            caratteri = self.surname
        for lettera in caratteri:
            print(lettera) #debug
            for vocale in self.vocali:
                if lettera == vocale:
                    #print(f"{lettera} è uguale a {vocale}")debug
                    temp_vocali.append(lettera)
                    break
            else:
                print(f"{lettera} non è uguale a {vocale}")
                temp_consonanti.append(lettera)

        #print(temp_vocali)debug
        #print(temp_consonanti)debug
        if len(temp_consonanti) > 3 and is_a_name:
            temp_consonanti.pop(1)
        temp_surname = temp_consonanti + temp_vocali + ["X","X","X"]
        print(temp_surname)#debug
        stringa1 = temp_surname[0] + temp_surname[1] + temp_surname[2]
        return stringa1

# data di nascita

class DataDiNascita:
    def __init__(self, data, sesso):
        self.gg=""
        self.mm=""
        self.aa=""
        self.data= data
        self.sesso= sesso

    def split_data(self):
#27/10/1996
        self.gg, self.mm, self.aa = self.data.split("/")
        #print(self.data.split("/"))debug
        #print(self.gg + " " + self.mm + " " + self.aa)debug
        self.aa = self.aa[2:]
    def conversione_mese(self):
        mesi = ("A","B","C","D","E","H","L","M","P","R","S","T")
        self.mm = mesi[int(self.mm)-1]
        #print(self.mm)debug
    def conversione_giorno(self):
        if self.sesso == "femmina":
            self.gg = int(self.gg)
            self.gg = self.gg + 40
        #print(self.gg)debug
    def stringa_data(self):
        self.split_data()
        self.conversione_mese()
        self.conversione_giorno()
        self.gg = str(self.gg)
        return self.aa + self.mm + self.gg
class ComuneDiNascita:
    def __init__(self, comune):
        self.comune = comune
    def conversione_catastale(self):
        return codicicatastali.get(self.comune)
class CarattereDiControllo:
    def __init__(self, stringa):
        self.stringa = stringa
    def calcolocarcontr(self):
        contatore = 0
        pari = []
        dispari = []
        for caratteri in stringa:
            contatore += 1
            if contatore % 2 == 0:
                pari.append(caratteri)
            else:
                dispari.append(caratteri)



















    # self.surname.find(self.vocali)


obj= StringaDiTesto("CERIONI", "DOMENICO")#debug
print(f"I primi 3 caratteri del codice fiscale sono {obj.check_caratteri(False)}")#debug
print(f"I secondi 3 caratteri del codice fiscale sono {obj.check_caratteri(True)}")#debug

obj2= DataDiNascita("07/10/1996", "femmina")
print(f'I caratteri della data nel codice fiscale sono {obj2.stringa_data()}')



obj3= ComuneDiNascita("CANTU")
print(f"il tuo comune di nascita corrisponde al seguente codice catastale {obj3.conversione_catastale()}")
stringa = obj.check_caratteri(False) + obj.check_caratteri(True) + obj2.stringa_data() + obj3.conversione_catastale()
print(stringa)




#surname = input("Il tuo cognome? ")
#name = input("il tuo nome? ")
