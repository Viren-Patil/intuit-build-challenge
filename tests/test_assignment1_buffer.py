import pytest

from assignment1.buffer import BoundedBuffer


def test_invalid_capacity_raises_value_error():
    with pytest.raises(ValueError):
        BoundedBuffer(0)

    with pytest.raises(ValueError):
        BoundedBuffer(-5)


def test_fifo_single_thread_behavior():
    buf = BoundedBuffer[int](capacity=3)

    buf.put(1)
    buf.put(2)
    buf.put(3)

    assert buf.size() == 3
    assert buf.get() == 1
    assert buf.get() == 2
    assert buf.get() == 3
    assert buf.size() == 0


def test_is_empty_and_is_full_flags():
    buf = BoundedBuffer[int](capacity=2)

    assert buf.is_empty()
    assert not buf.is_full()

    buf.put(10)
    assert not buf.is_empty()
    assert not buf.is_full()

    buf.put(20)
    assert not buf.is_empty()
    assert buf.is_full()

    _ = buf.get()
    assert not buf.is_empty()
    assert not buf.is_full()

    _ = buf.get()
    assert buf.is_empty()
    assert not buf.is_full()
