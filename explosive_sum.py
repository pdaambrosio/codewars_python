def exp_sum(n: int) -> int:
    """
    "For each number i from 1 to n, add i to each of the numbers from i to n."
    
    The first line of the function is a guard clause that returns 0 if n is negative
    
    :param n: int
    :type n: int
    :return: The number of ways to write n as a sum of positive integers.
    """
    if n < 0:
        return 0
    result: list[int] = [1] + [0] * n
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            result[j] += result[j - i]
    return result[-1]


def main() -> None:
    """
    It returns the number of ways to sum up to n using positive integers
    """
    print(exp_sum(1))  # 1
    print(exp_sum(2))  # 2
    print(exp_sum(3))  # 3
    print(exp_sum(4))  # 5
    print(exp_sum(5))  # 7


if __name__ == "__main__":
    main()