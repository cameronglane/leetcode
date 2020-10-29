from collections import deque
import itertools

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_string = 0
        queue = deque([])
        
        for char in s:
            if queue.count(char) > 0:
                for _ in itertools.repeat(None,queue.index(char) + 1):
                    queue.popleft()
            queue.append(char)
            if len(queue) > longest_string:
                longest_string = len(queue)
        return longest_string