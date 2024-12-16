# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x2 = str(x)
        if len(x2) == 1:
            return True

        i = 0
        j = len(x2) - 1
        while i < len(x2) // 2:
            # print(f"x2[i]: {x2[i]}")
            # print(f"x2[j]: {x2[j]}")
            if x2[i] != x2[j]:
                return False
            i += 1
            j -= 1
        return True


s = Solution()
r = s.isPalindrome(100)
print(r)
