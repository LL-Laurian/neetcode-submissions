class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        if rows == 0:
            return
        cols = len(board[0])

        def overwrite(i, j):
            print(i,j)
            board[i][j] ='T'
            for nei_i, nei_j in neighbours(i,j):
                if board[nei_i][nei_j] == 'O':
                    overwrite(nei_i, nei_j)

        def neighbours(i,j):
            neis = []
            if i != 0:
                neis.append((i-1,j))
            if i != rows-1:
                neis.append((i+1,j))
            if j != 0:
                neis.append((i, j-1))
            if j != cols-1:
                neis.append((i, j+1))
            return neis
        
        for j in range(cols):
            if board[0][j] == 'O':
                overwrite(0,j)
            if board[rows-1][j] == 'O':
                overwrite(rows-1,j)
        
        for i in range(rows):
            if board[i][0] == 'O':
                overwrite(i,0)
            if board[i][cols-1] == 'O':
                overwrite(i,cols-1)

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    board[i][j] = 'O'