# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914
def hanoi(n, start, end, temp):
    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, temp, end)
    print(start, end)
    hanoi(n-1, temp, end, start)

n = int(input())
print(2**n - 1)
hanoi(n, 1, 3, 2)