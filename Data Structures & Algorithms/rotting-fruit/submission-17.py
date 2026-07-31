class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        seen_count = 0
        seen = set()

        n_rows = len(grid)
        n_cols = len(grid[0])
        total_fruit = 0

        q = set()  # store the (i, j)

        for i in range(n_rows):
            for j in range(n_cols):
                cur_cell = grid[i][j]

                if cur_cell != 0:
                    if cur_cell == 2:
                        q.add((i, j))

                    total_fruit += 1

        total_minute = 0

        while q:
            new_round = set()
            check = False

            print(total_minute, q)
            for i, j in q:
                if (i, j) not in seen:
                    print("yes")
                    seen.add((i, j)) 
                    grid[i][j] = 2
                    seen_count += 1
                    check = True

                    print("minute", total_minute, "row", i, "col", j, grid[i][j])

                    if i >= 1 and grid[i - 1][j] == 1 and (i - 1, j) not in seen:
                        new_round.add((i - 1, j))

                    if i < n_rows - 1 and grid[i + 1][j] == 1 and (i + 1, j) not in seen:
                        new_round.add((i + 1, j))

                    if j >= 1 and grid[i][j - 1] == 1 and (i, j - 1) not in seen:
                        new_round.add((i, j - 1))

                    if j < n_cols - 1 and grid[i][j + 1] == 1 and (i, j + 1) not in seen:
                        new_round.add((i, j + 1))
            q = new_round

            if check == False:
                total_minute-=1

            if check and new_round:
                print(check, new_round)
                total_minute += 1


        if seen_count == total_fruit:
            return total_minute
        else:
            return -1