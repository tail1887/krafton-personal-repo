# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
# 문제 풀이:
# 1. 입력 받기
# 2. 이분탐색 함수 정의
# 3. 이분탐색 함수 호출
# 4. 결과 출력

import sys

def find_number(numbers, target):
    left, right = 0, len(numbers) - 1
    while(left <= right):
        mid = (left + right) // 2
        if numbers[mid] == target:
            return 1
        elif numbers[mid] > target:
            right = mid - 1
        elif numbers[mid] < target:
            left = mid + 1
    return 0

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
numbers.sort()
m = int(sys.stdin.readline().strip())
targets = list(map(int, sys.stdin.readline().strip().split()))

for target in targets:
    print(find_number(numbers, target))