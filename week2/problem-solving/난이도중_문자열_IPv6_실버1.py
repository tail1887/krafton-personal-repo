# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107
ipv6 = input()
ipv6 = ipv6.split(':')
for i in range(len(ipv6)):
    if ipv6[i] == '':
        ipv6[i] = '0' * (4 - len(ipv6[i]))
    elif len(ipv6[i]) < 4:
        ipv6[i] = '0' * (4 - len(ipv6[i])) + ipv6[i]
print(':'.join(ipv6))