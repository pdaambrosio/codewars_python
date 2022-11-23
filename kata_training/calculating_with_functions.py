def zero(num = None) -> int:
    """
    "If num is None, return 0, else return num(0)."
    
    The function zero() is a function that takes in a function as an argument
    
    :param num: a function that takes in a value and returns a value
    :return: The function zero is being returned.
    """
    return 0 if not num else num(0)


def one(num = None) -> int:
    """
    "If num is None, return 1, otherwise return num(1)."
    
    The function one is a higher order function. It takes a function as an argument and returns a
    function
    
    :param num: A function that takes an int and returns an int
    :return: 1
    """
    return 1 if not num else num(1)


def two(num = None) -> int:
    """
    "If num is None, return 2, otherwise return num(2)."
    
    The function two() is a higher-order function that takes a function as an argument and calls it with
    the value 2
    
    :param num: a function that takes in a number and returns a number
    :return: A function that takes a function as an argument and returns the result of that function
    applied to 2.
    """
    return 2 if not num else num(2)


def three(num = None) -> int:
    """
    "If num is None, return 3, otherwise return num(3)."
    
    The function three() is a higher order function. It takes a function as an argument and returns a
    function
    
    :param num: a function that takes in a number and returns a number
    :return: The function three is being returned.
    """
    return 3 if not num else num(3)


def four(num = None) -> int:
    """
    "If num is None, return 4, otherwise return num(4)."
    
    The function four takes an optional parameter num. If num is None, the function returns 4.
    Otherwise, the function returns num(4)
    
    :param num: a function that takes an int and returns an int
    :return: 4
    """
    return 4 if not num else num(4)


def five(num = None) -> int:
    """
    "If num is None, return 5, otherwise return num(5)."
    
    The function five() takes an optional argument num. If num is None, five() returns 5. Otherwise,
    five() returns num(5)
    
    :param num: a function that takes an int and returns an int
    :return: 5
    """
    return 5 if not num else num(5)


def six(num = None) -> int:
    """
    "If num is None, return 6, otherwise return num(6)."
    
    The function six() takes an optional parameter num. If num is None, the function returns 6.
    Otherwise, the function returns num(6)
    
    :param num: A function that takes an int and returns an int
    :return: 6
    """
    return 6 if not num else num(6)


def seven(num = None) -> int:
    """
    "If num is None, return 7, otherwise return num(7)."
    
    The function seven(num) takes a single argument, num, and does one of two things:
    
    If num is None, the function returns 7.
    If num is not None, the function returns num(7).
    The function seven(num) always returns an integer
    
    :param num: a function that takes in a number and returns a number
    :return: 7
    """
    return 7 if not num else num(7)


def eight(num = None) -> int:
    """
    "If num is None, return 8, otherwise return num(8)."
    
    The function eight() has one parameter, num, which is optional. If num is not provided, the function
    returns 8. If num is provided, the function returns num(8)
    
    :param num: A function that takes in a number and returns a number
    :return: 8
    """
    return 8 if not num else num(8)


def nine(num = None) -> int:
    """
    "If num is None, return 9, otherwise return num(9)."
    
    The function nine() is defined with a default parameter of None
    
    :param num: A function that takes a number and returns a number
    :return: 9
    """
    return 9 if not num else num(9)


def plus(y: int):
    """
    Plus is a function that takes an integer y and returns a function that takes an integer x and
    returns x + y.
    
    :param y: int
    :type y: int
    :return: A function that takes an int and returns an int.
    """
    return lambda x: x + y


def minus(y: int):
    """
    "minus returns a function that takes an int and returns an int."
    
    The above function is equivalent to the following:
    
    # Python
    def minus(y):
        def minus_y(x):
            return x - y
        return minus_y
    
    :param y: int
    :type y: int
    :return: A function that takes an int and returns an int.
    """
    return lambda x: x - y


def times(y: int):
    """
    Times returns a function that takes an int and returns the product of that int and y.
    
    :param y: int - This is the parameter that we're going to pass into the function
    :type y: int
    :return: A function that takes an argument x and returns x * y
    """
    return lambda x: x * y


def divided_by(y: int):
    """
    Divided_by returns a function that divides its argument by y.
    
    :param y: int - the number to divide by
    :type y: int
    :return: A function that takes an integer and divides it by the integer passed into the divided_by
    function.
    """
    return lambda x: x // y


def main() -> None:
    print(seven(times(five()))) # 35
    print(four(plus(nine()))) # 13
    print(eight(minus(three()))) # 5
    print(six(divided_by(two()))) # 3
    

if __name__ == '__main__':
    main()
