# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/


# Topics
# Math
# String
# Greedy


class Solution:
    def minimumPushes(self, word: str) -> int:
        s = set(sorted(word, key=lambda k: word.count(k), reverse=True))

        d = {}
        level = 0
        for i, w in enumerate(s):
            if i % 8 == 0:
                level += 1
            d[w] = level

        return sum(d.values())


s = Solution()
print(s.minimumPushes("xycdefghij"))
