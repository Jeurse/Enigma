texte=input ("saisir texte: ")
l=len (texte)
compteur=0
for i in texte:
    if i == "a":
        compteur += 1
print (compteur)
