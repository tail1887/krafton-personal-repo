# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190
# 문제 풀이:
# 1. 입력 받기
# 2. 큐 생성
# 3. 큐 탐색
# 4. 결과 출력

from collections import deque

# 1. 보드 및 사과 정보 설정
n = int(input())
k = int(input())
board = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1  # 사과는 1로 표시

# 2. 방향 전환 정보 설정
l = int(input())
times = {}
for _ in range(l):
    x, c = input().split()
    times[int(x)] = c

# 3. 초기 설정 (상, 우, 하, 좌 방향 벡터)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def simulate():
    # 초기 설정: 우(0), 하(1), 좌(2), 상(3) 순서 (시계방향)
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    direction = 0 
    
    r, c = 1, 1
    snake = deque([(r, c)])
    board[r][c] = 2
    time = 0

    while True:
        time += 1 # 1초 흐름
        nr = r + dr[direction]
        nc = c + dc[direction]

        # 벽에 부딪히거나 자기 몸에 부딪히는지 확인
        if 1 <= nr <= n and 1 <= nc <= n and board[nr][nc] != 2:
            # 사과가 없는 경우
            if board[nr][nc] == 0:
                tail_r, tail_c = snake.popleft() # 꼬리 자르기
                board[tail_r][tail_c] = 0
            
            # 머리 이동
            board[nr][nc] = 2
            snake.append((nr, nc))
            r, c = nr, nc
        else:
            return time # 충돌 시 종료

        # X초가 끝난 뒤 방향 전환 확인
        if time in times:
            if times[time] == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4

print(simulate())
