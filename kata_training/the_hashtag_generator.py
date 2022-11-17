from typing import Union


def generate_hashtag(s: str) -> Union[str, bool]:
    """
    If the length of the string is 0 or greater than 140, return False, otherwise return the string with
    a hashtag in front of it and each word capitalized
    
    :param s: str - the string to be converted to a hashtag
    :type s: str
    :return: A string with the hashtag symbol and the words in the string capitalized.
    """
    if len(s) == 0 or len(s) > 140:
        return False
    else:
        return '#' + ''.join([word.capitalize() for word in s.split()])


def main() -> None:
    print(generate_hashtag('hello world')) # '#HelloWorld'
    print(generate_hashtag('')) # False
    print(generate_hashtag(' ' * 200)) # False
    print(generate_hashtag('Do We have A Hashtag')) # '#DoWeHaveAHashtag'
    print(generate_hashtag('c n i')) # '#CNI'


if __name__ == '__main__':
    main()
    