# AsyncIO — Practical & Well-Documented Guide (Python)

This repository is a **learning-first, concept-driven guide** to Python’s **AsyncIO**.
It is designed to be **read, executed, and experimented with**, not skimmed.

The goal is to help you **build the correct mental model** of AsyncIO rather than
memorizing APIs.

## What This Repository Focuses On

This guide covers AsyncIO **from fundamentals to real-world usage**, including:

- Event loop fundamentals
- Coroutines and their lifecycle
- `await` mechanics and execution flow
- Tasks and cooperative concurrency
- `asyncio.gather` vs `asyncio.TaskGroup`
- Futures and result propagation
- Synchronization primitives:
  - Locks
  - Semaphores
  - Events
- Real-world concurrency patterns and pitfalls

## Learning Order (Recommended)

Follow the files in this exact order:

1. **When to use AsyncIO**
2. **Event Loop**
3. **Coroutines**
4. **`await` mechanics**
5. **Why naive async is still sequential**
6. **Tasks (`create_task`)**
7. **`asyncio.gather`**
8. **`TaskGroup` (Structured Concurrency)**
9. **Futures**
10. **Synchronization primitives**
    - Locks
    - Semaphores
    - Events

Each step intentionally answers **one question at a time**.


## What This Repository Is NOT

- ❌ Not a cheat sheet
- ❌ Not a framework-specific tutorial
- ❌ Not a performance benchmarking repo

This is a **foundational AsyncIO guide** meant to prepare you for:
- FastAPI
- Async database drivers
- Async message brokers (RabbitMQ, Kafka)
- High-concurrency backend systems

## Requirements

- Python **3.11 or newer**
- Basic Python knowledge (functions, classes, imports)

## How to Use This Repository

1. Read the file top to bottom
2. Predict the output before running
3. Execute the file
4. Modify delays, task counts, and logic
5. Observe how the event loop behaves

AsyncIO is best learned by **thinking**, not memorizing.

## References & Credits

### Video Reference

- **"AsyncIO in Python — Complete Guide"**  
  YouTube  
  https://www.youtube.com/watch?v=Qb9s3UiMSTA

  This video strongly influenced the **concept-first approach**, especially:
  - Building the event loop mental model
  - Understanding why `async` does not imply concurrency by default
  - Emphasizing *why* before *how*

> This repository does **not copy** the video content, but expands on the ideas
> with original explanations, structure, and runnable examples.

### Official Documentation

- Python AsyncIO Documentation  
  https://docs.python.org/3/library/asyncio.html

- AsyncIO TaskGroup (Python 3.11+)  
  https://docs.python.org/3/library/asyncio-task.html

- PEP 492 — Coroutines with `async` / `await`  
  https://peps.python.org/pep-0492/

- PEP 654 — Exception Groups and Task Groups  
  https://peps.python.org/pep-0654/

### Conceptual Influence

- Structured Concurrency principles
- Cooperative multitasking models
- Event-driven system design


## Final Note

AsyncIO does **not** make programs faster by default.
It makes them more **responsive**, **scalable**, and **efficient at waiting**.

Once the mental model clicks, everything else becomes obvious.