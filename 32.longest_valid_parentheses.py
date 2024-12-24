# https://leetcode.com/problems/longest-valid-parentheses/description/

# Example 1:
# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".

# Example 2:
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

# Example 3:
# Input: s = ""
# Output: 0


# ref: https://youtu.be/r0-zx5ejdq0?si=l18n5DzhEXdNNiac


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        m = 0
        for i, _ in enumerate(s):
            si = stack[-1]
            stack.append(i)
            if (si >= 0 and s[si] == "(") and s[i] == ")":
                # print(m, stack)
                stack.pop()
                stack.pop()
                m = max(m, i - stack[-1])

        return m


s = Solution()

print(s.longestValidParentheses("()(()))())("))
