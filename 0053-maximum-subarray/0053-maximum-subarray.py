class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        final = float("-inf")
        sum = 0
        for i in nums:
            sum = sum+i
            final = max(final,sum)
            if (sum<0):
                sum=0
        return final