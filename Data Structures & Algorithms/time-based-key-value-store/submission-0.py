class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = [[value, timestamp]]   
        else:
            self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        key_list = self.timeMap[key]
        L, R = 0, len(key_list)-1
        res = "" #candidate
        while L <= R:
            mid = (L+R)//2 
            if key_list[mid][1] == timestamp:
                return key_list[mid][0]
            elif key_list[mid][1] > timestamp:
                R = mid-1
            else:
                res = key_list[mid][0]
                L = mid+1

        return res
            #how t handle f there are multiple such values, it returns the value associated with the largest timestamp_prev

        
