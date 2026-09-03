class TimeMap:

    def __init__(self):
        self.keyStore = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore:
            return ""
        arr = self.keyStore[key]
        print(arr)
        l, r = 0, len(arr)
        res = ""
        while l<r:
            mid = (l+r)//2
            if arr[mid][1] < timestamp:
                res= arr[mid][0]
                l = mid + 1
            elif arr[mid][1] > timestamp:
                r = mid
            else:
                return arr[mid][0]
        return res


