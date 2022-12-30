# > A `Quark` is a particle with a `color`, a `flavor`, and a `baryon_number`
class Quark:
    def __init__(self, color: str, flavor: str):
        self.color = color
        self.flavor = flavor
        self.baryon_number = 1/3
        
    def interact(self, other: 'Quark'):
        self.color, other.color = other.color, self.color


def main() -> None:
    """
    It tests Quark class
    """
    q1 = Quark("red", "up")
    q2 = Quark("blue", "strange")
    print(q1.color)
    print(q1.flavor)
    print(q1.baryon_number)
    q2.interact(q1)
    print(q1.color)
    print(q2.color)


if __name__ == '__main__':
    main()
