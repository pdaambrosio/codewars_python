def digital_root(n: int) -> int:
    """
    While the sum of the digits of n is greater than 9, keep summing the digits of n.
    
    The function uses a while loop to keep summing the digits of n until the sum is less than or equal
    to 9
    
    :param n: int
    :type n: int
    :return: The digital root of the number.
    """
    while n > 9:
        n = sum(int(i) for i in str(n))
    return n


def main() -> None:
    print(digital_root(16))  # 7
    print(digital_root(942))  # 6
    print(digital_root(132189))  # 6
    print(digital_root(493193))  # 2
    

if __name__ == '__main__':
    main()
