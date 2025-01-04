vardu_saraksts = {"A":"","Ā":"","B":"","C":"","Č":"","D":"","E":"","Ē":"","F":"","G":"","Ģ":"",
                  "H":"","I":"","Ī":"","J":"","K":"","Ķ":"","L":"","Ļ":"","M":"","N":"","Ņ":"",
                  "O":"","P":"","R":"","S":"","Š":"","T":"","U":"","Ū":"","V":"","Z":"","Ž":""}

# funkcija  kas parbauda vai visas pozicijas vardnica ir aizpilditas
def vai_saraksts_aizpildits(vardu_saraksts):
    vardu_saraksts_aizpildits = True
    for key in vardu_saraksts:
        if vardu_saraksts[key] == "":
            vardu_saraksts_aizpildits = False
    return vardu_saraksts_aizpildits
# funkcija kas nodrosina pareizu vardu ievadi
def varda_ievade():
    vards_ievadits_pareizi = False
    while vards_ievadits_pareizi == False:
        vards = input("Ievadi vardu: ")
        if not vards.isalpha():
            print("Nepareiza ievade! Ievadei ir jabut derigam vardam!")
            vards_ievadits_pareizi = False
        elif not vards[0].isupper():
            print("Nepareiza ievade! Vardam jasakas ar lielo burtu!")
            vards_ievadits_pareizi = False
        elif len(vards.split()) > 1:
            print("Nepareiza ievade! Drikst ievadit tikai 1 vardu!")
            vards_ievadits_pareizi = False
        else:
            vards_ievadits_pareizi = True
            return vards

# izpildam darbibas kamer nav aizpildita visa vardnica
while vai_saraksts_aizpildits(vardu_saraksts) == False:
    vards = varda_ievade()
    varda_pirmais_burts = vards[0]
    if vardu_saraksts[varda_pirmais_burts] == "":
        print("Vards tiek ievietots", list(vardu_saraksts).index(varda_pirmais_burts) + 1, "pozicija!")
        vardu_saraksts[varda_pirmais_burts] = vards
    else:
        print("Vards tiek aizvietots", list(vardu_saraksts).index(varda_pirmais_burts) + 1, "pozicija!")
        vardu_saraksts[varda_pirmais_burts]  = vards