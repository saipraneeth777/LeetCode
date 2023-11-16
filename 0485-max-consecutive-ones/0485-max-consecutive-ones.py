class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        value,count = 0,0
        for i in range(len(nums)):
            if (nums[i]!=0):
                count = count+1
                value = max(value,count)
            else:
                count = 0
        return value