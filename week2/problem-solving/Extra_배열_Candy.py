# 배열 - Candy
# 문제 링크: https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150


## 1) CON
# CON:
# - ratings 길이 n (1 <= n <= 2*10^4)
# - 각 아이는 최소 1개 사탕
# - 인접한 아이보다 평점이 높으면 사탕도 더 많아야 함
# OUT_CON:
# - complexity_budget: O(n) ~ O(n log n)
# - constraints_summary: 인접 제약 + 총합 최소화
# - edge_inputs: [1], [1,1,1], [1,2,3,4], [4,3,2,1], [1,3,2,2,1]

## 2) DEF
# IN: OUT_CON
# DEF:
# - left[i]: 왼쪽 조건만 고려했을 때 i의 최소 사탕 수
# - right_need: 오른쪽 조건만 고려했을 때 i의 최소 사탕 수(우->좌 순회 중 계산)
# - 각 i의 최종 사탕 수 = max(left[i], right_need)
# OUT_DEF:
# - state_definition: left 배열 + right_need 스칼라
# - transition_or_rule:
#   if ratings[i] > ratings[i-1]: left[i] = left[i-1] + 1 else 1
#   if ratings[i] > ratings[i+1]: right_need += 1 else 1
# - objective: 모든 제약을 만족하면서 총합 최소

## 3) CS
# IN: OUT_CON + OUT_DEF
# CS:
# - DEF 확장: 각 i의 최소 필요량은 left[i](좌측 요구)와 right_need(우측 요구)의 결합값 max(left[i], right_need)
# - 이 결합을 빠르게 계산하려면 "좌->우 하한 계산 + 우->좌 하한 계산" 구조가 자연스럽다.
# - 후보1: 반복 완화(조건 위반 시 계속 수정) -> 결합값을 간접적으로 맞추며 최악 O(n^2)
# - 후보2: 최소힙/정렬 기반 -> 전역 순서로 갱신 가능하나 인접 제약의 국소 하한 결합 표현이 불명확
# - 후보3: 양방향 그리디(좌->우, 우->좌) -> DEF의 결합식을 직접 구현, O(n)
# OUT_CS:
# - candidates_with_tc: O(n^2), O(n log n), O(n)
# - pruned_candidates: 후보1(시간 초과 위험), 후보2(정의와의 대응 약함)
# - selected_strategy: two-pass greedy

## 4) LOG
# IN: OUT_CS
# LOG:
# 1) left를 전부 1로 초기화
# 2) 좌->우 순회하며 증가 구간이면 left 갱신
# 3) 우->좌 순회하며 right_need 갱신
# 4) ans += max(left[i], right_need)
# OUT_LOG:
# - pseudocode_steps: 위 1~4
# - update_order: left pass -> right pass + sum
# - io_flow: ratings 입력 -> 최소 총합 반환

## 5) PRF
# IN: OUT_LOG
# PRF:
# - left[i]는 왼쪽 조건을 만족하는 최소값
# - right_need는 오른쪽 조건을 만족하는 최소값
# - 두 조건을 동시에 만족하려면 i는 둘 중 큰 값 이상이어야 함
# - 따라서 max(left[i], right_need)를 더한 총합이 최소
# OUT_PRF:
# - correctness_claim: 양방향 최소 요구를 max로 결합하면 전역 최소
# - invariant_or_key_reason: 각 방향 최소 요구 하한 결합

## 6) TC/SC
# IN: OUT_LOG
# TC: O(n) (좌->우 1회 + 우->좌 1회)
# SC: O(n) (left 배열)
# OUT_CX:
# - final_tc_sc: O(n), O(n)
# - feasibility: True

## 7) IMP