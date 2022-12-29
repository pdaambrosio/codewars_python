def split_the_bill(group: dict) -> dict:
    """
    It takes a dictionary of people and their expenses, and returns a dictionary of people and the
    amount they should pay or be paid
    
    :param group: a dict with the names of the people in the group as keys and the amount they owe as
    values
    :type group: dict
    :return: A dictionary with the amount each person should pay.
    """
    total: int = sum(group.values())
    return {k: round(v - total / len(group), 2) for k, v in group.items()}


def main() -> None:
    """Main function"""
    group = {"A": 20, "B": 15, "C": 10}
    print(split_the_bill(group))  # {'A': 5.0, 'B': 0.0, 'C': -5.0}
    group = {"A": 40, "B": 25, "X": 10}
    print(split_the_bill(group))  # {'A': 15.0, 'B': 0.0, 'X': -15.0}


if __name__ == '__main__':
    main()
