# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

# import sys

# if __name__ == "__main__":
#     input_data = iter(sys.stdin.read().split())
#     n, m = int(next(input_data)), int(next(input_data))

#     if(m == 2):
#         for i in range(n-1):
#             print(f"{i} {i+1}")
#     elif(m > 2):
#         for i in range(m):
#             print(f"0 {i+1}")
#         check = n - (m + 1)
#         if check:
#             print(f"1 {m+1}")
#             if check > 1:
#                 for i in range(check-1):
#                     num = m + 1 + i
#                     print(f"{num} {num+1}")

import sys

if __name__ == "__main__":
    input_data = iter(sys.stdin.read().split())
    n, m = int(next(input_data)), int(next(input_data))
    for i in range(m):
        print(f"0 {i+1}")
    num = 1
    for i in range(m+1, n):
        print(f"{num} {i}")
        num = i