class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

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

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                
                boxes[(box_row, box_col)].add(board[i][j])

        
        return True