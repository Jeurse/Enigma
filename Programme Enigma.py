#ne pas mettre de chiffres, ponctuation accents dans le listemessage
#respecter les instructions sous peine de faire buger le programme
#en cas de quelconque problème ou erreur relancez le programme
#et reinitialisez la machine en ecrivant "oui" (sans majuscule) quand demandé
reset=input ("voulez vous reset la machine ?:")
if reset=="oui":
    lentrée = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lsortie = ['w', 'h', 'm', 'b', 'p', 'j', 'c', 'x', 'a', 'n', 'q', 'f', 'd', 'u', 'r', 'k', 'i', 'y', 'e', 'v', 'g', 'z', 'l', 's', 'o', 't']
    lsortie2 = ['j', 'v', 'q', 'i', 's', 'b', 'k', 'y', 'd', 'n', 't', 'a', 'p', 'u', 'c', 'r', 'e', 'h', 'x', 'g', 'm', 'l', 'f', 'w', 'z', 'o']
    lentrée2 = lentrée
    t=25
    s=1
    compteurrotor1 = 0
    t2=25
    s2=1
texte=input ("saisir les lettres à remplacer dans l'ordre sans utiliser deux fois la même lettre: ")
L1=0
L2=0
L3=0
L4=0
L5=0
L6=0
L7=0
L8=0
L9=0
L10=0
L11=0
L12=0
L13=0
L14=0
L15=0
L16=0
L17=0
L18=0
L19=0
L20=0
L21=0
L22=0
L23=0
L24=0
L25=0
L26=0
liste = []
l=len (texte)
if l > 6:
    texte = 0
    print ("seulement 6 lettres peuvent être modifiées")
if l < 6:
    texte = 0
    print ("il faut tapper 6 lettres on pourra remplacer une des lettres par la même")
compteur=0
for i in texte:
    if i == "a":
        liste.append(i)
    if i == "b":
        liste.append(i)
    if i == "c":
        liste.append(i)
    if i == "d":
        liste.append(i)
    if i == "e":
        liste.append(i)
    if i == "f":
        liste.append(i)
    if i == "g":
        liste.append(i)
    if i == "h":
        liste.append(i)
    if i == "i":
        liste.append(i)
    if i == "j":
        liste.append(i)
    if i == "k":
        liste.append(i)
    if i == "l":
        liste.append(i)
    if i == "m":
        liste.append(i)
    if i == "n":
        liste.append(i)
    if i == "o":
        liste.append(i)
    if i == "p":
        liste.append(i)
    if i == "q":
        liste.append(i)
    if i == "r":
        liste.append(i)
    if i == "s":
        liste.append(i)
    if i == "t":
        liste.append(i)
    if i == "u":
        liste.append(i)
    if i == "v":
        liste.append(i)
    if i == "w":
        liste.append(i)
    if i == "x":
        liste.append(i)
    if i == "y":
        liste.append(i)
    if i == "z":
        liste.append(i)

liste2=[]
print ("ne pas utiliser les lettres",liste,"sauf pour remplacer une lettre par la même")
for i in liste:
    print("remplacer",i,":")
    L1=input()
    liste2.append(L1)
message=input ("saisir le message:")
listemessage = []
for i in message:
    if i == "a":
        listemessage.append(i)
    if i == "b":
        listemessage.append(i)
    if i == "c":
        listemessage.append(i)
    if i == "d":
        listemessage.append(i)
    if i == "e":
        listemessage.append(i)
    if i == "f":
        listemessage.append(i)
    if i == "g":
        listemessage.append(i)
    if i == "h":
        listemessage.append(i)
    if i == "i":
        listemessage.append(i)
    if i == "j":
        listemessage.append(i)
    if i == "k":
        listemessage.append(i)
    if i == "l":
        listemessage.append(i)
    if i == "m":
        listemessage.append(i)
    if i == "n":
        listemessage.append(i)
    if i == "o":
        listemessage.append(i)
    if i == "p":
        listemessage.append(i)
    if i == "q":
        listemessage.append(i)
    if i == "r":
        listemessage.append(i)
    if i == "s":
        listemessage.append(i)
    if i == "t":
        listemessage.append(i)
    if i == "u":
        listemessage.append(i)
    if i == "v":
        listemessage.append(i)
    if i == "w":
        listemessage.append(i)
    if i == "x":
        listemessage.append(i)
    if i == "y":
        listemessage.append(i)
    if i == "z":
        listemessage.append(i)
    if i == " ":
        listemessage.append(i)
