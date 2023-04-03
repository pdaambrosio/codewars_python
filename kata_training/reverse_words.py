def reverse_words(text: str) -> str:
    return ' '.join(word[::-1] for word in text.split(' '))


def main() -> None:
    print(reverse_words("This is an example!"))
    print(reverse_words("double  spaces"))
    
    
if __name__ == '__main__':
    main()
