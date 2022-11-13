def max_sequence(arr: list[int]) -> int:
    """
    We keep track of the maximum sum we've seen so far, and the maximum sum we've seen ending at the
    previous element
    
    :param arr: list[int] -> the list of integers
    :type arr: list[int]
    :return: The maximum sum of a contiguous subarray within the array.
    """
    now: int = 0
    prev: int = 0
    for i in range(len(arr)):
        prev = max(0, prev + arr[i])
        now = max(prev, now) 
    return now


def main() -> None:
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
    print(max_sequence([]))  # 0
    print(max_sequence([-1]))  # 0
    print(max_sequence([-1, -2]))  # 0
    

if __name__ == "__main__":
    main()
