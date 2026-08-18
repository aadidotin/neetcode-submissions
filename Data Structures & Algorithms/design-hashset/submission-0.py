class MyHashSet:

    def __init__(self):
        self.data = []
        

    def add(self, key: int) -> None:
        self.data.append(key)
        self.data = list(set(self.data))

    def remove(self, key: int) -> None:
        try:
            self.data.remove(key)
        except:
            pass

    def contains(self, key: int) -> bool:
        return key in self.data


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)