def solve_n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    cols = set()
    diag1 = set()
    diag2 = set()
    answer = []

    def backtrack(row):
        if row == n:
            for line in board:
                answer.append("".join(line))
            return True

        for col in range(n):
            if col in cols:
                continue
            if row - col in diag1:
                continue
            if row + col in diag2:
                continue

            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            if backtrack(row + 1):
                return True

            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return False

    backtrack(0)
    return answer


n = int(input())
result = solve_n_queens(n)

for row in result:
    print(row)