from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        h = []
        
        for key, value in count.items():
            if len(h)<k:
                heapq.heappush(h, (value, key))
            
            else:
                if h[0][0]< value:
                    heapq.heappop(h)
                    heapq.heappush(h, (value, key))
                else: continue
        
        return [x[1] for x in h]