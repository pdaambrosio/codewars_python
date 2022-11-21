def is_solved(board: list) -> int:
    """
    > We check if there are any rows, columns, or diagonals that have the same value and are not 0. If
    there are, we return that value. If there are no rows, columns, or diagonals that have the same
    value and are not 0, we check if there are any 0s in the board. If there are, we return -1. If there
    are no 0s in the board, we return 0.
    
    :param board: list - a list of lists, each of which represents a row of the board
    :type board: list
    """
    columns = list(zip(*board))
    rows: list = board 
    diagonals: list = [[board[i][i] for i in range(3)]] + [[board[i][2-i] for i in range(3)]]
    
    for col in columns:
        if len(set(col)) == 1 and col[0] != 0: 
            return col[0] 
    for row in rows:
        if len(set(row)) == 1 and row[0] != 0: 
            return row[0] 
    for diag in diagonals:
        if len(set(diag)) == 1 and diag[0] != 0: 
            return diag[0] 
    
    if 0 in [j for i in board for j in i]:
        return -1 
    return 0


def main() -> None:
    """
    It returns -1 if the board is not solved, 1 if the board is solved by X, and 2 if the board is
    solved by O
    """
    print(is_solved([[0, 0, 1], [0, 1, 2], [2, 1, 0]])) # -1
    print(is_solved([[0, 1, 1], [0, 1, 2], [2, 1, 0]])) # 1
    print(is_solved([[0, 1, 1], [0, 1, 2], [2, 2, 2]])) # 2
    print(is_solved([[2, 1, 2], [2, 1, 1], [1, 2, 1]])) # 0


if __name__ == '__main__':
    main()
