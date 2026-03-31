# 그리디 - 멀티탭 스케줄링 (백준 골드1)
# 문제 링크: https://www.acmicpc.net/problem/1700
import sys
# 입력
input_data  = (word for line in sys.stdin for word in line.split())

n, k = int(next(input_data)), int(next(input_data))
uses = []
for i in range(k):
    uses.append(int(next(input_data)))
#####
print(uses)
#####
# 콘센트 집합 생성
multi_tab = set()
# 답 카운트 변수 생성 및 초기화
res = 0
# 수열의 처음부터 끝까지 순회하기
for i in range(k):
    # 먄약 집합에 있으면 스킵하기
    if uses[i] in multi_tab:
        continue
    # 집합에 없는데
    else:
        #공간이 있으면 집합에 넣기
        if len(multi_tab) < n:
            multi_tab.add(uses[i])
            # print(multi_tab)
        #공간이 없으면 하나 빼고 넣기    
        else:
            target_to_remove = 0
            far_idx = -1
            for plugged in multi_tab:
                if plugged not in uses[i+1:]:
                    target_to_remove = plugged
                    break
                else:
                    next_idx = uses[i+1:].index(plugged)
                    if next_idx > far_idx:
                        far_idx = next_idx
                        target_to_remove = plugged
            
            multi_tab.discard(target_to_remove)
            multi_tab.add(uses[i])
            res += 1
            # print(multi_tab)
#답 출력하기 
print(res)



            # # 집합과 남은 수열을 비교해야 함(순회방식)
            # for num in uses[k-1:i:-1]:
            #     if num in multi_tab and check == 0: #집합의 숫자가 남은 수열에 있고 check가 0일 경우에는 한번만 저장
            #         check = num
            #     elif num not in multi_tab:
            #         check2 = num
            # if check == 0:# 집합의 숫자가 남은 수열에 없을 경우 아무거나 빼기
            #     multi_tab.pop()
            # else: #있을 경우에는
            #     if check2 != 0: #만약 수열에 없는 집합의 숫자가 있을경우에 그 숫자를 제거하고
            #        multi_tab.discard(check2)
            #     else: #아니면 맨 처음 저장된 숫자 빼기
            #         multi_tab.discard(check)
            # multi_tab.add(uses[i])
            # print(multi_tab)
            # print(check)
            # res += 1