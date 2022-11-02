def add_binary(a: int, b: int) -> str:
    """
    Add two numbers and return the result as a binary string.
    keyword arguments:
    a -- first number
    b -- second number
    sum_num -- sum of a and b
    Returns: sum of a and b as a binary string
    """
    sum_numbers: int = a + b
    return bin(sum_numbers).replace("0b", "")


def main() -> None:
    print(add_binary(1, 1))
    print(add_binary(0, 1))
    print(add_binary(1, 0))
    print(add_binary(2, 2))
    print(add_binary(51, 12))
    print(add_binary(0,2174483647))
    

if __name__ == "__main__":
    main()
