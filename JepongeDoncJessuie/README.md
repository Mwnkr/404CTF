# J'éponge donc j'essuie
## Category
Crypto
## Difficulty
Medium
## Statement
While scuba diving with a friend penguin, I came across a rather reserved but very friendly animal! So I decided to create my own hash algorithm. I challenge you to break it.

## Resources

[challenge.py](challenge.py)

## Author
**acmo0**

# Solution Idea

The vulnerability here lies in the formatting at the beginning of the hash algorithm, which depends on the length of the input string, and in the `absorb` function. Indeed, we realize that by adding the correct number of 0s at the beginning of the hash, as well as the string "b'0x10'" at the beginning and end of the plaintext, we "cancel" the `absorb` function until we end up with the same states as the original plaintext. This will produce the same hash.
