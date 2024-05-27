# Le petit bain
## Category
Crypto
## Difficulty
Easy
## Statement

Unfortunately, your rematch against your rival ended in defeat. In all fairness, you suspect he cheated. Stung, you search his locker and find a strange note. It's up to you to decipher it.

## Data:
[challenge.py](challenge.py)

## Authors
**acmo0** and **Little_endi4ane**

# Solution Idea

The solution to this problem relies on two key observations:

1. **Cyclic Structure:** The permutation used has an order of 6 and acts on the code in blocks of 6 characters. Therefore, we are dealing with 6 successive affine ciphers.

2. **Affine Composition:** An affine cipher applied to another affine cipher remains an affine cipher.

**Exploitation of the Partial Flag:**

The known start of the flag ("404CTF{tHe_c") provides us with 12 characters, which makes two blocks of 6. These two blocks give us two equations sufficient to determine the 6 (a, b) pairs necessary for decryption.

**Summary:**

Knowing the beginning of the flag allows us to solve the system of equations corresponding to the first two ciphers. Once these (a, b) pairs are found, we can decrypt the entire message.
