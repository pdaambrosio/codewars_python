def filter_list(l: list) -> list:
    """
    Return a new list with the strings filtered out.
    keyword arguments:
    l -- list of numbers and strings
    Returns: list of numbers
    """
    return [i for i in l if type(i) == int]


def main() -> None:
    print(filter_list([1, 2, 'a', 'b']))  # [1, 2]
    print(filter_list([1, 'a', 'b', 0, 15]))  # [1, 0, 15]
    print(filter_list([1, 2, 'aasf', '1', '123', 123]))  # [1, 2, 123]
    

if __name__ == '__main__':
    main()
