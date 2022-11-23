def narcissistic(value: int) -> bool:
    """
    Determine if a number is narcissistic.
    keyword arguments:
    value -- number to check
    str_value -- string version of value
    count -- number of digits in value
    Returns: True if value is narcissistic, False otherwise
    """
    str_value: str = str(value)
    count: int = len(str_value)
    return sum(int(i) ** count for i in str_value) == int(value)


def main() -> None:
    print(narcissistic(7)) # True
    print(narcissistic(371)) # True
    print(narcissistic(122)) # False
    print(narcissistic(4887)) # False
    

if __name__ == '__main__':
    main()
