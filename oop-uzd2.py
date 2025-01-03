class kubs:
    # metode kas inicialize objektu - konstruktors
    def __init__(self, garums, krasa):
        if garums in range(2, 11):
            self.garums = garums
        else:
            print("Malas garums neatbilst nosacijumiem!")
            self.garums = 2
        self.krasa = krasa

    # metode kas aprekina kuba tilpumu
    def aprekinat_tilpumu(self):
        tilpums = self.garums ** 3
        return tilpums 
    
    # metode pretstats inicializejosanas objektam, tiek izsaukta kad programma beidzas un iznicinas, nodzes objektu
    def __del__(self):
        print(f"Objekts ir likvidets! Ta krasa bija {self.krasa}")

class bloks(kubs):
    def __init__(self, garums, krasa, kubu_skaits, forma):
        super().__init__(garums, krasa)
        if kubu_skaits >= 1 and kubu_skaits <= 4:
            self.__kubu_skaits = kubu_skaits
        else:
            print("Nepareiza kubu skaita vertiba!")
            self.__kubu_skaits = 1
        self.nosaukums = str(self.krasa) + str(self.__kubu_skaits)
        iespejamas_vertibas = [11, 12, 13, 14, 22]
        if forma not in iespejamas_vertibas:
            print("Forma neatbilst nosacijumiem!")
            self.derigums = 0
        else:
            self.derigums = 1

    def tilpums(self):
        kuba_tilpums = self.garums ** 3
        bloka_tilpums = kuba_tilpums * self.__kubu_skaits
        return bloka_tilpums

    def mainit_formu(self, jauna_forma):
        iespejamas_vertibas = [11, 12, 13, 14, 22]
        if jauna_forma not in iespejamas_vertibas:
            print("Forma neatbilst nosacijumiem!")
            self.derigums = 0
        else:
            self.derigums = 1


# objekti bloks

orange3 = bloks(5, "oranza", 3, 13)
print(orange3.nosaukums, orange3.tilpums())
blue5 = bloks(7, "zila", 5, 23)
print(blue5.nosaukums, blue5.derigums)
blue5.mainit_formu(12)
print(blue5.nosaukums, blue5.derigums)


# objekti kubs
kubg = kubs(10, "zala")
kubr = kubs(1, "sarkana")
print(kubg.krasa, kubg.aprekinat_tilpumu())
print(kubr.garums)
# objekta kubr dzesana
del kubr
# parbauda vai kubr eksiste
try:
    print(kubr.garums)
except:
    print("Objekts neeksiste!")
print(kubg.garums)
