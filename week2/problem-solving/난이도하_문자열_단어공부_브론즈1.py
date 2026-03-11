# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157
s = input().upper()
max_count = 0
max_char = ''
for char in set(s):
    count = s.count(char)
    if count > max_count:
        max_count = count
        max_char = char
    elif count == max_count:
        max_char = '?'
print(max_char)