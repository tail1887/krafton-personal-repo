# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

import sys
from collections import deque
sys.setrecursionlimit(10**6)

input_data = (word for line in sys.stdin for word in line.split())

n, m, root = int(next(input_data)), int(next(input_data)), int(next(input_data))

graph = [[] for _ in range(n+1)]

for _ in range(m):
    k, v = int(next(input_data)), int(next(input_data))
    graph[k].append(v)
    graph[v].append(k)

for i in range(1, n + 1):
    graph[i].sort()

result_dfs = []
visited = [False] * (n + 1)

def dfs(root):
    visited[root] = True
    if graph[root] == None:
        return result_dfs.append(root)
    result_dfs.append(root)
    for node in graph[root]:
        if not visited[node]:
            dfs(node)

dfs(root)

print(*(result_dfs))

q = deque()

result2 = []

visited = [False] * (n + 1) 

def bfs(root):
    #초기값 넣기
    q.append(root)
    visited[root] = 1
    #스텍 시작
    while q:
        num = q.popleft() #하나 뽑고 
        result2.append(num)
        for node in graph[num]:
            if not visited[node]:
                visited[node] = 1
                q.append(node)
bfs(root)

print(*result2)
