### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/asyncio-extending.html "Extending") \|
- [previous](https://docs.python.org/3/library/asyncio-policy.html "Policies") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
- [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html) »
- [Platform Support](https://docs.python.org/3/library/asyncio-platforms.html)
- \|

- Theme
AutoLightDark \|

# Platform Support [¶](https://docs.python.org/3/library/asyncio-platforms.html\#platform-support "Link to this heading")

The [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") module is designed to be portable,
but some platforms have subtle differences and limitations
due to the platforms’ underlying architecture and capabilities.

## All Platforms [¶](https://docs.python.org/3/library/asyncio-platforms.html\#all-platforms "Link to this heading")

- [`loop.add_reader()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_reader "asyncio.loop.add_reader") and [`loop.add_writer()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_writer "asyncio.loop.add_writer")
cannot be used to monitor file I/O.


## Windows [¶](https://docs.python.org/3/library/asyncio-platforms.html\#windows "Link to this heading")

**Source code:** [Lib/asyncio/proactor\_events.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/proactor_events.py),
[Lib/asyncio/windows\_events.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/windows_events.py),
[Lib/asyncio/windows\_utils.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/windows_utils.py)

* * *

Changed in version 3.8: On Windows, [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop") is now the default event loop.

All event loops on Windows do not support the following methods:

- [`loop.create_unix_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection") and
[`loop.create_unix_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_server "asyncio.loop.create_unix_server") are not supported.
The [`socket.AF_UNIX`](https://docs.python.org/3/library/socket.html#socket.AF_UNIX "socket.AF_UNIX") socket family is specific to Unix.

- [`loop.add_signal_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_signal_handler "asyncio.loop.add_signal_handler") and
[`loop.remove_signal_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.remove_signal_handler "asyncio.loop.remove_signal_handler") are not supported.


[`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop") has the following limitations:

- [`SelectSelector`](https://docs.python.org/3/library/selectors.html#selectors.SelectSelector "selectors.SelectSelector") is used to wait on socket events:
it supports sockets and is limited to 512 sockets.

- [`loop.add_reader()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_reader "asyncio.loop.add_reader") and [`loop.add_writer()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_writer "asyncio.loop.add_writer") only accept
socket handles (e.g. pipe file descriptors are not supported).

- Pipes are not supported, so the [`loop.connect_read_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_read_pipe "asyncio.loop.connect_read_pipe")
and [`loop.connect_write_pipe()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_write_pipe "asyncio.loop.connect_write_pipe") methods are not implemented.

- [Subprocesses](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio-subprocess) are not supported, i.e.
[`loop.subprocess_exec()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_exec "asyncio.loop.subprocess_exec") and [`loop.subprocess_shell()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.subprocess_shell "asyncio.loop.subprocess_shell")
methods are not implemented.


[`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop") has the following limitations:

- The [`loop.add_reader()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_reader "asyncio.loop.add_reader") and [`loop.add_writer()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_writer "asyncio.loop.add_writer")
methods are not supported.


The resolution of the monotonic clock on Windows is usually around 15.6
milliseconds. The best resolution is 0.5 milliseconds. The resolution depends on the
hardware (availability of [HPET](https://en.wikipedia.org/wiki/High_Precision_Event_Timer)) and on the
Windows configuration.

### Subprocess Support on Windows [¶](https://docs.python.org/3/library/asyncio-platforms.html\#subprocess-support-on-windows "Link to this heading")

On Windows, the default event loop [`ProactorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.ProactorEventLoop "asyncio.ProactorEventLoop") supports
subprocesses, whereas [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop") does not.

## macOS [¶](https://docs.python.org/3/library/asyncio-platforms.html\#macos "Link to this heading")

Modern macOS versions are fully supported.

macOS <= 10.8

On macOS 10.6, 10.7 and 10.8, the default event loop
uses [`selectors.KqueueSelector`](https://docs.python.org/3/library/selectors.html#selectors.KqueueSelector "selectors.KqueueSelector"), which does not support
character devices on these versions. The [`SelectorEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.SelectorEventLoop "asyncio.SelectorEventLoop")
can be manually configured to use [`SelectSelector`](https://docs.python.org/3/library/selectors.html#selectors.SelectSelector "selectors.SelectSelector")
or [`PollSelector`](https://docs.python.org/3/library/selectors.html#selectors.PollSelector "selectors.PollSelector") to support character devices on
these older versions of macOS. Example:

Copy

```
import asyncio
import selectors

selector = selectors.SelectSelector()
loop = asyncio.SelectorEventLoop(selector)
asyncio.set_event_loop(loop)
```

### [Table of Contents](https://docs.python.org/3/contents.html)

- [Platform Support](https://docs.python.org/3/library/asyncio-platforms.html#)
  - [All Platforms](https://docs.python.org/3/library/asyncio-platforms.html#all-platforms)
  - [Windows](https://docs.python.org/3/library/asyncio-platforms.html#windows)
    - [Subprocess Support on Windows](https://docs.python.org/3/library/asyncio-platforms.html#subprocess-support-on-windows)
  - [macOS](https://docs.python.org/3/library/asyncio-platforms.html#macos)

#### Previous topic

[Policies](https://docs.python.org/3/library/asyncio-policy.html "previous chapter")

#### Next topic

[Extending](https://docs.python.org/3/library/asyncio-extending.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/asyncio-platforms.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/asyncio-extending.html "Extending") \|
- [previous](https://docs.python.org/3/library/asyncio-policy.html "Policies") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
- [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html) »
- [Platform Support](https://docs.python.org/3/library/asyncio-platforms.html)
- \|

- Theme
AutoLightDark \|