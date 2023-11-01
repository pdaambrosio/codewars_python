"""
To square(root) or not to square(root)
Function that takes a list of integers and returns a list of the square root of each number.
If the number is not a perfect square, it should be rounded to the nearest square root.
"""
def square_or_square_root(arr):
    return [int(x**0.5) if (x**0.5).is_integer() else x**2 for x in arr]


def main():
    print(square_or_square_root([4, 3, 9, 7, 2, 1]))
    # [2, 9, 3, 49, 4, 1]
    print(square_or_square_root([100, 101, 5, 5, 1, 1]))
    # [10, 10201, 25, 25, 1, 1]
    print(square_or_square_root([1, 2, 3, 4, 5, 6]))
    # [1, 4, 9, 2, 25, 36]
