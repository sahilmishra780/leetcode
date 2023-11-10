class TimeMap:
    def __init__(self):
        self.mp = {}

    def set(self, key, value, timestamp):
        if key not in self.mp:
            self.mp [key] = []
        self.mp [key].append((timestamp, value))
        

    def get(self, key, timestamp):
        if key not in self.mp:
            return ""
        a = self.mp[key]
        l, r = 0, len(a) - 1
        ans = -1
        while l <= r:
            m = l + (r - l) // 2
            if a[m][0] == timestamp:
                return a[m][1]
            elif a[m][0] < timestamp:
                ans = m
                l = m + 1
            else:
                r = m -  1
        if ans != -1: return a[ans][1]
        return ""

timeMap = TimeMap()
timeMap.set("love","high",10)
timeMap.set("love","low",20)
timeMap.get("love",5)