def sort_array(source_array: list[int]) -> list[int]:
    list_odds = sorted(x for x in source_array if x % 2 != 0)
    it = iter(list_odds)
    return [next(it) if x % 2 != 0 else x for x in source_array]

def main() -> None:
    test_sort_array1 = [7, 1]
    test_sort_array2 = [5, 8, 6, 3, 4]
    test_sort_array3 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(sort_array(test_sort_array1))
    print(sort_array(test_sort_array2))
    print(sort_array(test_sort_array3))

if __name__ == "__main__":
    main()
