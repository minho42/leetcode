# https://leetcode.com/problems/subsets/


# ref: https://youtu.be/L0NxT2i-LOY?si=BcQ29Dfw-qfRka7q

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

from typing import List

# Topics
# Array
# Backtracking
# Bit Manipulation


class Solution:
    # for-loop based backtracking
    def subsets2(self, nums: List[int]) -> List[List[int]]:
        r = []

        def backtrack(start, path):
            r.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return r

    # binary decision tree
    def subsets(self, nums: List[int]) -> List[List[int]]:
        r = []
        sol = []

        def backtrack(i):
            # base case
            if i == len(nums):
                r.append(sol[:])
                return

            # don't pick nums[i]
            backtrack(i + 1)

            # pick nums[i]
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)
        return r


s = Solution()
print(s.subsets([1, 2, 3]))
print(s.subsets2([1, 2, 3]))
