# 그래프, BFS - Word Ladder
# 문제 링크: https://leetcode.com/problems/word-ladder/description/?envType=study-plan-v2&envId=top-interview-150
from collections import deque
# 그래프, BFS - Word Ladder
# 문제 링크: https://leetcode.com/problems/word-ladder/description/?envType=study-plan-v2&envId=top-interview-150

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        def bfs():
            #큐 초기화 및 초기값 생성 및 방문 배열 생성(set)및 초기화
            q = deque([(beginWord, 1)])
            visited = set()
            visited.add(beginWord)
            # a_z까지 있는 배열 생성
            alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
            while q:
                #하나꺼내서 순회돌기
                cur_word, level = q.popleft()
                #순회방식은 두가지
                #1. 각 자리에 알파벳 넣어서 배열에 있는지 확인하기 26*n
                # 알파벳 배열 생성 필요, 그리고 빠른 조회를 위해서 문자리스트를 집합으로 변경
                for i in range(len(beginWord)):
                    for alphabet in alphabets:
                        check = cur_word[:i] + alphabet + cur_word[i+1:]
                        if check in word_set and not check in visited:
                            visited.add(check)
                            if check == endWord:
                                return level+1
                            q.append([check, level+1])
            return 0
        return bfs()
