class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap =[]
        heapq.heapify(minheap)

        for num in nums:
            if len(minheap) <k:
                heapq.heappush(minheap, num)
            elif minheap[0] < num:
                heapq.heappop(minheap)
                heapq.heappush(minheap, num)
        
        if minheap:
            return minheap[0]
        else: return -100000