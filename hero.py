"""
Function that takes the number of bullets and the number of dragons and returns True
if there are enough bullets to kill all the dragons, False otherwise.

:param bullets: number of bullets
:param dragons: number of dragons
:return: True if there are enough bullets to kill all the dragons, False otherwise.
"""
def hero(bullets: int, dragrons: int) -> bool:
    return bullets/2 >= dragrons


def main() -> None:
    print(hero(10, 5))
    print(hero(7, 4))
    print(hero(4, 5))
    print(hero(100, 40))
    print(hero(1500, 751))
    print(hero(0, 1))


if __name__ == '__main__':
    main()