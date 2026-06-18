class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if nums is None:
            return

        for i in nums:
            # since values in the array are 1 - n, find corresponding index
            idx = abs(i) - 1
            if nums[idx] > 0: 
                nums[idx] = -nums[idx]
            elif nums[idx] < 0: 
                return abs(i)
                

