class Employee:
    def __init__(self, name, h_pay):
        #tredicesima = 80 % di uno stipendio mensile
        self.name = name
        self.h_pay = h_pay

    def calc_wage(self):
        tredicesima = self.h_pay * 8 * 20 * 0.8
        print(f"RAL di {self.name}")
        ral = self.h_pay * 8 * 20 * 12 + tredicesima
        return ral

    def say_hello(self):
        print(F"Ciao sono {self.name} e prendo {self.h_pay} euro all'ora")


class Manager(Employee):
    perc_yearly_bonus = 20
    def __init__(self, name, h_pay, division):
        #scaricabarile
        super().__init__(name, h_pay)
        self.division = division

    def calc_wage(self):
        ral = super().calc_wage()
        bonus = ral * self.perc_yearly_bonus / 100
        return ral + bonus

class Clerk(Employee):
    def __init__(self, name, h_pay, boss):
        #scaricabarile
        super().__init__(name, h_pay)
        self.boss = boss

class Intern(Clerk):
    forfait = 500
    def __init__(self, name, boss):
        super().__init__(name, 0, boss)
    #override del metodo calc_wage()
    def calc_wage(self):
        print(f"{self.name} prende {self.forfait} euro al mese ")
        ral = self.forfait * 12
        return ral

obj1 = Manager("Elon Musk", 50, "Mondo")
obj2 = Clerk("Pippo", 35, obj1)
obj3 = Intern("Povero Topino", obj1)
obj1.say_hello()
obj2.say_hello()
obj3.say_hello()
print(obj1.calc_wage())
print(obj2.calc_wage())
print(obj3.calc_wage())