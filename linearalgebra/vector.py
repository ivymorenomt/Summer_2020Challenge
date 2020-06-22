from math import sqrt
from decimal import Decimal, getcontext

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def plus(self, v):
        new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
        return (f'Add Coordinates {Vector(new_coordinates)}')

    def minus(self, v):
        new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
        return (f'Subtract Coordinates {Vector(new_coordinates)}')

    def times_scalar(self, c):
        new_coordinates = [c*x for x in self.coordinates]
        return Vector(new_coordinates)

    def dot_product(self, v):
        return sum([x*y for x, y in zip(self.coordinates, v.coordinates)])

    def magnitude(self):
        coordinates_squared = [x ** 2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalize(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(1. / magnitude)

        except ZeroDivisionError:
            raise Exception('Cannot normalize the zero vector')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

print('Vector Operations:')
v = Vector([8.218, -9.341])
w = Vector([-1.129, 2.111])
print(v.plus(w))

print('Magnitude:')
vm1 = Vector([-0.221, 7.437])
print(vm1.magnitude())
vm2 = Vector([8.813, -1.331, -6.247])
print(vm2.magnitude())
print('Normalize')
n1 = Vector([5.581, -2.136])
print(n1.normalize())
n2 = Vector([1.996, 3.108, -4.554])
print(n2.normalize())

print('Dot Product')
d1 = Vector([7.887, 4.138])
w1 = Vector([-8.802, 6.776])
print()

