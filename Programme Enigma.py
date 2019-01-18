#ne pas mettre de chiffres, ponctuation accents dans le listemessage
#respecter les instructions sous peine de faire buger le programme
#en cas de quelconque problème ou erreur relancez le programme
#et reinitialisez la machine en ecrivant "oui" (sans majuscule) quand demandé
reset=input ("voulez vous reset la machine ?:")
if reset=="oui":
    lentrée = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lsortie = ['w', 'h', 'm', 'b', 'p', 'j', 'c', 'x', 'a', 'n', 'q', 'f', 'd', 'u', 'r', 'k', 'i', 'y', 'e', 'v', 'g', 'z', 'l', 's', 'o', 't']
    lsortie2 = ['j', 'v', 'q', 'i', 's', 'b', 'k', 'y', 'd', 'n', 't', 'a', 'p', 'u', 'c', 'r', 'e', 'h', 'x', 'g', 'm', 'l', 'f', 'w', 'z', 'o']
    lsortie3 = ['g','r','m','z','t','o','e','k','v','x','s','f','u','a','n','i','w','c','p','h','l','q','b','d','j','y']
    lentréeb3 = ['j', 'u', 'q', 'z', 'h', 'l', 'x', 'e', 'm', 'a', 'y', 'f', 'i', 't', 's', 'v', 'c', 'w', 'o', 'n', 'b', 'p', 'r', 'g', 'k', 'd']
    lentrée2 = lentrée
    lentrée3 = lentrée
    lsortieb = lentrée
    lsortieb2 = lentrée
    lsortieb3 = lentrée
    lentréeb = lsortie
    lentréeb2 = lsortie2
    lentrée4 = lentrée
    lentréeb5 = lsortie3
    t=25
    s=1
    compteurrotor1 = 1
    t2=25
    s2=1
    compteurrotor2 = 1
    t3=25
    s3=1
    t4=25
    s5=1
texte=input ("saisir les lettres à remplacer dans l'ordre sans utiliser deux fois la même lettre: ")
L1=0
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
    liste.append(i)
    '''
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
'''
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

