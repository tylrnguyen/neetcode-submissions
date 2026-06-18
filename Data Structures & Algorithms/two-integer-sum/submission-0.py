class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {} 
        '''  
        output = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                val = nums[i] + nums[j]
                if val == target: 
                    output.append(i)
                    output. append(j)
        return output
        '''
        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        return output