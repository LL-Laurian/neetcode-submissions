class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r, max_piles = max(piles), max(piles)
        
        l = math.ceil(sum(piles)/h)
        res = 0

        while l <= r:
            mid = math.ceil((l+r)/2)
            #print(l, r, mid)
            if (r > max_piles):
                return -1
            acc = 0
            for p in piles:
                acc += math.ceil(p/mid)
            
            #print("acc", acc)
            if acc > h:
                l = mid +1 
            else:
                res = mid
                r = mid -1
        return res
