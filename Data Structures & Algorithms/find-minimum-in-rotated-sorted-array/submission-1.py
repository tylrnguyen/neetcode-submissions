class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        n = 0, [1,2,3,4,5,6]

        n = 1, [6,1,2,3,4,5]
        n = 2, [5,6,1,2,3,4]
        n = 3, [4,5,6,1,2,3]
        n = 4, [3,4,5,6,1,2]
        n = 5, [2,3,4,5,6,1]
        n = 6, [1,2,3,4,5,6]

                      l m r
        n = 3, [4,5,6,1,2,3]
        min_num = 1


        '''

        # at most, the array has been rotated len(nums) times
        # binary search? 

        n = len(nums)
        l = 0
        r = n - 1

        min_num = nums[0]
        while l <= r: 

            if nums[l] < nums[r]:
                min_num = min(min_num, nums[l])
                break

            m = (l + r) // 2
            min_num = min(min_num, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1

        return min_num 