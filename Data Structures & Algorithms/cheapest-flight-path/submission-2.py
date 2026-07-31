from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for start, end, price in flights:
            adj[start].append((end, price))

        heap = []
        heapq.heappush(heap, (0, src, 0))
        # cost, node, flights_used

        while heap:
            curr_total, node, flights_used = heapq.heappop(heap)

            if node == dst:
                return curr_total

            if flights_used <= k:
                for nei, price in adj[node]:
                    heapq.heappush(heap, (curr_total + price, nei, flights_used + 1))

        return -1
