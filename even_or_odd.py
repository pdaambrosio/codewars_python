"""
Function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
:param number: integer
:return: "Even" or "Odd"
"""
def even_or_odd(number: int) -> str:
    if number % 2 == 0:
        return "Even"
    return "Odd"


def main() -> None:
    print(even_or_odd(2))
    print(even_or_odd(0))
    print(even_or_odd(7))
    print(even_or_odd(1))
    print(even_or_odd(-1))
    print(even_or_odd(-2))
