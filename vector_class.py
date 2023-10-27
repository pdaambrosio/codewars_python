from __future__ import annotations

class Vector:
    # "A Vector is a list of numbers."
    # 
    # The first thing we do is define the constructor. The constructor is a special method that is called
    # when we create a new instance of the class. In this case, we create a new instance of the class by
    # calling `Vector([1, 2, 3])`. The constructor takes a list of numbers as an argument and assigns it
    # to the `values` attribute

    def __init__(self, values: list) -> None:
        self.values = values

    def __str__(self) -> str:
        string: str = '('
        for i in range(len(self.values)):
            string += str(self.values[i])
            if i != len(self.values) - 1:
                string += ','
            else:
                string += ')'
        return string

    def equals(self, other: any) -> bool:
        return self.values == other.values

    def add(self, other: any) -> Vector:
        assert len(self.values) == len(other.values)
        result: Vector = Vector([x + y for x, y in zip(self.values, other.values)])
        return result

    def subtract(self, other: any) -> Vector:
        assert len(self.values) == len(other.values)
        result: Vector = Vector([x - y for x, y in zip(self.values, other.values)])
        return result

    def dot(self, other: any) -> int:
        result: Vector = Vector([x * y for x, y in zip(self.values, other.values)])
        return sum(result.values)

    def norm(self) -> float:
        result: int = 0
        for i in self.values:
            result += i ** 2
        return result ** .5


def main() -> None:
    a: Vector = Vector([1, 2, 3])
    b: Vector = Vector([3, 4, 5])
    c: Vector = Vector([1, 2])
    d: Vector = Vector([3, 4])
    print(c.add(d).equals(c))
    print(a.add(b))
    print(a.subtract(b))
    print(a.dot(b))
    print(a.norm())
    print(a.add(c))


if __name__ == '__main__':
    main()
