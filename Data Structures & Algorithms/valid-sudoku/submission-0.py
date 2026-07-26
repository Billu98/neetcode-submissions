class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = set()

            for value in row:
                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        for col in range(9):

            seen = set()

            for row in range(9):

                value = board[row][col]

                if value == ".":
                    continue

                if value in seen:
                    return False

                seen.add(value)

        for startRow in [0,3,6]:

            for startCol in [0,3,6]:

                seen = set()

                for r in range(startRow, startRow+3):

                    for c in range(startCol, startCol+3):

                        value = board[r][c]

                        if value == ".":
                            continue

                        if value in seen:
                            return False

                        seen.add(value)

        return True

board =[["1","2",".",".","3",".",".",".","."],
["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

print(Solution().isValidSudoku(board))