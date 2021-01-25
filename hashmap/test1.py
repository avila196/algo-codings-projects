class HashMap:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _get_hash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size


    def insert(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

    def keys(self):
        arr = []
        for i in range(0, len(self.map)):
            if self.map[i]:
                arr.append(self.map[i][0])
        return arr

    def print(self):
        for item in self.map:
            if item is not None:
                print(str(item))

if __name__ == "__main__":
    h = HashMap()
    h.insert(3, 8)
    h.insert(14, 15)
    h.insert(50, 20)
    h.insert(27, -5)
    h.insert(36, 40)
    h.print()

# h = HashMap()
# h.add(5, 3)
# h.add(1, 2)
# h.add('Ming', '333-8233')
# h.add('Ankit', '293-8625')
# h.add('Aditya', '852-6551')
# h.add('Alicia', '632-4123')
# h.add('Mike', '567-2188')
# h.add('Aditya', '777-8888')
# h.print()
# h.delete('Bob')
# h.print()
# print('Ming: ' + h.get('Ming'))
# print(h.keys())

