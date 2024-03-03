class Solution:    
    def checkValidStringGreedy(self, s: str) -> bool:
        """
        There are two conditions in which the string becomes unbalanced:
        1. During iteration we encounter too many ')'
        2. Post iteration we have still have '(' which don't have matching ')'

        Maintain two variables cmax and cmin. 

        cmax:
        - counts max number of '(' that COULD be paired with ')'
        - Here we treat each '*' as '(' to pair max number of ')'
        - So at any point if cmax < 0 it means with all '(' and '*' treated as '('
          we still have too many ')'. Return False in this case
        - Takes care of condition 1 i.e. too many ')'
        
        cmin:
        - counts min number of '(' that MUST be paired to make string valid.
        - Aim of cmin is to get to 0 ASAP. So we treat each '*' as ')' and whenever
          we see '*' or ')' we decrement cmin
        - cmin cannot be negative. If this happens we can assume that some of the past '*' were
          actually empty strings. Therefore everytime cmin < 0 we reset it to 0
        - Post iteration if cmin is still > 0 that means with all the '*' as ')' and the existing
          ')' we still have too many '('
        - Takes care of condition 2 i.e. too many '('
        """

        cmin = cmax = 0
        for c in s:
            if c == '(':
                cmax += 1
                cmin += 1
            elif c == ')':
                cmin -= 1
                cmax -= 1
            else: # '*'
                cmax += 1
                cmin -= 1
            
            if cmin < 0:
                cmin = 0
            if cmax < 0:
                return False
        
        return cmin == 0
    
    def checkValidStringRecursive(self, s: str) -> bool:
        def recurse(i, open):
            if i == len(s):
                return open == 0
            
            ans = False
            if s[i] == '*':
                # treat as open parentheses: '('
                ans |= recurse(i + 1, open + 1)
                # treat as close parentheses: ')'
                # adding a close bracket closes the open bracket so decrement open
                # add close bracket only if there are open brackets
                if open: 
                    ans |= recurse(i + 1, open - 1)
                # treat as empty
                ans |= recurse(i + 1, open)
            elif s[i] == '(':
                ans |= recurse(i + 1, open + 1)
            else: # s[i] == ')'
                if open:
                    ans |= recurse(i + 1, open - 1)
            return ans
        return recurse(0, 0)
    
    def checkValidStringMemo(self, s: str) -> bool:
        memo = [[-1] * len(s) for _ in range(len(s))]
        def recurse(i, open):
            if i == len(s):
                return open == 0
            
            if memo[i][open] != -1:
                return memo[i][open]
            ans = False
            if s[i] == '*':
                # treat as open parentheses: '('
                ans |= recurse(i + 1, open + 1)
                # treat as close parentheses: ')'
                # adding a close bracket closes the open bracket so decrement open
                # add close bracket only if there are open brackets
                if open: 
                    ans |= recurse(i + 1, open - 1)
                # treat as empty
                ans |= recurse(i + 1, open)
            elif s[i] == '(':
                ans |= recurse(i + 1, open + 1)
            else: # s[i] == ')'
                if open:
                    ans |= recurse(i + 1, open - 1)
            
            memo[i][open] = ans
            return ans
        
        return recurse(0, 0)

soln = Solution()

assert soln.checkValidStringGreedy("()") == True
assert soln.checkValidStringGreedy("(*)") == True
assert soln.checkValidStringGreedy("(*))") == True
assert soln.checkValidStringGreedy("(") == False

assert soln.checkValidStringRecursive("()") == True
assert soln.checkValidStringRecursive("(*)") == True
assert soln.checkValidStringRecursive("(*))") == True
assert soln.checkValidStringRecursive("(") == False

assert soln.checkValidStringMemo("()") == True
assert soln.checkValidStringMemo("(*)") == True
assert soln.checkValidStringMemo("(*))") == True
assert soln.checkValidStringMemo("(") == False

print("Success!!!")