class Student:
    # "A student has a name, fives, tens, and twenties, and can tell you who has the most money."
    # 
    # The first line of the class definition is the class header. It tells Python that we're defining a
    # class called Student
    def __init__(self, name: str, fives: int, tens: int, twenties: int) -> None:
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
    
    @staticmethod    
    def most_money(students: list) -> str:
        """
        `max_students = [i.name for i in students if total(i) == max_total]`
        
        This is a list comprehension that creates a list of student names who have the maximum total amount
        of money
        
        :param students: a list of students
        :type students: list
        :return: The name of the student who has the most money.
        """
        total = lambda x: x.fives * 5 + x.tens * 10 + x.twenties * 20
        max_total = max(map(total, students))
        max_students = [i.name for i in students if total(i) == max_total]
        return max_students[0] if len(max_students) == 1 else 'all'
    

def main() -> None:
    phill: Student = Student("Phill", 2, 2, 1)
    cam: Student = Student("Cameron", 2, 2, 0)
    geoff: Student = Student("Geoff", 0, 3, 0)
    print(phill.most_money([phill, cam, geoff]))
    print(cam.most_money([cam, geoff]))


if __name__ == "__main__":
    main()
