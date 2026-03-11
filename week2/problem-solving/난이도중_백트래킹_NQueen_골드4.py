# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663
def is_safe(board, row, col, n):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def n_queens(board, row, n):
    if row == n:
        return 1
    count = 0
    for col in range(n):
        if is_safe(board, row, col, n):     
            board[row] = col
            count += n_queens(board, row + 1, n)
            board[row] = -1
    return count

n = int(input())
board = [-1] * n
print(n_queens(board, 0, n))
