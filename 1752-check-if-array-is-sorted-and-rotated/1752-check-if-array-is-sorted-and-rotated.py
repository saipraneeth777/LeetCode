class Solution:
    def check(self, nums: List[int]) -> bool:
        k=0
        while(k<=len(nums)):
            b = sorted(nums)
            b[:]=b[:][::-1]
            b[:k]=b[:k][::-1]
            b[k:]=b[k:][::-1]
            if(b==nums):
                return True
            k+=1
        return False