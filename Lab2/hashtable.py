class HashTable:
    def __init__(self, size=10):
        self.list = [[] for _ in range(size)]

    def add(self, item):
        index = self._index(item)
        bucket = self.list[index]
        if item not in bucket:
            bucket.append(item)
        return index, len(bucket) - 1

    def remove(self, item):
        bucket = self.list[self._index(item)]
        if item in bucket:
            bucket.remove(item)
            return True
        return False

    @staticmethod
    def _hash(key):
        return sum((index + 1) * ord(character) for index, character in enumerate(repr(key).lstrip("'")))

    def _index(self, key):
        return self._hash(key) % self.size()

    def __repr__(self):
        output = "B\tI\tItem"
        for index, bucket in enumerate(self.list):
            for item_index, item in enumerate(bucket):
                output += f"\n{index}\t{item_index}\t{repr(item)}"
        return output

    def __contains__(self, item):
        return item in self.list[self._index(item)]

    def get_pos(self, item):
        index = self._index(item)
        if item in self.list[index]:
            return index, self.list.index(item),
        return None

    def get_item(self, bucket, index):
        return self.list[bucket][index]

    def size(self):
        return len(self.list)

    def __len__(self):
        return len(self.list)