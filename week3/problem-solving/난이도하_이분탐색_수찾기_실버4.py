# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920
import sys

def find_number(numbers, target):
    numbers.sort()
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return 1
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
targets = list(map(int, sys.stdin.readline().strip().split()))
for target in targets:
    print(find_number(numbers, target))