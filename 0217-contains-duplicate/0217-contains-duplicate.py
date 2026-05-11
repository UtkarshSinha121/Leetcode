class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newdict = {}
        for i in range(len(nums)):
            if nums[i] in newdict:
                return True
            else:
                newdict[nums[i]] = i
        return False
        