from random import choice

class RandomizedSet:

    def __init__(self):
        self.container_list = []
        self.container_set = set()

    def insert(self, val: int) -> bool:
        if val in self.container_set:
            return False

        self.container_set.add(val)
        self.container_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.container_set:
            self.container_list.remove(val)
            self.container_set.remove(val)
            return True

        return False

    def getRandom(self) -> int:
        return choice(self.container_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()