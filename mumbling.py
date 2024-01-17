def accum(s: str) -> str:
    """
    The `accum` function takes a string `s` and returns a modified version of the string where each
    character is repeated a number of times equal to its index position in the string, with each
    repetition capitalized and separated by hyphens.
    
    :param s: The parameter `s` is a string that represents the input string
    :type s: str
    :return: The function `accum` returns a string where each character in the input string `s` is
    repeated a number of times equal to its index position in `s`, with each repetition capitalized. The
    repeated characters are then joined together with hyphens.
    """
    return '-'.join([(s[i] * (i+1)).capitalize() for i in range(len(s))])


def main():
    print(accum("abcd"))
    print(accum("RqaEzty"))
    print(accum("cwAt"))
    
    
if __name__ == "__main__":
    main()

# Path: codewars_python/mumbling.py
# The best solution I found on Codewars:
# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))