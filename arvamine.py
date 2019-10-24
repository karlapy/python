import random

elu = 3

def elud_otsas():
    print("Sul said kõik elud otsa ja kaotasid mängu.")

def raskuaste():
    a = input("Valige raskusaste: kerge/keskmine/raske: ")
    if a == "kerge":
        Kerge()
    elif a == "keskmine":
        Keskmine()
    elif a == "raske":
        Raske()
        

def Kerge():
    global elu
    
    arv = random.randint(1,2)
    
    print("Arvuti mõtleb arvu 1'st 2'ni. ")
    
    if elu == 3:
        print("Mis arvad, millisest arvust arvuti mõtleb?")
        arvamus = int(input())
    if arv < arvamus:
        print("Kahjuks arvasid valesti! Arvuti mõtles numbrist " + str(arv))
        elu -= 1
    elif arv >  arvamus:
        print("Kahjuks arvasid valesti! Arvuti mõtles numbrist " + str(arv))
        elu -= 1
    elif arv == arvamus:
        print("Arvasid ära!")
        elu += 1
    if elu == 0:
        return;

def Keskmine():
    global elu
    
    arv = random.randint(1,4)
    
    print("Arvuti mõtleb arvu 1'st 4'ni. ")
    
    if elu == 3:
        print("Mis arvad, millisest arvust arvuti mõtleb?")
        arvamus = int(input())
    if arv < arvamus:
        print("Kahjuks arvasid valesti! Arvuti mõtles numbrist " + str(arv))
        elu -= 1
    elif arv >  arvamus:
        print("Kahjuks arvasid valesti! Arvuti mõtles numbrist " + str(arv))
        elu -= 1
    elif arv == arvamus:
        print("Arvasid ära!")
        elu += 1
    if elu == 0:
        return;
    
def Raske():
    global elu
    
    arv = random.randint(1,6)
    
    print("Arvuti mõtleb arvu 1'st 6'ni. ")
    
    if elu == 3:
        print("Mis arvad, millisest arvust arvuti mõtleb?")
        arvamus = int(input())
    if arv < arvamus:
        print("Kahjuks arvasid valesti! Arvuti mõtles numbrist " + str(arv))
        elu -= 1
    elif arv >  arvamus:
        print("Kahjuks arvasid valesti! Arvuti mõtles numbrist " + str(arv))
        elu -= 1
    elif arv == arvamus:
        print("Arvasid ära!")
        elu += 1
    if elu == 0:
        return;

raskuaste()
print("Mäng on lõppenud. Sinu tulemus: " + str(elu))

