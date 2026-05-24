#Problem Link: https://leetcode.com/problems/contains-duplicate/

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp_set = {}
        if len(nums)<2:
            return False
        for i in range(len(nums)):
            if nums[i] in temp_set:
                return True
            temp_set[nums[i]] = nums[i]
        return False