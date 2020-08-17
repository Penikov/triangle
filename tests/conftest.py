import pytest


@pytest.fixture()
def edges():
    edge_1 = {'x': 1, 'y': -5}
    edge_2 = {'x': 8, 'y': 7}
    edge_3 = {'x': 0, 'y': 5}
    return edge_1, edge_2, edge_3
