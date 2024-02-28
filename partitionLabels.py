from typing import *

class Solution:
    def partitionLabelsMergeIntervals(self, s: str) -> List[int]:
        mp = {}
        for i, c in enumerate(list(s)):
            if c not in mp:
                mp[c] = [i, i]
            else:
                mp[c][1] = i
        vals =  list(mp.values())
        # no sorting of intervals needed as python dict preserves order
        # of insertion
        merged = []
        for start, end in vals:
            if not merged:
                merged.append([start, end])
            else:
                prevStart, prevEnd = merged[-1]
                if start <= prevEnd:
                    merged[-1] = [min(prevStart, start), max(prevEnd, end)]
                else:
                    merged.append([start, end])
        return [end - begin + 1 for begin, end in merged]
    
    def partitionLabelsGreedy(self, s: str) -> List[int]:
        mp = {}
        for i, c in enumerate(list(s)):
            mp[c] = i
        start, end = 0, 0
        ans = []
        for i in range(len(s)):
            c = s[i]
            end = max(end, mp[c])
            if end == i:
                ans.append(end - start + 1)
                start = i + 1
        return ans

soln = Solution()
assert soln.partitionLabelsMergeIntervals("ababcbacadefegdehijhklij") == [9,7,8]
assert soln.partitionLabelsMergeIntervals("eccbbbbdec") == [10]
assert soln.partitionLabelsGreedy("ababcbacadefegdehijhklij") == [9,7,8]
assert soln.partitionLabelsGreedy("eccbbbbdec") == [10]