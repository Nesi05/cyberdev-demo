# Voici notre premier project
# nous voulons un code python qui permet a l'utilisateur de deviner un nombre:
# Entrer un nombre, et quand l'utilisateur entre le nombre, ça dit si le nombre entré est grand ou petit. ou il a trouver le bon nombre



import randon  # fonction de nombre aléatoire 
A= random.randint(0, 20) # nombre aléatoire comprise entre 0 et 20
N= int(input()) # Entrer un nombre entier 
if N>A:
  print(N " est plus grand que le nombre aléatoire ")
else if N<A:
  print(N " est plus que le nombre aléatoire ")
else 
  print(A "Nombre aléatoire ")
  print(N " nombre saisie correspondant au nombre aléatoire ")
