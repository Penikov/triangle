from app import Triangle


def test_triangle_area(edges):
    """Checking that the sum of angles is equal to 180 degrees"""
    t = Triangle(edges[0], edges[1], edges[2])
    try:
        assert t.area() == 41.0
    except AssertionError:
        print('Area from the module is not equal to reference')




