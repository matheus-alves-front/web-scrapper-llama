### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/asyncio-protocol.html "Transports and Protocols") \|
- [previous](https://docs.python.org/3/library/asyncio-eventloop.html "Event Loop") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
- [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html) »
- [Futures](https://docs.python.org/3/library/asyncio-future.html)
- \|

- Theme
AutoLightDark \|

# Futures [¶](https://docs.python.org/3/library/asyncio-future.html\#futures "Link to this heading")

**Source code:** [Lib/asyncio/futures.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/futures.py),
[Lib/asyncio/base\_futures.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/base_futures.py)

* * *

_Future_ objects are used to bridge **low-level callback-based code**
with high-level async/await code.

## Future Functions [¶](https://docs.python.org/3/library/asyncio-future.html\#future-functions "Link to this heading")

asyncio.isfuture( _obj_) [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.isfuture "Link to this definition")

Return `True` if _obj_ is either of:

- an instance of [`asyncio.Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future"),

- an instance of [`asyncio.Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task"),

- a Future-like object with a `_asyncio_future_blocking`
attribute.


Added in version 3.5.

asyncio.ensure\_future( _obj_, _\*_, _loop=None_) [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.ensure_future "Link to this definition")

Return:

- _obj_ argument as is, if _obj_ is a [`Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future"),
a [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task"), or a Future-like object ( [`isfuture()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.isfuture "asyncio.isfuture")
is used for the test.)

- a [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task") object wrapping _obj_, if _obj_ is a
coroutine ( [`iscoroutine()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.iscoroutine "asyncio.iscoroutine") is used for the test);
in this case the coroutine will be scheduled by
`ensure_future()`.

- a [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task") object that would await on _obj_, if _obj_ is an
awaitable ( [`inspect.isawaitable()`](https://docs.python.org/3/library/inspect.html#inspect.isawaitable "inspect.isawaitable") is used for the test.)


If _obj_ is neither of the above a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised.

Important

Save a reference to the result of this function, to avoid
a task disappearing mid-execution.

See also the [`create_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task "asyncio.create_task") function which is the
preferred way for creating new tasks or use [`asyncio.TaskGroup`](https://docs.python.org/3/library/asyncio-task.html#asyncio.TaskGroup "asyncio.TaskGroup")
which keeps reference to the task internally.

Changed in version 3.5.1: The function accepts any [awaitable](https://docs.python.org/3/glossary.html#term-awaitable) object.

Deprecated since version 3.10: Deprecation warning is emitted if _obj_ is not a Future-like object
and _loop_ is not specified and there is no running event loop.

asyncio.wrap\_future( _future_, _\*_, _loop=None_) [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.wrap_future "Link to this definition")

Wrap a [`concurrent.futures.Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future") object in a
[`asyncio.Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future") object.

Deprecated since version 3.10: Deprecation warning is emitted if _future_ is not a Future-like object
and _loop_ is not specified and there is no running event loop.

## Future Object [¶](https://docs.python.org/3/library/asyncio-future.html\#future-object "Link to this heading")

_class_ asyncio.Future( _\*_, _loop=None_) [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "Link to this definition")

A Future represents an eventual result of an asynchronous
operation. Not thread-safe.

Future is an [awaitable](https://docs.python.org/3/glossary.html#term-awaitable) object. Coroutines can await on
Future objects until they either have a result or an exception
set, or until they are cancelled. A Future can be awaited multiple
times and the result is same.

Typically Futures are used to enable low-level
callback-based code (e.g. in protocols implemented using asyncio
[transports](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-transports-protocols))
to interoperate with high-level async/await code.

The rule of thumb is to never expose Future objects in user-facing
APIs, and the recommended way to create a Future object is to call
[`loop.create_future()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_future "asyncio.loop.create_future"). This way alternative event loop
implementations can inject their own optimized implementations
of a Future object.

Changed in version 3.7: Added support for the [`contextvars`](https://docs.python.org/3/library/contextvars.html#module-contextvars "contextvars: Context Variables") module.

Deprecated since version 3.10: Deprecation warning is emitted if _loop_ is not specified
and there is no running event loop.

result() [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.result "Link to this definition")

Return the result of the Future.

If the Future is _done_ and has a result set by the
[`set_result()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.set_result "asyncio.Future.set_result") method, the result value is returned.

If the Future is _done_ and has an exception set by the
[`set_exception()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.set_exception "asyncio.Future.set_exception") method, this method raises the exception.

If the Future has been _cancelled_, this method raises
a [`CancelledError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError") exception.

If the Future’s result isn’t yet available, this method raises
an [`InvalidStateError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.InvalidStateError "asyncio.InvalidStateError") exception.

set\_result( _result_) [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.set_result "Link to this definition")

Mark the Future as _done_ and set its result.

Raises an [`InvalidStateError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.InvalidStateError "asyncio.InvalidStateError") error if the Future is
already _done_.

set\_exception( _exception_) [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.set_exception "Link to this definition")

Mark the Future as _done_ and set an exception.

Raises an [`InvalidStateError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.InvalidStateError "asyncio.InvalidStateError") error if the Future is
already _done_.

done() [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.done "Link to this definition")

Return `True` if the Future is _done_.

A Future is _done_ if it was _cancelled_ or if it has a result
or an exception set with [`set_result()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.set_result "asyncio.Future.set_result") or
[`set_exception()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.set_exception "asyncio.Future.set_exception") calls.

cancelled() [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.cancelled "Link to this definition")

Return `True` if the Future was _cancelled_.

The method is usually used to check if a Future is not
_cancelled_ before setting a result or an exception for it:

Copy

```
if not fut.cancelled():
    fut.set_result(42)
```

add\_done\_callback( _callback_, _\*_, _context=None_) [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.add_done_callback "Link to this definition")

Add a callback to be run when the Future is _done_.

The _callback_ is called with the Future object as its only
argument.

If the Future is already _done_ when this method is called,
the callback is scheduled with [`loop.call_soon()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon").

An optional keyword-only _context_ argument allows specifying a
custom [`contextvars.Context`](https://docs.python.org/3/library/contextvars.html#contextvars.Context "contextvars.Context") for the _callback_ to run in.
The current context is used when no _context_ is provided.

[`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") can be used to pass parameters
to the callback, e.g.:

Copy

```
# Call 'print("Future:", fut)' when "fut" is done.
fut.add_done_callback(
    functools.partial(print, "Future:"))
```

Changed in version 3.7: The _context_ keyword-only parameter was added.
See [**PEP 567**](https://peps.python.org/pep-0567/) for more details.

remove\_done\_callback( _callback_) [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.remove_done_callback "Link to this definition")

Remove _callback_ from the callbacks list.

Returns the number of callbacks removed, which is typically 1,
unless a callback was added more than once.

cancel( _msg=None_) [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.cancel "Link to this definition")

Cancel the Future and schedule callbacks.

If the Future is already _done_ or _cancelled_, return `False`.
Otherwise, change the Future’s state to _cancelled_,
schedule the callbacks, and return `True`.

Changed in version 3.9: Added the _msg_ parameter.

exception() [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.exception "Link to this definition")

Return the exception that was set on this Future.

The exception (or `None` if no exception was set) is
returned only if the Future is _done_.

If the Future has been _cancelled_, this method raises a
[`CancelledError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.CancelledError "asyncio.CancelledError") exception.

If the Future isn’t _done_ yet, this method raises an
[`InvalidStateError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.InvalidStateError "asyncio.InvalidStateError") exception.

get\_loop() [¶](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.get_loop "Link to this definition")

Return the event loop the Future object is bound to.

Added in version 3.7.

This example creates a Future object, creates and schedules an
asynchronous Task to set result for the Future, and waits until
the Future has a result:

Copy

```
async def set_after(fut, delay, value):
    # Sleep for *delay* seconds.
    await asyncio.sleep(delay)

    # Set *value* as a result of *fut* Future.
    fut.set_result(value)

async def main():
    # Get the current event loop.
    loop = asyncio.get_running_loop()

    # Create a new Future object.
    fut = loop.create_future()

    # Run "set_after()" coroutine in a parallel Task.
    # We are using the low-level "loop.create_task()" API here because
    # we already have a reference to the event loop at hand.
    # Otherwise we could have just used "asyncio.create_task()".
    loop.create_task(
        set_after(fut, 1, '... world'))

    print('hello ...')

    # Wait until *fut* has a result (1 second) and print it.
    print(await fut)

asyncio.run(main())
```

Important

The Future object was designed to mimic
[`concurrent.futures.Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future"). Key differences include:

- unlike asyncio Futures, [`concurrent.futures.Future`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future "concurrent.futures.Future")
instances cannot be awaited.

- [`asyncio.Future.result()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.result "asyncio.Future.result") and [`asyncio.Future.exception()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.exception "asyncio.Future.exception")
do not accept the _timeout_ argument.

- [`asyncio.Future.result()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.result "asyncio.Future.result") and [`asyncio.Future.exception()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.exception "asyncio.Future.exception")
raise an [`InvalidStateError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.InvalidStateError "asyncio.InvalidStateError") exception when the Future is not
_done_.

- Callbacks registered with [`asyncio.Future.add_done_callback()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.add_done_callback "asyncio.Future.add_done_callback")
are not called immediately. They are scheduled with
[`loop.call_soon()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.call_soon "asyncio.loop.call_soon") instead.

- asyncio Future is not compatible with the
[`concurrent.futures.wait()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.wait "concurrent.futures.wait") and
[`concurrent.futures.as_completed()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.as_completed "concurrent.futures.as_completed") functions.

- [`asyncio.Future.cancel()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future.cancel "asyncio.Future.cancel") accepts an optional `msg` argument,
but [`concurrent.futures.Future.cancel()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Future.cancel "concurrent.futures.Future.cancel") does not.


### [Table of Contents](https://docs.python.org/3/contents.html)

- [Futures](https://docs.python.org/3/library/asyncio-future.html#)
  - [Future Functions](https://docs.python.org/3/library/asyncio-future.html#future-functions)
  - [Future Object](https://docs.python.org/3/library/asyncio-future.html#future-object)

#### Previous topic

[Event Loop](https://docs.python.org/3/library/asyncio-eventloop.html "previous chapter")

#### Next topic

[Transports and Protocols](https://docs.python.org/3/library/asyncio-protocol.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/asyncio-future.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/asyncio-protocol.html "Transports and Protocols") \|
- [previous](https://docs.python.org/3/library/asyncio-eventloop.html "Event Loop") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
- [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html) »
- [Futures](https://docs.python.org/3/library/asyncio-future.html)
- \|

- Theme
AutoLightDark \|