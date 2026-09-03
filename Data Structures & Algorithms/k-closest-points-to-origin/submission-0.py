class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap =[]
        heapq.heapify(min_heap)
        for point in points:
            dist = math.sqrt((point[0])**2 + (point[1])**2)
            if len(min_heap)<k:
                heapq.heappush(min_heap, (-dist, point))
            else:
                if -min_heap[0][0] > dist:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, (-dist, point))
        
        res = []
        for _, point in min_heap:
            res.append(point)
        
        return res