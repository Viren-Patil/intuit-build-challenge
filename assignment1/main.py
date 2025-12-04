from typing import List

from .buffer import BoundedBuffer
from .producer import Producer
from .consumer import Consumer


def run_demo():
    """
    Run a simple producer consumer demo.

    Sets up:
    - a source list of integers
    - a shared bounded buffer
    - a destination list
    and runs a producer and consumer thread to transfer all items.
    """
    source_data = list(range(1, 21))
    destination_data = []

    buffer = BoundedBuffer[int](capacity=5)

    producer = Producer(source=source_data, buffer=buffer, delay_seconds=0.01, verbose=True)
    consumer = Consumer(buffer=buffer, destination=destination_data, delay_seconds=0.02, verbose=True)

    print("Starting producer and consumer.")
    producer.start()
    consumer.start()

    producer.join()
    consumer.join()
    print("Producer and consumer have finished.")

    print("Source data:     ", source_data)
    print("Destination data:", destination_data)


if __name__ == "__main__":
    run_demo()
