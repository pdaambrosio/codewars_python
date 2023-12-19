def high_and_low(numbers: str) -> str:
    """
    The function "high_and_low" takes a string of numbers, splits it into a list, converts each element
    to an integer, and returns the maximum and minimum values as a string.
    
    :param numbers: A string containing a series of numbers separated by spaces
    :type numbers: str
    :return: The function `high_and_low` returns a string that contains the highest and lowest numbers
    from the input string of numbers. The highest number is followed by a space and then the lowest
    number.
    """
    numbers = numbers.split()
    numbers = [int(i) for i in numbers]
    return str(max(numbers)) + " " + str(min(numbers))


def main() -> None:
    print(high_and_low("1 2 3 4 5"))  # return "5 1"
    print(high_and_low("1 2 -3 4 5"))  # return "5 -3"
    print(high_and_low("1 9 3 4 -5"))  # return "9 -5"
    print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))  # return "42 -9"


if __name__ == "__main__":
    main()

## best solution of the kata:
# def high_and_low(numbers):
#   numbers = [int(c) for c in numbers.split(' ')]
#   return f"{max(numbers)} {min(numbers)}"