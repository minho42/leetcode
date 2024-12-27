# https://leetcode.com/problems/subsets-ii/description/

# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]


from typing import List

# Topics
# Array
# Backtracking
# Bit Manipulation


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        r = []

        def backtrack(start: int, path: List[int]):
            sorted_path = sorted(path[:])
            if sorted_path not in r:
                r.append(sorted_path)
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return r


s = Solution()
# print(s.subsetsWithDup([1, 2, 2]))
print(s.subsetsWithDup([4, 4, 4, 1, 4]))
