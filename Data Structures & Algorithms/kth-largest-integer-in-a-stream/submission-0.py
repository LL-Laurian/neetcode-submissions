class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort(reverse=True)
        self.k_largest = nums[:k]

        heapq.heapify(self.k_largest)

        

    def add(self, val: int) -> int:
        if len(self.k_largest) < self.k:
            heapq.heappush(self.k_largest, val)

        elif val > self.k_largest[0]:
            heapq.heappop(self.k_largest)
            heapq.heappush(self.k_largest, val)

        return self.k_largest[0]

        


