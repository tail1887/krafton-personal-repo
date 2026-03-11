# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344
n = int(input())
for _ in range(n):
    scores = list(map(int, input().split()))
    average = sum(scores[1:]) / scores[0]
    count = 0
    for score in scores[1:]:
        if score > average:
            count += 1
    print(f"{count / scores[0] * 100:.3f}%")