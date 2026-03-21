# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724

import sys
from collections import deque
sys.setrecursionlimit(10000)

input_data = (word for line in sys.stdin for word in line.split())

n, m = int(next(input_data)), int(next(input_data))

visited = [0] * (n+1)

graph = [[] for _ in range(n+1)]

for _ in range(m):
    l, k = int(next(input_data)), int(next(input_data))
    graph[l].append(k)
    graph[k].append(l)

def dfs(j):
    if visited[j] == 1:
        return
    visited[j] = 1
    for num in graph[j]:
        dfs(num)

q = deque()

def bfs(j):
    if visited[j] == 1:
        return
    visited[j] = 1
    q.append(j)
    while q:
        num = q.popleft()
        visited[num] = 1
        for k in graph[num]:
            if visited[k] == 0:
                q.append(k)
                visited[k] = 1


count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        bfs(i)

print(count)