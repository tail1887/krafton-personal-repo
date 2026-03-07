# 배열 - Candy
# 문제 링크: https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150

## 1) CON
# CON:
# - ratings 길이 n(최대 2 * 10^4), 각 값은 정수.
# - 모든 아이는 최소 1개, 인접 비교 조건을 만족해야 한다.
# - 전체 합 최소화를 요구하므로 전역적으로 일관된 배치가 필요하다.
# OUT_CON:
# - complexity_budget: O(n) 또는 O(n log n) 이내
# - constraints_summary: 인접 제약 + 최소합
# - edge_inputs: n=1, 모두 같음, strictly inc/dec, 봉우리/골짜기

## 2) DEF
# IN: OUT_CON 
# DEF:
# - left[i]: "왼쪽 이웃 조건만" 만족할 때 i의 최소 사탕 수
#   규칙: ratings[i] > ratings[i-1] 이면 left[i] = left[i-1] + 1, 아니면 1
# - right_need: 오른쪽 이웃 조건을 오른쪽에서 보며 계산한 i의 필요 최소값
#   규칙: ratings[i] > ratings[i+1] 이면 right_need = prev + 1, 아니면 1
# - 최종 i의 사탕 = max(left[i], right_need)
# OUT_DEF:
# - state_definition: left 배열 + right_need 스칼라
# - transition_or_rule: 양방향 인접 제약을 분리해 계산
# - objective: 각 i의 필요 최소를 더해 총합 최소화


## 3) CS
# IN: OUT_CON + OUT_DEF
# CS:
# - 후보1 브루트포스/백트래킹: 배치 경우의 수가 급증 -> 비현실적
# - 후보2 반복 완화(relaxation): 최악 O(n^2)
# - 후보3 양방향 그리디:
#   왼쪽 제약, 오른쪽 제약을 각각 O(n)에 계산 후 max 병합
# OUT_CS:
# - candidates_with_tc: brute force(폭발), relax(O(n^2)), two-pass greedy(O(n))
# - pruned_candidates: brute force, O(n^2) 탈락
# - selected_strategy: two-pass greedy

## 4) LOG
# IN: OUT_CS
# LOG:
# - step1) left를 전부 1로 초기화
# - step2) 좌->우 순회: 증가 구간이면 left[i] = left[i-1] + 1
# - step3) 우->좌 순회: right_need 갱신, ans += max(left[i], right_need)
# - step4) 누적합 ans 반환
# OUT_LOG:
# - pseudocode_steps:
#   left = [1]*n
#   for i in 1..n-1:
#       if ratings[i] > ratings[i-1]: left[i] = left[i-1] + 1
#   ans = 0; right_need = 1
#   for i in n-1..0:
#       if i < n-1 and ratings[i] > ratings[i+1]: right_need += 1
#       else: right_need = 1
#       ans += max(left[i], right_need)
# - update_order: left pass -> right pass + merge(sum)
# - io_flow: ratings 입력 -> 최소 총사탕 정수 출력


## 5) PRF
# IN: OUT_LOG
# PRF:
# - left[i]는 왼쪽 조건을 만족하는 i의 최소값이다.
# - right_need는 오른쪽 조건을 만족하는 i의 최소값이다.
# - 두 조건을 동시에 만족하려면 i는 각각의 최소 요구치보다 작을 수 없으므로
#   최소 가능값은 max(left[i], right_need)이다.
# - 이를 모든 i에 대해 합하면 조건을 만족하는 전역 최소합이 된다.
# OUT_PRF:
# - correctness_claim: 양방향 조건을 독립 최소로 계산 후 max 병합 시 최적
# - invariant_or_key_reason: 각 방향 최소요구의 하한 결합

## 6) TC/SC
# IN: OUT_LOG
# TC:
# - left 1회 순회 O(n) + right 1회 순회 O(n) = O(n)
# SC:
# - left 배열 O(n), 기타 스칼라 O(1)
# OUT_CX:
# - final_tc_sc: TC O(n), SC O(n)
# - feasibility: 제약 내 충분히 가능

## 7) IMP
# IN: OUT_LOG + OUT_PRF + OUT_CX
# IMP:
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0

        # DEF(left): 왼쪽 조건 기준 최소 사탕 수
        left = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1

        # DEF(right_need): 오른쪽 조건 최소 요구치(스칼라)
        ans = 0
        right_need = 1

        for i in range(n - 1, -1, -1):
            if i < n - 1 and ratings[i] > ratings[i + 1]:
                right_need += 1
            else:
                right_need = 1

            # LOG(merge): 양방향 조건을 동시에 만족하는 최소값
            ans += max(left[i], right_need)

        return ans


if __name__ == "__main__":
    tests = [
        ([1, 0, 2], 5),
        ([1, 2, 2], 4),
        ([1], 1),
        ([1, 2, 3, 4], 10),
        ([4, 3, 2, 1], 10),
        ([1, 3, 2, 2, 1], 7),
    ]

    sol = Solution()
    for ratings, expected in tests:
        got = sol.candy(ratings)
        print(f"ratings={ratings}, got={got}, expected={expected}, ok={got == expected}")