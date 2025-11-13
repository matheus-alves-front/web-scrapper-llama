### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/asyncio-llapi-index.html "Low-level API Index") \|
- [previous](https://docs.python.org/3/library/asyncio-extending.html "Extending") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
- [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html) »
- [High-level API Index](https://docs.python.org/3/library/asyncio-api-index.html)
- \|

- Theme
AutoLightDark \|

# High-level API Index [¶](https://docs.python.org/3/library/asyncio-api-index.html\#high-level-api-index "Link to this heading")

This page lists all high-level async/await enabled asyncio APIs.

## Tasks [¶](https://docs.python.org/3/library/asyncio-api-index.html\#tasks "Link to this heading")

Utilities to run asyncio programs, create Tasks, and
await on multiple things with timeouts.

|     |     |
| --- | --- |
| [`run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run") | Create event loop, run a coroutine, close the loop. |
| [`Runner`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.Runner "asyncio.Runner") | A context manager that simplifies multiple async function calls. |
| [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task") | Task object. |
| [`TaskGroup`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup "asyncio.TaskGroup") | A context manager that holds a group of tasks. Provides<br>a convenient and reliable way to wait for all tasks in the group to<br>finish. |
| [`create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task") | Start an asyncio Task, then returns it. |
| [`current_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.current_task "asyncio.current_task") | Return the current Task. |
| [`all_tasks()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.all_tasks "asyncio.all_tasks") | Return all tasks that are not yet finished for an event loop. |
| `await` [`sleep()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.sleep "asyncio.sleep") | Sleep for a number of seconds. |
| `await` [`gather()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather "asyncio.gather") | Schedule and wait for things concurrently. |
| `await` [`wait_for()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait_for "asyncio.wait_for") | Run with a timeout. |
| `await` [`shield()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.shield "asyncio.shield") | Shield from cancellation. |
| `await` [`wait()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait "asyncio.wait") | Monitor for completion. |
| [`timeout()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.timeout "asyncio.timeout") | Run with a timeout. Useful in cases when `wait_for` is not suitable. |
| [`to_thread()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.to_thread "asyncio.to_thread") | Asynchronously run a function in a separate OS thread. |
| [`run_coroutine_threadsafe()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.run_coroutine_threadsafe "asyncio.run_coroutine_threadsafe") | Schedule a coroutine from another OS thread. |
| `for in` [`as_completed()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.as_completed "asyncio.as_completed") | Monitor for completion with a `for` loop. |

Examples

- [Using asyncio.gather() to run things in parallel](https://docs.python.org/3/library/asyncio-task.html#asyncio-example-gather).

- [Using asyncio.wait\_for() to enforce a timeout](https://docs.python.org/3/library/asyncio-task.html#asyncio-example-waitfor).

- [Cancellation](https://docs.python.org/3/library/asyncio-task.html#asyncio-example-task-cancel).

- [Using asyncio.sleep()](https://docs.python.org/3/library/asyncio-task.html#asyncio-example-sleep).

- See also the main [Tasks documentation page](https://docs.python.org/3/library/asyncio-task.html#coroutine).


## Queues [¶](https://docs.python.org/3/library/asyncio-api-index.html\#queues "Link to this heading")

Queues should be used to distribute work amongst multiple asyncio Tasks,
implement connection pools, and pub/sub patterns.

|     |     |
| --- | --- |
| [`Queue`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue "asyncio.Queue") | A FIFO queue. |
| [`PriorityQueue`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.PriorityQueue "asyncio.PriorityQueue") | A priority queue. |
| [`LifoQueue`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.LifoQueue "asyncio.LifoQueue") | A LIFO queue. |

Examples

- [Using asyncio.Queue to distribute workload between several\\
Tasks](https://docs.python.org/3/library/asyncio-queue.html#asyncio-example-queue-dist).

- See also the [Queues documentation page](https://docs.python.org/3/library/asyncio-queue.html#asyncio-queues).


## Subprocesses [¶](https://docs.python.org/3/library/asyncio-api-index.html\#subprocesses "Link to this heading")

Utilities to spawn subprocesses and run shell commands.

|     |     |
| --- | --- |
| `await` [`create_subprocess_exec()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_exec "asyncio.create_subprocess_exec") | Create a subprocess. |
| `await` [`create_subprocess_shell()`](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.create_subprocess_shell "asyncio.create_subprocess_shell") | Run a shell command. |

Examples

- [Executing a shell command](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio-example-subprocess-shell).

- See also the [subprocess APIs](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio-subprocess)
documentation.


## Streams [¶](https://docs.python.org/3/library/asyncio-api-index.html\#streams "Link to this heading")

High-level APIs to work with network IO.

|     |     |
| --- | --- |
| `await` [`open_connection()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection") | Establish a TCP connection. |
| `await` [`open_unix_connection()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_unix_connection "asyncio.open_unix_connection") | Establish a Unix socket connection. |
| `await` [`start_server()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server") | Start a TCP server. |
| `await` [`start_unix_server()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_unix_server "asyncio.start_unix_server") | Start a Unix socket server. |
| [`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader") | High-level async/await object to receive network data. |
| [`StreamWriter`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter") | High-level async/await object to send network data. |

Examples

- [Example TCP client](https://docs.python.org/3/library/asyncio-stream.html#asyncio-example-stream).

- See also the [streams APIs](https://docs.python.org/3/library/asyncio-stream.html#asyncio-streams)
documentation.


## Synchronization [¶](https://docs.python.org/3/library/asyncio-api-index.html\#synchronization "Link to this heading")

Threading-like synchronization primitives that can be used in Tasks.

|     |     |
| --- | --- |
| [`Lock`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Lock "asyncio.Lock") | A mutex lock. |
| [`Event`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Event "asyncio.Event") | An event object. |
| [`Condition`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Condition "asyncio.Condition") | A condition object. |
| [`Semaphore`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore "asyncio.Semaphore") | A semaphore. |
| [`BoundedSemaphore`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.BoundedSemaphore "asyncio.BoundedSemaphore") | A bounded semaphore. |
| [`Barrier`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier "asyncio.Barrier") | A barrier object. |

Examples

- [Using asyncio.Event](https://docs.python.org/3/library/asyncio-sync.html#asyncio-example-sync-event).

- [Using asyncio.Barrier](https://docs.python.org/3/library/asyncio-sync.html#asyncio-example-barrier).

- See also the documentation of asyncio
[synchronization primitives](https://docs.python.org/3/library/asyncio-sync.html#asyncio-sync).


## Exceptions [¶](https://docs.python.org/3/library/asyncio-api-index.html\#exceptions "Link to this heading")

|     |     |
| --- | --- |
| [`asyncio.CancelledError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError") | Raised when a Task is cancelled. See also [`Task.cancel()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task.cancel "asyncio.Task.cancel"). |
| [`asyncio.BrokenBarrierError`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.BrokenBarrierError "asyncio.BrokenBarrierError") | Raised when a Barrier is broken. See also [`Barrier.wait()`](https://docs.python.org/3/library/asyncio-sync.html#asyncio.Barrier.wait "asyncio.Barrier.wait"). |

Examples

- [Handling CancelledError to run code on cancellation request](https://docs.python.org/3/library/asyncio-task.html#asyncio-example-task-cancel).

- See also the full list of
[asyncio-specific exceptions](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio-exceptions).


### [Table of Contents](https://docs.python.org/3/contents.html)

- [High-level API Index](https://docs.python.org/3/library/asyncio-api-index.html#)
  - [Tasks](https://docs.python.org/3/library/asyncio-api-index.html#tasks)
  - [Queues](https://docs.python.org/3/library/asyncio-api-index.html#queues)
  - [Subprocesses](https://docs.python.org/3/library/asyncio-api-index.html#subprocesses)
  - [Streams](https://docs.python.org/3/library/asyncio-api-index.html#streams)
  - [Synchronization](https://docs.python.org/3/library/asyncio-api-index.html#synchronization)
  - [Exceptions](https://docs.python.org/3/library/asyncio-api-index.html#exceptions)

#### Previous topic

[Extending](https://docs.python.org/3/library/asyncio-extending.html "previous chapter")

#### Next topic

[Low-level API Index](https://docs.python.org/3/library/asyncio-llapi-index.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/asyncio-api-index.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/asyncio-llapi-index.html "Low-level API Index") \|
- [previous](https://docs.python.org/3/library/asyncio-extending.html "Extending") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
- [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html) »
- [High-level API Index](https://docs.python.org/3/library/asyncio-api-index.html)
- \|

- Theme
AutoLightDark \|