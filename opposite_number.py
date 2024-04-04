def opposite_number(number: int) -> int:
    """
    The `opposite_number` function returns the negative of the input number.
    
    :param number: The `opposite_number` function takes an integer as input and returns its opposite
    (negation)
    :type number: int
    :return: The function `opposite_number` returns the opposite of the input number.
    """
    return -number


def main():
    print(opposite_number(1))  # 1
    print(opposite_number(-1))  # -1
    print(opposite_number(14))  # -14


if __name__ == '__main__':
    main()
