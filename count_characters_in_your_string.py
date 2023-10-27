def count(string: str) -> dict:
    """
    It takes a string and returns a dictionary where the keys are the unique characters in the string
    and the values are the number of times that character appears in the string
    
    :param string: str
    :type string: str
    :return: A dictionary with the unique characters in the string as keys and the number of times they
    appear in the string as values.
    """
    return {i: string.count(i) for i in set(string)}


def main() -> None:
    print(count('aba'))  # {'a': 2, 'b': 1}
    print(count(''))  # {}
    

if __name__ == '__main__':
    main()
