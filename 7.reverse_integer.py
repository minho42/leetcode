# https://leetcode.com/problems/reverse-integer/

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Topics
# Math


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            n = str(x)[1:][::-1]
        else:
            sign = 1
            n = str(x)[::-1]
        r = sign * int(n)
        if -(2**31) <= r <= 2**31 - 1:
            return r
        else:
            return 0


s = Solution()
print(s.reverse(123))
print(s.reverse(-123))
print(s.reverse(120))
print(s.reverse(1534236469))
