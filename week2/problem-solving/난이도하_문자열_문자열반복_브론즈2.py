# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675
t = int(input())
for _ in range(t):
    r, s = input().split()
    for char in s:
        print(char * int(r), end='')
    print()