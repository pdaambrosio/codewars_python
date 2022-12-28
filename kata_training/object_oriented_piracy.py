# A ship is worth it if its draft minus 1.5 times its crew is greater than 20.
class Ship:
    def __init__(self, draft: int, crew: int):
        self.draft = draft
        self.crew = crew
        
    def is_worth_it(self) -> bool:
        return self.draft - (self.crew * 1.5) > 20
    

def main() -> None:
    """
    It returns True if the ship's capacity is greater than its cost, and False otherwise
    """
    titanic = Ship(50, 5)
    print(titanic.is_worth_it())  # True
    titanic = Ship(10, 15)
    print(titanic.is_worth_it())  # False
    titanic = Ship(20, 20)
    print(titanic.is_worth_it())  # False
    titanic = Ship(2, 1)
    print(titanic.is_worth_it())  # False
    

if __name__ == "__main__":
    main()
