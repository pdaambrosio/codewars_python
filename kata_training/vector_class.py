import math


class Vector:
    def __init__(self, *args) -> None:
        self.args = args

    def add(self, other):
        result: Vector = Vector(*[x + y for x, y in zip(*self.args, *other.args)])
        return result.args

    def subtract(self, other):
        result: Vector = Vector(*[x - y for x, y in zip(*self.args, *other.args)])
        return result.args

    def dot(self, other):
        result: Vector = Vector(*[x * y for x, y in zip(*self.args, *other.args)])
        return sum(result.args)

    def norm(self):
        result: int = 0
        for i in self.args:
            for j in i:
                result += j ** 2
        return result ** .5

    def equals(self, other):
        return len(self.args) == len(other.args)


a: Vector = Vector([1, 2, 3])
b: Vector = Vector([3, 4, 5])
c: Vector = Vector([1, 2])
d: Vector = Vector([3, 4])
# print(c.add(d).equals(Vector([4, 6])))
print(a.add(b))
print(a.subtract(b))
print(a.dot(b))
print(a.norm())
print(a.add(c))
