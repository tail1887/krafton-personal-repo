# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

#1. 입력
#2. 초기화
#3. 그래프 생성
#4. DFS 탐색
#5. BFS 탐색
#6. 결과 출력
import sys
from collections import deque

input_data = (word for line in sys.stdin for word in line.split())

n = int(next(input_data))
m = int(next(input_data))

def dfs(graph, start, visited):
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
    return visited

def bfs(graph, start):
    visited = [False] * (n+1)
    visited[start] = True
    queue = deque([start])
    while queue:                        
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return visited

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = int(next(input_data)), int(next(input_data))
    graph[a].append(b)
    graph[b].append(a)
    print(dfs(graph, 1, [False] * (n+1)).count(True) - 1)
    print(bfs(graph, 1).count(True) - 1)