# Le petit bain
## Catégorie
Crypto
## Difficulté
Facile
## Énoncé

Malheureusement, votre revanche contre votre rival s'est soldée par une défaite. En toute bonne foi, vous le suspectez d'avoir triché. Piqué au vif, vous fouillez son casier et tombez sur un étrange mot. À vous de le déchiffrer.

## Données :
[challenge.py](challenge.py)

## Auteurs
**acmo0** et **Little_endi4ane**

# Idée de la solution

La résolution de ce problème repose sur deux observations clés :

1. **Structure cyclique :** La permutation utilisée est d'ordre 6 et agit sur le code par blocs de 6 caractères. Nous sommes donc face à 6 chiffrements affines successifs.

2. **Composition affine :** Un chiffrement affine appliqué à un autre chiffrement affine reste un chiffrement affine.

**Exploitation du flag partiel :**

Le début du flag connu ("404CTF{tHe_c") nous fournit 12 caractères, soit deux blocs de 6.  Ces deux blocs nous donnent deux équations suffisantes pour déterminer les 6 couples (a, b) nécessaires au déchiffrement.

**En résumé :**

La connaissance du début du flag permet de résoudre le système d'équations correspondant aux deux premiers chiffrements. Une fois ces couples (a, b) trouvés, nous pouvons déchiffrer l'intégralité du message.
