# https://leetcode.com/problems/first-missing-positive/

# Example 1:
# Input: nums = [1,2,0]
# Output: 3
# Explanation: The numbers in the range [1,2] are all in the array.

# Example 2:
# Input: nums = [3,4,-1,1]
# Output: 2
# Explanation: 1 is in the array but 2 is missing.

# Example 3:
# Input: nums = [7,8,9,11,12]
# Output: 1
# Explanation: The smallest positive integer 1 is missing.


from typing import List

# Topics
# Array
# Hash Table


def firstMissingPositive(nums: List[int]) -> int:
    d = {}
    for n in nums:
        d[n] = 1

    for i in range(1, len(nums) + 1):
        if i not in d:
            return i

    return max(nums) + 1


print(firstMissingPositive([1, 2, 0]))
print(firstMissingPositive([3, 4, -1, 1]))
print(firstMissingPositive([7, 8, 9, 11, 12]))
print(firstMissingPositive([1]))
print(firstMissingPositive([2]))
