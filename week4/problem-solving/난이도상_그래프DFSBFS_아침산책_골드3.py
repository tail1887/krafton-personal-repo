# 그래프, DFS, BFS - 아침 산책 (백준 골드3)
# 문제 링크: https://www.acmicpc.net/problem/21606
# 그래프, DFS, BFS - 아침 산책 (백준 골드3)
# 문제 링크: https://www.acmicpc.net/problem/21606

import sys
from collections import deque

input_data = (word for line in sys.stdin for word in line.split())

#입력 받기
n = int(next(input_data))

#1은 실내 0은 실외
str = next(input_data)
is_indoor = [0] + [int(char) for char in str]

# print(is_indoor)

#그래프 생성
graph = [[]for _ in range(n+1)]

#결과값 초기화
result = 0

#그래프 초기화
for _ in range(n - 1):
    u, v = int(next(input_data)), int(next(input_data))
    graph[u].append(v)
    graph[v].append(u)
    if is_indoor[u] and is_indoor[v]:
        result += 2

# print(graph)

out_visited = visited = [0]*(n+1)

#bfs
def bfs(root):
    #방문 배열 생성
    indoors = set()
    #큐 생성 및 초기화
    q = deque([root])
    out_visited[root] = 1
    while q:
        cur = q.popleft()
        for next_node in graph[cur]:
            if is_indoor[next_node]:
                indoors.add(next_node)
            else:
                if not out_visited[next_node]:
                    out_visited[next_node] = 1
                    q.append(next_node)
    return len(indoors)

for i in range(1,n+1):
    if not is_indoor[i] and not out_visited[i]:
        k = bfs(i)
        result += k*(k-1)

print(result)
