from threading import Thread
from time import sleep
from typing import Iterable, Any, Optional

from .buffer import BoundedBuffer, SENTINEL


class Producer(Thread):
    """
    Producer thread that reads items from a source container and
    puts them into a shared bounded buffer.
    """

    def __init__(self, source: Iterable[Any], buffer: BoundedBuffer, delay_seconds: float = 0.0, verbose: bool = False):
        super().__init__()
        self.source = source
        self.buffer = buffer
        self.delay_seconds = delay_seconds
        self.verbose = verbose

    def run(self) -> None:
        for item in self.source:
            if self.delay_seconds > 0:
                sleep(self.delay_seconds)
            self.buffer.put(item)
            if self.verbose:
                print(f"[Producer] Produced: {item}")

        # Signal to consumer that production is complete.
        self.buffer.put(SENTINEL)
        if self.verbose:
            print("[Producer] Sent sentinel, production complete.")
