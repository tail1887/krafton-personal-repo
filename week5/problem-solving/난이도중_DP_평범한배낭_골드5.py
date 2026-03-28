# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865
#N개의 물건, 배낭의 최대무게 K
#무게 W와 가치 V
#최대 가치를 가지는 조합을 찾는 문제

import sys

input_data = (word for line in sys.stdin for word in line.split())

n, k = int(next(input_data)), int(next(input_data))

items = []

for _ in range(n):
    weight, price = int(next(input_data)), int(next(input_data))
    items.append((weight, price))

dp = [0] * (k+1)

for w, p in items:
    for i in range(k, w-1, -1):
        dp[i] = max(dp[i], dp[i - w] + p)

print(dp[k])
    