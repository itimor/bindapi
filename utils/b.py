# -*- coding: utf-8 -*-
# author: itimor


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i
        return max_length


a = [2, 4, 3]
b = [5, 6, 4]
print(Solution().lengthOfLongestSubstring("abcabcbdab"))
