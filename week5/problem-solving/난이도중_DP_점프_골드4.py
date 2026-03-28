# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253
# N개의 돌
# 처음 점프는 한칸만 점프 가능
# 그다음부터는 x-1, x, x+1칸 점프가능
# 못올라가는 돌 있음

import sys
from collections import deque

#입력
input_data = (word for line in sys.stdin for word in line.split())

n, m = int(next(input_data)), int(next(input_data))

small_stones = set()

for _ in range(m):
    small_stones.add(int(next(input_data)))

# def bfs(): #현재 위치 ,x값, count
#     visited =  [[0] * 300 for _ in range(n+1)]
#     if n < 2 or 2 in small_stones:
#         print("-1")
#         return
#     else:
#         q = deque([(2,1,1)])
#         visited[2][1] = 1
#     while q:
#         node, x, count = q.popleft()
#         if node == n:
#             return print(count)
#         for jump in [x-1, x, x+1]:
#             if jump > 0 and node + jump <= n and node + jump not in small_stones:
#                 if visited[node + jump][jump] != 1:
#                     visited[node+jump][jump] = 1
#                     q.append((node+jump, jump, count+1))
#     return print(-1)
# bfs()

max_v = int((2 * n)**0.5) + 1
inf = float('inf')

dp = [[inf] * (max_v + 1) for _ in range(n + 1)]

# for i in range(2, n + 1):
#     for v in range(1, max_v):
#         if dp[i][v] == inf:
#             continue
#         for dv in [v - 1, v, v + 1]:
#             if dv <= 0: continue
#             next_pos = i + dv
#             if next_pos <= n and next_pos not in small_stones:
#                 dp[next_pos][dv] = min(dp[next_pos][dv], dp[i][v] + 1)

# print(min(dp[n]))

dp[2][1] = 1

for i in range(3, n + 1):
    if i in small_stones:
            continue 
    for v in range(1, 150):
        # 점화식 그대로 대입
        # i번 돌에 v 속도로 왔다면, 직전 위치는 i - v 입니다.
        prev_pos = i - v
        # 직전 위치가 유효한 범위(1번 돌 이후)여야 합니다.
        if prev_pos <= 0:
            continue
        # 점화식: dp[i][v] = min(이전 속도 후보들) + 1
        # 직전 속도 후보: v-1, v, v+1
        # 단, v-1은 1 이상이어야 하고 v+1은 max_v를 넘지 않아야 함
        candidates = []
        # 1. v-1 속도에서 온 경우
        if v - 1 > 0:
            candidates.append(dp[prev_pos][v - 1])
        # 2. v 속도에서 온 경우
        candidates.append(dp[prev_pos][v])
        # 3. v+1 속도에서 온 경우
        if v + 1 <= max_v:
            candidates.append(dp[prev_pos][v + 1])
        # 후보들 중 최솟값을 찾아 현재 칸을 갱신
        min_prev = min(candidates)
        if min_prev != inf:
            dp[i][v] = min_prev + 1