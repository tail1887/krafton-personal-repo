# 초보자용 단계별 알고리즘 템플릿

이 템플릿은 `CON -> DEF -> CS -> LOG -> PRF -> TC/SC -> IMP`를 한 번에 완벽히 하려는 용도가 아니다.  
처음에는 3단계만, 익숙해지면 5단계, 마지막에 7단계 전체를 적용한다.

---

## 0) 문제 정보

- 문제명:
- 링크:
- 제한 시간 / 메모리:
- 입력 크기(예: N 최대):
- 오늘 목표 단계:
  - [ ] Lv1 (CON, LOG, IMP)
  - [ ] Lv2 (CON, DEF, CS, LOG, IMP)
  - [ ] Lv3 (CON, DEF, CS, LOG, PRF, TC/SC, IMP)

---

## Lv1 (입문) - 15~25분

목표: "코드를 짜기 전에 최소한의 안전장치 만들기"

### 1) CON

- [ ] 입력 크기와 제한을 읽었다.
- [ ] 대략 허용 복잡도를 정했다.
- [ ] 최소 3개 edge case를 뽑았다.

기록:

- complexity_budget:
- edge_inputs: `[]`, `최소값`, `최대값`, `단조/중복` 중 해당 항목

### 2) LOG (간단 의사코드)

- [ ] 처리 순서를 3~5줄로 적었다.
- [ ] 반복문 종료 조건을 적었다.

기록:

1.
2.
3.

### 3) IMP

- [ ] 의사코드 순서대로 구현했다.
- [ ] edge case부터 테스트했다.

---

## Lv2 (기초) - 25~40분

목표: "왜 이 전략을 쓰는지 설명 가능하게 만들기"

### 1) CON

- complexity_budget:
- constraints_summary:
- edge_inputs:

### 2) DEF

- [ ] 상태를 1~2개 문장으로 정의했다.
- [ ] 목표(최소/최대/존재/개수)를 명시했다.

기록:

- state_definition:
- transition_or_rule:
- objective:

### 3) CS

- [ ] 후보 전략을 최소 2개 적었다.
- [ ] 후보별 복잡도를 계산했다.
- [ ] 하나를 탈락 근거와 함께 버렸다.

기록:

- candidates_with_tc:
- pruned_candidates:
- selected_strategy:

### 4) LOG + IMP

- pseudocode_steps:
- update_order:
- 구현 후 실패한 테스트:

---

## Lv3 (표준) - 40~60분

목표: "정답 근거 + 복잡도 근거까지 완성"

### 1) CON

- complexity_budget:
- constraints_summary:
- edge_inputs:

### 2) DEF

- state_definition:
- transition_or_rule:
- objective:

### 3) CS

- candidates_with_tc:
- pruned_candidates:
- selected_strategy:

### 4) LOG

- pseudocode_steps:
- update_order:
- io_flow:

### 5) PRF

- correctness_claim (1~2문장):
- invariant_or_key_reason (1~2문장):

### 6) TC/SC

- final_tc_sc:
- feasibility (True/False):

### 7) IMP

- [ ] OUT_LOG 순서 유지
- [ ] edge_inputs 선검증
- [ ] 예제 + 반례 1개 이상 통과

---

## 제출 전 1분 체크

- [ ] `OUT_*`이 다음 단계 `IN`으로 연결되어 있는가?
- [ ] 탈락한 전략의 이유를 설명할 수 있는가?
- [ ] 내 코드의 종료 조건을 한 문장으로 설명할 수 있는가?
- [ ] 틀렸을 때 어느 단계(CON/DEF/CS/LOG/PRF/TCSC)가 깨졌는지 말할 수 있는가?

---

## 오답 회고(필수)

- 틀린 원인 단계:
- 놓친 edge case:
- 다음 문제에서 고칠 1가지:

