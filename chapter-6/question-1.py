class HashItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"{{{self.key}: {self.value}}}"


class HashTable:
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0

    def __repr__(self):
        text = ""
        for index, slot in enumerate(self.slots):
            if slot:
                text += f", {index}: {slot}"
        plural = "" if self.used_slots == 1 else "s"
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]'

    def _hash(self, key):
        """
        Hashing function. Can be changed for a custom one.
        """
        return len(key) % self.size

    def _find_free_slot(self, start):
        """
        Starting from 'start' find the next free slot available.

        Parameters:
        - 'start': Starting point for the search.

        Returns: The index of the next free slot or None if no free slots
        """
        i = start
        count = 0
        while i < self.size:
            if count == 2:
                return None

            if self.slots[i] == None:
                return i

            if i == self.size - 1:
                count += 1
                i = 0
            else:
                i += 1


h = HashTable()

h.slots = [True] * 256


print(h._find_free_slot(0))
print(h._find_free_slot(16))
print(h._find_free_slot(17))
print(h._find_free_slot(33))
print(h._find_free_slot(46))
print(h._find_free_slot(49))
print(h._find_free_slot(64))
print(h._find_free_slot(65))
print(h._find_free_slot(253))
print(h._find_free_slot(254))
print(h._find_free_slot(255))
