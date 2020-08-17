from app import Triangle
from math import degrees
from math import acos
from math import ceil
from custom_errors import NoneExistentTriangleException


def test_triangle_coordinates(edges):
    """Coordinates Input checking"""
    t = Triangle(edges[0], edges[1], edges[2])
    try:
        assert t.edge_1 == edges[0]
    except NoneExistentTriangleException:
        print('Edge coordinates are differ from the reference')

    try:
        assert t.edge_2 == edges[1]
    except NoneExistentTriangleException:
        print('Edge coordinates are differ from the reference')

    try:
        assert t.edge_3 == edges[2]
    except NoneExistentTriangleException:
        print('Edge coordinates are differ from the reference')


def test_triangle_angles(edges):
    """Checking that the sum of angles is equal to 180 degrees"""
    t = Triangle(edges[0], edges[1], edges[2])
    angle_a = degrees(acos(((t.side_b ** 2) + (t.side_c ** 2) - (t.side_a ** 2)) / ((t.side_b * t.side_c) * 2)))
    angle_b = degrees(acos(((t.side_a ** 2) + (t.side_c ** 2) - (t.side_b ** 2)) / ((t.side_a * t.side_c) * 2)))
    angle_c = degrees(acos(((t.side_a ** 2) + (t.side_b ** 2) - (t.side_c ** 2)) / ((t.side_a * t.side_b) * 2)))
    assert ceil(angle_a + angle_b + angle_c) == 180









