# Poor Random Number Generator 2/2
## Catégorie
Crypto
## Difficulté
Moyen
## Énoncé

Félicitation ! C'est vrai que mon PRNG précédent n'était pas terrible... Je l'ai donc patché ! J'ai de nouveau chiffré un nouveau fichier PNG et cette fois-ci j'ai essayé de limiter les données en clair qui ont fuité.

Bonne chance !

## Ressources

[challenge.zip](challenge.zip)

## Auteur
**acmo0**

# Idée de la solution

Nous sommes face à un LFSR combiné à 3 registres de taille 19. Nous avons également 35 bytes de clair connu. Nous nous en servons pour obtenir le début de la suite chiffrante du LFSR combiné.

En faisant la table de vérité :

|x1 |x2 |x3 |f(x) |
|-|-|-|-|
|0 |0 |0 |0 |
|0 |0 |1 |0 |
|0 |1 |0 |0 |
|0 |1 |1 |1 |
|1 |0 |0 |0 |
|1 |0 |1 |1 |
|1 |1 |0 |1 |
|1 |1 |1 |1 |

Nous nous rendons compte que chaque registre a une probabilité de 75% que sa sortie soit la même que la sortie de la fonction de combinaison du LFSR.

Nous allons donc appliquer une attaque par corrélation pour retrouver l'état initial de chaque registre.
