# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946
import sys

input_data = (word for line in sys.stdin for word in line.split())

t = int(next(input_data))

for _ in range(t):
    n = int(next(input_data))
    ratings = []
    for i in range(n):
        doc_rate, inter_rate = int(next(input_data)), int(next(input_data))
        ratings.append((doc_rate, inter_rate))
    doc_ratings = sorted(ratings, key = lambda x: x[0], reverse=False)
    result = 0
    min_inter_rate = 100001
    for idx, (doc_rate, inter_rate) in enumerate(doc_ratings):
        if min_inter_rate > inter_rate:
            result += 1
            min_inter_rate = inter_rate
    print(result)