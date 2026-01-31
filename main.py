# Voici notre premier project
# nous voulons un code python qui permet a l'utilisateur de deviner un nombre:
# Entrer un nombre, et quand l'utilisateur entre le nombre, ça dit si le nombre entré est grand ou petit. ou il a trouver le bon nombre
import random

genere_un_nombre = random.randint(1, 50)
print("le nombre génénér est de :", genere_un_nombre)

nbr= int(input("entrer un nombre"))

if nbr > genere_un_nombre:

    print("le nombre entrer est grand")

else:
    print("le nombre entrer est petit")
