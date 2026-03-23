# 트리 - Implement Trie (Prefix Tree)
# 문제 링크: https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150
# 트리 - Implement Trie (Prefix Tree)
# 문제 링크: https://leetcode.com/problems/implement-trie-prefix-tree/?envType=study-plan-v2&envId=top-interview-150
class TrieNode:
    def __init__(self):
        #자속 노드들을 저장
        self.children = {}
        #끝값확인 초기화
        self.is_end = False

class Trie(object):

    def __init__(self):

        self.root = TrieNode()


    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            # 만약 현재 글자가 자식 중에 없다면, 새 노드 생성
            if char not in curr.children:
                curr.children[char] = TrieNode()
            # 해당 글자 노드로 이동
            curr = curr.children[char]
        # 단어의 마지막 글자 노드에 '끝' 표시
        curr.is_end = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # 경로가 있더라도, 그게 '단어의 끝'으로 표시되어 있어야 진짜 존재하는 단어
        return curr.is_end
        
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for char in word: # prefix를 순회해야 함 (오타 주의)
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # 경로만 존재하면 '시작하는 단어'가 있는 것이므로 무조건 True
        return True

