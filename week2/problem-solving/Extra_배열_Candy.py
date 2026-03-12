# 배열 - Candy
# 문제 링크: https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150

# 제약 조건
# n == ratings.length
# 1 <= n <= 2 * 104
# 0 <= ratings[i] <= 2 * 10^4

# 복잡도 예산 
# O(n)~O(nlogn)

# 핵심 제약
# 각 어린이는 최소한 사탕 하나씩을 가져야 합니다.
# 평점이 높은 아이들은 이웃 아이들보다 더 많은 사탕을 받습니다.

# 엣지케이스
# 1
# 1 1 1
# 1 2 3
# 3 2 1
# 1 2 3 2 1

# 정의
# left[i]: 왼쪽 조건만 고려할시의 i의 최소 사탕수
# right[i]: 오른쪽 조건만 고려할시의 i의 최소 사탕수
# max(left[i], right[i]): 각 i의 최소 사탕 수

# 상태변화 규칙
# if ratings[i] > ratings[i-1] : left[i] = left[i-1] + 1 else 1
# if ratings[i] > ratings[i+1] : right[i] = right[i+1] + 1 else 1

# CS
# 양방향 그리디:O(n) 적합
# 점수가 작은것부터: 부적합

# 의사코드
# 1) left를 전부 1로 초기화
# 2) 좌->우 순회하며 증가 구간이면 left 갱신
# 3) 우->좌 순회하며 증가 구간이면 right 갱신
# 4) ans += max(left[i], right_need)



class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # 1) left를 전부 1로 초기화
        # 2) 좌->우 순회하며 증가 구간이면 left 갱신
        # 3) 우->좌 순회하며 증가 구간이면 right 갱신
        # 4) ans += max(left[i], right_need)
        n = len(ratings)
        left = [1] * n
        right = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right[i] = right[i+1] + 1
        return sum(max(left[i], right[i]) for i in range(n))