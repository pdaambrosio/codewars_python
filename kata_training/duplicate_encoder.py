def duplicate_encode(word: str) -> str:
    """
    "For each character in the word, if it appears more than once, add a ')', otherwise add a '('."
    
    The first line of the function converts the word to lowercase
    
    :param word: str
    :type word: str
    :return: A string of parentheses.
    """
    word = word.lower()
    return ''.join([')' if word.count(c) > 1 else '(' for c in word])


def main() -> None:
    """Run sample duplicate_encode functions. Do not import."""
    print(duplicate_encode('din')) # (((
    print(duplicate_encode('recede')) # ()()()
    print(duplicate_encode('Success')) # )())())
    print(duplicate_encode('(( @')) # ))((
    

if __name__ == '__main__':
    main()
