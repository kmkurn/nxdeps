import networkx as nx

from nxdeps import get_projective_edges


def test_deptree():
    # Figure 1 of (Nivre, 2008)
    proj_edges = [(0, 8), (1, 2), (3, 5), (5, 4), (6, 7)]
    nonproj_edges = [(5, 1), (0, 3), (3, 6)]
    G = nx.DiGraph(proj_edges + nonproj_edges)
    assert set(get_projective_edges(G)) == set(proj_edges)

    # Figure 2 of (Nivre, 2008)
    G = nx.DiGraph([(2, 1), (3, 2), (0, 3), (5, 4), (3, 5), (5, 6), (8, 7), (6, 8), (3, 9)])
    assert set(get_projective_edges(G)) == set(G.edges)


def test_depgraph():
    # Figure 1 of (Kuhlmann and Johnson, 2015)
    G = nx.DiGraph([(1, 2), (5, 2), (3, 4), (4, 5), (5, 9), (5, 7), (6, 7), (9, 7), (9, 10)])
    assert set(get_projective_edges(G)) == set(G.edges)

    # Figure 1 of (Kuhlmann and Johnson, 2015) with a root added
    proj_edges = [(1, 2), (3, 4), (4, 5), (6, 7), (9, 10), (0, 1)]
    nonproj_edges = [(0, 3), (0, 6), (0, 8), (5, 2), (5, 7), (5, 9), (9, 7)]
    G = nx.DiGraph(proj_edges + nonproj_edges)
    assert set(get_projective_edges(G)) == set(proj_edges)
