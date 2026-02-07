# Python Concurrency & Parallelism

This repository is a **concept-first, execution-aware guide** to understanding how Python handles **concurrency, parallelism, and external processes**.

It focuses on **how things actually work**, not just *how to write syntax*.


## What This Repository Covers

This repository explains and contrasts:

* **Subprocess (OS-level processes)**
* **Threading (I/O-bound concurrency)**
* **AsyncIO (single-threaded cooperative concurrency)**
* **Multiprocessing (true parallelism)**
* **The Global Interpreter Lock (GIL)**

Each topic is treated as a **separate execution model**, not interchangeable buzzwords.


## Core Mental Model

Before diving in, internalize this:

> **Concurrency is about structure**
> **Parallelism is about execution**

You can have:

* Concurrency **without** parallelism
* Parallelism **without** concurrency
* Or both


## 1. Subprocess — Running External Commands

### What is Subprocess?

`subprocess` allows Python to **spawn and control external OS-level programs**.

This is **not threading** and **not multiprocessing inside Python**.

Each subprocess:

* Has its **own memory**
* Has its **own lifecycle**
* Is scheduled entirely by the **operating system**

### When to Use Subprocess

Use `subprocess` when you need to:

* Call system tools (`ls`, `grep`, `curl`, `git`, `ffmpeg`)
* Integrate Python with non-Python programs
* Capture `stdout`, `stderr`, and exit codes
* Build automation pipelines
* Replace shell scripts safely

### Key Characteristics

* Blocking by default
* Errors do **not** raise exceptions unless explicitly requested
* Output handling is explicit and controllable
* Ideal for system-level workflows


## 2. Threading — I/O-Bound Concurrency

### What is Threading?

Threading allows multiple **threads of execution** inside the **same Python process**.

Threads:

* Share memory
* Share global variables
* Are lightweight compared to processes

### What Threading is Good At

✔ I/O-bound tasks

✔ Network requests

✔ File operations

✔ Waiting on external resources

Threads shine when **waiting dominates execution time**.

### What Threading is NOT Good At

✖ CPU-bound tasks

✖ Heavy computation

✖ Parallel numerical work

Because of the **GIL**, threads cannot execute Python bytecode in parallel.

## 3. Thread Safety — Why Locks Exist

### The Core Problem

When multiple threads access **shared mutable state**, race conditions occur.

The issue is **not memory corruption**, but **logical corruption**.

### Why Locks Are Required

* Operations like `counter += 1` are **not atomic**
* Threads can interleave execution unpredictably
* Results vary across runs

### Key Idea

> **The GIL does NOT guarantee correctness**

Locks (`threading.Lock`) ensure:

* Mutual exclusion
* Deterministic behavior
* Data integrity


## 4. AsyncIO — Cooperative Concurrency

### What is AsyncIO?

AsyncIO is **single-threaded, single-process concurrency** driven by an **event loop**.

It works by:

* Suspending tasks at `await`
* Resuming other tasks while waiting
* Never blocking the event loop

### When AsyncIO Excels

✔ High-concurrency networking

✔ APIs & web servers

✔ Thousands of sockets

✔ Fine-grained control over scheduling

AsyncIO is ideal when **latency dominates** and **tasks spend time waiting**.

### What AsyncIO Is NOT

✖ Parallel execution

✖ CPU-bound acceleration

✖ A replacement for multiprocessing

AsyncIO provides **concurrency, not parallelism**.


## 5. Multiprocessing — True Parallelism

### What is Multiprocessing?

Multiprocessing uses **multiple OS processes**, each with:

* Its own Python interpreter
* Its own memory space
* Its own GIL

This allows **true parallel execution on multiple CPU cores**.

### When to Use Multiprocessing

✔ CPU-bound tasks

✔ Image processing

✔ Data transformation

✔ Scientific computation

Multiprocessing bypasses the GIL entirely.

### Trade-offs

* Higher memory usage
* Inter-process communication overhead
* Slower startup time
* Serialization (pickling) costs


## 6. Process Pools & Executors

### Why Pools Exist

Creating processes manually does not scale well.

Pools:

* Reuse worker processes
* Manage task distribution
* Balance workload automatically

### Two Common APIs

* `multiprocessing.Pool`
* `concurrent.futures.ProcessPoolExecutor`

Both simplify parallel execution while hiding OS complexity.


## 7. The Global Interpreter Lock (GIL)

### What the GIL Is

The GIL is a **mutex** that ensures:

* Only one thread executes Python bytecode at a time
* Memory safety for CPython

### What the GIL Solves

✔ Prevents memory corruption

✔ Simplifies garbage collection

✔ Makes C extensions safer

### What the GIL Does NOT Solve

✖ Logical race conditions

✖ Thread safety

✖ CPU-bound performance

### Key Takeaway

> **The GIL limits CPU-bound threading, not I/O-bound concurrency**


## Choosing the Right Model

### Decision Matrix

| Task Type             | Best Tool           |
| --------------------- | ------------------- |
| External commands     | Subprocess          |
| Network I/O           | Threading / AsyncIO |
| High-concurrency APIs | AsyncIO             |
| CPU-heavy work        | Multiprocessing     |
| Shared-memory logic   | Threading + Locks   |


## Final Takeaways

* There is **no single “best” concurrency model**
* Each tool solves a **different class of problems**
* Performance without correctness is meaningless
* Understanding execution models matters more than syntax


## Philosophy of This Repository

This repository is designed to help you:

* Think like the Python runtime
* Reason about execution, not just code
* Avoid cargo-cult concurrency
* Choose the right tool intentionally
