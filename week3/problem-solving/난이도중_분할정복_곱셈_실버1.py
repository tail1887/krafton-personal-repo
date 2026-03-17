# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629
# 문제 풀이:
# 1. 입력 받기
# 2. 분할정복 함수 정의
# 3. 분할정복 함수 호출
# 4. 결과 출력

# 입력 받기
import sys

def divide_conquer(a, b, c):
    # 기저 조건: b가 1이면 더 나눌 수 없음
    if b == 1:
        return a % c
    
    # 지수를 절반으로 나누어 재귀 호출
    temp = divide_conquer(a, b // 2, c)
    
    # 지수가 짝수라면: (a^(b//2) * a^(b//2)) % c
    if b % 2 == 0:
        return (temp * temp) % c
    # 지수가 홀수라면: (a^(b//2) * a^(b//2) * a) % c
    else:
        return (temp * temp % c) * a % c

a, b, c = map(int, sys.stdin.readline().split())
print(divide_conquer(a, b, c))