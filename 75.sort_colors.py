# https://leetcode.com/problems/sort-colors/

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Topics
# Array
# Two Pointers
# Sorting


from collections import Counter
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)

        k = 0
        for i in range(3):
            for j in range(c[i]):
                nums[k] = i
                k += 1


s = Solution()
nums = [2, 0, 2, 1, 1, 0]
s.sortColors(nums)
print(nums)
