# 위상정렬 - 임계경로 (백준 플래5)
# 문제 링크: https://www.acmicpc.net/problem/1948
input_data = (word for line in sys.stdin for word in line.split())

n, m = int(next(input_data)), int(next(input_data))

#후순위 그래프 생성

graph = [[] for _ in range(n+1)]
reverse_graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = int(next(input_data)),int(next(input_data)),int(next(input_data))
    graph[u].append((v,w))
    reverse_graph[v].append((u, w))


#시작이랑 끝 입력 받기
start, end = int(next(input_data)), int(next(input_data))

# print(graph)

#차수 배열 생성 및 초기화ㅊㅊ
indegree = [0]*(n+1)

for i in range(1, n+1):
    for num in graph[i]:
        indegree[num[0]] += 1

# print(indegree)

def dp():        
    # 1. 큐 초기화 (리스트로 감싸줘야 함)
    q = deque([start]) 
    max_time = [0] * (n + 1)
    
    while q:
        #하나꺼내기
        cur = q.popleft()
        
        # 후속 노드들 확인 (graph[cur]로 수정)
        for next_node, weight in graph[cur]:
            # 3. 각 노드마다 맥스값 갱신
            max_time[next_node] = max(max_time[next_node], max_time[cur] + weight)
            
            # 4. 다음 노드의 진입 차수 감소
            indegree[next_node] -= 1
            
            # 5. 다음 노드의 차수가 0일 때 큐에 삽입
            if indegree[next_node] == 0:
                q.append(next_node)
                     
    return max_time

def bfs(max_time):
    q = deque([end]) # 도착점부터 시작
    visited = [False] * (n + 1)
    visited[end] = True
    count = 0 # 황금을 칠할 도로의 수
    
    while q:
        curr = q.popleft()
        
        # 역방향 그래프를 탐색 (curr로 들어왔던 이전 노드들을 확인)
        for prev_node, weight in reverse_graph[curr]:
            
            # 핵심 조건: "이 도로가 최장 경로의 일부인가?"
            if max_time[curr] == max_time[prev_node] + weight:
                count += 1 # 조건 맞으면 무조건 도로 개수 +1
                
                # 노드 중복 방문 방지 (큐에는 한 번만 넣음)
                if not visited[prev_node]:
                    visited[prev_node] = True
                    q.append(prev_node)
                    
    return count

# 실행 부분
# 1. DP를 통해 각 도시별 최장 도달 시간 계산
result_time_array = dp()

# 2. 도착 도시의 최장 시간 출력
print(result_time_array[end])

# 3. 역추적 BFS를 통해 임계 경로(도로) 개수 출력
print(bfs(result_time_array))