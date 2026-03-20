# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

import sys

def solve():
    input = sys.stdin.readline
    n = int(input().strip())
    board = [list(map(int, input().split())) for _ in range(n)]

    stack = [(0, 0)]  # 시작점
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    while stack:
        r, c = stack.pop()
        jump = board[r][c]

        if jump == -1:
            print("HaruHaru")
            return
        if jump == 0:
            continue

        # 오른쪽, 아래로 jump만큼 이동
        for nr, nc in ((r, c + jump), (r + jump, c)):
            if nr < n and nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                stack.append((nr, nc))

    print("Hing")


solve()


# import sys

# if __name__ == "__main__":
#     input_data = iter(sys.stdin.read().split())
#     n, m = int(next(input_data)), int(next(input_data))

#     if(m == 2):
#         for i in range(n-1):
#             print(f"{i} {i+1}")
#     elif(m > 2):
#         for i in range(m):
#             print(f"0 {i+1}")
#         check = n - (m + 1)
#         if check:
#             print(f"1 {m+1}")
#             if check > 1:
#                 for i in range(check-1):
#                     num = m + 1 + i
#                     print(f"{num} {num+1}")
