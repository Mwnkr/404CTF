# La Seine
## Category
Crypto
## Difficulty
Hard

## Statement

The apnea competition is about to begin, the water is a bit murky but the previous challenges have shaped your determination. Just as you are about to enter the water, your coach sternly orders: "When you put your head underwater, do not come up until you have solved this problem, good luck to you." You take a deep breath and dive headfirst into this problem:

## Resources

[LaSeine.py](LaSeine.py)

## Author
**GMO_Goat**

# Solution Idea

This challenge is somewhat unique, so I think the best approach would be to contact me directly on Discord @mairwane to discuss it.

The goal here is to find `a` and `b`.

First, I started writing down the first iterations of `xn` and `yn` by hand. I recognized the values from Pascal's triangle, which often correlates with the binomial theorem.

Indeed, we find two formulas for the even and odd cases. Since this was just a conjecture at this stage, a proof by induction quickly confirmed its validity.

Since we have access to the data for an even iteration, we will use it cleverly with modular arithmetic to find a value of `a^2 + b^2`.

From there, I used dCode and the equations I had calculated to obtain possible values for `a` and `b`.

Next, we brute force until we obtain the FLAG.
