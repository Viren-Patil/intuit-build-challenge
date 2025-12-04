from threading import Thread
from time import sleep
from typing import List, Any

from .buffer import BoundedBuffer, SENTINEL


class Consumer(Thread):

    def __init__(self, buffer: BoundedBuffer, destination: List[Any], delay_seconds: float = 0.0, verbose: bool = False):
        super().__init__()
        self.buffer = buffer
        self.destination = destination
        self.delay_seconds = delay_seconds
        self.verbose = verbose

    def run(self) -> None:
        while True:
            item = self.buffer.get()

            if item is SENTINEL:
                if self.verbose:
                    print("[Consumer] Received sentinel, consumption complete.")
                break

            if self.delay_seconds > 0:
                sleep(self.delay_seconds)

            self.destination.append(item)
            if self.verbose:
                print(f"[Consumer] Consumed: {item}")
