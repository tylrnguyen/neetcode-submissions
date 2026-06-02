class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # shouldn't sort, O(nlogn)

        # remove duplicates 
        arr = set(nums)

        longest = 0

        for i in nums:
            if (i - 1) not in arr: 
                length = 1
                while i + length in arr: 
                    length += 1
                longest = max(longest, length)
        return longest
                