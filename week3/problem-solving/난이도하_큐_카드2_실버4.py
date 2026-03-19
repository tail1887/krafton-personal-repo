# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

from collections import deque
import sys

input_data = iter(sys.stdin.read().split())

N = int(next(input_data))

queue = deque(range(1, N + 1))

while len(queue) > 1:
    queue.popleft()
    if len(queue) == 1:
        break
    change = queue.popleft()
    queue.append(change)

print(*queue)