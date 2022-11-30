def rot13(message: str) -> str:
    """
    It takes a string, and for each character in the string, if it's a letter, it shifts it 13
    characters forward in the alphabet, wrapping around if necessary, and if it's not a letter, it
    leaves it alone
    
    :param message: str
    :type message: str
    :return: the result of the rot13 function.
    """
    result: str = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') - 13) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') - 13) % 26 + ord('A'))
        else:
            result += char
    return result


def main() -> None:
    print(rot13("EBG13 rknzcyr")) # ROT13 example
    print(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf.")) # Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.    
    print(rot13("123")) # 123
    print(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)")) # This is actually the first thing I ever wrote. Thanks for reviewing it! :)
    print(rot13("@[`{")) # @[`{


if __name__ == '__main__':
    main()
