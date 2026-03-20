# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639
# 트리 - 이진 검색 트리 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/5639

import sys

sys.setrecursionlimit(10**6)

input_data = (word for line in sys.stdin for word in line.split())

preorder = list(map(int, input_data))

def postorder(start, end):
    if start > end: # 더 자를 게 없으면 돌아가!
        return
    
    root = preorder[start] # 1. 주머니에 루트(50) 챙기기
    
    # 2. 어디서 자를지 '가위 위치(mid)' 찾기
    mid = start + 1
    while mid <= end:
        if preorder[mid] > root: # 나보다 큰 놈 발견!
            break
        mid += 1
    
    # 3. 왼쪽 덩어리 시키기 (루트 다음부터 가위질 전까지)
    postorder(start + 1, mid - 1)
    
    # 4. 오른쪽 덩어리 시키기 (가위질 위치부터 끝까지)
    postorder(mid, end)
    
    # 5. 드디어 내가 내 번호 외치기! (후위 순회의 핵심)
    print(root)

postorder(0, len(preorder) - 1)