# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

import sys
from collections import deque

def find_last_card(n):
    # deque를 사용하여 큐 생성
    queue = deque(range(1, n + 1))
    
    while len(queue) > 1:
        # 1. 맨 위 카드를 버림
        queue.popleft()
        # 2. 그다음 맨 위 카드를 맨 아래로 이동
        if queue: # 카드가 한 장 남았을 경우를 대비한 체크
            queue.append(queue.popleft())
            
    return queue[0]

n = int(sys.stdin.readline().strip())
print(find_last_card(n))