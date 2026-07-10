class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            return self.move_to_front(key)
        return -1
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.move_to_front(key)
        else:
            if len(self.cache)  == self.capacity:
                idx = next(iter(self.cache))
                self.cache.pop(idx)
            self.cache[key] = value
        return None


    def move_to_front(self,key)-> int:
        val = self.cache.pop(key)
        self.cache[key] = val
        return val

        
