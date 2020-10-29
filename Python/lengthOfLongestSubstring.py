class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last, res, st = {}, 0, 0
        for i, v in enumerate(s):
            if v not in last or last[v] < st:
                res = max(res, i - st + 1)
            else:
                st = last[v] + 1
            last[v] = i
        return res