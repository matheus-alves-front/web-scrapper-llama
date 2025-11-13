### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/asyncio-api-index.html "High-level API Index") \|
- [previous](https://docs.python.org/3/library/asyncio-platforms.html "Platform Support") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
- [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html) »
- [Extending](https://docs.python.org/3/library/asyncio-extending.html)
- \|

- Theme
AutoLightDark \|

# Extending [¶](https://docs.python.org/3/library/asyncio-extending.html\#extending "Link to this heading")

The main direction for [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") extending is writing custom _event loop_
classes. Asyncio has helpers that could be used to simplify this task.

Note

Third-parties should reuse existing asyncio code with caution,
a new Python version is free to break backward compatibility
in _internal_ part of API.

## Writing a Custom Event Loop [¶](https://docs.python.org/3/library/asyncio-extending.html\#writing-a-custom-event-loop "Link to this heading")

[`asyncio.AbstractEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop "asyncio.AbstractEventLoop") declares very many methods. Implementing all them
from scratch is a tedious job.

A loop can get many common methods implementation for free by inheriting from
`asyncio.BaseEventLoop`.

In turn, the successor should implement a bunch of _private_ methods declared but not
implemented in `asyncio.BaseEventLoop`.

For example, `loop.create_connection()` checks arguments, resolves DNS addresses, and
calls `loop._make_socket_transport()` that should be implemented by inherited class.
The `_make_socket_transport()` method is not documented and is considered as an
_internal_ API.

## Future and Task private constructors [¶](https://docs.python.org/3/library/asyncio-extending.html\#future-and-task-private-constructors "Link to this heading")

[`asyncio.Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future") and [`asyncio.Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task") should be never created directly,
please use corresponding [`loop.create_future()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_future "asyncio.loop.create_future") and [`loop.create_task()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task"),
or [`asyncio.create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task") factories instead.

However, third-party _event loops_ may _reuse_ built-in future and task implementations
for the sake of getting a complex and highly optimized code for free.

For this purpose the following, _private_ constructors are listed:

Future.\_\_init\_\_( _\*_, _loop=None_) [¶](https://docs.python.org/3/library/asyncio-extending.html#asyncio.Future.__init__ "Link to this definition")

Create a built-in future instance.

_loop_ is an optional event loop instance.

Task.\_\_init\_\_( _coro_, _\*_, _loop=None_, _name=None_, _context=None_) [¶](https://docs.python.org/3/library/asyncio-extending.html#asyncio.Task.__init__ "Link to this definition")

Create a built-in task instance.

_loop_ is an optional event loop instance. The rest of arguments are described in
[`loop.create_task()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task") description.

Changed in version 3.11: _context_ argument is added.

## Task lifetime support [¶](https://docs.python.org/3/library/asyncio-extending.html\#task-lifetime-support "Link to this heading")

A third party task implementation should call the following functions to keep a task
visible by [`asyncio.all_tasks()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.all_tasks "asyncio.all_tasks") and [`asyncio.current_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.current_task "asyncio.current_task"):

asyncio.\_register\_task( _task_) [¶](https://docs.python.org/3/library/asyncio-extending.html#asyncio._register_task "Link to this definition")

Register a new _task_ as managed by _asyncio_.

Call the function from a task constructor.

asyncio.\_unregister\_task( _task_) [¶](https://docs.python.org/3/library/asyncio-extending.html#asyncio._unregister_task "Link to this definition")

Unregister a _task_ from _asyncio_ internal structures.

The function should be called when a task is about to finish.

asyncio.\_enter\_task( _loop_, _task_) [¶](https://docs.python.org/3/library/asyncio-extending.html#asyncio._enter_task "Link to this definition")

Switch the current task to the _task_ argument.

Call the function just before executing a portion of embedded _coroutine_
( [`coroutine.send()`](https://docs.python.org/3/reference/datamodel.html#coroutine.send "coroutine.send") or [`coroutine.throw()`](https://docs.python.org/3/reference/datamodel.html#coroutine.throw "coroutine.throw")).

asyncio.\_leave\_task( _loop_, _task_) [¶](https://docs.python.org/3/library/asyncio-extending.html#asyncio._leave_task "Link to this definition")

Switch the current task back from _task_ to `None`.

Call the function just after [`coroutine.send()`](https://docs.python.org/3/reference/datamodel.html#coroutine.send "coroutine.send") or [`coroutine.throw()`](https://docs.python.org/3/reference/datamodel.html#coroutine.throw "coroutine.throw")
execution.

### [Table of Contents](https://docs.python.org/3/contents.html)

- [Extending](https://docs.python.org/3/library/asyncio-extending.html#)
  - [Writing a Custom Event Loop](https://docs.python.org/3/library/asyncio-extending.html#writing-a-custom-event-loop)
  - [Future and Task private constructors](https://docs.python.org/3/library/asyncio-extending.html#future-and-task-private-constructors)
  - [Task lifetime support](https://docs.python.org/3/library/asyncio-extending.html#task-lifetime-support)

#### Previous topic

[Platform Support](https://docs.python.org/3/library/asyncio-platforms.html "previous chapter")

#### Next topic

[High-level API Index](https://docs.python.org/3/library/asyncio-api-index.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/asyncio-extending.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/asyncio-api-index.html "High-level API Index") \|
- [previous](https://docs.python.org/3/library/asyncio-platforms.html "Platform Support") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
- [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html) »
- [Extending](https://docs.python.org/3/library/asyncio-extending.html)
- \|

- Theme
AutoLightDark \|