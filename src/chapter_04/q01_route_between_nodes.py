import collections

import pytest

import graphs


def reachable(graph: graphs.Graph[str], from_: str, to: str) -> bool:
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
def fixture_graph() -> graphs.Graph[str]:
    # NOTE: See assets/ch04_q01.svg
    return graphs.Graph(
        a={"b", "c"},
        b=set(),
        c=set(),
        d={"e"},
        e={"d", "f", "g"},
        f={"d"},
        g={"e", "f", "h"},
        h={"f"},
    )


def test_reachable(graph: graphs.Graph[str]) -> None:
    assert reachable(graph, "a", "c")
    assert reachable(graph, "d", "h")
    assert reachable(graph, "f", "e")


def test_unreachable(graph: graphs.Graph[str]) -> None:
    assert not reachable(graph, "b", "d")
    assert not reachable(graph, "b", "a")
    assert not reachable(graph, "f", "c")
