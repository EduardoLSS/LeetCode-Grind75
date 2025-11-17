from typing import List # Not used in Leetcode, imported to stop problem check in VSCode
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        neededValue = {}
        for index, item in enumerate(nums):
            complement = target - item
            if complement in neededValue:
                return [index, neededValue[complement]]
            neededValue[item] = index
        return []