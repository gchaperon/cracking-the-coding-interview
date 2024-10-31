# The Heavy Pill

1. Put the bottles in a line
2. Make a pile of pills, taking one from the first bottle, two, from the
   second, etc. up to twenty from the last bottle.
3. Weigh the pile of pills.
4. The index of the bottle with the heavy pills is the wight of the pile minus
   two hundred and ten, times ten.

If all pills were equal, the total weigh of the pile would be two hundred and
ten, i.e. sum(1..20). This pile will be heavier, because some pills are heaver
that one gram. Now depending on how much heavier the pile is, we can derive the
position of the heavy bottle. If the total weigh is just 0.1 grams over the
base weigh, we know there is just one pill heavier in the pile, and given how
we've constructed the pile we can derive that the first bottle contains heavier
pills.

Given this method, if we multiply by ten the extra weight over the base weight,
we can get the index of the bottle with heavier pills.
