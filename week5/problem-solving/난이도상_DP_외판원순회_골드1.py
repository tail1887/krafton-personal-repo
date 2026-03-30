# DP - 외판원 순회 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/2098
import sys

sys.setrecursionlimit(10**6)

input_data = (word for line in sys.stdin for word in line.split())

n = int(next(input_data))

world_map = []

for _ in range(n):
    world_map.append([int(next(input_data)) for i in range(n)])

dp = [[-1] * (1 << n) for _ in range(n)]
INF = 1e9  # 적당히 큰 값

def solve(curr, visited):
    #모든 도시를 방문했을 때
    if visited == (1 << n) - 1:
        # 다시 시작점(0번)으로 돌아가는 길이 있다면 그 비용 반환(길이 없으면 없다고 알림, 최솟값 확인에서 무시)
        return world_map[curr][0] if world_map[curr][0] > 0 else INF

    # 이미 계산된 상태라면 즉시 리턴
    if dp[curr][visited] != -1:
        return dp[curr][visited]

    res = INF
    # 다음 도시로 이동
    for next_city in range(n):
        # 길이 있고, 아직 방문하지 않은 도시라면
        if world_map[curr][next_city] > 0 and not (visited & (1 << next_city)): # 두 이진수가 1인 자리만 1을 넣음 결과가 0이면 둘이 안겹치는거임
            # 현재 이동 비용 + 남은 경로의 최솟값
            tmp = world_map[curr][next_city] + solve(next_city, visited | (1 << next_city)) # 두 이진수를 합침(겹치는건 계산안함, 집합연산에서 중복은 자동으로 무시하는 것)
            # 그리고 최솟값 확인
            res = min(res, tmp)
    # 4. 결과 저장
    dp[curr][visited] = res
    return res

# 0번 도시에서 시작, 방문 상태 0번 미리 체크
print(solve(0, 1))