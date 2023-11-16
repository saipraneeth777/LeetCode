from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,i,r=0,0,len(nums)-1
        while(i<=r):
            if nums[i]<1:
                nums[i],nums[l]=nums[l],nums[i]
                l+=1
            elif nums[i]>1:
                nums[i],nums[r]=nums[r],nums[i]
                r-=1
                i-=1
            i+=1