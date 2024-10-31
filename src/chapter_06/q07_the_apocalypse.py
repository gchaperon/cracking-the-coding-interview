"""The Apocalypse

The ratio will be 1:1
"""

import random
from collections import defaultdict


def simulate(n: int, seed: int) -> float:
    """Simulates n families following the requirement of having one girl.

    Returns the boy-girl ratio after the simulation.
    """
    rng = random.Random(seed)

    counts: dict[str, int] = defaultdict(int)
    for _ in range(n):
        while True:
            child = rng.choice(["boy", "girl"])
            counts[child] += 1
            if child == "girl":
                break
    return counts["boy"] / counts["girl"]


# ******************** Tests ********************


def test_simulate() -> None:
    import pytest

    assert simulate(10_000, 123) == pytest.approx(1.0, rel=0.01)
