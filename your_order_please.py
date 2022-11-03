def order(sentence: str) -> str:
    """
    Sort the words in a sentence by the number in the word.
    keyword arguments:
    sentence -- sentence to be sorted
    words -- list of words in sentence
    returns: sentence with words sorted by number in word
    """
    words = sentence.split()
    return ' '.join(sorted(words, key=lambda w: int(''.join(filter(str.isdigit, w)))))


def main() -> None:
    print(order(""))
    print(order("is2 Thi1s T4est 3a"))
    print(order("4of Fo1r pe6ople g3ood th5e the2"))
    

if __name__ == '__main__':
    main()
