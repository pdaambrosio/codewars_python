def solution(n: int) -> str:
    """
    It converts an integer to a roman numeral.
    
    :param n: int = the number to be converted to a roman numeral
    :type n: int
    :return: The roman numeral representation of the given integer.
    """
    romans = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    result: str = ''
    for key in romans:
        while n >= key:
            result += romans[key]
            n -= key
    return result


def main() -> None:
    print(solution(1))  # I
    print(solution(4))  # IV
    print(solution(6))  # VI
    print(solution(14))  # XIV
    print(solution(21))  # XXI
    print(solution(89))  # LXXXIX
    

if __name__ == '__main__':
    main()