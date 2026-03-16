# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933

def find_password(words):
    for word in words:
        if word[::-1] in words:
            return word
    return None

words = []
for _ in range(int(input())):
    words.append(input())
print(find_password(words))