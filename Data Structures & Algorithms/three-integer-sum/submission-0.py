class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = sorted(nums)

        # [-4, -1, -1, 0, 1, 2]
        # i    j             k 

        # [-4, -1, -1, 0, 1, 4]
        # i    j             k 

        res = []

        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            j = i + 1
            k = len(arr) - 1

            while j < k:
                total = arr[i] + arr[j] + arr[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    res.append([arr[i], arr[j], arr[k]])
                    j += 1
                    k -= 1

                    while j < k and arr[j] == arr[j - 1]:
                        j += 1

        return res