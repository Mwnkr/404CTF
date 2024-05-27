# Poor Random Number Generator 2/2
## Category
Crypto
## Difficulty
Medium
## Statement

Congratulations! It's true that my previous PRNG wasn't great... So I patched it! I have re-encrypted a new PNG file and this time I tried to limit the leaked plaintext data.

Good luck!

## Resources

[challenge.zip](challenge.zip)

## Author
**acmo0**

# Solution Idea

We are dealing with an LFSR combined with 3 registers of size 19. We also have 35 bytes of known plaintext. We use this to obtain the start of the keystream from the combined LFSR.

By making the truth table:

| x1 | x2 | x3 | f(x) |
|----|----|----|------|
| 0  | 0  | 0  | 0    |
| 0  | 0  | 1  | 0    |
| 0  | 1  | 0  | 0    |
| 0  | 1  | 1  | 1    |
| 1  | 0  | 0  | 0    |
| 1  | 0  | 1  | 1    |
| 1  | 1  | 0  | 1    |
| 1  | 1  | 1  | 1    |

We realize that each register has a 75% probability that its output is the same as the output of the LFSR combination function.

We will then apply a correlation attack to find the initial state of each register.
