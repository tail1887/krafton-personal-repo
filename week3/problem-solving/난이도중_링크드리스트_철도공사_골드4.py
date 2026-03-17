# 링크드리스트 - 철도 공사 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/23309
# 문제 풀이:
# 1. 입력 받기
# 2. 링크드리스트 클래스 정의
# 3. 링크드리스트 클래스 호출
# 4. 결과 출력

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next
        print("No data")

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def add_after(self, data, next_data):
        new_node = Node(data)
        current = self.head
        while current:
            if current.data == next_data:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("No data")

# 입력 받기
def railway_construction(n, m):
    for _ in range(m):
        command = input().split()
        if command[0] == "add":
            linked_list.add_after(command[1], command[2])
        elif command[0] == "delete":
            linked_list.delete(command[1])
        elif command[0] == "print":
            linked_list.print_list()

n, m = map(int, input().split())
linked_list = LinkedList()
railway_construction(n, m) 