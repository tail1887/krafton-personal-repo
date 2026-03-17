# 해시 테이블 - 세 수의 합 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2295
# 문제 풀이:
# 1. 입력 받기
# 2. 해시 테이블 생성
# 3. 해시 테이블 탐색
# 4. 결과 출력

# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if numbers[i] + numbers[j] + numbers[k] == 0:
                print(numbers[i], numbers[j], numbers[k])
                break

# 결과 출력
print(numbers)