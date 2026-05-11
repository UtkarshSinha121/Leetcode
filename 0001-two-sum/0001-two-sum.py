class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newdict = {}
        for i in range(len(nums)):
            newdict[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in newdict and newdict[complement] != i:
                return [i, newdict[complement]]
        return []
