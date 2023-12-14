class Solution:
    def longestPalindromeSlidingWindow(self, s: str) -> str:
        maxLen, maxL, maxR = 0, None, None

        for i in range(len(s)):
            """
            Start from indices l and r that form a palindrome and expand the window 
            to see if there are more palindromes around the current l, r
            1. When l and r start from the same pos i, they expand to form odd length palindroms
            2. When l and r start from 1-off positions i, i+1, they expand to form even length palindromes
            """    
            for l, r in ((i, i), (i, i+1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    currPalindromeLen = r - l + 1
                    if r - l + 1 > maxLen:
                        maxLen, maxL, maxR = currPalindromeLen, l, r
                    r += 1
                    l -= 1
        
        return s[maxL:maxR+1]
    
    def longestPalindromeDP(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        maxLen = 1
        maxLenStartIdx = 0

        for left in range(n - 1, -1, -1):
            for right in range(left, n):

                # Boundary characters match
                if s[left] == s[right]:
                    # Now, there are multiple cases for the substring formed via s[left,right]
                    # 1. substring is 1 char long i.e. left === right In this case yes it is a palindrome
                    # 2. substring is 2 char long i.e. left + 1 == right. In this case yes it is a palindrome as s[left] == s[right]
                    # 3. substring is 3 char long i.e  left + 2 == right. In this case again it is a palindrome as s[left] == s[right]
                    # 4. substring is > 3 char long. In this case the answer depends on the substring formed via s[left + 1, right - 1]

                    # Case 1, 2, and 3 can be summarized as right - left <= 2 or right - 1 <= left + 1
                    # Case 4 can be determined from the dp
                    if (right - 1 <= left + 1 or dp[left + 1][right - 1]):
                        dp[left][right] = True
                        curLen = right - left + 1
                        if curLen > maxLen:
                            maxLen = curLen
                            maxLenStartIdx = left
                            
        return s[maxLenStartIdx: maxLenStartIdx + maxLen]   
    
    def longestPalindromeRecursion(self, s: str) -> str:
        n = len(s)
        memo = [[-1] * n for _ in range(n)]
        def isPali(s, l, r):
            if l >= r:
                return True
            # now l < r, i.e substring is atleast 2 chars
            if s[l] != s[r]:
                return False
            # s[l] and s[r] are identical and substring is atleast 2 chars
            
            # Check if we have a cached result
            if memo[l][r] != -1:
                return memo[l][r]
            
            # No cached result. Update cache
            memo[l][r] = isPali(s, l + 1, r - 1)
            
            return memo[l][r]
        
        maxLen = 1
        maxLenStartIdx = 0

        for left in range(n):
            for right in range(left, n):
                if s[left] == s[right] and isPali(s, left + 1, right - 1):
                    curLen = right - left + 1
                    if curLen > maxLen:
                        maxLen = curLen
                        maxLenStartIdx = left

        return s[maxLenStartIdx: maxLenStartIdx + maxLen]   

print(Solution().longestPalindromeSlidingWindow("babad"))
print(Solution().longestPalindromeSlidingWindow("cbbd"))

print(Solution().longestPalindromeDP("babad"))
print(Solution().longestPalindromeDP("cbbd"))

print(Solution().longestPalindromeRecursion("babad"))
print(Solution().longestPalindromeRecursion("cbbd"))


