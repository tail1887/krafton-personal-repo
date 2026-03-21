# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178
import sys
from collections import deque

# 입력 받기
input = sys.stdin.read().split()
n, m = int(input[0]), int(input[1])
# 붙어서 들어오는 미로 데이터를 2차원 리스트로 변환
graph = [list(map(int, list(input[i+2]))) for i in range(n)]

# BFS로 해결
def bfs(x, y):
    q = deque([(x, y)])
    
    # 상, 하, 좌, 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        
        # 4방향 확인
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # 미로 범위 내에 있고, 갈 수 있는 길(1)인 경우
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    # 이전 칸의 거리 + 1을 현재 칸에 저장 (방문 처리 겸용)
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
    
    return graph[n-1][m-1]

print(bfs(0, 0))