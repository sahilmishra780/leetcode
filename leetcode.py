from typing import *

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = ""

class Solution:
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word
    
    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return len(node.word) > 0
    
    def buildTrie(self, words):
        self.root = TrieNode()
        for word in words:
            self.add(word)

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.buildTrie(words)

        R, C = len(board), len(board[0])
        ans = []
        def bt(r, c, node):
            if node.word:
                ans.append(node.word)
                node.word = ""
            if (
                r < 0 or
                r >= R or
                c < 0 or
                c >= C
            ):
                return
            s = board[r][c]
            if s not in node.children:
                return
            board[r][c] = "#"
            node = node.children[s]
            bt(r - 1, c, node)
            bt(r + 1, c, node)
            bt(r, c - 1, node)
            bt(r, c + 1, node)
            board[r][c] = s

        for r in range(R):
            for c in range(C):
                s = board[r][c]
                if s in self.root.children:
                    bt(r, c, self.root)
        return ans

Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])