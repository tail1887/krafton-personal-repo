# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978

n = int(input())
numbers = list(map(int, input().split()))

prime_numbers = 0
for number in numbers:
    if number == 1:
        continue
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        prime_numbers += 1

print(prime_numbers)