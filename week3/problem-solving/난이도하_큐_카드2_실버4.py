# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

import sys

def find_last_card(n):
    queue = list(range(1, n + 1))
    while len(queue) > 1:
        queue.pop(0)
        queue.append(queue.pop(0))
    return queue[0]

print(find_last_card(int(sys.stdin.readline().strip())))