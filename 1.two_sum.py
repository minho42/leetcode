# https://leetcode.com/problems/two-sum/description/

# nums = [2,7,11,15]
# target = 9

# nums = [3,2,4]
# target = 6

# nums = [3,3]
# target = 6

nums = [-1,-2,-3,-4,-5]
target = -8

def two_sum(nums, target):
    a = sorted(nums)
    
    for i in range(len(a)-1):
        for j in range(1, len(a)):
            print(a[i], a[j], a[i]+a[j])
            if a[i] + a[j] == target:
                first = nums.index(a[i])
                second = len(nums) - nums[::-1].index(a[j])- 1
                return [first, second]
        

def two_sum_hash(nums, target):
    h = {}
    
    for i in range(len(nums)):
        h[nums[i]] = i
    
    for i in range(len(nums)):
        y = target - nums[i]
        if y in h and h[y] != i:
            return [i, h[y]]

r = two_sum(nums, target)
print(r)

r2 = two_sum_hash(nums, target)
print(r2)