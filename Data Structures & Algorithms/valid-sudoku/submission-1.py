class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]

        cols = [[] for _ in range(9)]

        boxes = {}

        for i in range(9):
            box_col = i//3
            for j in range(9):
                box_row = j // 3

                if board[i][j] == ".":
                    continue

                box = boxes.get((box_row, box_col))

                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                if box is not None and board[i][j] in box:
                    return False

                rows[i].append(board[i][j])
                cols[j].append(board[i][j])
                if box is None: boxes[(box_row, box_col)] =[]
                boxes[(box_row, box_col)].append(board[i][j])

        
        return True