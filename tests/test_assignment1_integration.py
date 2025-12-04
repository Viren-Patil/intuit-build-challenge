# tests/test_assignment1_integration.py

from typing import List

from assignment1.buffer import BoundedBuffer
from assignment1.producer import Producer
from assignment1.consumer import Consumer


def _run_producer_consumer(source: List[int], capacity: int = 5) -> List[int]:
    destination: List[int] = []
    buffer = BoundedBuffer[int](capacity=capacity)

    producer = Producer(source=source, buffer=buffer, delay_seconds=0.0, verbose=False)
    consumer = Consumer(buffer=buffer, destination=destination, delay_seconds=0.0, verbose=False)

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    return destination


def test_all_items_transferred_preserve_order():
    source = list(range(1, 101))  # simple increasing sequence
    destination = _run_producer_consumer(source, capacity=10)

    # All items should be transferred in the same order.
    assert destination == source


def test_empty_source_results_in_empty_destination():
    source: List[int] = []
    destination = _run_producer_consumer(source, capacity=5)

    assert destination == []


def test_small_capacity_still_transfers_all_items():
    # Here capacity is 1 to force frequent blocking and wakeups.
    source = list(range(10))
    destination = _run_producer_consumer(source, capacity=1)

    assert destination == source
