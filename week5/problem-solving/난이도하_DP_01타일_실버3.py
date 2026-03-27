# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904
# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

# 0,1타일들이 있는데 1은 한쌍으로씩 이루어져있다 0은 낱장으로만 이루어져있다.

#타일로 크기가 n인 이진수열을 만드는데

# dp[1] = 1
# 1
# dp[2] = 2
# 00
# 11
# dp[3] = 3
# 001 X
# 100
# 111
# dp[4] = 5
# 1100
# 1001
# 0011
# 0000
# 1111

n = int(input())

def pibo(n):
    if n == 1: return 1
    if n == 2: return 2
    a, b = 1, 2
    for _ in range(n-2):
        a, b = b, (a+b)%15746
    return b

print(pibo(n))