listematrice = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
listematrice2 = [23,8,13,2,16,10,3,24,1,14,17,6,4,21,18,11,9,25,5,22,7,26,12,19,15,20]
listematrice3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
listematrice4 = [10,22,17,9,19,2,11,25,4,14,20,1,16,21,3,18,5,8,24,7,13,12,6,23,26,15]
listematrice5 = [7,18,13,26,20,15,5,11,22,24,19,6,21,1,14,9,23,3,16,8,12,17,2,4,10,25]
listematrice6 = [10,21,17,26,8,12,24,5,13,1,25,6,9,20,19,22,3,23,15,14,2,16,18,7,11,4]
lalphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lpostroror1 = []
lpostrotor2 = []
lpostrotor3 = []
lpostrotor4 = []
lpostrotorb3 = []
lpostrotorb2 = []
lpostrotorb = []
messagecodé = []
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
        lpostrotor2 =[]
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
    for l in lpostrotor2:
        lpostrotor3 = []
        if l == lentrée3[0]:
            lpostrotor3.append(lsortie3[0])
        if l == lentrée3[1]:
            lpostrotor3.append(lsortie3[1])
        if l == lentrée3[2]:
            lpostrotor3.append(lsortie3[2])
        if l == lentrée3[3]:
            lpostrotor3.append(lsortie3[3])
        if l == lentrée3[4]:
            lpostrotor3.append(lsortie3[4])
        if l == lentrée3[5]:
            lpostrotor3.append(lsortie3[5])
        if l == lentrée3[6]:
            lpostrotor3.append(lsortie3[6])
        if l == lentrée3[7]:
            lpostrotor3.append(lsortie3[7])
        if l == lentrée3[8]:
            lpostrotor3.append(lsortie3[8])
        if l == lentrée3[9]:
            lpostrotor3.append(lsortie3[9])
        if l == lentrée3[10]:
            lpostrotor3.append(lsortie3[10])
        if l == lentrée3[11]:
            lpostrotor3.append(lsortie3[11])
        if l == lentrée3[12]:
            lpostrotor3.append(lsortie3[12])
        if l == lentrée3[13]:
            lpostrotor3.append(lsortie3[13])
        if l == lentrée3[14]:
            lpostrotor3.append(lsortie3[14])
        if l == lentrée3[15]:
            lpostrotor3.append(lsortie3[15])
        if l == lentrée3[16]:
            lpostrotor3.append(lsortie3[16])
        if l == lentrée3[17]:
            lpostrotor3.append(lsortie3[17])
        if l == lentrée3[18]:
            lpostrotor3.append(lsortie3[18])
        if l == lentrée3[19]:
            lpostrotor3.append(lsortie3[19])
        if l == lentrée3[20]:
            lpostrotor3.append(lsortie3[20])
        if l == lentrée3[21]:
            lpostrotor3.append(lsortie3[21])
        if l == lentrée3[22]:
            lpostrotor3.append(lsortie3[22])
        if l == lentrée3[23]:
            lpostrotor3.append(lsortie3[23])
        if l == lentrée3[24]:
            lpostrotor3.append(lsortie3[24])
        if l == lentrée3[25]:
            lpostrotor3.append(lsortie3[25])
        if l == " ":
            lpostrotor3.append(" ")
        if compteurrotor2 == 676:
            lentrée3 = []
            lsortie3 = []
            for i in lalphabet:
                if t3 == 26:
                    t3 = 0
                if t3+1 == 1:
                    lentrée3.append("a")
                    t3 += 1

                else:
                    if t3+1 == 2:
                        lentrée3.append("b")
                        t3 += 1

                    else:
                        if t3+1 == 3:
                            lentrée3.append("c")
                            t3 += 1
                        else:
                            if t3+1 == 4:
                                lentrée3.append("d")
                                t3 += 1
                            else:
                                if t3+1 == 5:
                                    lentrée3.append("e")
                                    t3 += 1

                                else:
                                    if t3+1 == 6:
                                        lentrée3.append("f")
                                        t3 += 1
                                    else:
                                        if t3+1 == 7:
                                            lentrée3.append("g")
                                            t3 += 1
                                        else:
                                            if t3+1 == 8:
                                                lentrée3.append("h")
                                                t3 += 1

                                            else:
                                                if t3+1 == 9:
                                                    lentrée3.append("i")
                                                    t3 += 1
                                                else:
                                                    if t3+1 == 10:
                                                        lentrée3.append("j")
                                                        t3 += 1
                                                    else:
                                                        if t3+1 == 11:
                                                            lentrée3.append("k")
                                                            t3 += 1

                                                        else:
                                                            if t3+1 == 12:
                                                                lentrée3.append("l")
                                                                t3 += 1
                                                            else:
                                                                if t3+1 == 13:
                                                                    lentrée3.append("m")
                                                                    t3 += 1
                                                                else:
                                                                    if t3+1 == 14:
                                                                        lentrée3.append("n")
                                                                        t3 += 1

                                                                    else:
                                                                        if t3+1 == 15:
                                                                            lentrée3.append("o")
                                                                            t3 += 1
                                                                        else:
                                                                            if t3+1 == 16:
                                                                                lentrée3.append("p")
                                                                                t3 += 1
                                                                            else:
                                                                                if t3+1 == 17:
                                                                                    lentrée3.append("q")
                                                                                    t3 += 1

                                                                                else:
                                                                                    if t3+1 == 18:
                                                                                        lentrée3.append("r")
                                                                                        t3 += 1
                                                                                    else:
                                                                                        if t3+1 == 19:
                                                                                            lentrée3.append("s")
                                                                                            t3 += 1
                                                                                        else:
                                                                                            if t3+1 == 20:
                                                                                                lentrée3.append("t")
                                                                                                t3 += 1

                                                                                            else:
                                                                                                if t3+1 == 21:
                                                                                                    lentrée3.append("u")
                                                                                                    t3 += 1
                                                                                                else:
                                                                                                    if t3+1 == 22:
                                                                                                        lentrée3.append("v")
                                                                                                        t3 += 1
                                                                                                    else:
                                                                                                        if t3+1 == 23:
                                                                                                            lentrée3.append("w")
                                                                                                            t3 += 1

                                                                                                        else:
                                                                                                            if t3+1 == 24:
                                                                                                                lentrée3.append("x")
                                                                                                                t3 += 1
                                                                                                            else:
                                                                                                                if t3+1 == 25:
                                                                                                                    lentrée3.append("y")
                                                                                                                    t3 += 1
                                                                                                                else:
                                                                                                                    if t3+1 == 26:
                                                                                                                        lentrée3.append("z")
                                                                                                                        t3 += 1
            t3 -= 1
            for i in listematrice5:
                i = i - s3
                if s3 == 26:
                    s3 = 0
                if i < 0:
                    i += 26
                if i == 0:
                    i += 26
                if i == 1:
                    lsortie3.append("a")

                else:
                    if i == 2:
                        lsortie3.append("b")

                    else:
                        if i == 3:
                            lsortie3.append("c")

                        else:
                            if i == 4:
                                lsortie3.append("d")

                            else:
                                if i == 5:
                                    lsortie3.append("e")

                                else:
                                    if i == 6:
                                        lsortie3.append("f")

                                    else:
                                        if i == 7:
                                            lsortie3.append("g")

                                        else:
                                            if i == 8:
                                                lsortie3.append("h")

                                            else:
                                                if i == 9:
                                                    lsortie3.append("i")

                                                else:
                                                    if i == 10:
                                                        lsortie3.append("j")

                                                    else:
                                                        if i == 11:
                                                            lsortie3.append("k")

                                                        else:
                                                            if i == 12:
                                                                lsortie3.append("l")

                                                            else:
                                                                if i == 13:
                                                                    lsortie3.append("m")

                                                                else:
                                                                    if i == 14:
                                                                        lsortie3.append("n")

                                                                    else:
                                                                        if i == 15:
                                                                            lsortie3.append("o")

                                                                        else:
                                                                            if i == 16:
                                                                                lsortie3.append("p")

                                                                            else:
                                                                                if i == 17:
                                                                                    lsortie3.append("q")

                                                                                else:
                                                                                    if i == 18:
                                                                                        lsortie3.append("r")

                                                                                    else:
                                                                                        if i == 19:
                                                                                            lsortie3.append("s")

                                                                                        else:
                                                                                            if i == 20:
                                                                                                lsortie3.append("t")

                                                                                            else:
                                                                                                if i == 21:
                                                                                                    lsortie3.append("u")

                                                                                                else:
                                                                                                    if i == 22:
                                                                                                        lsortie3.append("v")

                                                                                                    else:
                                                                                                        if i == 23:
                                                                                                            lsortie3.append("w")

                                                                                                        else:
                                                                                                            if i == 24:
                                                                                                                lsortie3.append("x")

                                                                                                            else:
                                                                                                                if i == 25:
                                                                                                                    lsortie3.append("y")

                                                                                                                else:
                                                                                                                    if i == 26:
                                                                                                                        lsortie3.append("z")
            s3 += 1
    for l in lpostrotor3:
        lpostrotor4 = []
        if l == lentrée4[0]:
            lpostrotor4.append(lentréeb3[0])
        if l == lentrée4[1]:
            lpostrotor4.append(lentréeb3[1])
        if l == lentrée4[2]:
            lpostrotor4.append(lentréeb3[2])
        if l == lentrée4[3]:
            lpostrotor4.append(lentréeb3[3])
        if l == lentrée4[4]:
            lpostrotor4.append(lentréeb3[4])
        if l == lentrée4[5]:
            lpostrotor4.append(lentréeb3[5])
        if l == lentrée4[6]:
            lpostrotor4.append(lentréeb3[6])
        if l == lentrée4[7]:
            lpostrotor4.append(lentréeb3[7])
        if l == lentrée4[8]:
            lpostrotor4.append(lentréeb3[8])
        if l == lentrée4[9]:
            lpostrotor4.append(lentréeb3[9])
        if l == lentrée4[10]:
            lpostrotor4.append(lentréeb3[10])
        if l == lentrée4[11]:
            lpostrotor4.append(lentréeb3[11])
        if l == lentrée4[12]:
            lpostrotor4.append(lentréeb3[12])
        if l == lentrée4[13]:
            lpostrotor4.append(lentréeb3[13])
        if l == lentrée4[14]:
            lpostrotor4.append(lentréeb3[14])
        if l == lentrée4[15]:
            lpostrotor4.append(lentréeb3[15])
        if l == lentrée4[16]:
            lpostrotor4.append(lentréeb3[16])
        if l == lentrée4[17]:
            lpostrotor4.append(lentréeb3[17])
        if l == lentrée4[18]:
            lpostrotor4.append(lentréeb3[18])
        if l == lentrée4[19]:
            lpostrotor4.append(lentréeb3[19])
        if l == lentrée4[20]:
            lpostrotor4.append(lentréeb3[20])
        if l == lentrée4[21]:
            lpostrotor4.append(lentréeb3[21])
        if l == lentrée4[22]:
            lpostrotor4.append(lentréeb3[22])
        if l == lentrée4[23]:
            lpostrotor4.append(lentréeb3[23])
        if l == lentrée4[24]:
            lpostrotor4.append(lentréeb3[24])
        if l == lentrée4[25]:
            lpostrotor4.append(lentréeb3[25])
        if l == " ":
            lpostrotor4.append(" ")
        if compteurrotor2 == 676:
            compteurrotor2 = 0
            lentrée4 = []
            lentréeb3 = []
            for i in lalphabet:
                if t4 == 26:
                    t4 = 0
                if t4+1 == 1:
                    lentrée4.append("a")
                    t4 += 1

                else:
                    if t4+1 == 2:
                        lentrée4.append("b")
                        t4 += 1

                    else:
                        if t4+1 == 3:
                            lentrée4.append("c")
                            t4 += 1
                        else:
                            if t4+1 == 4:
                                lentrée4.append("d")
                                t4 += 1
                            else:
                                if t4+1 == 5:
                                    lentrée4.append("e")
                                    t4 += 1

                                else:
                                    if t4+1 == 6:
                                        lentrée4.append("f")
                                        t4 += 1
                                    else:
                                        if t4+1 == 7:
                                            lentrée4.append("g")
                                            t4 += 1
                                        else:
                                            if t4+1 == 8:
                                                lentrée4.append("h")
                                                t4 += 1

                                            else:
                                                if t4+1 == 9:
                                                    lentrée4.append("i")
                                                    t4 += 1
                                                else:
                                                    if t4+1 == 10:
                                                        lentrée4.append("j")
                                                        t4 += 1
                                                    else:
                                                        if t4+1 == 11:
                                                            lentrée4.append("k")
                                                            t4 += 1

                                                        else:
                                                            if t4+1 == 12:
                                                                lentrée4.append("l")
                                                                t4 += 1
                                                            else:
                                                                if t4+1 == 13:
                                                                    lentrée4.append("m")
                                                                    t4 += 1
                                                                else:
                                                                    if t4+1 == 14:
                                                                        lentrée4.append("n")
                                                                        t4 += 1

                                                                    else:
                                                                        if t4+1 == 15:
                                                                            lentrée4.append("o")
                                                                            t4 += 1
                                                                        else:
                                                                            if t4+1 == 16:
                                                                                lentrée4.append("p")
                                                                                t4 += 1
                                                                            else:
                                                                                if t4+1 == 17:
                                                                                    lentrée4.append("q")
                                                                                    t4 += 1

                                                                                else:
                                                                                    if t4+1 == 18:
                                                                                        lentrée4.append("r")
                                                                                        t4 += 1
                                                                                    else:
                                                                                        if t4+1 == 19:
                                                                                            lentrée4.append("s")
                                                                                            t4 += 1
                                                                                        else:
                                                                                            if t4+1 == 20:
                                                                                                lentrée4.append("t")
                                                                                                t4 += 1

                                                                                            else:
                                                                                                if t4+1 == 21:
                                                                                                    lentrée4.append("u")
                                                                                                    t4 += 1
                                                                                                else:
                                                                                                    if t4+1 == 22:
                                                                                                        lentrée4.append("v")
                                                                                                        t4 += 1
                                                                                                    else:
                                                                                                        if t4+1 == 23:
                                                                                                            lentrée4.append("w")
                                                                                                            t4 += 1

                                                                                                        else:
                                                                                                            if t4+1 == 24:
                                                                                                                lentrée4.append("x")
                                                                                                                t4 += 1
                                                                                                            else:
                                                                                                                if t4+1 == 25:
                                                                                                                    lentrée4.append("y")
                                                                                                                    t4 += 1
                                                                                                                else:
                                                                                                                    if t4+1 == 26:
                                                                                                                        lentrée4.append("z")
                                                                                                                        t4 += 1
            t4 -= 1
            for i in listematrice6:
                i = i - s5
                if s5 == 26:
                    s5 = 0
                if i < 0:
                    i += 26
                if i == 0:
                    i += 26
                if i == 1:
                    lentréeb3.append("a")

                else:
                    if i == 2:
                        lentréeb3.append("b")

                    else:
                        if i == 3:
                            lentréeb3.append("c")

                        else:
                            if i == 4:
                                lentréeb3.append("d")

                            else:
                                if i == 5:
                                    lentréeb3.append("e")

                                else:
                                    if i == 6:
                                        lentréeb3.append("f")

                                    else:
                                        if i == 7:
                                            lentréeb3.append("g")

                                        else:
                                            if i == 8:
                                                lentréeb3.append("h")

                                            else:
                                                if i == 9:
                                                    lentréeb3.append("i")

                                                else:
                                                    if i == 10:
                                                        lentréeb3.append("j")

                                                    else:
                                                        if i == 11:
                                                            lentréeb3.append("k")

                                                        else:
                                                            if i == 12:
                                                                lentréeb3.append("l")

                                                            else:
                                                                if i == 13:
                                                                    lentréeb3.append("m")

                                                                else:
                                                                    if i == 14:
                                                                        lentréeb3.append("n")

                                                                    else:
                                                                        if i == 15:
                                                                            lentréeb3.append("o")

                                                                        else:
                                                                            if i == 16:
                                                                                lentréeb3.append("p")

                                                                            else:
                                                                                if i == 17:
                                                                                    lentréeb3.append("q")

                                                                                else:
                                                                                    if i == 18:
                                                                                        lentréeb3.append("r")

                                                                                    else:
                                                                                        if i == 19:
                                                                                            lentréeb3.append("s")

                                                                                        else:
                                                                                            if i == 20:
                                                                                                lentréeb3.append("t")

                                                                                            else:
                                                                                                if i == 21:
                                                                                                    lentréeb3.append("u")

                                                                                                else:
                                                                                                    if i == 22:
                                                                                                        lentréeb3.append("v")

                                                                                                    else:
                                                                                                        if i == 23:
                                                                                                            lentréeb3.append("w")

                                                                                                        else:
                                                                                                            if i == 24:
                                                                                                                lentréeb3.append("x")

                                                                                                            else:
                                                                                                                if i == 25:
                                                                                                                    lentréeb3.append("y")

                                                                                                                else:
                                                                                                                    if i == 26:
                                                                                                                        lentréeb3.append("z")
            s5 += 1
    for l in lpostrotor4:
        lpostrotorb3 = []
        if l == lentréeb5[0]:
            lpostrotorb3.append(lsortieb3[0])
        if l == lentréeb5[1]:
            lpostrotorb3.append(lsortieb3[1])
        if l == lentréeb5[2]:
            lpostrotorb3.append(lsortieb3[2])
        if l == lentréeb5[3]:
            lpostrotorb3.append(lsortieb3[3])
        if l == lentréeb5[4]:
            lpostrotorb3.append(lsortieb3[4])
        if l == lentréeb5[5]:
            lpostrotorb3.append(lsortieb3[5])
        if l == lentréeb5[6]:
            lpostrotorb3.append(lsortieb3[6])
        if l == lentréeb5[7]:
            lpostrotorb3.append(lsortieb3[7])
        if l == lentréeb5[8]:
            lpostrotorb3.append(lsortieb3[8])
        if l == lentréeb5[9]:
            lpostrotorb3.append(lsortieb3[9])
        if l == lentréeb5[10]:
            lpostrotorb3.append(lsortieb3[10])
        if l == lentréeb5[11]:
            lpostrotorb3.append(lsortieb3[11])
        if l == lentréeb5[12]:
            lpostrotorb3.append(lsortieb3[12])
        if l == lentréeb5[13]:
            lpostrotorb3.append(lsortieb3[13])
        if l == lentréeb5[14]:
            lpostrotorb3.append(lsortieb3[14])
        if l == lentréeb5[15]:
            lpostrotorb3.append(lsortieb3[15])
        if l == lentréeb5[16]:
            lpostrotorb3.append(lsortieb3[16])
        if l == lentréeb5[17]:
            lpostrotorb3.append(lsortieb3[17])
        if l == lentréeb5[18]:
            lpostrotorb3.append(lsortieb3[18])
        if l == lentréeb5[19]:
            lpostrotorb3.append(lsortieb3[19])
        if l == lentréeb5[20]:
            lpostrotorb3.append(lsortieb3[20])
        if l == lentréeb5[21]:
            lpostrotorb3.append(lsortieb3[21])
        if l == lentréeb5[22]:
            lpostrotorb3.append(lsortieb3[22])
        if l == lentréeb5[23]:
            lpostrotorb3.append(lsortieb3[23])
        if l == lentréeb5[24]:
            lpostrotorb3.append(lsortieb3[24])
        if l == lentréeb5[25]:
            lpostrotorb3.append(lsortieb3[25])
        if l == " ":
            lpostrotorb3.append(" ")
    for l in lpostrotorb3:
        lpostrotorb2 = []
        if l == lentréeb2[0]:
            lpostrotorb2.append(lsortieb2[0])
        if l == lentréeb2[1]:
            lpostrotorb2.append(lsortieb2[1])
        if l == lentréeb2[2]:
            lpostrotorb2.append(lsortieb2[2])
        if l == lentréeb2[3]:
            lpostrotorb2.append(lsortieb2[3])
        if l == lentréeb2[4]:
            lpostrotorb2.append(lsortieb2[4])
        if l == lentréeb2[5]:
            lpostrotorb2.append(lsortieb2[5])
        if l == lentréeb2[6]:
            lpostrotorb2.append(lsortieb2[6])
        if l == lentréeb2[7]:
            lpostrotorb2.append(lsortieb2[7])
        if l == lentréeb2[8]:
            lpostrotorb2.append(lsortieb2[8])
        if l == lentréeb2[9]:
            lpostrotorb2.append(lsortieb2[9])
        if l == lentréeb2[10]:
            lpostrotorb2.append(lsortieb2[10])
        if l == lentréeb2[11]:
            lpostrotorb2.append(lsortieb2[11])
        if l == lentréeb2[12]:
            lpostrotorb2.append(lsortieb2[12])
        if l == lentréeb2[13]:
            lpostrotorb2.append(lsortieb2[13])
        if l == lentréeb2[14]:
            lpostrotorb2.append(lsortieb2[14])
        if l == lentréeb2[15]:
            lpostrotorb2.append(lsortieb2[15])
        if l == lentréeb2[16]:
            lpostrotorb2.append(lsortieb2[16])
        if l == lentréeb2[17]:
            lpostrotorb2.append(lsortieb2[17])
        if l == lentréeb2[18]:
            lpostrotorb2.append(lsortieb2[18])
        if l == lentréeb2[19]:
            lpostrotorb2.append(lsortieb2[19])
        if l == lentréeb2[20]:
            lpostrotorb2.append(lsortieb2[20])
        if l == lentréeb2[21]:
            lpostrotorb2.append(lsortieb2[21])
        if l == lentréeb2[22]:
            lpostrotorb2.append(lsortieb2[22])
        if l == lentréeb2[23]:
            lpostrotorb2.append(lsortieb2[23])
        if l == lentréeb2[24]:
            lpostrotorb2.append(lsortieb2[24])
        if l == lentréeb2[25]:
            lpostrotorb2.append(lsortieb2[25])
        if l == " ":
            lpostrotorb2.append(" ")
    for l in lpostrotorb2:
        lpostrotorb = []
        if l == lentréeb[0]:
            lpostrotorb.append(lsortieb[0])
        if l == lentréeb[1]:
            lpostrotorb.append(lsortieb[1])
        if l == lentréeb[2]:
            lpostrotorb.append(lsortieb[2])
        if l == lentréeb[3]:
            lpostrotorb.append(lsortieb[3])
        if l == lentréeb[4]:
            lpostrotorb.append(lsortieb[4])
        if l == lentréeb[5]:
            lpostrotorb.append(lsortieb[5])
        if l == lentréeb[6]:
            lpostrotorb.append(lsortieb[6])
        if l == lentréeb[7]:
            lpostrotorb.append(lsortieb[7])
        if l == lentréeb[8]:
            lpostrotorb.append(lsortieb[8])
        if l == lentréeb[9]:
            lpostrotorb.append(lsortieb[9])
        if l == lentréeb[10]:
            lpostrotorb.append(lsortieb[10])
        if l == lentréeb[11]:
            lpostrotorb.append(lsortieb[11])
        if l == lentréeb[12]:
            lpostrotorb.append(lsortieb[12])
        if l == lentréeb[13]:
            lpostrotorb.append(lsortieb[13])
        if l == lentréeb[14]:
            lpostrotorb.append(lsortieb[14])
        if l == lentréeb[15]:
            lpostrotorb.append(lsortieb[15])
        if l == lentréeb[16]:
            lpostrotorb.append(lsortieb[16])
        if l == lentréeb[17]:
            lpostrotorb.append(lsortieb[17])
        if l == lentréeb[18]:
            lpostrotorb.append(lsortieb[18])
        if l == lentréeb[19]:
            lpostrotorb.append(lsortieb[19])
        if l == lentréeb[20]:
            lpostrotorb.append(lsortieb[20])
        if l == lentréeb[21]:
            lpostrotorb.append(lsortieb[21])
        if l == lentréeb[22]:
            lpostrotorb.append(lsortieb[22])
        if l == lentréeb[23]:
            lpostrotorb.append(lsortieb[23])
        if l == lentréeb[24]:
            lpostrotorb.append(lsortieb[24])
        if l == lentréeb[25]:
            lpostrotorb.append(lsortieb[25])
        if l == " ":
            lpostrotorb.append(" ")
    for l in lpostrotorb:
        if l == liste[0]:
            messagecodé.append(liste2[0])
            compteur3 += 1
        if l == liste[1]:
            messagecodé.append(liste2[1])
            compteur3 += 1
        if l == liste[2]:
            messagecodé.append(liste2[2])
            compteur3 += 1
        if l == liste[3]:
            messagecodé.append(liste2[3])
            compteur3 += 1
        if l == liste[4]:
            messagecodé.append(liste2[4])
            compteur3 += 1
        if l == liste[5]:
            messagecodé.append(liste2[5])
            compteur3 += 1
        if l == liste2[0]:
            messagecodé.append(liste[0])
            compteur3 += 1
        if l == liste2[1]:
            messagecodé.append(liste[1])
            compteur3 += 1
        if l == liste2[2]:
            messagecodé.append(liste[2])
            compteur3 += 1
        if l == liste2[3]:
            messagecodé.append(liste[3])
            compteur3 += 1
        if l == liste2[4]:
            messagecodé.append(liste[4])
            compteur3 += 1
        if l == liste2[5]:
            messagecodé.append(liste[5])
            compteur3 += 1
        if compteur3 == 0:
            messagecodé.append(l)
        compteur3 = 0
    lsortieb = lentrée
    lsortieb2 = lentrée2
    lsortieb3 = lentrée3
    lentréeb = lsortie
    lentréeb2 = lsortie2
    lentréeb5 = lsortie3
    compteurrotor1 += 1
    compteurrotor2 += 1
print("".join(messagecodé))
