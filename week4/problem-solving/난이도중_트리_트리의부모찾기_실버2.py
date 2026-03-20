# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

import sys

sys.setrecursionlimit(10**6)

input_data = (word for line in sys.stdin for word in line.split())

n = int(next(input_data))

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)
parents = [0] * (n+1)

def dfs(start):
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            parents[neighbor] = start
            dfs(neighbor)
    return visited

for _ in range(n-1): 
    a, b = int(next(input_data)), int(next(input_data))
    graph[a].append(b)
    graph[b].append(a)

parents[1] = 1
dfs(1)

print('\n'.join(map(str, parents[2:])))