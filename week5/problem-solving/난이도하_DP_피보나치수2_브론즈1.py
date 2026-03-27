# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

#0, 1로 시작하는데 0,1,1,2,3,5,8,13......

n = int(input())

def pibo(n):
    if n == 0: return 0
    if n == 1: return 1
    dp = []
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1]+ dp[i-2]
    return dp[-1]

print(pibo(n))