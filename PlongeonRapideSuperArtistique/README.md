# Plongeon Rapide Super Artistique !
## Category
Crypto
## Difficulty
Medium
## Statement

You step onto the diving board, the crowd is so excited that the board is trembling. This is the final dive before you get your final score and your ranking in this sport. You jump, the world slows down, and just like in training, you perform the sequence of moves you practiced. Once you surface, none of the judges show a score! A flash hits you, you remember that the score is transmitted via RSA encryption! But after your multiple aerial moves, you only remember your public key and the trajectory you took...

## Resources

[PlongeonRapideSuperArtistique.py](PlongeonRapideSuperArtistique.py)

## Author
**GMO_Goat**

# Solution Idea

We have access to the polynomial N(X) and the value of the RSA key N(r).

It is easy to factor N(X), which we know has two factors P(X) and Q(X) that can be found easily.

Thus, we just need to find r to factor the key N(r) by evaluating P or Q at r.

To do this, we simply need to find a root of the polynomial Z(X) = N(X) - N(r) that suits us. It is easy to find the roots of a polynomial.
