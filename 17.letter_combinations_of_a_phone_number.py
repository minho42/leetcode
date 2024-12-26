# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


from typing import List

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]


d = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        r = []
        # e.g. digits: "23" -> input: ["abc", "def"]
        input = [d[digit] for digit in digits]

        # start: index for input
        def backtrack(path, start):
            # base case
            if len(path) == len(digits):
                path_str = "".join(path)
                if len(path) and path_str not in r:
                    r.append(path_str)
                return

            # for-loop based backtracking
            for i in range(len(input[start])):
                path.append(input[start][i])
                backtrack(path[:], start + 1)
                path.pop()

        backtrack([], 0)

        return r


s = Solution()
# print(s.letterCombinations("23"))
# print(s.letterCombinations(""))
# print(s.letterCombinations("2"))
# print(s.letterCombinations("234"))
# print(s.letterCombinations("7"))
print(s.letterCombinations("5678"))
