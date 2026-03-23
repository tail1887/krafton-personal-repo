# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294
# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294
from collections import deque

def solve():
    # n: 동전 종류 수, k: 목표 금액
    n, k = map(int, input().split())
    coins = sorted(list(set(int(input()) for _ in range(n)))) # 중복 제거 및 정렬(중요함 속도 업)
    
    queue = deque([(0, 0)]) # (현재 금액 sum, 사용한 동전 개수 count)
    visited = [False] * (k + 1)
    visited[0] = True #그냥 템플릿 습관
    
    while queue:
        curr_sum, count = queue.popleft()
        
        # 목표 금액 도달 시 즉시 반환 (최소 개수 보장)
        if curr_sum == k:
            return count
        
        for coin in coins:
            next_sum = curr_sum + coin
            
            # 범위를 벗어나지 않고, 방문한 적 없는 금액일 때만 진행
            if next_sum <= k and not visited[next_sum]:
                visited[next_sum] = True
                queue.append((next_sum, count + 1))
                
    return -1 # 큐가 빌 때까지 k를 못 만들면 -1

print(solve())