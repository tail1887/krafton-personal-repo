# [문제명]
# 문제 링크: [URL]
# 사용 규칙:
# - 각 OUT_*은 "메모"가 아니라 다음 단계 IN으로 쓰는 입력값
# - 막히면 코드 고치기 전에 이전 OUT_*부터 수정
# - 최소 작성 순서: CON -> LOG -> IMP (입문), 권장: 7단계 전체

## 1) CON
# CON:
# - 입력 크기/값 범위/제한(시간, 메모리) 확인
# - 허용 복잡도 상한 결정
# OUT_CON:
# - complexity_budget: (예: O(N), O(N log N))
# - constraints_summary: (예: 중복 O, 음수 X, 정렬 X)
# - edge_inputs: (예: 빈 입력/최소/최대/단조/중복)

## 2) DEF
# IN: OUT_CON
# DEF:
# - 상태(state), 관계(rule), 목표(objective) 정의
# - 변수/배열/자료구조의 의미를 문장으로 고정
# OUT_DEF:
# - state_definition: (예: dp[i] = i까지의 최적값)
# - transition_or_rule: (예: dp[i] = max(dp[i-1], dp[i-2] + a[i]))
# - objective: (예: 최대 합 / 최소 비용 / 존재 여부)

## 3) CS
# IN: OUT_CON + OUT_DEF
# CS:
# - 후보 접근 2~3개(브루트포스 포함) 작성
# - 후보별 경우의 수/복잡도 계산
# - 탈락 후보와 근거 기록
# OUT_CS:
# - candidates_with_tc: (예: brute O(N^2), heap O(N log N), two-pointer O(N))
# - pruned_candidates: (예: brute -> complexity_budget 초과)
# - selected_strategy: (예: two-pointer)

## 4) LOG
# IN: OUT_CS
# LOG:
# - 채택 전략을 step 단위 의사코드로 변환
# - 갱신 순서(비교/삽입/삭제/누적) 고정
# OUT_LOG:
# - pseudocode_steps: (step1~stepK)
# - update_order: (예: 비교 -> 삭제 -> 삽입 -> 누적)
# - io_flow: (입력 -> 처리 -> 출력)

## 5) PRF
# IN: OUT_LOG
# PRF:
# - 정당성 핵심 근거(불변식/귀납/반례 배제) 2~4줄
# OUT_PRF:
# - correctness_claim: (이 알고리즘이 정답인 이유 한 줄)
# - invariant_or_key_reason: (유지되는 성질/핵심 근거)

## 6) TC/SC
# IN: OUT_LOG
# TC:
# - 반복 횟수 합산으로 계산
# SC:
# - 입력 외 추가 메모리 기준으로 계산
# OUT_CX:
# - final_tc_sc: (예: TC O(N), SC O(N))
# - feasibility: (True/False)

## 7) IMP
# IN: OUT_LOG + OUT_PRF + OUT_CX
# IMP:
# - 의사코드 순서를 유지하며 구현
# - edge case 선검증 -> 예제/반례 검증
# - 실패 시 역추적: IMP -> LOG -> CS -> DEF -> CON


def solve():
    # TODO: 입력 처리
    # TODO: 로직 구현
    # TODO: 출력
    pass


if __name__ == "__main__":
    solve()
