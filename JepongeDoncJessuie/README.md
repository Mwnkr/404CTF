# J'éponge donc j'essuie
## Catégorie
Crypto
## Difficulté
Moyen
## Énoncé
En faisant de la plongée sous-marine avec un ami gorfou je suis tombé sur un animal plutôt réservé mais fort sympathique ! J'ai donc décidé de faire mon propre algorithme de hash. Je vous mets au défi de le casser.

## Ressources

[challenge.py](challenge.py)

## Auteur
**acmo0**

# Idée de la solution

Ici, la faille réside dans le formatage au début de l'algorithme de hash qui dépend de la longueur de la chaîne donnée en entrée et dans la fonction absorb. En effet, on se rend compte qu'en rajoutant le bon nombre de 0 au début du hash ainsi que la chaîne "b'0x10'" au début et à la fin du clair, on "annule" la fonction absorb jusqu'à ce qu'on se retrouve avec les mêmes états que le clair original. On obtiendra ainsi le même hash.