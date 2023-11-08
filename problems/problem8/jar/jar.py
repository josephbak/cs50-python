class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        if int(n) + self._size > self._capacity:
            raise ValueError("Exceeding the number of cookies")
        else:
            self._size += int(n)

    def withdraw(self, n):
        if int(n) > self._size:
            raise ValueError("Not enugh number of cookies")
        else:
            self._size -= int(n)

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size