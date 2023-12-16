from typing import List

class Solution:
    def wordBreakMemo(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [None] * n
        def recurse(i):
            if i == n:
                return True
            if dp[i] != None:
                return dp[i]
            for word in wordDict:
                wordLen = len(word)
                if i + wordLen <= n and s[i:i + wordLen] == word:
                    if recurse(i + wordLen):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        
        return recurse(0)
    
    def wordBreakDp(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for word in wordDict:
                wordLen = len(word)
                if i + wordLen <= n and s[i:i + wordLen] == word:
                    dp[i] = dp[i + wordLen]
                    if dp[i]:
                        break        
        return dp[0]
    
assert Solution().wordBreakMemo("leetcode", ["leet","code"]) == True
assert Solution().wordBreakMemo("applepenapple", ["apple","pen"]) == True
assert Solution().wordBreakMemo("catsandog", ["cats","dog","sand","and","cat"]) == False
assert Solution().wordBreakMemo("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) == False

assert Solution().wordBreakDp("leetcode", ["leet","code"]) == True
assert Solution().wordBreakDp("applepenapple", ["apple","pen"]) == True
assert Solution().wordBreakDp("catsandog", ["cats","dog","sand","and","cat"]) == False
assert Solution().wordBreakDp("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]) == False

print("Success")

