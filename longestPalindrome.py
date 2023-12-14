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

        # dp[i][j] = True indicates that the string formed by s[i:j+1] (i.e. from s[i] to s[j] (inclusive))
        # is a palindrome
        dp = [[False] * n for _ in range(n)]

        # single characters are palindromes
        for i in range(n):
            dp[i][i] = True

        longest_palindrome_start, longest_palindrome_len = 0, 1

        for right in range(0, n): # right can be 0, 1, 2, ..., n - 1
            for left in range(right - 1, -1, -1): # left can be right - 1, right - 2, ..., 0

                if s[left] == s[right]:
                    # chars pointed by left and right match. 
                    
                    # Is the string formed from s[left+1] .. s[right - 1]?
                    # Yes if
                    # 1. right = left + 1 OR (no string formed therefore a palindrom)
                    # 2. dp[left + 1][right - 1] is True (we've previously determined the enclosed string to be a palindrom)
                    if right == left + 1 or dp[left + 1][right - 1]:
                        dp[left][right] = True
                        current_palindrome_len = right - left + 1
                        if current_palindrome_len > longest_palindrome_len:
                            longest_palindrome_start = left
                            longest_palindrome_len = current_palindrome_len
        return s[longest_palindrome_start:longest_palindrome_start + longest_palindrome_len]

print(Solution().longestPalindromeSlidingWindow("babad"))
print(Solution().longestPalindromeSlidingWindow("cbbd"))

print(Solution().longestPalindromeDP("babad"))
print(Solution().longestPalindromeDP("cbbd"))


