# https://leetcode.com/problems/generate-parentheses/description/


from typing import List

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Topics
# String
# Dynamic Programming
# Backtracking


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        r = []

        # binary decision tree backtracking
        # lc: "(" count
        # rc: ")" count
        def backtrack(path: List[str], lc, rc):
            # base cases
            if rc > lc:
                return
            if len(path) == n * 2:
                r.append("".join(path))
                return

            # go left
            if lc < n:
                path.append("(")
                backtrack(path, lc + 1, rc)
                path.pop()

            # go right
            if rc < n:
                path.append(")")
                backtrack(path, lc, rc + 1)
                path.pop()

            return

        backtrack([], 0, 0)
        return r


s = Solution()
# print(s.generateParenthesis(1))
print(s.generateParenthesis(3))
# print(s.generateParenthesis(6))
