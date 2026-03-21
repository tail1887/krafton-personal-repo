# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707

# 1. 이분 그래프의 조건
# 삼각형이 생기지 않을 것
import sys

sys.setrecursionlimit(10**6) # DFS 사용 시 필수

input_data  = (word for line in sys.stdin for word in line.split())

t = int(next(input_data))

def dfs(now, visited, graph, current_color):
    visited[now] = current_color
    for node in graph[now]:
        if visited[node] == 0:
            if not dfs(node, visited, graph, 3 - current_color):
                return False
        elif visited[node] == visited[now]:
            return False
    return True

for _ in range(t):
    n, m  = int(next(input_data)), int(next(input_data))
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    color = [False] * (n+1)
    for _ in range(m):
        k, v = int(next(input_data)), int(next(input_data))
        graph[k].append(v)
        graph[v].append(k)
    is_possible = True
    for i in range(1, n + 1):
        if visited[i] == 0:
            # 하나라도 이분 그래프가 아니면 실패
            if not dfs(i, visited, graph, 1):
                is_possible = False
                break
    
    print("YES" if is_possible else "NO")