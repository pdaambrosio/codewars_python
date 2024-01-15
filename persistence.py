from functools import reduce

def persistance(n: int) -> int:
    """
    The `persistance` function calculates the multiplicative persistence of a given number.
    
    :param n: The parameter `n` is an integer
    :type n: int
    :return: The function `persistance` returns the number of times the digits of the input number `n`
    need to be multiplied together until a single digit number is obtained.
    """
    count: int = 0
    while n >= 10:
        n = reduce(lambda x, y: x*y, [int(i) for i in str(n)])
        count += 1

    return count


def main():
    print(persistance(39))
    print(persistance(999))
    print(persistance(4))
    

if __name__ == '__main__':
    main()