listemessagecodé = []
compteur3 = 0
for i in listemessage:
    if i == liste[0]:
        listemessagecodé.append(liste2[0])
        compteur3 += 1
    if i == liste[1]:
        listemessagecodé.append(liste2[1])
        compteur3 += 1
    if i == liste[2]:
        listemessagecodé.append(liste2[2])
        compteur3 += 1
    if i == liste[3]:
        listemessagecodé.append(liste2[3])
        compteur3 += 1
    if i == liste[4]:
        listemessagecodé.append(liste2[4])
        compteur3 += 1
    if i == liste[5]:
        listemessagecodé.append(liste2[5])
        compteur3 += 1
    if i == liste2[0]:
        listemessagecodé.append(liste[0])
        compteur3 += 1
    if i == liste2[1]:
        listemessagecodé.append(liste[1])
        compteur3 += 1
    if i == liste2[2]:
        listemessagecodé.append(liste[2])
        compteur3 += 1
    if i == liste2[3]:
        listemessagecodé.append(liste[3])
        compteur3 += 1
    if i == liste2[4]:
        listemessagecodé.append(liste[4])
        compteur3 += 1
    if i == liste2[5]:
        listemessagecodé.append(liste[5])
        compteur3 += 1
    if compteur3 == 0:
        listemessagecodé.append(i)
    compteur3 = 0
print("".join(listemessagecodé))

listematrice = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
listematrice2 = [23,8,13,2,16,10,3,24,1,14,17,6,4,21,18,11,9,25,5,22,7,26,12,19,15,20]
listematrice3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
listematrice4 = [10,22,17,9,19,2,11,25,4,14,20,1,16,21,3,18,5,8,24,7,13,12,6,23,26,15]
lalphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

