# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
# 문제 풀이:
# 1. 입력 받기
# 2. 이분탐색 함수 정의
# 3. 이분탐색 함수 호출
# 4. 결과 출력

# 이분탐색 함수 정의
def find_two_solutions(solutions):
    left = 0
    right = len(solutions) - 1
    while left < right:
        if solutions[left] + solutions[right] == 0:
            return solutions[left], solutions[right]
        elif solutions[left] + solutions[right] < 0:
            left += 1
        else:
            right -= 1
    return None

n = int(input())
solutions = list(map(int, input().split()))
solutions.sort()
result = find_two_solutions(solutions)
print(result[0], result[1]) if result else print("No solution")