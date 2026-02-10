#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
class Solution:
    def twoSum(self, nums, target):
        seen = {}   # number -> index

        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in seen:
                return [seen[needed], i]

            seen[nums[i]] = i