lpostrotor1 = []
lpostrotor2 = []
for i in listemessagecodé:
    lpostrotor1 = []
    if i == lentrée[0]:
        lpostrotor1.append(lsortie[0])
    if i == lentrée[1]:
        lpostrotor1.append(lsortie[1])
    if i == lentrée[2]:
        lpostrotor1.append(lsortie[2])
    if i == lentrée[3]:
        lpostrotor1.append(lsortie[3])
    if i == lentrée[4]:
        lpostrotor1.append(lsortie[4])
    if i == lentrée[5]:
        lpostrotor1.append(lsortie[5])
    if i == lentrée[6]:
        lpostrotor1.append(lsortie[6])
    if i == lentrée[7]:
        lpostrotor1.append(lsortie[7])
    if i == lentrée[8]:
        lpostrotor1.append(lsortie[8])
    if i == lentrée[9]:
        lpostrotor1.append(lsortie[9])
    if i == lentrée[10]:
        lpostrotor1.append(lsortie[10])
    if i == lentrée[11]:
        lpostrotor1.append(lsortie[11])
    if i == lentrée[12]:
        lpostrotor1.append(lsortie[12])
    if i == lentrée[13]:
        lpostrotor1.append(lsortie[13])
    if i == lentrée[14]:
        lpostrotor1.append(lsortie[14])
    if i == lentrée[15]:
        lpostrotor1.append(lsortie[15])
    if i == lentrée[16]:
        lpostrotor1.append(lsortie[16])
    if i == lentrée[17]:
        lpostrotor1.append(lsortie[17])
    if i == lentrée[18]:
        lpostrotor1.append(lsortie[18])
    if i == lentrée[19]:
        lpostrotor1.append(lsortie[19])
    if i == lentrée[20]:
        lpostrotor1.append(lsortie[20])
    if i == lentrée[21]:
        lpostrotor1.append(lsortie[21])
    if i == lentrée[22]:
        lpostrotor1.append(lsortie[22])
    if i == lentrée[23]:
        lpostrotor1.append(lsortie[23])
    if i == lentrée[24]:
        lpostrotor1.append(lsortie[24])
    if i == lentrée[25]:
        lpostrotor1.append(lsortie[25])
    if i == " ":
        lpostrotor1.append(" ")
    del(lentrée)
    del(lsortie)
    lentrée = []
    lsortie = []
    for i in lalphabet:
        if t == 26:
            t = 0
        if t+1 == 1:
            lentrée.append("a")
            t += 1

        else:
            if t+1 == 2:
                lentrée.append("b")
                t += 1

            else:
                if t+1 == 3:
                    lentrée.append("c")
                    t += 1
                else:
                    if t+1 == 4:
                        lentrée.append("d")
                        t += 1
                    else:
                        if t+1 == 5:
                            lentrée.append("e")
                            t += 1

                        else:
                            if t+1 == 6:
                                lentrée.append("f")
                                t += 1
                            else:
                                if t+1 == 7:
                                    lentrée.append("g")
                                    t += 1
                                else:
                                    if t+1 == 8:
                                        lentrée.append("h")
                                        t += 1

                                    else:
                                        if t+1 == 9:
                                            lentrée.append("i")
                                            t += 1
                                        else:
                                            if t+1 == 10:
                                                lentrée.append("j")
                                                t += 1
                                            else:
                                                if t+1 == 11:
                                                    lentrée.append("k")
                                                    t += 1

                                                else:
                                                    if t+1 == 12:
                                                        lentrée.append("l")
                                                        t += 1
                                                    else:
                                                        if t+1 == 13:
                                                            lentrée.append("m")
                                                            t += 1
                                                        else:
                                                            if t+1 == 14:
                                                                lentrée.append("n")
                                                                t += 1

                                                            else:
                                                                if t+1 == 15:
                                                                    lentrée.append("o")
                                                                    t += 1
                                                                else:
                                                                    if t+1 == 16:
                                                                        lentrée.append("p")
                                                                        t += 1
                                                                    else:
                                                                        if t+1 == 17:
                                                                            lentrée.append("q")
                                                                            t += 1

                                                                        else:
                                                                            if t+1 == 18:
                                                                                lentrée.append("r")
                                                                                t += 1
                                                                            else:
                                                                                if t+1 == 19:
                                                                                    lentrée.append("s")
                                                                                    t += 1
                                                                                else:
                                                                                    if t+1 == 20:
                                                                                        lentrée.append("t")
                                                                                        t += 1

                                                                                    else:
                                                                                        if t+1 == 21:
                                                                                            lentrée.append("u")
                                                                                            t += 1
                                                                                        else:
                                                                                            if t+1 == 22:
                                                                                                lentrée.append("v")
                                                                                                t += 1
                                                                                            else:
                                                                                                if t+1 == 23:
                                                                                                    lentrée.append("w")
                                                                                                    t += 1

                                                                                                else:
                                                                                                    if t+1 == 24:
                                                                                                        lentrée.append("x")
                                                                                                        t += 1
                                                                                                    else:
                                                                                                        if t+1 == 25:
                                                                                                            lentrée.append("y")
                                                                                                            t += 1
                                                                                                        else:
                                                                                                            if t+1 == 26:
                                                                                                                lentrée.append("z")
                                                                                                                t += 1
    t -= 1
    for i in listematrice2:
        i = i - s
        if s == 26:
            s = 0
        if i < 0:
            i += 26
        if i == 0:
            i += 26
        if i == 1:
            lsortie.append("a")

        else:
            if i == 2:
                lsortie.append("b")

            else:
                if i == 3:
                    lsortie.append("c")

                else:
                    if i == 4:
                        lsortie.append("d")

                    else:
                        if i == 5:
                            lsortie.append("e")

                        else:
                            if i == 6:
                                lsortie.append("f")

                            else:
                                if i == 7:
                                    lsortie.append("g")

                                else:
                                    if i == 8:
                                        lsortie.append("h")

                                    else:
                                        if i == 9:
                                            lsortie.append("i")

                                        else:
                                            if i == 10:
                                                lsortie.append("j")

                                            else:
                                                if i == 11:
                                                    lsortie.append("k")

                                                else:
                                                    if i == 12:
                                                        lsortie.append("l")

                                                    else:
                                                        if i == 13:
                                                            lsortie.append("m")

                                                        else:
                                                            if i == 14:
                                                                lsortie.append("n")

                                                            else:
                                                                if i == 15:
                                                                    lsortie.append("o")

                                                                else:
                                                                    if i == 16:
                                                                        lsortie.append("p")

                                                                    else:
                                                                        if i == 17:
                                                                            lsortie.append("q")

                                                                        else:
                                                                            if i == 18:
                                                                                lsortie.append("r")

                                                                            else:
                                                                                if i == 19:
                                                                                    lsortie.append("s")

                                                                                else:
                                                                                    if i == 20:
                                                                                        lsortie.append("t")

                                                                                    else:
                                                                                        if i == 21:
                                                                                            lsortie.append("u")

                                                                                        else:
                                                                                            if i == 22:
                                                                                                lsortie.append("v")

                                                                                            else:
                                                                                                if i == 23:
                                                                                                    lsortie.append("w")

                                                                                                else:
                                                                                                    if i == 24:
                                                                                                        lsortie.append("x")

                                                                                                    else:
                                                                                                        if i == 25:
                                                                                                            lsortie.append("y")

                                                                                                        else:
                                                                                                            if i == 26:
                                                                                                                lsortie.append("z")
    s += 1
    for l in lpostrotor1:
        if l == lentrée2[0]:
            lpostrotor2.append(lsortie2[0])
        if l == lentrée2[1]:
            lpostrotor2.append(lsortie2[1])
        if l == lentrée2[2]:
            lpostrotor2.append(lsortie2[2])
        if l == lentrée2[3]:
            lpostrotor2.append(lsortie2[3])
        if l == lentrée2[4]:
            lpostrotor2.append(lsortie2[4])
        if l == lentrée2[5]:
            lpostrotor2.append(lsortie2[5])
        if l == lentrée2[6]:
            lpostrotor2.append(lsortie2[6])
        if l == lentrée2[7]:
            lpostrotor2.append(lsortie2[7])
        if l == lentrée2[8]:
            lpostrotor2.append(lsortie2[8])
        if l == lentrée2[9]:
            lpostrotor2.append(lsortie2[9])
        if l == lentrée2[10]:
            lpostrotor2.append(lsortie2[10])
        if l == lentrée2[11]:
            lpostrotor2.append(lsortie2[11])
        if l == lentrée2[12]:
            lpostrotor2.append(lsortie2[12])
        if l == lentrée2[13]:
            lpostrotor2.append(lsortie2[13])
        if l == lentrée2[14]:
            lpostrotor2.append(lsortie2[14])
        if l == lentrée2[15]:
            lpostrotor2.append(lsortie2[15])
        if l == lentrée2[16]:
            lpostrotor2.append(lsortie2[16])
        if l == lentrée2[17]:
            lpostrotor2.append(lsortie2[17])
        if l == lentrée2[18]:
            lpostrotor2.append(lsortie2[18])
        if l == lentrée2[19]:
            lpostrotor2.append(lsortie2[19])
        if l == lentrée2[20]:
            lpostrotor2.append(lsortie2[20])
        if l == lentrée2[21]:
            lpostrotor2.append(lsortie2[21])
        if l == lentrée2[22]:
            lpostrotor2.append(lsortie2[22])
        if l == lentrée2[23]:
            lpostrotor2.append(lsortie2[23])
        if l == lentrée2[24]:
            lpostrotor2.append(lsortie2[24])
        if l == lentrée2[25]:
            lpostrotor2.append(lsortie2[25])
        if l == " ":
            lpostrotor2.append(" ")
        if compteurrotor1 == 26:
            compteurrotor1 = 0
            lentrée2 = []
            lsortie2 = []
            for i in lalphabet:
                if t2 == 26:
                    t2 = 0
                if t2+1 == 1:
                    lentrée2.append("a")
                    t2 += 1

                else:
                    if t2+1 == 2:
                        lentrée2.append("b")
                        t2 += 1

                    else:
                        if t2+1 == 3:
                            lentrée2.append("c")
                            t2 += 1
                        else:
                            if t2+1 == 4:
                                lentrée2.append("d")
                                t2 += 1
                            else:
                                if t2+1 == 5:
                                    lentrée2.append("e")
                                    t2 += 1

                                else:
                                    if t2+1 == 6:
                                        lentrée2.append("f")
                                        t2 += 1
                                    else:
                                        if t2+1 == 7:
                                            lentrée2.append("g")
                                            t2 += 1
                                        else:
                                            if t2+1 == 8:
                                                lentrée2.append("h")
                                                t2 += 1

                                            else:
                                                if t2+1 == 9:
                                                    lentrée2.append("i")
                                                    t2 += 1
                                                else:
                                                    if t2+1 == 10:
                                                        lentrée2.append("j")
                                                        t2 += 1
                                                    else:
                                                        if t2+1 == 11:
                                                            lentrée2.append("k")
                                                            t2 += 1

                                                        else:
                                                            if t2+1 == 12:
                                                                lentrée2.append("l")
                                                                t2 += 1
                                                            else:
                                                                if t2+1 == 13:
                                                                    lentrée2.append("m")
                                                                    t2 += 1
                                                                else:
                                                                    if t2+1 == 14:
                                                                        lentrée2.append("n")
                                                                        t2 += 1

                                                                    else:
                                                                        if t2+1 == 15:
                                                                            lentrée2.append("o")
                                                                            t2 += 1
                                                                        else:
                                                                            if t2+1 == 16:
                                                                                lentrée2.append("p")
                                                                                t2 += 1
                                                                            else:
                                                                                if t2+1 == 17:
                                                                                    lentrée2.append("q")
                                                                                    t2 += 1

                                                                                else:
                                                                                    if t2+1 == 18:
                                                                                        lentrée2.append("r")
                                                                                        t2 += 1
                                                                                    else:
                                                                                        if t2+1 == 19:
                                                                                            lentrée2.append("s")
                                                                                            t2 += 1
                                                                                        else:
                                                                                            if t2+1 == 20:
                                                                                                lentrée2.append("t")
                                                                                                t2 += 1

                                                                                            else:
                                                                                                if t2+1 == 21:
                                                                                                    lentrée2.append("u")
                                                                                                    t2 += 1
                                                                                                else:
                                                                                                    if t2+1 == 22:
                                                                                                        lentrée2.append("v")
                                                                                                        t2 += 1
                                                                                                    else:
                                                                                                        if t2+1 == 23:
                                                                                                            lentrée2.append("w")
                                                                                                            t2 += 1

                                                                                                        else:
                                                                                                            if t2+1 == 24:
                                                                                                                lentrée2.append("x")
                                                                                                                t2 += 1
                                                                                                            else:
                                                                                                                if t2+1 == 25:
                                                                                                                    lentrée2.append("y")
                                                                                                                    t2 += 1
                                                                                                                else:
                                                                                                                    if t2+1 == 26:
                                                                                                                        lentrée2.append("z")
                                                                                                                        t2 += 1
            t2 -= 1
            for i in listematrice4:
                i = i - s2
                if s2 == 26:
                    s2 = 0
                if i < 0:
                    i += 26
                if i == 0:
                    i += 26
                if i == 1:
                    lsortie2.append("a")

                else:
                    if i == 2:
                        lsortie2.append("b")

                    else:
                        if i == 3:
                            lsortie2.append("c")

                        else:
                            if i == 4:
                                lsortie2.append("d")

                            else:
                                if i == 5:
                                    lsortie2.append("e")

                                else:
                                    if i == 6:
                                        lsortie2.append("f")

                                    else:
                                        if i == 7:
                                            lsortie2.append("g")

                                        else:
                                            if i == 8:
                                                lsortie2.append("h")

                                            else:
                                                if i == 9:
                                                    lsortie2.append("i")

                                                else:
                                                    if i == 10:
                                                        lsortie2.append("j")

                                                    else:
                                                        if i == 11:
                                                            lsortie2.append("k")

                                                        else:
                                                            if i == 12:
                                                                lsortie2.append("l")

                                                            else:
                                                                if i == 13:
                                                                    lsortie2.append("m")

                                                                else:
                                                                    if i == 14:
                                                                        lsortie2.append("n")

                                                                    else:
                                                                        if i == 15:
                                                                            lsortie2.append("o")

                                                                        else:
                                                                            if i == 16:
                                                                                lsortie2.append("p")

                                                                            else:
                                                                                if i == 17:
                                                                                    lsortie2.append("q")

                                                                                else:
                                                                                    if i == 18:
                                                                                        lsortie2.append("r")

                                                                                    else:
                                                                                        if i == 19:
                                                                                            lsortie2.append("s")

                                                                                        else:
                                                                                            if i == 20:
                                                                                                lsortie2.append("t")

                                                                                            else:
                                                                                                if i == 21:
                                                                                                    lsortie2.append("u")

                                                                                                else:
                                                                                                    if i == 22:
                                                                                                        lsortie2.append("v")

                                                                                                    else:
                                                                                                        if i == 23:
                                                                                                            lsortie2.append("w")

                                                                                                        else:
                                                                                                            if i == 24:
                                                                                                                lsortie2.append("x")

                                                                                                            else:
                                                                                                                if i == 25:
                                                                                                                    lsortie2.append("y")

                                                                                                                else:
                                                                                                                    if i == 26:
                                                                                                                        lsortie2.append("z")
            s2 += 1
        compteurrotor1 += 1
        print("".join(lpostrotor2))
