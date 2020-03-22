"""Networkx extension to work with dependency graphs for NLP."""

__version__ = '0.0.0'

import networkx as nx


def is_projective(G: nx.DiGraph) -> bool:
    """Check if a directed graph is projective/non-crossing.

    A directed graph is projective/non-crossing with respect to some node ordering iff
    the arcs can be drawn without any crossing on the upper half-plane formed by placing
    the nodes along a line according to the ordering.

    Args:
        G: Directed graph to check.

    Returns:
        Whether the graph is projective.
    """
    for head, depd in G.edges:
        left, right = min(head, depd), max(head, depd)
        for head2, depd2 in G.edges:
            if head == head2 and depd == depd2:  # identical arc
                continue
            left2, right2 = min(head2, depd2), max(head2, depd2)
            if left < left2 < right < right2 or left2 < left < right2 < right:
                return False
    return True
