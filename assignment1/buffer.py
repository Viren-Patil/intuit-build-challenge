from collections import deque
from threading import Lock, Condition
from typing import Deque, Generic, TypeVar, Optional

T = TypeVar("T")

# Sentinel object used to signal completion from producer to consumer.
# It is guaranteed to be unique.
SENTINEL: object = object()


class BoundedBuffer(Generic[T]):
    """
    Thread safe bounded buffer implementing a blocking queue.

    Producers call put to add items.
    Consumers call get to remove items.

    When the buffer is full:
        put blocks until a consumer removes an item.
    When the buffer is empty:
        get blocks until a producer adds an item.
    """

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")

        self._capacity = capacity
        self._queue: Deque[T] = deque()

        self._lock: Lock = Lock()
        self._not_empty: Condition = Condition(self._lock)
        self._not_full: Condition = Condition(self._lock)

    def put(self, item: T) -> None:
        """
        Add an item to the buffer.
        Blocks if the buffer has reached capacity until space becomes available.
        """
        with self._not_full:
            # We wait while the buffer is full.
            while len(self._queue) >= self._capacity:
                self._not_full.wait()

            # There is space, add the item.
            self._queue.append(item)

            # Notify one waiting consumer that an item is available.
            self._not_empty.notify()

    def get(self) -> T:
        """
        Remove and return the next item from the buffer.
        Blocks if the buffer is empty until an item is available.
        """
        with self._not_empty:
            # We wait while the buffer is empty.
            while len(self._queue) == 0:
                self._not_empty.wait()

            # There is at least one item, remove it.
            item = self._queue.popleft()

            # Notify one waiting producer that there is free space.
            self._not_full.notify()

            return item

    def size(self) -> int:
        with self._lock:
            return len(self._queue)

    def capacity(self) -> int:
        return self._capacity

    def is_empty(self) -> bool:
        with self._lock:
            return len(self._queue) == 0

    def is_full(self) -> bool:
        with self._lock:
            return len(self._queue) >= self._capacity
