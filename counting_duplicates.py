def duplicate_count(text: str) -> int:
    """
    Count the duplicates in a string.
    keyword arguments:
    text -- string to count duplicates in
    Return: number of duplicates in text
    """
    text = text.lower()
    return len([x for x in set(text) if text.count(x) > 1])


def main() -> None:
    """Main function"""
    print(duplicate_count("abcde"))  # 0
    print(duplicate_count("aabbcde"))  # 2
    print(duplicate_count("aabBcde"))  # 2
    print(duplicate_count("Indivisibility"))  # 1
    print(duplicate_count("Indivisibilities"))  # 2
    print(duplicate_count("aA11"))  # 2
    print(duplicate_count("ABBA"))  # 2
    
    
if __name__ == "__main__":
    main()
