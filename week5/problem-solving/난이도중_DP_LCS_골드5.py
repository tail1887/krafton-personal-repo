# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251

import sys

def solve():
    s1 = sys.stdin.readline().strip()
    s2 = sys.stdin.readline().strip()
    
    n = len(s1)
    m = len(s2)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    # 최종 결과 출력
    print(dp[n][m])

solve()