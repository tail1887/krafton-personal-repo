# 그래프 - Course Schedule
# 문제 링크: https://leetcode.com/problems/course-schedule/?envType=study-plan-v2&envId=top-interview-150
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 1. 그래프 생성 및 진입 차수(indegree) 계산
        adj = defaultdict(list)
        indegree = [0] * numCourses
        
        for dest, src in prerequisites:
            adj[src].append(dest)
            indegree[dest] += 1
            
        # 2. 진입 차수가 0인 노드(선행 과목이 없는 과목)를 큐에 삽입
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        visited_count = 0
        
        # 3. 큐가 빌 때까지 반복
        while queue:
            current = queue.popleft()
            visited_count += 1
            
            # 현재 과목을 들었으므로, 이와 연결된 다음 과목들의 진입 차수를 1 감소
            for neighbor in adj[current]:
                indegree[neighbor] -= 1
                # 새롭게 진입 차수가 0이 된 과목이 있다면 큐에 추가
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 4. 방문한 노드 수가 전체 과목 수와 같다면 사이클이 없는 것
        return visited_count == numCourses