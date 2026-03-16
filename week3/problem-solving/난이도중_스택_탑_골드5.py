# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

import sys

def find_top(heights):
    stack = []
    result = []
    for index, height in enumerate(heights):
        while stack and stack[-1][0] < height:
            stack.pop()
        if stack:
            result.append(stack[-1][1] + 1)
        else:
            result.append(0)
        stack.append((height, index))
    return result

n = int(sys.stdin.readline().strip())
numbers = list(map(int, sys.stdin.readline().strip().split()))
print(*(find_top(numbers)))