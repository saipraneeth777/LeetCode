class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup ={}
        for i in nums:
            if i in dup:
                return True
            else:
                dup[i]=1