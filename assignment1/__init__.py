"""
Assignment 1: Producer consumer pattern with thread synchronization.

This package contains:
- BoundedBuffer: a thread safe bounded blocking queue
- Producer: a producer thread that reads from a source container
- Consumer: a consumer thread that writes into a destination container
"""

from .buffer import BoundedBuffer, SENTINEL
from .producer import Producer
from .consumer import Consumer

__all__ = ["BoundedBuffer", "SENTINEL", "Producer", "Consumer"]
