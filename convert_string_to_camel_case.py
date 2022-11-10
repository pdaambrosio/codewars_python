def to_camel_case(text: str) -> str:
    """
    1. Replace all dashes with underscores.
    2. Split the string into a list of words.
    3. Capitalize the first letter of each word.
    4. Join the list of words into a string
    
    :param text: str - the string to convert
    :type text: str
    :return: A string
    """
    result: list[str] = text.replace('-', '_').split('_')
    return result[0] + ''.join([word.capitalize() for word in result[1:]])
    

def main() -> None:
    print(to_camel_case('the_stealth_warrior')) # 'theStealthWarrior'
    print(to_camel_case('The-Stealth-Warrior')) # 'TheStealthWarrior'
    print(to_camel_case('A-B-C')) # 'ABC'
    print(to_camel_case('')) # ''
    
    
if __name__ == '__main__':
    main()
