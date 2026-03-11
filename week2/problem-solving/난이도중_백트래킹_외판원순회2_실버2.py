# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971
def tsp(n, graph, visited, current, cost, min_cost):
    if len(visited) == n:
        return min(cost, min_cost)
    for i in range(n):
        if i not in visited:
            visited.append(i)
            tsp(n, graph, visited, i, cost + graph[current][i], min_cost)
            visited.pop()
    return min_cost

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
print(tsp(n, graph, [], 0, 0, float('inf')))