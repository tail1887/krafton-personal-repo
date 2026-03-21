# 위상정렬 - 작업 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2056

import sys
from collections import deque

input_data = (word for line in sys.stdin for word in line.split())

n = int(next(input_data))

work = [[[] for _ in range(2)] for _ in range(n+1)] #work[][0]은 소요시간 work[][1] 은 후속임무리스트

indegree = [0] * (n+1) #차수는 별도 배열에 보관

for i in range(1,n+1): #초기데이터 삽입
    work[i][0] = int(next(input_data))
    indegree[i] = int(next(input_data))
    for _ in range(indegree[i]):
        work[int(next(input_data))][1].append(i)

q = deque()
dp = [0] * (n + 1)

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        dp[i] = work[i][0] # 선행 없으니 내 시간이 곧 완료 시각

while q:
    current = q.popleft()
    
    for next_node in work[current][1]:
        
        # '간 보기': 선행 작업들 중 누가 제일 늦게 끝나나 기록 (기다리기)
        dp[next_node] = max(dp[next_node], dp[current])

        # 선행 작업 하나 완료 보고
        indegree[next_node] -= 1
        
        # 모든 선행 작업이 끝났다면 (진입차수 0)
        if indegree[next_node] == 0:
            # 드디어 내 작업을 시작해서 '완료 시각' 확정!
            dp[next_node] += work[next_node][0]
            q.append(next_node)

print(max(dp))



# 직렬
# #우선순위 큐에 초기데이터 삽입
# for i in range(1, n+1):
#     if indegree[i] == 0:
#         heapq.heappush(prior_queue, (work[i][0], i))

# while prior_queue:
#     current = heapq.heappop(prior_queue)
#     result += current[0]
#     for i in range(1, n+1):
#         if current[0] in work[i][1]:
#             work[i][1].pop(current[0])
#             indegree[i] -= 1
#             if indegree[i] == 0:
#                 heapq.heappush(prior_queue, (work[i][0], i))

