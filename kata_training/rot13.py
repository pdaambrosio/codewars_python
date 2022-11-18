def rot13(message: str) -> str:
    """
    It takes a string, and for each character in the string, if it's a letter, it rotates it by 13
    characters, and if it's not a letter, it leaves it alone
    
    :param message: str
    :type message: str
    :return: The result of the rot13 function is a string.
    """
    result: str = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            result += char
    return result


def main() -> None:
    """Run sample rot13 functions. Do not import."""
    print(rot13("test"))
    print(rot13("Test"))
    print(rot13("Codewars"))
    print(rot13("Ruby is cool!"))
    print(rot13("10+2 is twelve."))
    

if __name__ == '__main__':
    main()
