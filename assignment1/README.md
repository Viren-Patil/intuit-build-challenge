
---

# **assignment1/README.md (copy paste exactly this)**

```markdown
# Assignment 1: Producer Consumer Pattern with Thread Synchronization

This module implements a classic producer consumer workflow using Python threads,
a custom bounded buffer, and explicit wait or notify coordination.

## Objectives Covered

### Thread synchronization
A shared `Lock` and two `Condition` objects ensure safe access to shared state:

- `_not_full` waits when the buffer is full and notifies when space becomes available  
- `_not_empty` waits when the buffer is empty and notifies when an item arrives  

### Blocking queue behavior
`BoundedBuffer` acts as a blocking queue:

- `put` blocks until space is available  
- `get` blocks until an item is available  

### Wait or notify mechanism
`Condition.wait()` suspends threads.  
`Condition.notify()` wakes a waiting thread at the appropriate time.

### Concurrent programming
Producer and consumer are subclasses of `threading.Thread` and run in parallel, moving data safely from a source container to a destination container.

## File Structure

assignment1/
│
├── buffer.py # BoundedBuffer implementation (blocking queue)
├── producer.py # Producer thread logic
├── consumer.py # Consumer thread logic
├── main.py # Demonstration script
└── README.md


## Design Overview

### BoundedBuffer
Implements a FIFO queue with:

- fixed capacity  
- blocking `put`  
- blocking `get`  
- single lock  
- condition variables for empty and full states  

It stores items internally with `collections.deque`.

### Sentinel Based Shutdown
A unique `SENTINEL` object signals completion:

- Producer inserts the sentinel after producing all items  
- Consumer stops when the sentinel is retrieved  

This avoids busy waiting or extra shared flags.

### Producer
Reads items from a source iterable, calls `buffer.put(item)`, and finally sends the sentinel.  
Optional delay simulates realistic pacing.  
Verbose mode prints each produced item.

### Consumer
Continuously calls `buffer.get()` and appends the result to a destination list.  
Stops cleanly when sentinel is received.  
Optional delay simulates slower consumption.  
Verbose mode prints each consumed item.

## Running the Demo

From the project root:

```bash
python -m assignment1.main
```

Expected output:

```
[Main] Starting producer and consumer.
[Producer] Produced: 1
[Consumer] Consumed: 1
...
[Producer] Sent sentinel, production complete.
[Consumer] Received sentinel, consumption complete.
[Main] Producer and consumer have finished.
[Main] Source data:      [...]
[Main] Destination data: [...]
```

The destination list should exactly match the source.

## Testing

Tests live under `tests/`:

`test_assignment1_buffer.py`

- FIFO behavior
- size tracking
- invalid capacity checks
- empty and full state checks

`test_assignment1_integration.py`

- full producer consumer pipeline
- empty source handling
- correctness even with capacity = 1

## Run tests

``bash
pytest
```