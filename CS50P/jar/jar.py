class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return ("🍪" * self.size)

    def deposit(self, n):
        if n > self.capacity or n + self.size > self.capacity:
            raise ValueError("Exceeded Capacity")
        self._size += n

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Exceeds cookie balance")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


jar = Jar()
jar.deposit(3)
jar.withdraw(1)
print(jar)
print(jar.capacity)
print(jar.size)
