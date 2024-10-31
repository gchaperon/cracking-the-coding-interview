# Ants on a Triangle

The ants collide if they walk in different directions. Put otherwise, the only
time they _don't_ collide is when they all walk in the same direction.

This can either be clockwise of counter-clockwise. From this obsevation we get
the formula for the probability of collition.

1. P(collition) = 1 - P(no collition)
2. P(no collition) = P(all clockwise) + P(all counter-clockwise)
3. P(no collition) = 1/2 ^ n + 1/2 ^ n = 2 * 1/2 ^ n = 1/2 ^ (n - 1)
4. Therefore P(collition) = 1 - 1/2 ^ (n - 1)
