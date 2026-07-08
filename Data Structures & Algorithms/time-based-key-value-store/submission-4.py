class TimeMap:

    def __init__(self):
        self.values = {}
        self.timestamps = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.values:
            self.values[key].append(timestamp)
        else:
            self.values[key] = [timestamp]
        
        self.timestamps[(key,timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.values:
            return ""
        value = self.binary_search(key,timestamp)
        if value == -1:
            return ""
        return self.timestamps[(key, value)]

        
    def binary_search(self, key, value):
        l,r = 0, len(self.values[key])-1
        times = self.values[key]
        largest_val = -1 # If timestamp not present, largest smaller value
        while l<=r:
            mid = l +(r-l)//2 
            if times[mid] == value:
                return times[mid]
            elif value < times[mid]:
                r = mid-1
            elif value > times[mid] :
                largest_val = max(largest_val, times[mid]) 
                l = mid +1
        return largest_val
