import pytest

from graphs import Graph


def build_order(projects: set[str], dependencies: set[tuple[str, str]]) -> list[str]:
    graph = make_graph(projects, dependencies)
    sorted: list[str] = []
    seen = set()
    compiled = set()

    def compile(node: str) -> None:
        if node in compiled:
            return
        if node in seen:
            raise ValueError("Graph contains cycles")

        seen.add(node)
        for child in graph[node]:
            compile(child)

        sorted.append(node)
        compiled.add(node)

    heads = [
        node
        for node in graph
        if all(node not in graph[project] for project in projects)
    ]
    if not heads:
        raise ValueError("Graph contains cycles")
    for node in heads:
        compile(node)
    return sorted


def is_topological_order(dependents: list[str], dependencies: Graph[str]) -> bool:
    built: set[str] = set()
    for dependent in dependents:
        if not dependencies[dependent] <= built:
            return False
        built.add(dependent)
    return True


def make_graph(projects: set[str], dependencies: set[tuple[str, str]]) -> Graph[str]:
    graph = Graph({project: set() for project in projects})
    for dependency, dependent in dependencies:
        graph[dependent].add(dependency)
    return graph


# ******************** Tests ********************
@pytest.fixture(name="projects")
def fixture_projects() -> set[str]:
    return set("abcdef")


@pytest.fixture(name="dependencies")
def fixture_dependencies() -> set[tuple[str, str]]:
    return {("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")}


def test_make_graph(projects: set[str], dependencies: set[tuple[str, str]]) -> None:
    assert make_graph(projects, dependencies) == Graph(
        a={"f"}, b={"f"}, c={"d"}, d={"b", "a"}, e=set(), f=set()
    )


def test_is_topological_order(
    projects: set[str], dependencies: set[tuple[str, str]]
) -> None:
    graph = make_graph(projects, dependencies)
    assert is_topological_order(list("feabdc"), graph)


def test_build_order(projects: set[str], dependencies: set[tuple[str, str]]) -> None:
    graph = make_graph(projects, dependencies)
    assert is_topological_order(build_order(projects, dependencies), graph)


def test_build_order_sanity_check() -> None:
    projects = set("abc")
    dependencies: set[tuple[str, str]] = set()
    graph = make_graph(projects, dependencies)
    order = build_order(projects, dependencies)
    assert set(order) == projects
    assert is_topological_order(order, graph)

    projects = set("abc")
    dependencies = {("a", "b")}
    graph = make_graph(projects, dependencies)
    order = build_order(projects, dependencies)
    assert set(order) == projects
    assert is_topological_order(order, graph)

    projects = set("abc")
    dependencies = {("a", "b"), ("b", "c")}
    graph = make_graph(projects, dependencies)
    order = build_order(projects, dependencies)
    assert set(order) == projects
    assert is_topological_order(order, graph)


def test_build_order_cycles() -> None:
    with pytest.raises(ValueError):
        projects = set("ab")
        dependencies = {("a", "b"), ("b", "a")}
        graph = make_graph(projects, dependencies)
        order = build_order(projects, dependencies)
        assert is_topological_order(order, graph)

    # NOTE: Without cycle detection this hangs
    with pytest.raises(ValueError):
        projects = set("abc")
        dependencies = {("a", "b"), ("b", "a"), ("b", "c")}
        graph = make_graph(projects, dependencies)
        order = build_order(projects, dependencies)
        assert is_topological_order(order, graph)
