from math import sqrt


class NoneExistentTriangleError(ValueError):
    pass


class Triangle:
    def __init__(self, edge_1, edge_2, edge_3):
        """Triangle edges and sides"""
        self.edge_1 = edge_1
        self.edge_2 = edge_2
        self.edge_3 = edge_3
        self.side_a = sqrt(((edge_2['x'] - edge_1['x']) ** 2) + ((edge_2['y'] - edge_1['y']) ** 2))
        self.side_b = sqrt(((edge_3['x'] - edge_2['x']) ** 2) + ((edge_3['y'] - edge_2['y']) ** 2))
        self.side_c = sqrt(((edge_3['x'] - edge_1['x']) ** 2) + ((edge_3['y'] - edge_1['y']) ** 2))

    def __repr__(self):
        """Triangle parameters"""
        return 'Edge 1 is equal to {}\nEdge 2 is equal to {}\nEdge 3 is equal to {}\n' \
               'Side "A" is equal to {}\nSide "B" is equal to {}\nSide "C" is equal to {}'\
            .format(self.edge_1, self.edge_2, self.edge_3,
                    round(self.side_a, 2), round(self.side_b, 2), round(self.side_c, 2))

    def check(self):
        """Triangle existence check"""
        try:
            assert self.side_a + self.side_b > self.side_c \
                   and self.side_b + self.side_c > self.side_a \
                   and self.side_a + self.side_c > self.side_b
            print('Is True')
            return True

        except NoneExistentTriangleError:
            print('Triangle is non-existing')
            return False

        finally:
            print('Triangle is checked')

    def perimeter(self):
        p = self.side_a + self.side_b + self.side_c
        print('The perimeter is equal to {}'.format(round(p, 2)))
        return p

    def area(self):
        s = self.perimeter() / 2
        a = sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
        print('Triangle area is equal to {}'.format(round(a, 2)))
        return a


print(Triangle({'x': 0, 'y': 0}, {'x': 8, 'y': 7}, {'x': 8, 'y': 0}).area())
print(Triangle({'x': 0, 'y': 0}, {'x': 8, 'y': 7}, {'x': 8, 'y': 0}).__repr__())
