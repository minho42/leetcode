# https://leetcode.com/problems/container-with-most-water/description/

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49

# Example 2:
# Input: height = [1,1]
# Output: 1

# Topics
# Array T
# wo Pointers
# Greedy

from typing import List


def maxArea(height: List[int]) -> int:
    m = 0
    i = 0
    j = len(height) - 1

    while i < j:
        w = j - i
        left = height[i]
        right = height[j]
        h = min(left, right)
        if (q := w * h) > m:
            print(i, j, w, h)
            m = q

        # move lower index to the next higher point to the middle
        if height[i] < height[j]:
            while i < j and left >= height[i]:
                i += 1
        else:
            while i < j and right >= height[j]:
                j -= 1
    return m


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(maxArea([1, 1]))
print(maxArea([2, 1]))
print(maxArea([1, 2]))
print(maxArea([1, 2, 4, 3]))
