# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630
# 문제 풀이:
# 1. 입력 받기
# 2. 분할정복 함수 정의
# 3. 분할정복 함수 호출
# 4. 결과 출력

def divide_conquer(paper):
    if len(paper) == 1:
        return paper[0][0]
    else:
        return divide_conquer(paper[0:len(paper)//2]) + divide_conquer(paper[len(paper)//2:])

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
print(divide_conquer(paper))