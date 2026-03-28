# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

import sys

input_data = (word for line in sys.stdin for word in line.split())

n = int(next(input_data))

tasks = []

#끝나는 순대로 정렬

for i in range(n):
    start, end = int(next(input_data)), int(next(input_data))
    tasks.append((start, end))

tasks.sort(key = lambda x:(x[1], x[0]))

cur_time = 0
count = 0

for i in range(n):
    start, end = tasks[i]
    if start >= cur_time:
        cur_time = end
        count += 1

print(count)