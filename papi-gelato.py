opnieuw='y'
bakjestellen='.'
toppingeidelijk=0
aantalhorentjes=0
aantalbakjes=0
aantaleindelijk=0
print("Welkom bij Papi Gelato")

def partOfZakelijk():
    persoon = (input("Bent u A) particulier of B) zakelijk? : ")).lower
    if persoon == "A":
        vraagbolljes()
    elif persoon == "B":
        zakelijk()
    else:
        print("je vult een fout getal in probeer het opnieuw")

def zakelijk():
    aantalLiter = int(input("hoeveel liter wil je? : "))
    if     aantalLiter >= 0: 
            print ("de prijs is dan", (aantalLiter), "x", (prijsPlter), "en dat is", (aantalLiter * prijsPliter )) 
    smaakLiter()

def smaakLiter():
    for z in range(aantalLiter):
            smaakkeuze = smaakLiter('Welke smaak wilt u voor Liter '+ str(Nliter) + ' A) Aardbei, C) Chocolade, of V) Vanille?: ')
            Nliter = Nliter - 1
            allesmaken = allesmaken + " " + smaakkeuze

def vraagbolljes():
    while True:
        aantal = int(input("Hoeveel bolletjes wilt u? : ", ))
        if aantal <= 3:
            return aantal
        elif aantal <= 7:
            print(f'Dan krijgt u van mij een bakje met {aantal} bolletjes')
            return aantal
        elif aantal > 8:
            print("Sorry, zulke grote bakken hebben we niet")
        else:
            print("Sorry, dat is niet mogelijk....")
def smaakkiezen():
    Nbolletje = 1
    while Nbolletje <= int(aantal):
        smaak = input(f'Welke smaak wilt u voor bolletje nummer {Nbolletje}? A) Aardbei, C) Chocolade, M) Munt of V) Vanille? : ').lower()
        if smaak=='a' or smaak=='c' or smaak=='m' or smaak=='v':
            Nbolletje+=1
        else:
            print('Sorry, dat is niet mogelijk....')
def bakjeofhoorntje():
    while True and aantal <= 3:
        bakje = input(f'Wilt u deze {aantal} bolletje(s) in A) een hoorntje of B) een bakje? : ').lower()
        if bakje=='a':
            global aantalhorentjes
            bakje = 'Hoorntje'
            aantalhorentjes+=1
            return bakje
        elif bakje=='b':
            global aantalbakjes
            bakje = 'Bakje'
            aantalbakjes+=1
            return bakje
        else:
            print("Sorry, dat is niet mogelijk....")
def topping():
    while True:
        toppingkeuze=input('Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus? : ').lower()
        if toppingkeuze=='a':
            toppingkeuze=0
            return toppingkeuze
        elif toppingkeuze=='b':
            toppingkeuze=0.50
            return toppingkeuze
        elif toppingkeuze=='c':
            toppingkeuze=0.30
            return toppingkeuze
        elif toppingkeuze=='d':
            if bakje=='Hoorntje':
                toppingkeuze=0.60
                return toppingkeuze
            elif bakje=='Bakje':
                toppingkeuze=0.90
                return toppingkeuze
        else:
            print('Sorry, dat is niet mogelijk....')
def again():
    while True:
        opnieuw = input(f'Hier is uw {bakje} met {aantal} bolletje(s). Wilt u nog meer bestellen? (Y/N) : ').lower()
        if opnieuw == 'y':
            return opnieuw
        elif opnieuw =='n':
            print('Bedankt en tot ziens!')
            return opnieuw
        else:
            print('Sorry, dat is niet mogelijk....')
def bonnnetje():
    if aantalbakjes>=1:
        totalbakje=f'Bakje     {aantalbakjes} x €0,75 = €{round(aantalbakjes*0.75, 2)}'
    else:
        totalbakje=''
    if aantalhorentjes>=1:
        totalhoorntje=f'hoorntje  {aantalhorentjes} x €1,25 = €{round(aantalhorentjes*1.25, 2)}'
    else:
        totalhoorntje=''
    if toppingeidelijk>=0.1:
        totaltopping=f'topping    1 x €{toppingeidelijk} = €{toppingeidelijk}'
    else:
        totaltopping=''
    totalbolletjes=f'Bolletjes {aantaleindelijk} x €1,10 = €{round(aantaleindelijk*1.10, 2)}'
    totaalmoney=f'Totaal                €{round(aantalbakjes*0.75, 2)+round(aantaleindelijk*1.10, 2)+round(aantalhorentjes*1.25, 2)+round(toppingeidelijk, 2)}'
    print(f"""---------["Papi Gelato"]---------
        {totalbolletjes}
        {totalhoorntje}
        {totalbakje}
        {totaltopping}
                              ------+
        {totaalmoney}""")
while opnieuw=='y':
    aantal = vraagbolljes()
    smaakkiezen()
    bakje = bakjeofhoorntje()
    toppingkeuze=topping()
    opnieuw = again()
    toppingeidelijk+=toppingkeuze
    aantaleindelijk+=aantal
bonnnetje()

input("druk 'enter' om te sluiten")

