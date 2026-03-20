# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

import sys

input_data = (word for line in sys.stdin for word in line.split())

T = int(next(input_data))

for _ in range(T):
    n, m = int(next(input_data)), int(next(input_data))
    for _ in range(m):
        next(input_data); next(input_data)
    print(n-1)