class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [1] * len(nums)
        r = [1] * len(nums)

        # [1,2,4,6]
        # l = [1,1,2,8]
        # r = [1,6,24.48]
        # reverse r 
        # r = [48,24,6,1]
        # multiply l and r for output 

        # construct l
        for i in range(1, len(nums)):
            l[i] = nums[i - 1] * l[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            r[i] = nums[i + 1] * r[i + 1]

        res = []
        for i in range(len(nums)):
            res.append(l[i] * r[i])
        
        return res
