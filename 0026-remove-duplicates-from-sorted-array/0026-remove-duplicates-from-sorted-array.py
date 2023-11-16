class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dicty = {}
        for i in nums:
            if i in dicty:
                dicty[i]+=1
            else:
                dicty[i]=1
        new_arr = list(dicty.keys())
        for i in range(len(new_arr)):
            nums[i]=new_arr[i]
        nums[len(new_arr):] = ''
        return len(new_arr)       