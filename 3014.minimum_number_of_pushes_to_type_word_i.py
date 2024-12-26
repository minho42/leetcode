# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/


class Solution:
    def minimumPushes(self, word: str) -> int:
        cost = 0

        s = set(sorted(word, key=lambda k: word.count(k), reverse=True))
        print(s)

        d = {}
        level = 0
        for i, w in enumerate(s):
            if i % 8 == 0:
                level += 1
            d[w] = level

        print(d)
        for w in word:
            cost += d[w]

        return cost


s = Solution()
print(s.minimumPushes("xycdefghij"))
