# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

def solution(expression):
    # '-' 연산자를 기준으로 문자열 분리
    parts = expression.split('-')
    
    # 첫 번째 부분은 그대로 더해주고, 나머지 부분들은 모두 빼준다.
    result = sum(map(int, parts[0].split('+')))  # 첫 번째 부분 계산
    for part in parts[1:]:
        result -= sum(map(int, part.split('+')))  # 나머지 부분 계산하여 빼줌
    
    return result