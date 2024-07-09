import collections
import typing as tp

import pytest

Graph: tp.TypeAlias = dict[str, list[str]]


def reachable(graph: Graph, from_: str, to: str) -> bool:
    seen: set[str] = set()
    queue = collections.deque([from_])
    while queue:
        node = queue.popleft()
        seen.add(node)
        if node == to:
            return True
        for neighbour in graph[node]:
            if neighbour not in seen:
                queue.append(neighbour)
    return False


# ******************** Tests ********************
@pytest.fixture(name="graph")
def fixture_graph() -> Graph:
    """Graph depicted in assets/c04_q01_graph.svg"""
    return dict(
        a=["b", "c"],
        b=[],
        c=[],
        d=["e"],
        e=["d", "f", "g"],
        f=["d"],
        g=["e", "f", "h"],
        h=["f"],
    )


def test_reachable(graph: Graph) -> None:
    assert reachable(graph, "a", "c")
    assert reachable(graph, "d", "h")
    assert reachable(graph, "f", "e")


def test_unreachable(graph: Graph) -> None:
    assert not reachable(graph, "b", "d")
    assert not reachable(graph, "b", "a")
    assert not reachable(graph, "f", "c")
