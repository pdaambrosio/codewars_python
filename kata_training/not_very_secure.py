def alphanumeric(password: str) -> bool:
    """
    It returns True if the password is alphanumeric, and False otherwise
    
    :param password: str
    :type password: str
    :return: True or False
    """
    return password.isalnum()


def main() -> None:
    print(alphanumeric("Mazinkaiser"))
    print(alphanumeric("hello world_"))
    print(alphanumeric("PassW0rd"))
    print(alphanumeric("     "))
    

if __name__ == "__main__":
    main()
