def tribonacci(signature: list, n: int) -> list:
    """
    Calculate the first n elements of the tribonacci sequence.
    keyword arguments:
    signature -- first three elements of the sequence
    n -- number of elements to calculate
    Returns: list of first n elements of the tribonacci sequence
    """
    result: list = signature[:n]
    for _ in range(n - 3):
        result.append(sum(result[-3:]))
    return result
    

def main() -> None:
    print(tribonacci([1, 1, 1], 10)) # [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
    print(tribonacci([0, 0, 1], 10)) # [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]
    print(tribonacci([0, 1, 1], 10)) # [0, 1, 1, 2, 4, 7, 13, 24, 44, 81]
    print(tribonacci([1, 0, 0], 10)) # [1, 0, 0, 1, 1, 2, 4, 7, 13, 24]
    print(tribonacci([0.5, 0.5, 0.5], 30)) # [0.5, 0.5, 0.5, 1.5, 2.5, 4.5, 8.5, 15.5, 28.5, 52.5, 96.5, 177.5, 326.5, 600.5, 1104.5, 2031.5, 3736.5, 6872.5, 12640.5, 23249.5, 42762.5, 78652.5, 144664.5, 266079.5, 489396.5, 900140.5, 1655616.5, 3045153.5, 5600910.5, 10301680.5]


if __name__ == '__main__':
    main()
