# Plongeon Rapide Super Artistique !
## Catégorie
Crypto
## Difficulté
Moyen
## Énoncé

Vous vous avancez sur le plongeoir, la foule est tellement en liesse que la planche en tremble. C'est le dernier saut avant d'avoir votre note finale et donc votre classement pour ce sport. Vous sautez, le monde se ralentit et, comme à l'entrainement, vous effectuez l'enchaînement de figures que vous avez travaillées. Une fois la tête sortie de l'eau, personne du jury ne montre de note ! Un flash vous frappe, c'est vrai que la note est transmise par chiffrement RSA ! Mais après vos multiples figures aériennes, vous ne vous souvenez que de votre clef publique, et de la trajectoire que vous avez empruntée...

## Ressources

[PlongeonRapideSuperArtistique.py](PlongeonRapideSuperArtistique.py)

## Auteur
**GMO_Goat**

# Idée de la solution

Nous avons accès au polynôme N(X) et à la valeur de la clé RSA N(r).

Il est facile de factoriser N(X), dont on sait qu'il a deux facteurs P(X) et Q(X) que l'on retrouve facilement.

Ainsi, nous devons juste trouver r pour factoriser la clé N(r) en évaluant P ou Q en r.

Pour cela, il suffit de trouver une racine du polynôme Z(X) = N(X)-N(r) qui nous convient. Or, il est facile de trouver les racines d'un polynôme.

