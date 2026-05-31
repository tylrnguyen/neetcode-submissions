class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a dict 
        seen = {} 

        # add key, value -> how many times it appears 

        for i in nums: 
            if i not in seen: 
                seen[i] = 0
            else:
                return True 
        
        return False
        


