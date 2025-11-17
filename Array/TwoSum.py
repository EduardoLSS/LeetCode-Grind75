class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        neededValue = {}
        for index, item in enumerate(nums):
            complement = target - item
            if complement in neededValue:
                return [index, neededValue[complement]]
            neededValue[item] = index
        return []