from __future__ import annotations

class Person:
    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self, other: str) -> str:
        return f"Hello {other}, my name is {self.name}"


def main() -> None:
    jack: Person = Person("Jack")
    jill: Person = Person("Jill")
    print(jack.greet("Jill"))  # Hello Jill, my name is Jack
    print(jack.greet("Mary"))  # Hello Mary, my name is Jack
    print(jill.greet("Jack"))  # Hello Jack, my name is Jill
    print(jill.name)           # Jill


if __name__ == "__main__":
     main()
