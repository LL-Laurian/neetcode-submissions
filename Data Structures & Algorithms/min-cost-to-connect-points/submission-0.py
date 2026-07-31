class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        remainings = set(tuple(point) for point in points)

        start = tuple(points[0])
        heap = [(0, start)]

        total = 0

        while remainings:
            cur_dis, point = heapq.heappop(heap)

            if point not in remainings:
                continue

            total += cur_dis
            remainings.remove(point)

            for remain in remainings:
                distance = abs(remain[0] - point[0]) + abs(remain[1] - point[1])
                heapq.heappush(heap, (distance, remain))

        return total