# https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        d = {}
        for x in s:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        if (
            d.get("(") != d.get(")")
            or d.get("[") != d.get("]")
            or d.get("{") != d.get("}")
        ):
            return False

        stack = []
        for i, _ in enumerate(s):
            if len(stack) == 0:
                stack.append(i)
                continue

            pi = stack[-1]
            stack.append(i)
            if (
                (s[pi] == "(" and s[i] == ")")
                or (s[pi] == "[" and s[i] == "]")
                or (s[pi] == "{" and s[i] == "}")
            ):
                stack.pop()
                stack.pop()

        return len(stack) == 0


s = Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("([)]"))
