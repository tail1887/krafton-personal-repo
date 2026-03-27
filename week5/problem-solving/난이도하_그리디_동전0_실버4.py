# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

# N종류의 동전을가지고 가치의 합을 k로 만들려고 한다 이때 필요한 동전개수의 최소값
# 동전을 선택할때 현재 크기에서 선택 가능한 가장 큰 동전을 선택한다,
# 반복하다보면최소 동전갯수를 사용한다.
# BFS도 사용가능해 보이는데 그리디가 가장 깔끔해 보이는 문제
import sys

input_data = (word for line in sys.stdin for word in line.split())

n, k = int(next(input_data)), int(next(input_data))

coins = sorted([int(next(input_data)) for _ in range(n)])

price = k

def greedy(coins, k):
    price = k
    result = 0
    for coin in coins[::-1]:
        if coin <= price:
            result += (price // coin)
            price %= coin
    return result

print(greedy(coins, k))