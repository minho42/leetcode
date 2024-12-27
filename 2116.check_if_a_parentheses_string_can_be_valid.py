# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/


# Topics
# String
# Stack
# Greedy


def isvalid_right_to_left(s, locked):
    luc, ruc = 0, 0
    llc, rlc = 0, 0

    i = len(s) - 1
    while i > 0:
        if s[i] == "(" and locked[i] == "0":
            luc += 1
        if s[i] == ")" and locked[i] == "0":
            ruc += 1
        if s[i] == "(" and locked[i] == "1":
            llc += 1
        if s[i] == ")" and locked[i] == "1":
            rlc += 1

        if llc > rlc + ruc + luc:
            return False

        i -= 1

    return True


def isvalid_left_to_right(s, locked):
    luc, ruc = 0, 0
    llc, rlc = 0, 0

    for i in range(len(s)):
        if s[i] == "(" and locked[i] == "0":
            luc += 1
        if s[i] == ")" and locked[i] == "0":
            ruc += 1
        if s[i] == "(" and locked[i] == "1":
            llc += 1
        if s[i] == ")" and locked[i] == "1":
            rlc += 1

        if rlc > llc + luc + ruc:
            return False

    return True


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False

        if s[0] == ")" and locked[0] == "1" or s[-1] == "(" and locked[-1] == "1":
            return False

        return isvalid_left_to_right(s, locked) and isvalid_right_to_left(s, locked)


s = Solution()
ss = "))()))"
locked = "010100"
print(s.canBeValid(ss, locked))
