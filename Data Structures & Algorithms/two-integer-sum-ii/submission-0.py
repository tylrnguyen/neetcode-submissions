class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers) - 1

        while l < r: 
            num = numbers[r] + numbers[l]
            if target < num:
                r -= 1
            elif target > num:
                l += 1
            else:
                return [l + 1,r + 1]
