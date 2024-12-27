# https://leetcode.com/problems/roman-to-integer/description/


# Topics
# Hash Table
# Math
# String


class Solution:
    def romanToInt(self, s: str) -> int:
        # going backwards, if current symbol is smaller than prev, subtract, otherwise add
        # e.g.
        # IV: + V - I
        # LVIII: + I + I + I + V + L
        sym = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        r = 0
        prev = ""
        for x in s[::-1]:
            if prev and "IVXLCDM".index(x) < "IVXLCDM".index(prev):
                isAdding = False
            else:
                isAdding = True

            if isAdding:
                r += sym[x]
            else:
                r -= sym[x]

            prev = x
        return r


# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
