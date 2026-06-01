class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # go thru, bucket the numbers in the array 
        # index of bucket, amount of times seen
        # then, iterate through buckets from right to left, taking top k elements 

        n = len(nums)

        # remember how to make buckets 
        buckets = [[] for _ in range(n + 1)]

        count = {}

        for i in nums: 
            if i not in count: 
                count[i] = 1
            else:
                count[i] += 1

        # items() returns both key AND value, enumerate returns index and value
        for num, frq in count.items():
            buckets[frq].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res 