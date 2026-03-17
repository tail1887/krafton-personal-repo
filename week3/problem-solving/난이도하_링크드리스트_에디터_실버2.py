# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406
# 문제 풀이:
# 1. 입력 받기
# 2. 링크드리스트 생성
# 3. 링크드리스트 탐색
# 4. 결과 출력

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# 입력 받기
n = int(input())
linked_list = LinkedList()
for _ in range(n):
    linked_list.append(input().strip())

# 결과 출력
linked_list.print_list()