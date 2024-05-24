# La Seine
## Catégorie
Crypto
## Difficulté
Difficile

## Énoncé

La compétition d'apnée est sur le point de commencer, l'eau est un peu trouble mais les épreuves précédentes ont sculpté votre détermination. Au moment où vous vous apprêtez à rentrer dans l'eau, votre entraineur vous ordonne d'un ton sevère : "Lorsque tu mettras la tête sous l'eau, ne ressors pas avant d'avoir réussi ce problème, bonne chance à toi". Vous prenez une grande inspiration et plongez la tête baissée dans ce problème :

## Ressources

[LaSeine.py](LaSeine.py)

## Auteur
**GMO_Goat**

# Idée de la solution

Alors ici, le but est de retrouver a et b.

Tout d'abord, j'ai commencé à écrire à la main les premières itérations de xn, yn. J'y ai reconnu les valeurs du triangle de Pascal, ce qui rime souvent avec binôme de Newton.

Effectivement, on retrouve deux formules pour le cas pair et impair. Puisque tout cela n'est qu'au stade de la conjecture, une preuve par récurrence confirme rapidement la véracité de celle-ci.

Puisqu'on a accès aux données pour une itération pair, on va l'utiliser habilement avec de l'arithmétique modulaire pour retrouver une valeur de a^2 + b^2.

À partir de celle-ci, j'ai utilisé dCode et les équations que j'avais calculées pour obtenir des valeurs possibles de a et b.

Ensuite, on brute force jusqu'à obtention du FLAG.
