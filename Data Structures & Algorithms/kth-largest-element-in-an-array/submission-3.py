class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        stk = []
        max_heap = [-x for x in nums]

        heapq.heapify(max_heap)

        for i in range(k):
            stk.append(heapq.heappop(max_heap))
        
        result = stk.pop()
        return -result