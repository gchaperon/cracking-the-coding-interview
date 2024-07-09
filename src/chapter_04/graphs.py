from __future__ import annotations

import dataclasses
import typing as tp

T = tp.TypeVar("T")


class Graph(dict[T, list[T]], tp.Generic[T]):
    pass


@dataclasses.dataclass
class Node(tp.Generic[T]):
    value: T
    left: Node[T] | None = None
    right: Node[T] | None = None
