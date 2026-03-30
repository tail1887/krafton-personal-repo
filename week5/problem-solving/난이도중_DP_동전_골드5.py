# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084
import sys

# 입력을 효율적으로 받기 위한 설정
input = sys.stdin.read().split()
input_ptr = 0

def next_val():
    global input_ptr
    res = input[input_ptr]
    input_ptr += 1
    return res

T_str = next_val()
T = int(T_str)

for _ in range(T):
    N = int(next_val()) # 동전의 개수
    coins = [int(next_val()) for _ in range(N)] # 동전 종류
    M = int(next_val()) # 목표 금액
    
    # 1. 상태 정의 및 초기화
    dp = [0] * (M + 1)
    
    # 3. 초기 조건: 0원을 만드는 방법은 1가지
    dp[0] = 1
    
    # 4. 계산 순서: 동전 하나하나에 대해 dp 테이블 갱신
    for coin in coins:
        for i in range(coin, M + 1):
            # 2. 점화식: 현재 금액(i) 방법 수 += (현재 금액 - 동전가치)의 방법 수
            dp[i] += dp[i - coin]
            
    print(dp[M])