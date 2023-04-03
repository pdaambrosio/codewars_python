def reverse_words(text: str) -> str:
    """
    "Join the reversed words in the text, separated by spaces."
    
    The function is a bit more complicated than that, but that's the gist of it
    
    :param text: str - the string to reverse
    :type text: str
    :return: A string of the words in the text in reverse order.
    """
    return ' '.join(word[::-1] for word in text.split(' '))


def main() -> None:
    print(reverse_words("This is an example!"))
    print(reverse_words("double  spaces"))
    
    
if __name__ == '__main__':
    main()
