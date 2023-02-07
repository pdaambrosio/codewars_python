import uuid

def generate_name() -> str:
    """
    It generates a random string of 6 characters
    :return: A string of 6 characters
    """
    return str(uuid.uuid4())[:6]


def main() -> None:
    """
    Test function
    :return: None
    """
    print(generate_name())
    print(generate_name())
    print(generate_name())
    print(generate_name())
    

if __name__ == "__main__":
    main()
