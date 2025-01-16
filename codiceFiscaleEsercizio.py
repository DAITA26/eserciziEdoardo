
# Nome e cognome (primi 6 caratteri)
class StringaDiTesto:
    vocali = ("A", "E", "I", "O", "U")
    def __init__(self, surname, name):
        self.surname = surname
        self.name = name
    def check_surname(self):
        temp_vocali= []
        temp_consonanti = []
        for lettera in self.surname:
            print(lettera)
            for vocale in self.vocali:
                if lettera == vocale:
                    print(f"{lettera} è uguale a {vocale}")
                    temp_vocali.append(lettera)
                    break
            else:
                print(f"{lettera} non è uguale a {vocale}")
                temp_consonanti.append(lettera)

        print(temp_vocali)
        print(temp_consonanti)
        temp_surname = temp_consonanti + temp_vocali + ["X","X","X"]
        print(temp_surname)
        stringa1 = temp_surname[0] + temp_surname[1] + temp_surname[2]
        return stringa1







        #cf_surname = ""
        #for x in self.vocali:
            #carattere= self.surname
            #if carattere != self.vocali[x]:
                #cf_surname = cf_surname + carattere



#self.surname.find(self.vocali)


obj= StringaDiTesto("IANIRO", "MARIO")
print(f"Il codice fiscale fino ad ora è {obj.check_surname()}")






#surname = input("Il tuo cognome? ")
#name = input("il tuo nome? ")
