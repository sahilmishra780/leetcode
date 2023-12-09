from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLengthWithTrick(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                regex = word[:i] + "*" + word[i+1:]
                adj[regex].append(word)
        
        visited = set([beginWord])
        q = deque([beginWord])
        ans = 1
        while q:
            sz = len(q)
            for _ in range(sz):
                word = q.popleft()
                if word == endWord:
                    return ans
                for i in range(len(word)):
                    regex = word[:i] + "*" + word[i+1:]
                    for match in adj[regex]:
                        if match not in visited:
                            visited.add(match)
                            q.append(match)
            ans += 1
        
        return 0

    def ladderLengthAtoZ(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        allWords = set(wordList)
        if endWord not in allWords:
            return 0
        
        q = deque([beginWord])
        visited = set([beginWord])
        ans = 1
        while q:
            sz = len(q)
            for _ in range(sz):
                word = q.popleft()
                if word == endWord:
                    return ans
                
                for i in range(len(word)):
                    for charCode in range(ord('a'), ord('z')+1):
                        oneOffWord = word[:i] + chr(charCode) + word[i+1:]
                        if oneOffWord in allWords and oneOffWord not in visited:
                            q.append(oneOffWord)
                            visited.add(oneOffWord)
            ans += 1
        return 0
    
    def ladderLengthAdjacenyList(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        allWords = set(wordList)
        
        if endWord not in allWords:
            return 0
        
        adj = defaultdict(set)
        allWords.add(beginWord)
        for word in allWords:
            for i in range(len(word)):
                for charCode in range(ord('a'), ord('z')+1):
                    oneOffWord = word[:i] + chr(charCode) + word[i+1:]
                    if oneOffWord != word and oneOffWord in allWords:
                       adj[word].add(oneOffWord)
                       adj[oneOffWord].add(word)
        
        q = deque([beginWord])
        visited = set([beginWord])
        ans = 1
        while q:
            sz = len(q)
            for _ in range(sz):
                word = q.popleft()
                if word == endWord:
                    return ans
                
                for oneOffWord in adj[word]:
                    if oneOffWord not in visited:
                        q.append(oneOffWord)
                        visited.add(oneOffWord)
            ans += 1
        return 0

print(Solution().ladderLengthWithTrick("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(Solution().ladderLengthAtoZ("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
print(Solution().ladderLengthAdjacenyList("hit", "cog", ["hot","dot","dog","lot","log","cog"]))