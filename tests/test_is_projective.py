import networkx as nx

from nxdeps import is_projective


def test_deptree():
    # Figure 1 of (Nivre, 2008)
    G = nx.DiGraph([(5, 1), (1, 2), (0, 3), (5, 4), (3, 5), (3, 6), (6, 7), (0, 8)])
    assert not is_projective(G)

    # Figure 2 of (Nivre, 2008)
    G = nx.DiGraph([(2, 1), (3, 2), (0, 3), (5, 4), (3, 5), (5, 6), (8, 7), (6, 8), (3, 9)])
    assert is_projective(G)


def test_depgraph():
    # Figure 1 of (Kuhlmann and Johnson, 2015)
    G = nx.DiGraph([(1, 2), (5, 2), (3, 4), (4, 5), (5, 9), (5, 7), (6, 7), (9, 7), (9, 10)])
    assert is_projective(G)

    # Figure 1 of (Kuhlmann and Johnson, 2015) with a root added
    G = nx.DiGraph([(1, 2), (5, 2), (3, 4), (4, 5), (5, 9), (5, 7), (6, 7), (9, 7), (9, 10),
                    (0, 1), (0, 3), (0, 6), (0, 8)])
    assert not is_projective(G)
