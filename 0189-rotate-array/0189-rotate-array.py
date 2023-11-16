class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)        
        nums[0:len(nums)] = nums[0:len(nums)][::-1]
        nums[0:k] = nums[0:k][::-1]
        nums[k:len(nums)] = nums[k:len(nums)][::-1]
        