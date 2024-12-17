# https://leetcode.com/problems/longest-common-prefix/


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

from typing import List


def allStartsWith(strs, str):
    r = set()
    for x in strs:
        if str not in x:
            return False
        r.add(x.index(str))
    return len(r) == 1


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest = ""
        sorted_strs = sorted(strs, key=lambda x: len(x))
        first = sorted_strs[0]

        for i in range(len(first)):
            text = first[0 : i + 1]
            if allStartsWith(strs, text):
                if len(text) > len(longest):
                    longest = text
        return longest


s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
print(s.longestCommonPrefix(["reflower", "flow", "flight"]))
