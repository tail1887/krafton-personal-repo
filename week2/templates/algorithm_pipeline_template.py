# [문제명]
# 문제 링크: [URL]

## 1) CON
# CON:
# - 입력 크기/값 범위/제한(시간, 메모리) 확인
# - 허용 복잡도 상한 결정
# OUT_CON:
# - complexity_budget:
# - constraints_summary:
# - edge_inputs:

## 2) DEF
# IN: OUT_CON
# DEF:
# - 상태(state), 관계(rule), 목표(objective) 정의
# - 변수/배열/자료구조의 의미를 문장으로 고정
# OUT_DEF:
# - state_definition:
# - transition_or_rule:
# - objective:

## 3) CS
# IN: OUT_CON + OUT_DEF
# CS:
# - 후보 접근 2~3개(브루트포스 포함) 작성
# - 후보별 경우의 수/복잡도 계산
# - 탈락 후보와 근거 기록
# OUT_CS:
# - candidates_with_tc:
# - pruned_candidates:
# - selected_strategy:

## 4) LOG
# IN: OUT_CS
# LOG:
# - 채택 전략을 step 단위 의사코드로 변환
# - 갱신 순서(비교/삽입/삭제/누적) 고정
# OUT_LOG:
# - pseudocode_steps:
# - update_order:
# - io_flow:

## 5) PRF
# IN: OUT_LOG
# PRF:
# - 정당성 핵심 근거(불변식/귀납/반례 배제) 2~4줄
# OUT_PRF:
# - correctness_claim:
# - invariant_or_key_reason:

## 6) TC/SC
# IN: OUT_LOG
# TC:
# SC:
# OUT_CX:
# - final_tc_sc:
# - feasibility:

## 7) IMP
# IN: OUT_LOG + OUT_PRF + OUT_CX
# IMP:
# - 의사코드 순서를 유지하며 구현
# - edge case 선검증 -> 예제/반례 검증


def solve():
    # TODO: 입력 처리
    # TODO: 로직 구현
    # TODO: 출력
    pass


if __name__ == "__main__":
    solve()
