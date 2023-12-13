class Solution:
    def longestPalindrome(self, s: str) -> str:
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

print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("cbbd"))