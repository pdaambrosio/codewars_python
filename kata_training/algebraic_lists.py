# A Cons is a list of lists, where the first list is the head and the second list is the tail.
class Cons:
    def __init__(self, head: list, tail: list):
        """
        :param head: a list of the first n elements of the original list
        :type head: list
        :param tail: The tail of the list
        :type tail: list
        """
        self.head = head
        self.tail = tail

    def to_array(self):
        """
        If the tail is not None, then return the head and the tail converted to an array. Otherwise,
        return the head
        :return: The head of the list and the tail of the list.
        """
        """
        If the tail is not None, then return the head and the tail converted to an array. Otherwise,
        return the head
        :return: The head of the list and the tail of the list.
        """
        return [self.head] + (self.tail.to_array() if self.tail is not None else [])

    @classmethod
    def from_array(cls, arr: any):
        """
        "If the array is not empty, return a Cons whose car is the first element of the array and whose cdr
        is a Cons whose car is the second element of the array and whose cdr is a Cons whose car is the
        third element of the array and whose cdr is a Cons whose car is the fourth element of the array and
        whose cdr is a Cons whose car is the fifth element of the array and whose cdr is a Cons whose car is
        the sixth element of the array and whose cdr is a Cons whose car is the seventh element of the array
        and whose cdr is a Cons whose car is the eighth element of the array and whose cdr is a Cons whose
        car is the ninth element of the array and whose cdr is a Cons whose car is the tenth element of the
        array and whose cdr is a Cons whose car is the eleventh element of the array and whose cdr is a Cons
        whose car is the twelfth element of the array and whose
        
        :param cls: The class that the method is being called on
        :param arr: any
        :type arr: any
        :return: A Cons object
        """
        if arr:
            return Cons(arr[0], Cons.from_array(arr[1:]))

    def filter(self, fn: callable):
        """
        Filter returns a new Cons whose elements are those of the original Cons for which the given function
        returns True.
        
        :param fn: callable
        :type fn: callable
        :return: A Cons object
        """
        return Cons.from_array(list(filter(fn, self.to_array())))

    def map(self, fn: callable):
        """
        It takes a function `fn` and applies it to every element of the list, returning a new list with the
        results
        
        :param fn: callable
        :type fn: callable
        :return: A new Cons object with the mapped values.
        """
        return Cons.from_array(list(map(fn, self.to_array())))


def main() -> None:
    """
    It creates a Cons object from an array, filters out odd numbers, and then doubles the remaining
    numbers
    """
    test: callable = Cons.from_array([1, 2, 3, 4, 5])
    print(test.to_array())
    print(test.filter(lambda x: x % 2 == 0).to_array())
    print(test.map(lambda x: x * 2).to_array())


if __name__ == '__main__':
    main()
