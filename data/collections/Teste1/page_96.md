### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/whatsnew/3.4.html "What’s New In Python 3.4") \|
- [previous](https://docs.python.org/3/whatsnew/3.6.html "What’s New In Python 3.6") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [What’s New in Python](https://docs.python.org/3/whatsnew/index.html) »
- [What’s New In Python 3.5](https://docs.python.org/3/whatsnew/3.5.html)
- \|

- Theme
AutoLightDark \|

# What’s New In Python 3.5 [¶](https://docs.python.org/3/whatsnew/3.5.html\#what-s-new-in-python-3-5 "Link to this heading")

Editors:

Elvis Pranskevichus < [elvis@magic.io](mailto:elvis%40magic.io) >, Yury Selivanov < [yury@magic.io](mailto:yury%40magic.io) >

This article explains the new features in Python 3.5, compared to 3.4.
Python 3.5 was released on September 13, 2015. See the
[changelog](https://docs.python.org/3.5/whatsnew/changelog.html) for a full
list of changes.

See also

[**PEP 478**](https://peps.python.org/pep-0478/) \- Python 3.5 Release Schedule

## Summary – Release highlights [¶](https://docs.python.org/3/whatsnew/3.5.html\#summary-release-highlights "Link to this heading")

New syntax features:

- [PEP 492](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-492), coroutines with async and await syntax.

- [PEP 465](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-465), a new matrix multiplication operator: `a @ b`.

- [PEP 448](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-448), additional unpacking generalizations.


New library modules:

- [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`)."): [PEP 484 – Type Hints](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-484).

- [`zipapp`](https://docs.python.org/3/library/zipapp.html#module-zipapp "zipapp: Manage executable Python zip archives"): [PEP 441 Improving Python ZIP Application Support](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-zipapp).


New built-in features:

- `bytes % args`, `bytearray % args`: [PEP 461](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-461) –
Adding `%` formatting to bytes and bytearray.

- New [`bytes.hex()`](https://docs.python.org/3/library/stdtypes.html#bytes.hex "bytes.hex"), [`bytearray.hex()`](https://docs.python.org/3/library/stdtypes.html#bytearray.hex "bytearray.hex") and [`memoryview.hex()`](https://docs.python.org/3/library/stdtypes.html#memoryview.hex "memoryview.hex")
methods. (Contributed by Arnon Yaari in [bpo-9951](https://bugs.python.org/issue?@action=redirect&bpo=9951).)

- [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "memoryview") now supports tuple indexing (including multi-dimensional).
(Contributed by Antoine Pitrou in [bpo-23632](https://bugs.python.org/issue?@action=redirect&bpo=23632).)

- Generators have a new `gi_yieldfrom` attribute, which returns the
object being iterated by `yield from` expressions. (Contributed
by Benno Leslie and Yury Selivanov in [bpo-24450](https://bugs.python.org/issue?@action=redirect&bpo=24450).)

- A new [`RecursionError`](https://docs.python.org/3/library/exceptions.html#RecursionError "RecursionError") exception is now raised when maximum
recursion depth is reached. (Contributed by Georg Brandl
in [bpo-19235](https://bugs.python.org/issue?@action=redirect&bpo=19235).)


CPython implementation improvements:

- When the `LC_TYPE` locale is the POSIX locale (`C` locale),
[`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin") and [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") now use the
`surrogateescape` error handler, instead of the `strict` error handler.
(Contributed by Victor Stinner in [bpo-19977](https://bugs.python.org/issue?@action=redirect&bpo=19977).)

- `.pyo` files are no longer used and have been replaced by a more flexible
scheme that includes the optimization level explicitly in `.pyc` name.
(See [PEP 488 overview](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-488).)

- Builtin and extension modules are now initialized in a multi-phase process,
which is similar to how Python modules are loaded.
(See [PEP 489 overview](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-489).)


Significant improvements in the standard library:

- [`collections.OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict") is now
[implemented in C](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-ordereddict), which makes it
4 to 100 times faster.

- The [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects") module gained
[support for Memory BIO](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-sslmemorybio), which decouples SSL
protocol handling from network IO.

- The new [`os.scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") function provides a
[better and significantly faster way](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-471)
of directory traversal.

- [`functools.lru_cache()`](https://docs.python.org/3/library/functools.html#functools.lru_cache "functools.lru_cache") has been mostly
[reimplemented in C](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-lrucache), yielding much better
performance.

- The new [`subprocess.run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") function provides a
[streamlined way to run subprocesses](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-subprocess).

- The [`traceback`](https://docs.python.org/3/library/traceback.html#module-traceback "traceback: Print or retrieve a stack traceback.") module has been significantly
[enhanced](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-traceback) for improved
performance and developer convenience.


Security improvements:

- SSLv3 is now disabled throughout the standard library.
It can still be enabled by instantiating a [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext")
manually. (See [bpo-22638](https://bugs.python.org/issue?@action=redirect&bpo=22638) for more details; this change was
backported to CPython 3.4 and 2.7.)

- HTTP cookie parsing is now stricter, in order to protect
against potential injection attacks. (Contributed by Antoine Pitrou
in [bpo-22796](https://bugs.python.org/issue?@action=redirect&bpo=22796).)


Windows improvements:

- A new installer for Windows has replaced the old MSI.
See [Using Python on Windows](https://docs.python.org/3/using/windows.html#using-on-windows) for more information.

- Windows builds now use Microsoft Visual C++ 14.0, and extension modules
should use the same.


Please read on for a comprehensive list of user-facing changes, including many
other smaller improvements, CPython optimizations, deprecations, and potential
porting issues.

## New Features [¶](https://docs.python.org/3/whatsnew/3.5.html\#new-features "Link to this heading")

### PEP 492 - Coroutines with async and await syntax [¶](https://docs.python.org/3/whatsnew/3.5.html\#pep-492-coroutines-with-async-and-await-syntax "Link to this heading")

[**PEP 492**](https://peps.python.org/pep-0492/) greatly improves support for asynchronous programming in Python
by adding [awaitable objects](https://docs.python.org/3/glossary.html#term-awaitable),
[coroutine functions](https://docs.python.org/3/glossary.html#term-coroutine-function),
[asynchronous iteration](https://docs.python.org/3/glossary.html#term-asynchronous-iterable),
and [asynchronous context managers](https://docs.python.org/3/glossary.html#term-asynchronous-context-manager).

Coroutine functions are declared using the new [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def) syntax:

Copy

```
>>> async def coro():
...     return 'spam'
```

Inside a coroutine function, the new [`await`](https://docs.python.org/3/reference/expressions.html#await) expression can be used
to suspend coroutine execution until the result is available. Any object
can be _awaited_, as long as it implements the [awaitable](https://docs.python.org/3/glossary.html#term-awaitable) protocol by
defining the [`__await__()`](https://docs.python.org/3/reference/datamodel.html#object.__await__ "object.__await__") method.

PEP 492 also adds [`async for`](https://docs.python.org/3/reference/compound_stmts.html#async-for) statement for convenient iteration
over asynchronous iterables.

An example of a rudimentary HTTP client written using the new syntax:

Copy

```
import asyncio

async def http_get(domain):
    reader, writer = await asyncio.open_connection(domain, 80)

    writer.write(b'\r\n'.join([\
        b'GET / HTTP/1.1',\
        b'Host: %b' % domain.encode('latin-1'),\
        b'Connection: close',\
        b'', b''\
    ]))

    async for line in reader:
        print('>>>', line)

    writer.close()

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(http_get('example.com'))
finally:
    loop.close()
```

Similarly to asynchronous iteration, there is a new syntax for asynchronous
context managers. The following script:

Copy

```
import asyncio

async def coro(name, lock):
    print('coro {}: waiting for lock'.format(name))
    async with lock:
        print('coro {}: holding the lock'.format(name))
        await asyncio.sleep(1)
        print('coro {}: releasing the lock'.format(name))

loop = asyncio.get_event_loop()
lock = asyncio.Lock()
coros = asyncio.gather(coro(1, lock), coro(2, lock))
try:
    loop.run_until_complete(coros)
finally:
    loop.close()
```

will output:

Copy

```
coro 2: waiting for lock
coro 2: holding the lock
coro 1: waiting for lock
coro 2: releasing the lock
coro 1: holding the lock
coro 1: releasing the lock
```

Note that both [`async for`](https://docs.python.org/3/reference/compound_stmts.html#async-for) and [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with) can only
be used inside a coroutine function declared with [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def).

Coroutine functions are intended to be run inside a compatible event loop,
such as the [asyncio loop](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-event-loop).

Note

Changed in version 3.5.2: Starting with CPython 3.5.2, `__aiter__` can directly return
[asynchronous iterators](https://docs.python.org/3/glossary.html#term-asynchronous-iterator). Returning
an [awaitable](https://docs.python.org/3/glossary.html#term-awaitable) object will result in a
[`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning").

See more details in the [Asynchronous Iterators](https://docs.python.org/3/reference/datamodel.html#async-iterators) documentation
section.

See also

[**PEP 492**](https://peps.python.org/pep-0492/) – Coroutines with async and await syntax

PEP written and implemented by Yury Selivanov.

### PEP 465 - A dedicated infix operator for matrix multiplication [¶](https://docs.python.org/3/whatsnew/3.5.html\#pep-465-a-dedicated-infix-operator-for-matrix-multiplication "Link to this heading")

[**PEP 465**](https://peps.python.org/pep-0465/) adds the `@` infix operator for matrix multiplication.
Currently, no builtin Python types implement the new operator, however, it
can be implemented by defining [`__matmul__()`](https://docs.python.org/3/reference/datamodel.html#object.__matmul__ "object.__matmul__"),
[`__rmatmul__()`](https://docs.python.org/3/reference/datamodel.html#object.__rmatmul__ "object.__rmatmul__"), and [`__imatmul__()`](https://docs.python.org/3/reference/datamodel.html#object.__imatmul__ "object.__imatmul__") for regular,
reflected, and in-place matrix multiplication.
The semantics of these methods is similar to that of
methods defining other infix arithmetic operators.

Matrix multiplication is a notably common operation in many fields of
mathematics, science, engineering, and the addition of `@` allows writing
cleaner code:

Copy

```
S = (H @ beta - r).T @ inv(H @ V @ H.T) @ (H @ beta - r)
```

instead of:

Copy

```
S = dot((dot(H, beta) - r).T,
        dot(inv(dot(dot(H, V), H.T)), dot(H, beta) - r))
```

NumPy 1.10 has support for the new operator:

Copy

```
>>> import numpy

>>> x = numpy.ones(3)
>>> x
array([ 1., 1., 1.])

>>> m = numpy.eye(3)
>>> m
array([[ 1., 0., 0.],\
       [ 0., 1., 0.],\
       [ 0., 0., 1.]])

>>> x @ m
array([ 1., 1., 1.])
```

See also

[**PEP 465**](https://peps.python.org/pep-0465/) – A dedicated infix operator for matrix multiplication

PEP written by Nathaniel J. Smith; implemented by Benjamin Peterson.

### PEP 448 - Additional Unpacking Generalizations [¶](https://docs.python.org/3/whatsnew/3.5.html\#pep-448-additional-unpacking-generalizations "Link to this heading")

[**PEP 448**](https://peps.python.org/pep-0448/) extends the allowed uses of the `*` iterable unpacking
operator and `**` dictionary unpacking operator. It is now possible
to use an arbitrary number of unpackings in [function calls](https://docs.python.org/3/reference/expressions.html#calls):

Copy

```
>>> print(*[1], *[2], 3, *[4, 5])
1 2 3 4 5

>>> def fn(a, b, c, d):
...     print(a, b, c, d)
...

>>> fn(**{'a': 1, 'c': 3}, **{'b': 2, 'd': 4})
1 2 3 4
```

Similarly, tuple, list, set, and dictionary displays allow multiple
unpackings (see [Expression lists](https://docs.python.org/3/reference/expressions.html#exprlists) and [Dictionary displays](https://docs.python.org/3/reference/expressions.html#dict)):

Copy

```
>>> *range(4), 4
(0, 1, 2, 3, 4)

>>> [*range(4), 4]
[0, 1, 2, 3, 4]

>>> {*range(4), 4, *(5, 6, 7)}
{0, 1, 2, 3, 4, 5, 6, 7}

>>> {'x': 1, **{'y': 2}}
{'x': 1, 'y': 2}
```

See also

[**PEP 448**](https://peps.python.org/pep-0448/) – Additional Unpacking Generalizations

PEP written by Joshua Landau; implemented by Neil Girdhar,
Thomas Wouters, and Joshua Landau.

### PEP 461 - percent formatting support for bytes and bytearray [¶](https://docs.python.org/3/whatsnew/3.5.html\#pep-461-percent-formatting-support-for-bytes-and-bytearray "Link to this heading")

[**PEP 461**](https://peps.python.org/pep-0461/) adds support for the `%` [interpolation operator](https://docs.python.org/3/library/stdtypes.html#bytes-formatting) to [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")
and [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray").

While interpolation is usually thought of as a string operation, there are
cases where interpolation on `bytes` or `bytearrays` makes sense, and the
work needed to make up for this missing functionality detracts from the
overall readability of the code. This issue is particularly important when
dealing with wire format protocols, which are often a mixture of binary
and ASCII compatible text.

Examples:

Copy

```
>>> b'Hello %b!' % b'World'
b'Hello World!'

>>> b'x=%i y=%f' % (1, 2.5)
b'x=1 y=2.500000'
```

Unicode is not allowed for `%b`, but it is accepted by `%a` (equivalent of
`repr(obj).encode('ascii', 'backslashreplace')`):

Copy

```
>>> b'Hello %b!' % 'World'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: %b requires bytes, or an object that implements __bytes__, not 'str'

>>> b'price: %a' % '10€'
b"price: '10\\u20ac'"
```

Note that `%s` and `%r` conversion types, although supported, should
only be used in codebases that need compatibility with Python 2.

See also

[**PEP 461**](https://peps.python.org/pep-0461/) – Adding % formatting to bytes and bytearray

PEP written by Ethan Furman; implemented by Neil Schemenauer and
Ethan Furman.

### PEP 484 - Type Hints [¶](https://docs.python.org/3/whatsnew/3.5.html\#pep-484-type-hints "Link to this heading")

Function annotation syntax has been a Python feature since version 3.0
( [**PEP 3107**](https://peps.python.org/pep-3107/)), however the semantics of annotations has been left undefined.

Experience has shown that the majority of function annotation
uses were to provide type hints to function parameters and return values. It
became evident that it would be beneficial for Python users, if the
standard library included the base definitions and tools for type annotations.

[**PEP 484**](https://peps.python.org/pep-0484/) introduces a [provisional module](https://docs.python.org/3/glossary.html#term-provisional-API) to
provide these standard definitions and tools, along with some conventions
for situations where annotations are not available.

For example, here is a simple function whose argument and return type
are declared in the annotations:

Copy

```
def greeting(name: str) -> str:
    return 'Hello ' + name
```

While these annotations are available at runtime through the usual
[`__annotations__`](https://docs.python.org/3/reference/datamodel.html#object.__annotations__ "object.__annotations__") attribute, _no automatic type checking happens_
_at runtime_. Instead, it is assumed that a separate off-line type checker
(e.g. [mypy](https://mypy-lang.org/)) will be used for on-demand
source code analysis.

The type system supports unions, generic types, and a special type
named [`Any`](https://docs.python.org/3/library/typing.html#typing.Any "typing.Any") which is consistent with (i.e. assignable to
and from) all types.

See also

- [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") module documentation

- [**PEP 484**](https://peps.python.org/pep-0484/) – Type Hints

PEP written by Guido van Rossum, Jukka Lehtosalo, and Łukasz Langa;
implemented by Guido van Rossum.

- [**PEP 483**](https://peps.python.org/pep-0483/) – The Theory of Type Hints

PEP written by Guido van Rossum


### PEP 471 - os.scandir() function – a better and faster directory iterator [¶](https://docs.python.org/3/whatsnew/3.5.html\#pep-471-os-scandir-function-a-better-and-faster-directory-iterator "Link to this heading")

[**PEP 471**](https://peps.python.org/pep-0471/) adds a new directory iteration function, [`os.scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir"),
to the standard library. Additionally, [`os.walk()`](https://docs.python.org/3/library/os.html#os.walk "os.walk") is now
implemented using `scandir`, which makes it 3 to 5 times faster
on POSIX systems and 7 to 20 times faster on Windows systems. This is
largely achieved by greatly reducing the number of calls to [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")
required to walk a directory tree.

Additionally, `scandir` returns an iterator, as opposed to returning
a list of file names, which improves memory efficiency when iterating
over very large directories.

The following example shows a simple use of [`os.scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") to display all
the files (excluding directories) in the given _path_ that don’t start with
`'.'`. The [`entry.is_file()`](https://docs.python.org/3/library/os.html#os.DirEntry.is_file "os.DirEntry.is_file") call will generally
not make an additional system call:

Copy

```
for entry in os.scandir(path):
    if not entry.name.startswith('.') and entry.is_file():
        print(entry.name)
```

See also

[**PEP 471**](https://peps.python.org/pep-0471/) – os.scandir() function – a better and faster directory iterator

PEP written and implemented by Ben Hoyt with the help of Victor Stinner.

### PEP 475: Retry system calls failing with EINTR [¶](https://docs.python.org/3/whatsnew/3.5.html\#pep-475-retry-system-calls-failing-with-eintr "Link to this heading")

An [`errno.EINTR`](https://docs.python.org/3/library/errno.html#errno.EINTR "errno.EINTR") error code is returned whenever a system call, that
is waiting for I/O, is interrupted by a signal. Previously, Python would
raise [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") in such cases. This meant that, when writing a
Python application, the developer had two choices:

1. Ignore the `InterruptedError`.

2. Handle the `InterruptedError` and attempt to restart the interrupted
system call at every call site.


The first option makes an application fail intermittently.
The second option adds a large amount of boilerplate that makes the
code nearly unreadable. Compare:

Copy

```
print("Hello World")
```

and:

Copy

```
while True:
    try:
        print("Hello World")
        break
    except InterruptedError:
        continue
```

[**PEP 475**](https://peps.python.org/pep-0475/) implements automatic retry of system calls on
`EINTR`. This removes the burden of dealing with `EINTR`
or [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") in user code in most situations and makes
Python programs, including the standard library, more robust. Note that
the system call is only retried if the signal handler does not raise an
exception.

Below is a list of functions which are now retried when interrupted
by a signal:

- [`open()`](https://docs.python.org/3/library/functions.html#open "open") and [`io.open()`](https://docs.python.org/3/library/io.html#io.open "io.open");

- functions of the [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.") module;

- [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") functions: [`fchdir()`](https://docs.python.org/3/library/os.html#os.fchdir "os.fchdir"), [`fchmod()`](https://docs.python.org/3/library/os.html#os.fchmod "os.fchmod"),
[`fchown()`](https://docs.python.org/3/library/os.html#os.fchown "os.fchown"), [`fdatasync()`](https://docs.python.org/3/library/os.html#os.fdatasync "os.fdatasync"), [`fstat()`](https://docs.python.org/3/library/os.html#os.fstat "os.fstat"),
[`fstatvfs()`](https://docs.python.org/3/library/os.html#os.fstatvfs "os.fstatvfs"), [`fsync()`](https://docs.python.org/3/library/os.html#os.fsync "os.fsync"), [`ftruncate()`](https://docs.python.org/3/library/os.html#os.ftruncate "os.ftruncate"),
[`mkfifo()`](https://docs.python.org/3/library/os.html#os.mkfifo "os.mkfifo"), [`mknod()`](https://docs.python.org/3/library/os.html#os.mknod "os.mknod"), [`open()`](https://docs.python.org/3/library/os.html#os.open "os.open"),
[`posix_fadvise()`](https://docs.python.org/3/library/os.html#os.posix_fadvise "os.posix_fadvise"), [`posix_fallocate()`](https://docs.python.org/3/library/os.html#os.posix_fallocate "os.posix_fallocate"), [`pread()`](https://docs.python.org/3/library/os.html#os.pread "os.pread"),
[`pwrite()`](https://docs.python.org/3/library/os.html#os.pwrite "os.pwrite"), [`read()`](https://docs.python.org/3/library/os.html#os.read "os.read"), [`readv()`](https://docs.python.org/3/library/os.html#os.readv "os.readv"), [`sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile"),
[`wait3()`](https://docs.python.org/3/library/os.html#os.wait3 "os.wait3"), [`wait4()`](https://docs.python.org/3/library/os.html#os.wait4 "os.wait4"), [`wait()`](https://docs.python.org/3/library/os.html#os.wait "os.wait"),
[`waitid()`](https://docs.python.org/3/library/os.html#os.waitid "os.waitid"), [`waitpid()`](https://docs.python.org/3/library/os.html#os.waitpid "os.waitpid"), [`write()`](https://docs.python.org/3/library/os.html#os.write "os.write"),
[`writev()`](https://docs.python.org/3/library/os.html#os.writev "os.writev");

- special cases: [`os.close()`](https://docs.python.org/3/library/os.html#os.close "os.close") and [`os.dup2()`](https://docs.python.org/3/library/os.html#os.dup2 "os.dup2") now ignore
[`EINTR`](https://docs.python.org/3/library/errno.html#errno.EINTR "errno.EINTR") errors; the syscall is not retried (see the PEP
for the rationale);

- [`select`](https://docs.python.org/3/library/select.html#module-select "select: Wait for I/O completion on multiple streams.") functions: [`devpoll.poll()`](https://docs.python.org/3/library/select.html#select.devpoll.poll "select.devpoll.poll"),
[`epoll.poll()`](https://docs.python.org/3/library/select.html#select.epoll.poll "select.epoll.poll"),
[`kqueue.control()`](https://docs.python.org/3/library/select.html#select.kqueue.control "select.kqueue.control"),
[`poll.poll()`](https://docs.python.org/3/library/select.html#select.poll.poll "select.poll.poll"), [`select()`](https://docs.python.org/3/library/select.html#select.select "select.select");

- methods of the [`socket`](https://docs.python.org/3/library/socket.html#socket.socket "socket.socket") class: [`accept()`](https://docs.python.org/3/library/socket.html#socket.socket.accept "socket.socket.accept"),
[`connect()`](https://docs.python.org/3/library/socket.html#socket.socket.connect "socket.socket.connect") (except for non-blocking sockets),
[`recv()`](https://docs.python.org/3/library/socket.html#socket.socket.recv "socket.socket.recv"), [`recvfrom()`](https://docs.python.org/3/library/socket.html#socket.socket.recvfrom "socket.socket.recvfrom"),
[`recvmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.recvmsg "socket.socket.recvmsg"), [`send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send"),
[`sendall()`](https://docs.python.org/3/library/socket.html#socket.socket.sendall "socket.socket.sendall"), [`sendmsg()`](https://docs.python.org/3/library/socket.html#socket.socket.sendmsg "socket.socket.sendmsg"),
[`sendto()`](https://docs.python.org/3/library/socket.html#socket.socket.sendto "socket.socket.sendto");

- [`signal.sigtimedwait()`](https://docs.python.org/3/library/signal.html#signal.sigtimedwait "signal.sigtimedwait") and [`signal.sigwaitinfo()`](https://docs.python.org/3/library/signal.html#signal.sigwaitinfo "signal.sigwaitinfo");

- [`time.sleep()`](https://docs.python.org/3/library/time.html#time.sleep "time.sleep").


See also

[**PEP 475**](https://peps.python.org/pep-0475/) – Retry system calls failing with EINTR

PEP and implementation written by Charles-François Natali and
Victor Stinner, with the help of Antoine Pitrou (the French connection).

### PEP 479: Change StopIteration handling inside generators [¶](https://docs.python.org/3/whatsnew/3.5.html\#pep-479-change-stopiteration-handling-inside-generators "Link to this heading")

The interaction of generators and [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration") in Python 3.4 and
earlier was sometimes surprising, and could conceal obscure bugs. Previously,
`StopIteration` raised accidentally inside a generator function was
interpreted as the end of the iteration by the loop construct driving the
generator.

[**PEP 479**](https://peps.python.org/pep-0479/) changes the behavior of generators: when a `StopIteration`
exception is raised inside a generator, it is replaced with a
[`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") before it exits the generator frame. The main goal of
this change is to ease debugging in the situation where an unguarded
[`next()`](https://docs.python.org/3/library/functions.html#next "next") call raises `StopIteration` and causes the iteration controlled
by the generator to terminate silently. This is particularly pernicious in
combination with the `yield from` construct.

This is a backwards incompatible change, so to enable the new behavior,
a [\_\_future\_\_](https://docs.python.org/3/glossary.html#term-__future__) import is necessary:

Copy

```
>>> from __future__ import generator_stop

>>> def gen():
...     next(iter([]))
...     yield
...
>>> next(gen())
Traceback (most recent call last):
  File "<stdin>", line 2, in gen
StopIteration

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: generator raised StopIteration
```

Without a `__future__` import, a [`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning") will be
raised whenever a [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration") exception is raised inside a generator.

See also

[**PEP 479**](https://peps.python.org/pep-0479/) – Change StopIteration handling inside generators

PEP written by Chris Angelico and Guido van Rossum. Implemented by
Chris Angelico, Yury Selivanov and Nick Coghlan.

### PEP 485: A function for testing approximate equality [¶](https://docs.python.org/3/whatsnew/3.5.html\#pep-485-a-function-for-testing-approximate-equality "Link to this heading")

[**PEP 485**](https://peps.python.org/pep-0485/) adds the [`math.isclose()`](https://docs.python.org/3/library/math.html#math.isclose "math.isclose") and [`cmath.isclose()`](https://docs.python.org/3/library/cmath.html#cmath.isclose "cmath.isclose")
functions which tell whether two values are approximately equal or
“close” to each other. Whether or not two values are considered
close is determined according to given absolute and relative tolerances.
Relative tolerance is the maximum allowed difference between `isclose`
arguments, relative to the larger absolute value:

Copy

```
>>> import math
>>> a = 5.0
>>> b = 4.99998
>>> math.isclose(a, b, rel_tol=1e-5)
True
>>> math.isclose(a, b, rel_tol=1e-6)
False
```

It is also possible to compare two values using absolute tolerance, which
must be a non-negative value:

Copy

```
>>> import math
>>> a = 5.0
>>> b = 4.99998
>>> math.isclose(a, b, abs_tol=0.00003)
True
>>> math.isclose(a, b, abs_tol=0.00001)
False
```

See also

[**PEP 485**](https://peps.python.org/pep-0485/) – A function for testing approximate equality

PEP written by Christopher Barker; implemented by Chris Barker and
Tal Einat.

### PEP 486: Make the Python Launcher aware of virtual environments [¶](https://docs.python.org/3/whatsnew/3.5.html\#pep-486-make-the-python-launcher-aware-of-virtual-environments "Link to this heading")

[**PEP 486**](https://peps.python.org/pep-0486/) makes the Windows launcher (see [**PEP 397**](https://peps.python.org/pep-0397/)) aware of an active
virtual environment. When the default interpreter would be used and the
`VIRTUAL_ENV` environment variable is set, the interpreter in the virtual
environment will be used.

See also

[**PEP 486**](https://peps.python.org/pep-0486/) – Make the Python Launcher aware of virtual environments

PEP written and implemented by Paul Moore.

### PEP 488: Elimination of PYO files [¶](https://docs.python.org/3/whatsnew/3.5.html\#pep-488-elimination-of-pyo-files "Link to this heading")

[**PEP 488**](https://peps.python.org/pep-0488/) does away with the concept of `.pyo` files. This means that
`.pyc` files represent both unoptimized and optimized bytecode. To prevent the
need to constantly regenerate bytecode files, `.pyc` files now have an
optional `opt-` tag in their name when the bytecode is optimized. This has the
side-effect of no more bytecode file name clashes when running under either
[`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O) or [`-OO`](https://docs.python.org/3/using/cmdline.html#cmdoption-OO). Consequently, bytecode files generated from
[`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O), and [`-OO`](https://docs.python.org/3/using/cmdline.html#cmdoption-OO) may now exist simultaneously.
[`importlib.util.cache_from_source()`](https://docs.python.org/3/library/importlib.html#importlib.util.cache_from_source "importlib.util.cache_from_source") has an updated API to help with
this change.

See also

[**PEP 488**](https://peps.python.org/pep-0488/) – Elimination of PYO files

PEP written and implemented by Brett Cannon.

### PEP 489: Multi-phase extension module initialization [¶](https://docs.python.org/3/whatsnew/3.5.html\#pep-489-multi-phase-extension-module-initialization "Link to this heading")

[**PEP 489**](https://peps.python.org/pep-0489/) updates extension module initialization to take advantage of the
two step module loading mechanism introduced by [**PEP 451**](https://peps.python.org/pep-0451/) in Python 3.4.

This change brings the import semantics of extension modules that opt-in to
using the new mechanism much closer to those of Python source and bytecode
modules, including the ability to use any valid identifier as a module name,
rather than being restricted to ASCII.

See also

[**PEP 489**](https://peps.python.org/pep-0489/) – Multi-phase extension module initialization

PEP written by Petr Viktorin, Stefan Behnel, and Nick Coghlan;
implemented by Petr Viktorin.

## Other Language Changes [¶](https://docs.python.org/3/whatsnew/3.5.html\#other-language-changes "Link to this heading")

Some smaller changes made to the core Python language are:

- Added the `"namereplace"` error handlers. The `"backslashreplace"`
error handlers now work with decoding and translating.
(Contributed by Serhiy Storchaka in [bpo-19676](https://bugs.python.org/issue?@action=redirect&bpo=19676) and [bpo-22286](https://bugs.python.org/issue?@action=redirect&bpo=22286).)

- The [`-b`](https://docs.python.org/3/using/cmdline.html#cmdoption-b) option now affects comparisons of [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") with
[`int`](https://docs.python.org/3/library/functions.html#int "int"). (Contributed by Serhiy Storchaka in [bpo-23681](https://bugs.python.org/issue?@action=redirect&bpo=23681).)

- New Kazakh `kz1048` and Tajik `koi8_t` [codecs](https://docs.python.org/3/library/codecs.html#standard-encodings).
(Contributed by Serhiy Storchaka in [bpo-22682](https://bugs.python.org/issue?@action=redirect&bpo=22682) and [bpo-22681](https://bugs.python.org/issue?@action=redirect&bpo=22681).)

- Property docstrings are now writable. This is especially useful for
[`collections.namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") docstrings.
(Contributed by Berker Peksag in [bpo-24064](https://bugs.python.org/issue?@action=redirect&bpo=24064).)

- Circular imports involving relative imports are now supported.
(Contributed by Brett Cannon and Antoine Pitrou in [bpo-17636](https://bugs.python.org/issue?@action=redirect&bpo=17636).)


## New Modules [¶](https://docs.python.org/3/whatsnew/3.5.html\#new-modules "Link to this heading")

### typing [¶](https://docs.python.org/3/whatsnew/3.5.html\#typing "Link to this heading")

The new [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") [provisional](https://docs.python.org/3/glossary.html#term-provisional-API) module
provides standard definitions and tools for function type annotations.
See [Type Hints](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-484) for more information.

### zipapp [¶](https://docs.python.org/3/whatsnew/3.5.html\#zipapp "Link to this heading")

The new [`zipapp`](https://docs.python.org/3/library/zipapp.html#module-zipapp "zipapp: Manage executable Python zip archives") module (specified in [**PEP 441**](https://peps.python.org/pep-0441/)) provides an API and
command line tool for creating executable Python Zip Applications, which
were introduced in Python 2.6 in [bpo-1739468](https://bugs.python.org/issue?@action=redirect&bpo=1739468), but which were not well
publicized, either at the time or since.

With the new module, bundling your application is as simple as putting all
the files, including a `__main__.py` file, into a directory `myapp`
and running:

```
$ python -m zipapp myapp
$ python myapp.pyz
```

The module implementation has been contributed by Paul Moore in
[bpo-23491](https://bugs.python.org/issue?@action=redirect&bpo=23491).

See also

[**PEP 441**](https://peps.python.org/pep-0441/) – Improving Python ZIP Application Support

## Improved Modules [¶](https://docs.python.org/3/whatsnew/3.5.html\#improved-modules "Link to this heading")

### argparse [¶](https://docs.python.org/3/whatsnew/3.5.html\#argparse "Link to this heading")

The [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") class now allows disabling
[abbreviated usage](https://docs.python.org/3/library/argparse.html#prefix-matching) of long options by setting
[allow\_abbrev](https://docs.python.org/3/library/argparse.html#allow-abbrev) to `False`. (Contributed by Jonathan Paugh,
Steven Bethard, paul j3 and Daniel Eriksson in [bpo-14910](https://bugs.python.org/issue?@action=redirect&bpo=14910).)

### asyncio [¶](https://docs.python.org/3/whatsnew/3.5.html\#asyncio "Link to this heading")

Since the [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") module is [provisional](https://docs.python.org/3/glossary.html#term-provisional-API),
all changes introduced in Python 3.5 have also been backported to Python 3.4.x.

Notable changes in the [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") module since Python 3.4.0:

- New debugging APIs: [`loop.set_debug()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_debug "asyncio.loop.set_debug")
and [`loop.get_debug()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.get_debug "asyncio.loop.get_debug") methods.
(Contributed by Victor Stinner.)

- The proactor event loop now supports SSL.
(Contributed by Antoine Pitrou and Victor Stinner in [bpo-22560](https://bugs.python.org/issue?@action=redirect&bpo=22560).)

- A new [`loop.is_closed()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.is_closed "asyncio.loop.is_closed") method to
check if the event loop is closed.
(Contributed by Victor Stinner in [bpo-21326](https://bugs.python.org/issue?@action=redirect&bpo=21326).)

- A new [`loop.create_task()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task")
to conveniently create and schedule a new [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task")
for a coroutine. The `create_task` method is also used by all
asyncio functions that wrap coroutines into tasks, such as
[`asyncio.wait()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait "asyncio.wait"), [`asyncio.gather()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.gather "asyncio.gather"), etc.
(Contributed by Victor Stinner.)

- A new [`transport.get_write_buffer_limits()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.WriteTransport.get_write_buffer_limits "asyncio.WriteTransport.get_write_buffer_limits")
method to inquire for _high-_ and _low-_ water limits of the flow
control.
(Contributed by Victor Stinner.)

- The `async()` function is deprecated in favor of
[`ensure_future()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.ensure_future "asyncio.ensure_future").
(Contributed by Yury Selivanov.)

- New [`loop.set_task_factory()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.set_task_factory "asyncio.loop.set_task_factory") and
[`loop.get_task_factory()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.get_task_factory "asyncio.loop.get_task_factory")
methods to customize the task factory that [`loop.create_task()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_task "asyncio.loop.create_task") method uses. (Contributed by Yury
Selivanov.)

- New [`Queue.join()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.join "asyncio.Queue.join") and
[`Queue.task_done()`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue.task_done "asyncio.Queue.task_done") queue methods.
(Contributed by Victor Stinner.)

- The `JoinableQueue` class was removed, in favor of the
[`asyncio.Queue`](https://docs.python.org/3/library/asyncio-queue.html#asyncio.Queue "asyncio.Queue") class.
(Contributed by Victor Stinner.)


Updates in 3.5.1:

- The [`ensure_future()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.ensure_future "asyncio.ensure_future") function and all functions that
use it, such as [`loop.run_until_complete()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_until_complete "asyncio.loop.run_until_complete"),
now accept all kinds of [awaitable objects](https://docs.python.org/3/glossary.html#term-awaitable).
(Contributed by Yury Selivanov.)

- New [`run_coroutine_threadsafe()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.run_coroutine_threadsafe "asyncio.run_coroutine_threadsafe") function to submit
coroutines to event loops from other threads.
(Contributed by Vincent Michel.)

- New [`Transport.is_closing()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.is_closing "asyncio.BaseTransport.is_closing")
method to check if the transport is closing or closed.
(Contributed by Yury Selivanov.)

- The [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
method can now accept a list of hosts.
(Contributed by Yann Sionneau.)


Updates in 3.5.2:

- New [`loop.create_future()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_future "asyncio.loop.create_future")
method to create Future objects. This allows alternative event
loop implementations, such as
[uvloop](https://github.com/MagicStack/uvloop), to provide a faster
[`asyncio.Future`](https://docs.python.org/3/library/asyncio-future.html#asyncio.Future "asyncio.Future") implementation.
(Contributed by Yury Selivanov.)

- New [`loop.get_exception_handler()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.get_exception_handler "asyncio.loop.get_exception_handler")
method to get the current exception handler.
(Contributed by Yury Selivanov.)

- New [`StreamReader.readuntil()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader.readuntil "asyncio.StreamReader.readuntil")
method to read data from the stream until a separator bytes
sequence appears.
(Contributed by Mark Korenberg.)

- The [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection")
and [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server")
methods are optimized to avoid calling the system `getaddrinfo`
function if the address is already resolved.
(Contributed by A. Jesse Jiryu Davis.)

- The [`loop.sock_connect(sock, address)`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.sock_connect "asyncio.loop.sock_connect")
no longer requires the _address_ to be resolved prior to the call.
(Contributed by A. Jesse Jiryu Davis.)


### bz2 [¶](https://docs.python.org/3/whatsnew/3.5.html\#bz2 "Link to this heading")

The [`BZ2Decompressor.decompress`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.decompress "bz2.BZ2Decompressor.decompress")
method now accepts an optional _max\_length_ argument to limit the maximum
size of decompressed data. (Contributed by Nikolaus Rath in [bpo-15955](https://bugs.python.org/issue?@action=redirect&bpo=15955).)

### cgi [¶](https://docs.python.org/3/whatsnew/3.5.html\#cgi "Link to this heading")

The `FieldStorage` class now supports the [context manager](https://docs.python.org/3/glossary.html#term-context-manager)
protocol. (Contributed by Berker Peksag in [bpo-20289](https://bugs.python.org/issue?@action=redirect&bpo=20289).)

### cmath [¶](https://docs.python.org/3/whatsnew/3.5.html\#cmath "Link to this heading")

A new function [`isclose()`](https://docs.python.org/3/library/cmath.html#cmath.isclose "cmath.isclose") provides a way to test for approximate
equality. (Contributed by Chris Barker and Tal Einat in [bpo-24270](https://bugs.python.org/issue?@action=redirect&bpo=24270).)

### code [¶](https://docs.python.org/3/whatsnew/3.5.html\#code "Link to this heading")

The [`InteractiveInterpreter.showtraceback()`](https://docs.python.org/3/library/code.html#code.InteractiveInterpreter.showtraceback "code.InteractiveInterpreter.showtraceback")
method now prints the full chained traceback, just like the interactive
interpreter. (Contributed by Claudiu Popa in [bpo-17442](https://bugs.python.org/issue?@action=redirect&bpo=17442).)

### collections [¶](https://docs.python.org/3/whatsnew/3.5.html\#collections "Link to this heading")

The [`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict") class is now implemented in C, which
makes it 4 to 100 times faster. (Contributed by Eric Snow in [bpo-16991](https://bugs.python.org/issue?@action=redirect&bpo=16991).)

`OrderedDict.items()`, `OrderedDict.keys()`,
and `OrderedDict.values()` views now support [`reversed()`](https://docs.python.org/3/library/functions.html#reversed "reversed") iteration.
(Contributed by Serhiy Storchaka in [bpo-19505](https://bugs.python.org/issue?@action=redirect&bpo=19505).)

The [`deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque") class now defines
[`index()`](https://docs.python.org/3/library/collections.html#collections.deque.index "collections.deque.index"), [`insert()`](https://docs.python.org/3/library/collections.html#collections.deque.insert "collections.deque.insert"), and
[`copy()`](https://docs.python.org/3/library/collections.html#collections.deque.copy "collections.deque.copy"), and supports the `+` and `*` operators.
This allows deques to be recognized as a [`MutableSequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence")
and improves their substitutability for lists.
(Contributed by Raymond Hettinger in [bpo-23704](https://bugs.python.org/issue?@action=redirect&bpo=23704).)

Docstrings produced by [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") can now be updated:

Copy

```
Point = namedtuple('Point', ['x', 'y'])
Point.__doc__ += ': Cartesian coordinate'
Point.x.__doc__ = 'abscissa'
Point.y.__doc__ = 'ordinate'
```

(Contributed by Berker Peksag in [bpo-24064](https://bugs.python.org/issue?@action=redirect&bpo=24064).)

The [`UserString`](https://docs.python.org/3/library/collections.html#collections.UserString "collections.UserString") class now implements the
[`__getnewargs__()`](https://docs.python.org/3/library/pickle.html#object.__getnewargs__ "object.__getnewargs__"), [`__rmod__()`](https://docs.python.org/3/reference/datamodel.html#object.__rmod__ "object.__rmod__"), [`casefold()`](https://docs.python.org/3/library/stdtypes.html#str.casefold "str.casefold"),
[`format_map()`](https://docs.python.org/3/library/stdtypes.html#str.format_map "str.format_map"), [`isprintable()`](https://docs.python.org/3/library/stdtypes.html#str.isprintable "str.isprintable"), and [`maketrans()`](https://docs.python.org/3/library/stdtypes.html#str.maketrans "str.maketrans")
methods to match the corresponding methods of [`str`](https://docs.python.org/3/library/stdtypes.html#str "str").
(Contributed by Joe Jevnik in [bpo-22189](https://bugs.python.org/issue?@action=redirect&bpo=22189).)

### collections.abc [¶](https://docs.python.org/3/whatsnew/3.5.html\#collections-abc "Link to this heading")

The `Sequence.index()` method now
accepts _start_ and _stop_ arguments to match the corresponding methods
of [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), etc.
(Contributed by Devin Jeanpierre in [bpo-23086](https://bugs.python.org/issue?@action=redirect&bpo=23086).)

A new [`Generator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator") abstract base class. (Contributed
by Stefan Behnel in [bpo-24018](https://bugs.python.org/issue?@action=redirect&bpo=24018).)

New [`Awaitable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Awaitable "collections.abc.Awaitable"), [`Coroutine`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Coroutine "collections.abc.Coroutine"),
[`AsyncIterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator "collections.abc.AsyncIterator"), and
[`AsyncIterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterable "collections.abc.AsyncIterable") abstract base classes.
(Contributed by Yury Selivanov in [bpo-24184](https://bugs.python.org/issue?@action=redirect&bpo=24184).)

For earlier Python versions, a backport of the new ABCs is available in an
external [PyPI package](https://pypi.org/project/backports_abc/).

### compileall [¶](https://docs.python.org/3/whatsnew/3.5.html\#compileall "Link to this heading")

A new [`compileall`](https://docs.python.org/3/library/compileall.html#module-compileall "compileall: Tools for byte-compiling all Python source files in a directory tree.") option, `-j N`, allows running _N_ workers
simultaneously to perform parallel bytecode compilation.
The [`compile_dir()`](https://docs.python.org/3/library/compileall.html#compileall.compile_dir "compileall.compile_dir") function has a corresponding `workers`
parameter. (Contributed by Claudiu Popa in [bpo-16104](https://bugs.python.org/issue?@action=redirect&bpo=16104).)

Another new option, `-r`, allows controlling the maximum recursion
level for subdirectories. (Contributed by Claudiu Popa in [bpo-19628](https://bugs.python.org/issue?@action=redirect&bpo=19628).)

The `-q` command line option can now be specified more than once, in
which case all output, including errors, will be suppressed. The corresponding
`quiet` parameter in [`compile_dir()`](https://docs.python.org/3/library/compileall.html#compileall.compile_dir "compileall.compile_dir"),
[`compile_file()`](https://docs.python.org/3/library/compileall.html#compileall.compile_file "compileall.compile_file"), and [`compile_path()`](https://docs.python.org/3/library/compileall.html#compileall.compile_path "compileall.compile_path") can now
accept an integer value indicating the level of output suppression.
(Contributed by Thomas Kluyver in [bpo-21338](https://bugs.python.org/issue?@action=redirect&bpo=21338).)

### concurrent.futures [¶](https://docs.python.org/3/whatsnew/3.5.html\#concurrent-futures "Link to this heading")

The [`Executor.map()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.map "concurrent.futures.Executor.map") method now accepts a
_chunksize_ argument to allow batching of tasks to improve performance when
[`ProcessPoolExecutor()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor") is used.
(Contributed by Dan O’Reilly in [bpo-11271](https://bugs.python.org/issue?@action=redirect&bpo=11271).)

The number of workers in the [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor")
constructor is optional now. The default value is 5 times the number of CPUs.
(Contributed by Claudiu Popa in [bpo-21527](https://bugs.python.org/issue?@action=redirect&bpo=21527).)

### configparser [¶](https://docs.python.org/3/whatsnew/3.5.html\#configparser "Link to this heading")

[`configparser`](https://docs.python.org/3/library/configparser.html#module-configparser "configparser: Configuration file parser.") now provides a way to customize the conversion
of values by specifying a dictionary of converters in the
[`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser") constructor, or by defining them
as methods in `ConfigParser` subclasses. Converters defined in
a parser instance are inherited by its section proxies.

Example:

Copy

```
>>> import configparser
>>> conv = {}
>>> conv['list'] = lambda v: [e.strip() for e in v.split() if e.strip()]
>>> cfg = configparser.ConfigParser(converters=conv)
>>> cfg.read_string("""
... [s]
... list = a b c d e f g
... """)
>>> cfg.get('s', 'list')
'a b c d e f g'
>>> cfg.getlist('s', 'list')
['a', 'b', 'c', 'd', 'e', 'f', 'g']
>>> section = cfg['s']
>>> section.getlist('list')
['a', 'b', 'c', 'd', 'e', 'f', 'g']
```

(Contributed by Łukasz Langa in [bpo-18159](https://bugs.python.org/issue?@action=redirect&bpo=18159).)

### contextlib [¶](https://docs.python.org/3/whatsnew/3.5.html\#contextlib "Link to this heading")

The new [`redirect_stderr()`](https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stderr "contextlib.redirect_stderr") [context manager](https://docs.python.org/3/glossary.html#term-context-manager) (similar to
[`redirect_stdout()`](https://docs.python.org/3/library/contextlib.html#contextlib.redirect_stdout "contextlib.redirect_stdout")) makes it easier for utility scripts to
handle inflexible APIs that write their output to [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") and
don’t provide any options to redirect it:

Copy

```
>>> import contextlib, io, logging
>>> f = io.StringIO()
>>> with contextlib.redirect_stderr(f):
...     logging.warning('warning')
...
>>> f.getvalue()
'WARNING:root:warning\n'
```

(Contributed by Berker Peksag in [bpo-22389](https://bugs.python.org/issue?@action=redirect&bpo=22389).)

### csv [¶](https://docs.python.org/3/whatsnew/3.5.html\#csv "Link to this heading")

The [`writerow()`](https://docs.python.org/3/library/csv.html#csv.csvwriter.writerow "csv.csvwriter.writerow") method now supports arbitrary iterables,
not just sequences. (Contributed by Serhiy Storchaka in [bpo-23171](https://bugs.python.org/issue?@action=redirect&bpo=23171).)

### curses [¶](https://docs.python.org/3/whatsnew/3.5.html\#curses "Link to this heading")

The new [`update_lines_cols()`](https://docs.python.org/3/library/curses.html#curses.update_lines_cols "curses.update_lines_cols") function updates the [`LINES`](https://docs.python.org/3/library/curses.html#curses.LINES "curses.LINES")
and [`COLS`](https://docs.python.org/3/library/curses.html#curses.COLS "curses.COLS") module variables. This is useful for detecting
manual screen resizing. (Contributed by Arnon Yaari in [bpo-4254](https://bugs.python.org/issue?@action=redirect&bpo=4254).)

### dbm [¶](https://docs.python.org/3/whatsnew/3.5.html\#dbm "Link to this heading")

[`dumb.open`](https://docs.python.org/3/library/dbm.html#dbm.dumb.open "dbm.dumb.open") always creates a new database when the flag
has the value `"n"`. (Contributed by Claudiu Popa in [bpo-18039](https://bugs.python.org/issue?@action=redirect&bpo=18039).)

### difflib [¶](https://docs.python.org/3/whatsnew/3.5.html\#difflib "Link to this heading")

The charset of HTML documents generated by
[`HtmlDiff.make_file()`](https://docs.python.org/3/library/difflib.html#difflib.HtmlDiff.make_file "difflib.HtmlDiff.make_file")
can now be customized by using a new _charset_ keyword-only argument.
The default charset of HTML document changed from `"ISO-8859-1"`
to `"utf-8"`.
(Contributed by Berker Peksag in [bpo-2052](https://bugs.python.org/issue?@action=redirect&bpo=2052).)

The [`diff_bytes()`](https://docs.python.org/3/library/difflib.html#difflib.diff_bytes "difflib.diff_bytes") function can now compare lists of byte
strings. This fixes a regression from Python 2.
(Contributed by Terry J. Reedy and Greg Ward in [bpo-17445](https://bugs.python.org/issue?@action=redirect&bpo=17445).)

### distutils [¶](https://docs.python.org/3/whatsnew/3.5.html\#distutils "Link to this heading")

Both the `build` and `build_ext` commands now accept a `-j` option to
enable parallel building of extension modules.
(Contributed by Antoine Pitrou in [bpo-5309](https://bugs.python.org/issue?@action=redirect&bpo=5309).)

The `distutils` module now supports `xz` compression, and can be
enabled by passing `xztar` as an argument to `bdist --format`.
(Contributed by Serhiy Storchaka in [bpo-16314](https://bugs.python.org/issue?@action=redirect&bpo=16314).)

### doctest [¶](https://docs.python.org/3/whatsnew/3.5.html\#doctest "Link to this heading")

The [`DocTestSuite()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestSuite "doctest.DocTestSuite") function returns an empty
[`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") if _module_ contains no docstrings, instead of
raising [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"). (Contributed by Glenn Jones in [bpo-15916](https://bugs.python.org/issue?@action=redirect&bpo=15916).)

### email [¶](https://docs.python.org/3/whatsnew/3.5.html\#email "Link to this heading")

A new policy option [`Policy.mangle_from_`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy.mangle_from_ "email.policy.Policy.mangle_from_")
controls whether or not lines that start with `"From "` in email bodies are
prefixed with a `">"` character by generators. The default is `True` for
[`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.compat32 "email.policy.compat32") and `False` for all other policies.
(Contributed by Milan Oberkirch in [bpo-20098](https://bugs.python.org/issue?@action=redirect&bpo=20098).)

A new
[`Message.get_content_disposition()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.get_content_disposition "email.message.Message.get_content_disposition")
method provides easy access to a canonical value for the
_Content-Disposition_ header.
(Contributed by Abhilash Raj in [bpo-21083](https://bugs.python.org/issue?@action=redirect&bpo=21083).)

A new policy option [`EmailPolicy.utf8`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy.utf8 "email.policy.EmailPolicy.utf8")
can be set to `True` to encode email headers using the UTF-8 charset instead
of using encoded words. This allows `Messages` to be formatted according to
[**RFC 6532**](https://datatracker.ietf.org/doc/html/rfc6532.html) and used with an SMTP server that supports the [**RFC 6531**](https://datatracker.ietf.org/doc/html/rfc6531.html)`SMTPUTF8` extension. (Contributed by R. David Murray in
[bpo-24211](https://bugs.python.org/issue?@action=redirect&bpo=24211).)

The [`mime.text.MIMEText`](https://docs.python.org/3/library/email.mime.html#email.mime.text.MIMEText "email.mime.text.MIMEText") constructor now
accepts a [`charset.Charset`](https://docs.python.org/3/library/email.charset.html#email.charset.Charset "email.charset.Charset") instance.
(Contributed by Claude Paroz and Berker Peksag in [bpo-16324](https://bugs.python.org/issue?@action=redirect&bpo=16324).)

### enum [¶](https://docs.python.org/3/whatsnew/3.5.html\#enum "Link to this heading")

The [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum") callable has a new parameter _start_ to
specify the initial number of enum values if only _names_ are provided:

Copy

```
>>> Animal = enum.Enum('Animal', 'cat dog', start=10)
>>> Animal.cat
<Animal.cat: 10>
>>> Animal.dog
<Animal.dog: 11>
```

(Contributed by Ethan Furman in [bpo-21706](https://bugs.python.org/issue?@action=redirect&bpo=21706).)

### faulthandler [¶](https://docs.python.org/3/whatsnew/3.5.html\#faulthandler "Link to this heading")

The [`enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable"), [`register()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.register "faulthandler.register"),
[`dump_traceback()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback "faulthandler.dump_traceback") and
[`dump_traceback_later()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.dump_traceback_later "faulthandler.dump_traceback_later") functions now accept file
descriptors in addition to file-like objects.
(Contributed by Wei Wu in [bpo-23566](https://bugs.python.org/issue?@action=redirect&bpo=23566).)

### functools [¶](https://docs.python.org/3/whatsnew/3.5.html\#functools "Link to this heading")

Most of the [`lru_cache()`](https://docs.python.org/3/library/functools.html#functools.lru_cache "functools.lru_cache") machinery is now implemented in C, making
it significantly faster. (Contributed by Matt Joiner, Alexey Kachayev, and
Serhiy Storchaka in [bpo-14373](https://bugs.python.org/issue?@action=redirect&bpo=14373).)

### glob [¶](https://docs.python.org/3/whatsnew/3.5.html\#glob "Link to this heading")

The [`iglob()`](https://docs.python.org/3/library/glob.html#glob.iglob "glob.iglob") and [`glob()`](https://docs.python.org/3/library/glob.html#glob.glob "glob.glob") functions now support recursive
search in subdirectories, using the `"**"` pattern.
(Contributed by Serhiy Storchaka in [bpo-13968](https://bugs.python.org/issue?@action=redirect&bpo=13968).)

### gzip [¶](https://docs.python.org/3/whatsnew/3.5.html\#gzip "Link to this heading")

The _mode_ argument of the [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile") constructor now
accepts `"x"` to request exclusive creation.
(Contributed by Tim Heaney in [bpo-19222](https://bugs.python.org/issue?@action=redirect&bpo=19222).)

### heapq [¶](https://docs.python.org/3/whatsnew/3.5.html\#heapq "Link to this heading")

Element comparison in [`merge()`](https://docs.python.org/3/library/heapq.html#heapq.merge "heapq.merge") can now be customized by
passing a [key function](https://docs.python.org/3/glossary.html#term-key-function) in a new optional _key_ keyword argument,
and a new optional _reverse_ keyword argument can be used to reverse element
comparison:

Copy

```
>>> import heapq
>>> a = ['9', '777', '55555']
>>> b = ['88', '6666']
>>> list(heapq.merge(a, b, key=len))
['9', '88', '777', '6666', '55555']
>>> list(heapq.merge(reversed(a), reversed(b), key=len, reverse=True))
['55555', '6666', '777', '88', '9']
```

(Contributed by Raymond Hettinger in [bpo-13742](https://bugs.python.org/issue?@action=redirect&bpo=13742).)

### http [¶](https://docs.python.org/3/whatsnew/3.5.html\#http "Link to this heading")

A new [`HTTPStatus`](https://docs.python.org/3/library/http.html#http.HTTPStatus "http.HTTPStatus") enum that defines a set of
HTTP status codes, reason phrases and long descriptions written in English.
(Contributed by Demian Brecht in [bpo-21793](https://bugs.python.org/issue?@action=redirect&bpo=21793).)

### http.client [¶](https://docs.python.org/3/whatsnew/3.5.html\#http-client "Link to this heading")

[`HTTPConnection.getresponse()`](https://docs.python.org/3/library/http.client.html#http.client.HTTPConnection.getresponse "http.client.HTTPConnection.getresponse")
now raises a [`RemoteDisconnected`](https://docs.python.org/3/library/http.client.html#http.client.RemoteDisconnected "http.client.RemoteDisconnected") exception when a
remote server connection is closed unexpectedly. Additionally, if a
[`ConnectionError`](https://docs.python.org/3/library/exceptions.html#ConnectionError "ConnectionError") (of which `RemoteDisconnected`
is a subclass) is raised, the client socket is now closed automatically,
and will reconnect on the next request:

Copy

```
import http.client
conn = http.client.HTTPConnection('www.python.org')
for retries in range(3):
    try:
        conn.request('GET', '/')
        resp = conn.getresponse()
    except http.client.RemoteDisconnected:
        pass
```

(Contributed by Martin Panter in [bpo-3566](https://bugs.python.org/issue?@action=redirect&bpo=3566).)

### idlelib and IDLE [¶](https://docs.python.org/3/whatsnew/3.5.html\#idlelib-and-idle "Link to this heading")

Since idlelib implements the IDLE shell and editor and is not intended for
import by other programs, it gets improvements with every release. See
`Lib/idlelib/NEWS.txt` for a cumulative list of changes since 3.4.0,
as well as changes made in future 3.5.x releases. This file is also available
from the IDLE Help ‣ About IDLE dialog.

### imaplib [¶](https://docs.python.org/3/whatsnew/3.5.html\#imaplib "Link to this heading")

The [`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4") class now supports the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) protocol.
When used in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement, the IMAP4 `LOGOUT`
command will be called automatically at the end of the block.
(Contributed by Tarek Ziadé and Serhiy Storchaka in [bpo-4972](https://bugs.python.org/issue?@action=redirect&bpo=4972).)

The [`imaplib`](https://docs.python.org/3/library/imaplib.html#module-imaplib "imaplib: IMAP4 protocol client (requires sockets).") module now supports [**RFC 5161**](https://datatracker.ietf.org/doc/html/rfc5161.html) (ENABLE Extension)
and [**RFC 6855**](https://datatracker.ietf.org/doc/html/rfc6855.html) (UTF-8 Support) via the [`IMAP4.enable()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.enable "imaplib.IMAP4.enable")
method. A new [`IMAP4.utf8_enabled`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.utf8_enabled "imaplib.IMAP4.utf8_enabled")
attribute tracks whether or not [**RFC 6855**](https://datatracker.ietf.org/doc/html/rfc6855.html) support is enabled.
(Contributed by Milan Oberkirch, R. David Murray, and Maciej Szulik in
[bpo-21800](https://bugs.python.org/issue?@action=redirect&bpo=21800).)

The [`imaplib`](https://docs.python.org/3/library/imaplib.html#module-imaplib "imaplib: IMAP4 protocol client (requires sockets).") module now automatically encodes non-ASCII string usernames
and passwords using UTF-8, as recommended by the RFCs. (Contributed by Milan
Oberkirch in [bpo-21800](https://bugs.python.org/issue?@action=redirect&bpo=21800).)

### imghdr [¶](https://docs.python.org/3/whatsnew/3.5.html\#imghdr "Link to this heading")

The `what()` function now recognizes the
[OpenEXR](https://www.openexr.com/) format
(contributed by Martin Vignali and Claudiu Popa in [bpo-20295](https://bugs.python.org/issue?@action=redirect&bpo=20295)),
and the [WebP](https://en.wikipedia.org/wiki/WebP) format
(contributed by Fabrice Aneche and Claudiu Popa in [bpo-20197](https://bugs.python.org/issue?@action=redirect&bpo=20197).)

### importlib [¶](https://docs.python.org/3/whatsnew/3.5.html\#importlib "Link to this heading")

The [`util.LazyLoader`](https://docs.python.org/3/library/importlib.html#importlib.util.LazyLoader "importlib.util.LazyLoader") class allows for
lazy loading of modules in applications where startup time is important.
(Contributed by Brett Cannon in [bpo-17621](https://bugs.python.org/issue?@action=redirect&bpo=17621).)

The [`abc.InspectLoader.source_to_code()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.source_to_code "importlib.abc.InspectLoader.source_to_code")
method is now a static method. This makes it easier to initialize a module
object with code compiled from a string by running
`exec(code, module.__dict__)`.
(Contributed by Brett Cannon in [bpo-21156](https://bugs.python.org/issue?@action=redirect&bpo=21156).)

The new [`util.module_from_spec()`](https://docs.python.org/3/library/importlib.html#importlib.util.module_from_spec "importlib.util.module_from_spec")
function is now the preferred way to create a new module. As opposed to
creating a [`types.ModuleType`](https://docs.python.org/3/library/types.html#types.ModuleType "types.ModuleType") instance directly, this new function
will set the various import-controlled attributes based on the passed-in
spec object. (Contributed by Brett Cannon in [bpo-20383](https://bugs.python.org/issue?@action=redirect&bpo=20383).)

### inspect [¶](https://docs.python.org/3/whatsnew/3.5.html\#inspect "Link to this heading")

Both the [`Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "inspect.Signature") and [`Parameter`](https://docs.python.org/3/library/inspect.html#inspect.Parameter "inspect.Parameter") classes are
now picklable and hashable. (Contributed by Yury Selivanov in [bpo-20726](https://bugs.python.org/issue?@action=redirect&bpo=20726)
and [bpo-20334](https://bugs.python.org/issue?@action=redirect&bpo=20334).)

A new
[`BoundArguments.apply_defaults()`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.apply_defaults "inspect.BoundArguments.apply_defaults")
method provides a way to set default values for missing arguments:

Copy

```
>>> def foo(a, b='ham', *args): pass
>>> ba = inspect.signature(foo).bind('spam')
>>> ba.apply_defaults()
>>> ba.arguments
OrderedDict([('a', 'spam'), ('b', 'ham'), ('args', ())])
```

(Contributed by Yury Selivanov in [bpo-24190](https://bugs.python.org/issue?@action=redirect&bpo=24190).)

A new class method
[`Signature.from_callable()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.from_callable "inspect.Signature.from_callable") makes
subclassing of [`Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "inspect.Signature") easier. (Contributed
by Yury Selivanov and Eric Snow in [bpo-17373](https://bugs.python.org/issue?@action=redirect&bpo=17373).)

The [`signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature") function now accepts a _follow\_wrapped_
optional keyword argument, which, when set to `False`, disables automatic
following of `__wrapped__` links.
(Contributed by Yury Selivanov in [bpo-20691](https://bugs.python.org/issue?@action=redirect&bpo=20691).)

A set of new functions to inspect
[coroutine functions](https://docs.python.org/3/glossary.html#term-coroutine-function) and
[coroutine objects](https://docs.python.org/3/glossary.html#term-coroutine) has been added:
[`iscoroutine()`](https://docs.python.org/3/library/inspect.html#inspect.iscoroutine "inspect.iscoroutine"), [`iscoroutinefunction()`](https://docs.python.org/3/library/inspect.html#inspect.iscoroutinefunction "inspect.iscoroutinefunction"),
[`isawaitable()`](https://docs.python.org/3/library/inspect.html#inspect.isawaitable "inspect.isawaitable"), [`getcoroutinelocals()`](https://docs.python.org/3/library/inspect.html#inspect.getcoroutinelocals "inspect.getcoroutinelocals"),
and [`getcoroutinestate()`](https://docs.python.org/3/library/inspect.html#inspect.getcoroutinestate "inspect.getcoroutinestate").
(Contributed by Yury Selivanov in [bpo-24017](https://bugs.python.org/issue?@action=redirect&bpo=24017) and [bpo-24400](https://bugs.python.org/issue?@action=redirect&bpo=24400).)

The [`stack()`](https://docs.python.org/3/library/inspect.html#inspect.stack "inspect.stack"), [`trace()`](https://docs.python.org/3/library/inspect.html#inspect.trace "inspect.trace"),
[`getouterframes()`](https://docs.python.org/3/library/inspect.html#inspect.getouterframes "inspect.getouterframes"), and [`getinnerframes()`](https://docs.python.org/3/library/inspect.html#inspect.getinnerframes "inspect.getinnerframes")
functions now return a list of named tuples.
(Contributed by Daniel Shahaf in [bpo-16808](https://bugs.python.org/issue?@action=redirect&bpo=16808).)

### io [¶](https://docs.python.org/3/whatsnew/3.5.html\#io "Link to this heading")

A new [`BufferedIOBase.readinto1()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto1 "io.BufferedIOBase.readinto1")
method, that uses at most one call to the underlying raw stream’s
[`RawIOBase.read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read") or
[`RawIOBase.readinto()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto "io.RawIOBase.readinto") methods.
(Contributed by Nikolaus Rath in [bpo-20578](https://bugs.python.org/issue?@action=redirect&bpo=20578).)

### ipaddress [¶](https://docs.python.org/3/whatsnew/3.5.html\#ipaddress "Link to this heading")

Both the [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network") and [`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network") classes
now accept an `(address, netmask)` tuple argument, so as to easily construct
network objects from existing addresses:

Copy

```
>>> import ipaddress
>>> ipaddress.IPv4Network(('127.0.0.0', 8))
IPv4Network('127.0.0.0/8')
>>> ipaddress.IPv4Network(('127.0.0.0', '255.0.0.0'))
IPv4Network('127.0.0.0/8')
```

(Contributed by Peter Moody and Antoine Pitrou in [bpo-16531](https://bugs.python.org/issue?@action=redirect&bpo=16531).)

A new [`reverse_pointer`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address.reverse_pointer "ipaddress.IPv4Address.reverse_pointer") attribute for the
[`IPv4Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Address "ipaddress.IPv4Address") and [`IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address") classes
returns the name of the reverse DNS PTR record:

Copy

```
>>> import ipaddress
>>> addr = ipaddress.IPv4Address('127.0.0.1')
>>> addr.reverse_pointer
'1.0.0.127.in-addr.arpa'
>>> addr6 = ipaddress.IPv6Address('::1')
>>> addr6.reverse_pointer
'1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa'
```

(Contributed by Leon Weber in [bpo-20480](https://bugs.python.org/issue?@action=redirect&bpo=20480).)

### json [¶](https://docs.python.org/3/whatsnew/3.5.html\#json "Link to this heading")

The [`json.tool`](https://docs.python.org/3/library/json.html#module-json.tool "json.tool: A command-line interface to validate and pretty-print JSON.") command line interface now preserves the order of keys in
JSON objects passed in input. The new `--sort-keys` option can be used
to sort the keys alphabetically. (Contributed by Berker Peksag
in [bpo-21650](https://bugs.python.org/issue?@action=redirect&bpo=21650).)

JSON decoder now raises [`JSONDecodeError`](https://docs.python.org/3/library/json.html#json.JSONDecodeError "json.JSONDecodeError") instead of
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") to provide better context information about the error.
(Contributed by Serhiy Storchaka in [bpo-19361](https://bugs.python.org/issue?@action=redirect&bpo=19361).)

### linecache [¶](https://docs.python.org/3/whatsnew/3.5.html\#linecache "Link to this heading")

A new [`lazycache()`](https://docs.python.org/3/library/linecache.html#linecache.lazycache "linecache.lazycache") function can be used to capture information
about a non-file-based module to permit getting its lines later via
[`getline()`](https://docs.python.org/3/library/linecache.html#linecache.getline "linecache.getline"). This avoids doing I/O until a line is actually
needed, without having to carry the module globals around indefinitely.
(Contributed by Robert Collins in [bpo-17911](https://bugs.python.org/issue?@action=redirect&bpo=17911).)

### locale [¶](https://docs.python.org/3/whatsnew/3.5.html\#locale "Link to this heading")

A new [`delocalize()`](https://docs.python.org/3/library/locale.html#locale.delocalize "locale.delocalize") function can be used to convert a string into
a normalized number string, taking the `LC_NUMERIC` settings into account:

Copy

```
>>> import locale
>>> locale.setlocale(locale.LC_NUMERIC, 'de_DE.UTF-8')
'de_DE.UTF-8'
>>> locale.delocalize('1.234,56')
'1234.56'
>>> locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')
'en_US.UTF-8'
>>> locale.delocalize('1,234.56')
'1234.56'
```

(Contributed by Cédric Krier in [bpo-13918](https://bugs.python.org/issue?@action=redirect&bpo=13918).)

### logging [¶](https://docs.python.org/3/whatsnew/3.5.html\#logging "Link to this heading")

All logging methods ( [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") [`log()`](https://docs.python.org/3/library/logging.html#logging.Logger.log "logging.Logger.log"),
[`exception()`](https://docs.python.org/3/library/logging.html#logging.Logger.exception "logging.Logger.exception"), [`critical()`](https://docs.python.org/3/library/logging.html#logging.Logger.critical "logging.Logger.critical"),
[`debug()`](https://docs.python.org/3/library/logging.html#logging.Logger.debug "logging.Logger.debug"), etc.), now accept exception instances
as an _exc\_info_ argument, in addition to boolean values and exception
tuples:

Copy

```
>>> import logging
>>> try:
...     1/0
... except ZeroDivisionError as ex:
...     logging.error('exception', exc_info=ex)
ERROR:root:exception
```

(Contributed by Yury Selivanov in [bpo-20537](https://bugs.python.org/issue?@action=redirect&bpo=20537).)

The [`handlers.HTTPHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.HTTPHandler "logging.handlers.HTTPHandler") class now
accepts an optional [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") instance to configure SSL
settings used in an HTTP connection.
(Contributed by Alex Gaynor in [bpo-22788](https://bugs.python.org/issue?@action=redirect&bpo=22788).)

The [`handlers.QueueListener`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.QueueListener "logging.handlers.QueueListener") class now
takes a _respect\_handler\_level_ keyword argument which, if set to `True`,
will pass messages to handlers taking handler levels into account.
(Contributed by Vinay Sajip.)

### lzma [¶](https://docs.python.org/3/whatsnew/3.5.html\#lzma "Link to this heading")

The [`LZMADecompressor.decompress()`](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.decompress "lzma.LZMADecompressor.decompress")
method now accepts an optional _max\_length_ argument to limit the maximum
size of decompressed data.
(Contributed by Martin Panter in [bpo-15955](https://bugs.python.org/issue?@action=redirect&bpo=15955).)

### math [¶](https://docs.python.org/3/whatsnew/3.5.html\#math "Link to this heading")

Two new constants have been added to the [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).") module: [`inf`](https://docs.python.org/3/library/math.html#math.inf "math.inf")
and [`nan`](https://docs.python.org/3/library/math.html#math.nan "math.nan"). (Contributed by Mark Dickinson in [bpo-23185](https://bugs.python.org/issue?@action=redirect&bpo=23185).)

A new function [`isclose()`](https://docs.python.org/3/library/math.html#math.isclose "math.isclose") provides a way to test for approximate
equality. (Contributed by Chris Barker and Tal Einat in [bpo-24270](https://bugs.python.org/issue?@action=redirect&bpo=24270).)

A new [`gcd()`](https://docs.python.org/3/library/math.html#math.gcd "math.gcd") function has been added. The `fractions.gcd()`
function is now deprecated. (Contributed by Mark Dickinson and Serhiy
Storchaka in [bpo-22486](https://bugs.python.org/issue?@action=redirect&bpo=22486).)

### multiprocessing [¶](https://docs.python.org/3/whatsnew/3.5.html\#multiprocessing "Link to this heading")

[`sharedctypes.synchronized()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.sharedctypes.synchronized "multiprocessing.sharedctypes.synchronized")
objects now support the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) protocol.
(Contributed by Charles-François Natali in [bpo-21565](https://bugs.python.org/issue?@action=redirect&bpo=21565).)

### operator [¶](https://docs.python.org/3/whatsnew/3.5.html\#operator "Link to this heading")

[`attrgetter()`](https://docs.python.org/3/library/operator.html#operator.attrgetter "operator.attrgetter"), [`itemgetter()`](https://docs.python.org/3/library/operator.html#operator.itemgetter "operator.itemgetter"),
and [`methodcaller()`](https://docs.python.org/3/library/operator.html#operator.methodcaller "operator.methodcaller") objects now support pickling.
(Contributed by Josh Rosenberg and Serhiy Storchaka in [bpo-22955](https://bugs.python.org/issue?@action=redirect&bpo=22955).)

New [`matmul()`](https://docs.python.org/3/library/operator.html#operator.matmul "operator.matmul") and [`imatmul()`](https://docs.python.org/3/library/operator.html#operator.imatmul "operator.imatmul") functions
to perform matrix multiplication.
(Contributed by Benjamin Peterson in [bpo-21176](https://bugs.python.org/issue?@action=redirect&bpo=21176).)

### os [¶](https://docs.python.org/3/whatsnew/3.5.html\#os "Link to this heading")

The new [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir") function returning an iterator of
[`DirEntry`](https://docs.python.org/3/library/os.html#os.DirEntry "os.DirEntry") objects has been added. If possible, [`scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
extracts file attributes while scanning a directory, removing the need to
perform subsequent system calls to determine file type or attributes, which may
significantly improve performance. (Contributed by Ben Hoyt with the help
of Victor Stinner in [bpo-22524](https://bugs.python.org/issue?@action=redirect&bpo=22524).)

On Windows, a new
[`stat_result.st_file_attributes`](https://docs.python.org/3/library/os.html#os.stat_result.st_file_attributes "os.stat_result.st_file_attributes")
attribute is now available. It corresponds to the `dwFileAttributes` member
of the `BY_HANDLE_FILE_INFORMATION` structure returned by
`GetFileInformationByHandle()`. (Contributed by Ben Hoyt in [bpo-21719](https://bugs.python.org/issue?@action=redirect&bpo=21719).)

The [`urandom()`](https://docs.python.org/3/library/os.html#os.urandom "os.urandom") function now uses the `getrandom()` syscall on Linux 3.17
or newer, and `getentropy()` on OpenBSD 5.6 and newer, removing the need to
use `/dev/urandom` and avoiding failures due to potential file descriptor
exhaustion. (Contributed by Victor Stinner in [bpo-22181](https://bugs.python.org/issue?@action=redirect&bpo=22181).)

New [`get_blocking()`](https://docs.python.org/3/library/os.html#os.get_blocking "os.get_blocking") and [`set_blocking()`](https://docs.python.org/3/library/os.html#os.set_blocking "os.set_blocking") functions allow
getting and setting a file descriptor’s blocking mode ( [`O_NONBLOCK`](https://docs.python.org/3/library/os.html#os.O_NONBLOCK "os.O_NONBLOCK").)
(Contributed by Victor Stinner in [bpo-22054](https://bugs.python.org/issue?@action=redirect&bpo=22054).)

The [`truncate()`](https://docs.python.org/3/library/os.html#os.truncate "os.truncate") and [`ftruncate()`](https://docs.python.org/3/library/os.html#os.ftruncate "os.ftruncate") functions are now supported
on Windows. (Contributed by Steve Dower in [bpo-23668](https://bugs.python.org/issue?@action=redirect&bpo=23668).)

There is a new [`os.path.commonpath()`](https://docs.python.org/3/library/os.path.html#os.path.commonpath "os.path.commonpath") function returning the longest
common sub-path of each passed pathname. Unlike the
[`os.path.commonprefix()`](https://docs.python.org/3/library/os.path.html#os.path.commonprefix "os.path.commonprefix") function, it always returns a valid
path:

Copy

```
>>> os.path.commonprefix(['/usr/lib', '/usr/local/lib'])
'/usr/l'

>>> os.path.commonpath(['/usr/lib', '/usr/local/lib'])
'/usr'
```

(Contributed by Rafik Draoui and Serhiy Storchaka in [bpo-10395](https://bugs.python.org/issue?@action=redirect&bpo=10395).)

### pathlib [¶](https://docs.python.org/3/whatsnew/3.5.html\#pathlib "Link to this heading")

The new [`Path.samefile()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.samefile "pathlib.Path.samefile") method can be used
to check whether the path points to the same file as another path, which can
be either another [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") object, or a string:

Copy

```
>>> import pathlib
>>> p1 = pathlib.Path('/etc/hosts')
>>> p2 = pathlib.Path('/etc/../etc/hosts')
>>> p1.samefile(p2)
True
```

(Contributed by Vajrasky Kok and Antoine Pitrou in [bpo-19775](https://bugs.python.org/issue?@action=redirect&bpo=19775).)

The [`Path.mkdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir "pathlib.Path.mkdir") method now accepts a new optional
_exist\_ok_ argument to match `mkdir -p` and [`os.makedirs()`](https://docs.python.org/3/library/os.html#os.makedirs "os.makedirs")
functionality. (Contributed by Berker Peksag in [bpo-21539](https://bugs.python.org/issue?@action=redirect&bpo=21539).)

There is a new [`Path.expanduser()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.expanduser "pathlib.Path.expanduser") method to
expand `~` and `~user` prefixes. (Contributed by Serhiy Storchaka and
Claudiu Popa in [bpo-19776](https://bugs.python.org/issue?@action=redirect&bpo=19776).)

A new [`Path.home()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.home "pathlib.Path.home") class method can be used to get
a [`Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") instance representing the user’s home
directory.
(Contributed by Victor Salgado and Mayank Tripathi in [bpo-19777](https://bugs.python.org/issue?@action=redirect&bpo=19777).)

New [`Path.write_text()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_text "pathlib.Path.write_text"),
[`Path.read_text()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_text "pathlib.Path.read_text"),
[`Path.write_bytes()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.write_bytes "pathlib.Path.write_bytes"),
[`Path.read_bytes()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.read_bytes "pathlib.Path.read_bytes") methods to simplify
read/write operations on files.

The following code snippet will create or rewrite existing file
`~/spam42`:

Copy

```
>>> import pathlib
>>> p = pathlib.Path('~/spam42')
>>> p.expanduser().write_text('ham')
3
```

(Contributed by Christopher Welborn in [bpo-20218](https://bugs.python.org/issue?@action=redirect&bpo=20218).)

### pickle [¶](https://docs.python.org/3/whatsnew/3.5.html\#pickle "Link to this heading")

Nested objects, such as unbound methods or nested classes, can now be pickled
using [pickle protocols](https://docs.python.org/3/library/pickle.html#pickle-protocols) older than protocol version 4.
Protocol version 4 already supports these cases. (Contributed by Serhiy
Storchaka in [bpo-23611](https://bugs.python.org/issue?@action=redirect&bpo=23611).)

### poplib [¶](https://docs.python.org/3/whatsnew/3.5.html\#poplib "Link to this heading")

A new [`POP3.utf8()`](https://docs.python.org/3/library/poplib.html#poplib.POP3.utf8 "poplib.POP3.utf8") command enables [**RFC 6856**](https://datatracker.ietf.org/doc/html/rfc6856.html)
(Internationalized Email) support, if a POP server supports it.
(Contributed by Milan OberKirch in [bpo-21804](https://bugs.python.org/issue?@action=redirect&bpo=21804).)

### re [¶](https://docs.python.org/3/whatsnew/3.5.html\#re "Link to this heading")

References and conditional references to groups with fixed length are now
allowed in lookbehind assertions:

Copy

```
>>> import re
>>> pat = re.compile(r'(a|b).(?<=\1)c')
>>> pat.match('aac')
<_sre.SRE_Match object; span=(0, 3), match='aac'>
>>> pat.match('bbc')
<_sre.SRE_Match object; span=(0, 3), match='bbc'>
```

(Contributed by Serhiy Storchaka in [bpo-9179](https://bugs.python.org/issue?@action=redirect&bpo=9179).)

The number of capturing groups in regular expressions is no longer limited to
100\. (Contributed by Serhiy Storchaka in [bpo-22437](https://bugs.python.org/issue?@action=redirect&bpo=22437).)

The [`sub()`](https://docs.python.org/3/library/re.html#re.sub "re.sub") and [`subn()`](https://docs.python.org/3/library/re.html#re.subn "re.subn") functions now replace unmatched
groups with empty strings instead of raising an exception.
(Contributed by Serhiy Storchaka in [bpo-1519638](https://bugs.python.org/issue?@action=redirect&bpo=1519638).)

The [`re.error`](https://docs.python.org/3/library/re.html#re.PatternError "re.PatternError") exceptions have new attributes,
[`msg`](https://docs.python.org/3/library/re.html#re.PatternError.msg "re.PatternError.msg"), [`pattern`](https://docs.python.org/3/library/re.html#re.PatternError.pattern "re.PatternError.pattern"),
[`pos`](https://docs.python.org/3/library/re.html#re.PatternError.pos "re.PatternError.pos"), [`lineno`](https://docs.python.org/3/library/re.html#re.PatternError.lineno "re.PatternError.lineno"),
and [`colno`](https://docs.python.org/3/library/re.html#re.PatternError.colno "re.PatternError.colno"), that provide better context
information about the error:

Copy

```
>>> re.compile("""
...     (?x)
...     .++
... """)
Traceback (most recent call last):
   ...
sre_constants.error: multiple repeat at position 16 (line 3, column 7)
```

(Contributed by Serhiy Storchaka in [bpo-22578](https://bugs.python.org/issue?@action=redirect&bpo=22578).)

### readline [¶](https://docs.python.org/3/whatsnew/3.5.html\#readline "Link to this heading")

A new [`append_history_file()`](https://docs.python.org/3/library/readline.html#readline.append_history_file "readline.append_history_file") function can be used to append
the specified number of trailing elements in history to the given file.
(Contributed by Bruno Cauet in [bpo-22940](https://bugs.python.org/issue?@action=redirect&bpo=22940).)

### selectors [¶](https://docs.python.org/3/whatsnew/3.5.html\#selectors "Link to this heading")

The new [`DevpollSelector`](https://docs.python.org/3/library/selectors.html#selectors.DevpollSelector "selectors.DevpollSelector") supports efficient
`/dev/poll` polling on Solaris.
(Contributed by Giampaolo Rodola’ in [bpo-18931](https://bugs.python.org/issue?@action=redirect&bpo=18931).)

### shutil [¶](https://docs.python.org/3/whatsnew/3.5.html\#shutil "Link to this heading")

The [`move()`](https://docs.python.org/3/library/shutil.html#shutil.move "shutil.move") function now accepts a _copy\_function_ argument,
allowing, for example, the [`copy()`](https://docs.python.org/3/library/shutil.html#shutil.copy "shutil.copy") function to be used instead of
the default [`copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2") if there is a need to ignore file metadata
when moving.
(Contributed by Claudiu Popa in [bpo-19840](https://bugs.python.org/issue?@action=redirect&bpo=19840).)

The [`make_archive()`](https://docs.python.org/3/library/shutil.html#shutil.make_archive "shutil.make_archive") function now supports the _xztar_ format.
(Contributed by Serhiy Storchaka in [bpo-5411](https://bugs.python.org/issue?@action=redirect&bpo=5411).)

### signal [¶](https://docs.python.org/3/whatsnew/3.5.html\#signal "Link to this heading")

On Windows, the [`set_wakeup_fd()`](https://docs.python.org/3/library/signal.html#signal.set_wakeup_fd "signal.set_wakeup_fd") function now also supports
socket handles. (Contributed by Victor Stinner in [bpo-22018](https://bugs.python.org/issue?@action=redirect&bpo=22018).)

Various `SIG*` constants in the [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.") module have been converted into
[`Enums`](https://docs.python.org/3/library/enum.html#module-enum "enum: Implementation of an enumeration class."). This allows meaningful names to be printed
during debugging, instead of integer “magic numbers”.
(Contributed by Giampaolo Rodola’ in [bpo-21076](https://bugs.python.org/issue?@action=redirect&bpo=21076).)

### smtpd [¶](https://docs.python.org/3/whatsnew/3.5.html\#smtpd "Link to this heading")

Both the `SMTPServer` and `SMTPChannel` classes now
accept a _decode\_data_ keyword argument to determine if the `DATA` portion of
the SMTP transaction is decoded using the `"utf-8"` codec or is instead
provided to the
`SMTPServer.process_message()`
method as a byte string. The default is `True` for backward compatibility
reasons, but will change to `False` in Python 3.6. If _decode\_data_ is set
to `False`, the `process_message` method must be prepared to accept keyword
arguments.
(Contributed by Maciej Szulik in [bpo-19662](https://bugs.python.org/issue?@action=redirect&bpo=19662).)

The `SMTPServer` class now advertises the `8BITMIME` extension
( [**RFC 6152**](https://datatracker.ietf.org/doc/html/rfc6152.html)) if _decode\_data_ has been set `True`. If the client
specifies `BODY=8BITMIME` on the `MAIL` command, it is passed to
`SMTPServer.process_message()`
via the _mail\_options_ keyword.
(Contributed by Milan Oberkirch and R. David Murray in [bpo-21795](https://bugs.python.org/issue?@action=redirect&bpo=21795).)

The `SMTPServer` class now also supports the `SMTPUTF8`
extension ( [**RFC 6531**](https://datatracker.ietf.org/doc/html/rfc6531.html): Internationalized Email). If the client specified
`SMTPUTF8 BODY=8BITMIME` on the `MAIL` command, they are passed to
`SMTPServer.process_message()`
via the _mail\_options_ keyword. It is the responsibility of the
`process_message` method to correctly handle the `SMTPUTF8` data.
(Contributed by Milan Oberkirch in [bpo-21725](https://bugs.python.org/issue?@action=redirect&bpo=21725).)

It is now possible to provide, directly or via name resolution, IPv6
addresses in the `SMTPServer` constructor, and have it
successfully connect. (Contributed by Milan Oberkirch in [bpo-14758](https://bugs.python.org/issue?@action=redirect&bpo=14758).)

### smtplib [¶](https://docs.python.org/3/whatsnew/3.5.html\#smtplib "Link to this heading")

A new [`SMTP.auth()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.auth "smtplib.SMTP.auth") method provides a convenient way to
implement custom authentication mechanisms. (Contributed by Milan
Oberkirch in [bpo-15014](https://bugs.python.org/issue?@action=redirect&bpo=15014).)

The [`SMTP.set_debuglevel()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.set_debuglevel "smtplib.SMTP.set_debuglevel") method now
accepts an additional debuglevel (2), which enables timestamps in debug
messages. (Contributed by Gavin Chappell and Maciej Szulik in [bpo-16914](https://bugs.python.org/issue?@action=redirect&bpo=16914).)

Both the [`SMTP.sendmail()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.sendmail "smtplib.SMTP.sendmail") and
[`SMTP.send_message()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.send_message "smtplib.SMTP.send_message") methods now
support [**RFC 6531**](https://datatracker.ietf.org/doc/html/rfc6531.html) (SMTPUTF8).
(Contributed by Milan Oberkirch and R. David Murray in [bpo-22027](https://bugs.python.org/issue?@action=redirect&bpo=22027).)

### sndhdr [¶](https://docs.python.org/3/whatsnew/3.5.html\#sndhdr "Link to this heading")

The `what()` and `whathdr()` functions now return
a [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple"). (Contributed by Claudiu Popa in
[bpo-18615](https://bugs.python.org/issue?@action=redirect&bpo=18615).)

### socket [¶](https://docs.python.org/3/whatsnew/3.5.html\#socket "Link to this heading")

Functions with timeouts now use a monotonic clock, instead of a system clock.
(Contributed by Victor Stinner in [bpo-22043](https://bugs.python.org/issue?@action=redirect&bpo=22043).)

A new [`socket.sendfile()`](https://docs.python.org/3/library/socket.html#socket.socket.sendfile "socket.socket.sendfile") method allows
sending a file over a socket by using the high-performance [`os.sendfile()`](https://docs.python.org/3/library/os.html#os.sendfile "os.sendfile")
function on UNIX, resulting in uploads being from 2 to 3 times faster than when
using plain [`socket.send()`](https://docs.python.org/3/library/socket.html#socket.socket.send "socket.socket.send").
(Contributed by Giampaolo Rodola’ in [bpo-17552](https://bugs.python.org/issue?@action=redirect&bpo=17552).)

The [`socket.sendall()`](https://docs.python.org/3/library/socket.html#socket.socket.sendall "socket.socket.sendall") method no longer resets the
socket timeout every time bytes are received or sent. The socket timeout is
now the maximum total duration to send all data.
(Contributed by Victor Stinner in [bpo-23853](https://bugs.python.org/issue?@action=redirect&bpo=23853).)

The _backlog_ argument of the [`socket.listen()`](https://docs.python.org/3/library/socket.html#socket.socket.listen "socket.socket.listen")
method is now optional. By default it is set to
[`SOMAXCONN`](https://docs.python.org/3/library/socket.html#socket.SOMAXCONN "socket.SOMAXCONN") or to `128`, whichever is less.
(Contributed by Charles-François Natali in [bpo-21455](https://bugs.python.org/issue?@action=redirect&bpo=21455).)

### ssl [¶](https://docs.python.org/3/whatsnew/3.5.html\#ssl "Link to this heading")

#### Memory BIO Support [¶](https://docs.python.org/3/whatsnew/3.5.html\#memory-bio-support "Link to this heading")

(Contributed by Geert Jansen in [bpo-21965](https://bugs.python.org/issue?@action=redirect&bpo=21965).)

The new [`SSLObject`](https://docs.python.org/3/library/ssl.html#ssl.SSLObject "ssl.SSLObject") class has been added to provide SSL protocol
support for cases when the network I/O capabilities of [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket")
are not necessary or are suboptimal. `SSLObject` represents
an SSL protocol instance, but does not implement any network I/O methods, and
instead provides a memory buffer interface. The new [`MemoryBIO`](https://docs.python.org/3/library/ssl.html#ssl.MemoryBIO "ssl.MemoryBIO")
class can be used to pass data between Python and an SSL protocol instance.

The memory BIO SSL support is primarily intended to be used in frameworks
implementing asynchronous I/O for which [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket")’s readiness
model (“select/poll”) is inefficient.

A new [`SSLContext.wrap_bio()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_bio "ssl.SSLContext.wrap_bio") method can be used
to create a new `SSLObject` instance.

#### Application-Layer Protocol Negotiation Support [¶](https://docs.python.org/3/whatsnew/3.5.html\#application-layer-protocol-negotiation-support "Link to this heading")

(Contributed by Benjamin Peterson in [bpo-20188](https://bugs.python.org/issue?@action=redirect&bpo=20188).)

Where OpenSSL support is present, the [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects") module now implements
the _Application-Layer Protocol Negotiation_ TLS extension as described
in [**RFC 7301**](https://datatracker.ietf.org/doc/html/rfc7301.html).

The new [`SSLContext.set_alpn_protocols()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_alpn_protocols "ssl.SSLContext.set_alpn_protocols")
can be used to specify which protocols a socket should advertise during
the TLS handshake.

The new
[`SSLSocket.selected_alpn_protocol()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.selected_alpn_protocol "ssl.SSLSocket.selected_alpn_protocol")
returns the protocol that was selected during the TLS handshake.
The [`HAS_ALPN`](https://docs.python.org/3/library/ssl.html#ssl.HAS_ALPN "ssl.HAS_ALPN") flag indicates whether ALPN support is present.

#### Other Changes [¶](https://docs.python.org/3/whatsnew/3.5.html\#other-changes "Link to this heading")

There is a new [`SSLSocket.version()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.version "ssl.SSLSocket.version") method to
query the actual protocol version in use.
(Contributed by Antoine Pitrou in [bpo-20421](https://bugs.python.org/issue?@action=redirect&bpo=20421).)

The [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket") class now implements
a `SSLSocket.sendfile()` method.
(Contributed by Giampaolo Rodola’ in [bpo-17552](https://bugs.python.org/issue?@action=redirect&bpo=17552).)

The `SSLSocket.send()` method now raises either
the [`ssl.SSLWantReadError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantReadError "ssl.SSLWantReadError") or [`ssl.SSLWantWriteError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantWriteError "ssl.SSLWantWriteError") exception on a
non-blocking socket if the operation would block. Previously, it would return
`0`. (Contributed by Nikolaus Rath in [bpo-20951](https://bugs.python.org/issue?@action=redirect&bpo=20951).)

The [`cert_time_to_seconds()`](https://docs.python.org/3/library/ssl.html#ssl.cert_time_to_seconds "ssl.cert_time_to_seconds") function now interprets the input time
as UTC and not as local time, per [**RFC 5280**](https://datatracker.ietf.org/doc/html/rfc5280.html). Additionally, the return
value is always an [`int`](https://docs.python.org/3/library/functions.html#int "int"). (Contributed by Akira Li in [bpo-19940](https://bugs.python.org/issue?@action=redirect&bpo=19940).)

New `SSLObject.shared_ciphers()` and
[`SSLSocket.shared_ciphers()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.shared_ciphers "ssl.SSLSocket.shared_ciphers") methods return
the list of ciphers sent by the client during the handshake.
(Contributed by Benjamin Peterson in [bpo-23186](https://bugs.python.org/issue?@action=redirect&bpo=23186).)

The [`SSLSocket.do_handshake()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.do_handshake "ssl.SSLSocket.do_handshake"),
[`SSLSocket.read()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.read "ssl.SSLSocket.read"),
`SSLSocket.shutdown()`, and
[`SSLSocket.write()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.write "ssl.SSLSocket.write") methods of the [`SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket")
class no longer reset the socket timeout every time bytes are received or sent.
The socket timeout is now the maximum total duration of the method.
(Contributed by Victor Stinner in [bpo-23853](https://bugs.python.org/issue?@action=redirect&bpo=23853).)

The `match_hostname()` function now supports matching of IP addresses.
(Contributed by Antoine Pitrou in [bpo-23239](https://bugs.python.org/issue?@action=redirect&bpo=23239).)

### sqlite3 [¶](https://docs.python.org/3/whatsnew/3.5.html\#sqlite3 "Link to this heading")

The [`Row`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Row "sqlite3.Row") class now fully supports the sequence protocol,
in particular [`reversed()`](https://docs.python.org/3/library/functions.html#reversed "reversed") iteration and slice indexing.
(Contributed by Claudiu Popa in [bpo-10203](https://bugs.python.org/issue?@action=redirect&bpo=10203); by Lucas Sinclair,
Jessica McKellar, and Serhiy Storchaka in [bpo-13583](https://bugs.python.org/issue?@action=redirect&bpo=13583).)

### subprocess [¶](https://docs.python.org/3/whatsnew/3.5.html\#subprocess "Link to this heading")

The new [`run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run") function has been added.
It runs the specified command and returns a
[`CompletedProcess`](https://docs.python.org/3/library/subprocess.html#subprocess.CompletedProcess "subprocess.CompletedProcess") object, which describes a finished
process. The new API is more consistent and is the recommended approach
to invoking subprocesses in Python code that does not need to maintain
compatibility with earlier Python versions.
(Contributed by Thomas Kluyver in [bpo-23342](https://bugs.python.org/issue?@action=redirect&bpo=23342).)

Examples:

Copy

```
>>> subprocess.run(["ls", "-l"])  # doesn't capture output
CompletedProcess(args=['ls', '-l'], returncode=0)

>>> subprocess.run("exit 1", shell=True, check=True)
Traceback (most recent call last):
  ...
subprocess.CalledProcessError: Command 'exit 1' returned non-zero exit status 1

>>> subprocess.run(["ls", "-l", "/dev/null"], stdout=subprocess.PIPE)
CompletedProcess(args=['ls', '-l', '/dev/null'], returncode=0,
stdout=b'crw-rw-rw- 1 root root 1, 3 Jan 23 16:23 /dev/null\n')
```

### sys [¶](https://docs.python.org/3/whatsnew/3.5.html\#sys "Link to this heading")

A new `set_coroutine_wrapper()` function allows setting a global
hook that will be called whenever a [coroutine object](https://docs.python.org/3/glossary.html#term-coroutine)
is created by an [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def) function. A corresponding
`get_coroutine_wrapper()` can be used to obtain a currently set
wrapper. Both functions are [provisional](https://docs.python.org/3/glossary.html#term-provisional-API),
and are intended for debugging purposes only. (Contributed by Yury Selivanov
in [bpo-24017](https://bugs.python.org/issue?@action=redirect&bpo=24017).)

A new [`is_finalizing()`](https://docs.python.org/3/library/sys.html#sys.is_finalizing "sys.is_finalizing") function can be used to check if the Python
interpreter is [shutting down](https://docs.python.org/3/glossary.html#term-interpreter-shutdown).
(Contributed by Antoine Pitrou in [bpo-22696](https://bugs.python.org/issue?@action=redirect&bpo=22696).)

### sysconfig [¶](https://docs.python.org/3/whatsnew/3.5.html\#sysconfig "Link to this heading")

The name of the user scripts directory on Windows now includes the first
two components of the Python version. (Contributed by Paul Moore
in [bpo-23437](https://bugs.python.org/issue?@action=redirect&bpo=23437).)

### tarfile [¶](https://docs.python.org/3/whatsnew/3.5.html\#tarfile "Link to this heading")

The _mode_ argument of the [`open()`](https://docs.python.org/3/library/tarfile.html#tarfile.open "tarfile.open") function now accepts `"x"`
to request exclusive creation. (Contributed by Berker Peksag in [bpo-21717](https://bugs.python.org/issue?@action=redirect&bpo=21717).)

The [`TarFile.extractall()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extractall "tarfile.TarFile.extractall") and
[`TarFile.extract()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.extract "tarfile.TarFile.extract") methods now take a keyword
argument _numeric\_owner_. If set to `True`, the extracted files and
directories will be owned by the numeric `uid` and `gid` from the tarfile.
If set to `False` (the default, and the behavior in versions prior to 3.5),
they will be owned by the named user and group in the tarfile.
(Contributed by Michael Vogt and Eric Smith in [bpo-23193](https://bugs.python.org/issue?@action=redirect&bpo=23193).)

The [`TarFile.list()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.list "tarfile.TarFile.list") now accepts an optional
_members_ keyword argument that can be set to a subset of the list returned
by [`TarFile.getmembers()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.getmembers "tarfile.TarFile.getmembers").
(Contributed by Serhiy Storchaka in [bpo-21549](https://bugs.python.org/issue?@action=redirect&bpo=21549).)

### threading [¶](https://docs.python.org/3/whatsnew/3.5.html\#threading "Link to this heading")

Both the [`Lock.acquire()`](https://docs.python.org/3/library/threading.html#threading.Lock.acquire "threading.Lock.acquire") and
[`RLock.acquire()`](https://docs.python.org/3/library/threading.html#threading.RLock.acquire "threading.RLock.acquire") methods
now use a monotonic clock for timeout management.
(Contributed by Victor Stinner in [bpo-22043](https://bugs.python.org/issue?@action=redirect&bpo=22043).)

### time [¶](https://docs.python.org/3/whatsnew/3.5.html\#time "Link to this heading")

The [`monotonic()`](https://docs.python.org/3/library/time.html#time.monotonic "time.monotonic") function is now always available.
(Contributed by Victor Stinner in [bpo-22043](https://bugs.python.org/issue?@action=redirect&bpo=22043).)

### timeit [¶](https://docs.python.org/3/whatsnew/3.5.html\#timeit "Link to this heading")

A new command line option `-u` or `--unit=U` can be used to specify the time
unit for the timer output. Supported options are `usec`, `msec`,
or `sec`. (Contributed by Julian Gindi in [bpo-18983](https://bugs.python.org/issue?@action=redirect&bpo=18983).)

The [`timeit()`](https://docs.python.org/3/library/timeit.html#timeit.timeit "timeit.timeit") function has a new _globals_ parameter for
specifying the namespace in which the code will be running.
(Contributed by Ben Roberts in [bpo-2527](https://bugs.python.org/issue?@action=redirect&bpo=2527).)

### tkinter [¶](https://docs.python.org/3/whatsnew/3.5.html\#tkinter "Link to this heading")

The `tkinter._fix` module used for setting up the Tcl/Tk environment
on Windows has been replaced by a private function in the `_tkinter`
module which makes no permanent changes to environment variables.
(Contributed by Zachary Ware in [bpo-20035](https://bugs.python.org/issue?@action=redirect&bpo=20035).)

### traceback [¶](https://docs.python.org/3/whatsnew/3.5.html\#traceback "Link to this heading")

New [`walk_stack()`](https://docs.python.org/3/library/traceback.html#traceback.walk_stack "traceback.walk_stack") and [`walk_tb()`](https://docs.python.org/3/library/traceback.html#traceback.walk_tb "traceback.walk_tb")
functions to conveniently traverse frame and
[traceback objects](https://docs.python.org/3/reference/datamodel.html#traceback-objects).
(Contributed by Robert Collins in [bpo-17911](https://bugs.python.org/issue?@action=redirect&bpo=17911).)

New lightweight classes: [`TracebackException`](https://docs.python.org/3/library/traceback.html#traceback.TracebackException "traceback.TracebackException"),
[`StackSummary`](https://docs.python.org/3/library/traceback.html#traceback.StackSummary "traceback.StackSummary"), and [`FrameSummary`](https://docs.python.org/3/library/traceback.html#traceback.FrameSummary "traceback.FrameSummary").
(Contributed by Robert Collins in [bpo-17911](https://bugs.python.org/issue?@action=redirect&bpo=17911).)

Both the [`print_tb()`](https://docs.python.org/3/library/traceback.html#traceback.print_tb "traceback.print_tb") and [`print_stack()`](https://docs.python.org/3/library/traceback.html#traceback.print_stack "traceback.print_stack") functions
now support negative values for the _limit_ argument.
(Contributed by Dmitry Kazakov in [bpo-22619](https://bugs.python.org/issue?@action=redirect&bpo=22619).)

### types [¶](https://docs.python.org/3/whatsnew/3.5.html\#types "Link to this heading")

A new [`coroutine()`](https://docs.python.org/3/library/types.html#types.coroutine "types.coroutine") function to transform
[generator](https://docs.python.org/3/glossary.html#term-generator-iterator) and
[`generator-like`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator") objects into
[awaitables](https://docs.python.org/3/glossary.html#term-awaitable).
(Contributed by Yury Selivanov in [bpo-24017](https://bugs.python.org/issue?@action=redirect&bpo=24017).)

A new type called [`CoroutineType`](https://docs.python.org/3/library/types.html#types.CoroutineType "types.CoroutineType"), which is used for
[coroutine](https://docs.python.org/3/glossary.html#term-coroutine) objects created by [`async def`](https://docs.python.org/3/reference/compound_stmts.html#async-def) functions.
(Contributed by Yury Selivanov in [bpo-24400](https://bugs.python.org/issue?@action=redirect&bpo=24400).)

### unicodedata [¶](https://docs.python.org/3/whatsnew/3.5.html\#unicodedata "Link to this heading")

The [`unicodedata`](https://docs.python.org/3/library/unicodedata.html#module-unicodedata "unicodedata: Access the Unicode Database.") module now uses data from [Unicode 8.0.0](https://unicode.org/versions/Unicode8.0.0/).

### unittest [¶](https://docs.python.org/3/whatsnew/3.5.html\#unittest "Link to this heading")

The [`TestLoader.loadTestsFromModule()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromModule "unittest.TestLoader.loadTestsFromModule")
method now accepts a keyword-only argument _pattern_ which is passed to
`load_tests` as the third argument. Found packages are now checked for
`load_tests` regardless of whether their path matches _pattern_, because it
is impossible for a package name to match the default pattern.
(Contributed by Robert Collins and Barry A. Warsaw in [bpo-16662](https://bugs.python.org/issue?@action=redirect&bpo=16662).)

Unittest discovery errors now are exposed in the
[`TestLoader.errors`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.errors "unittest.TestLoader.errors") attribute of the
[`TestLoader`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader "unittest.TestLoader") instance.
(Contributed by Robert Collins in [bpo-19746](https://bugs.python.org/issue?@action=redirect&bpo=19746).)

A new command line option `--locals` to show local variables in
tracebacks. (Contributed by Robert Collins in [bpo-22936](https://bugs.python.org/issue?@action=redirect&bpo=22936).)

### unittest.mock [¶](https://docs.python.org/3/whatsnew/3.5.html\#unittest-mock "Link to this heading")

The [`Mock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock "unittest.mock.Mock") class has the following improvements:

- The class constructor has a new _unsafe_ parameter, which causes mock
objects to raise [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") on attribute names starting
with `"assert"`.
(Contributed by Kushal Das in [bpo-21238](https://bugs.python.org/issue?@action=redirect&bpo=21238).)

- A new [`Mock.assert_not_called()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_not_called "unittest.mock.Mock.assert_not_called")
method to check if the mock object was called.
(Contributed by Kushal Das in [bpo-21262](https://bugs.python.org/issue?@action=redirect&bpo=21262).)


The [`MagicMock`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.MagicMock "unittest.mock.MagicMock") class now supports
[`__truediv__()`](https://docs.python.org/3/reference/datamodel.html#object.__truediv__ "object.__truediv__"), [`__divmod__()`](https://docs.python.org/3/reference/datamodel.html#object.__divmod__ "object.__divmod__")
and [`__matmul__()`](https://docs.python.org/3/reference/datamodel.html#object.__matmul__ "object.__matmul__") operators.
(Contributed by Johannes Baiter in [bpo-20968](https://bugs.python.org/issue?@action=redirect&bpo=20968), and Håkan Lövdahl
in [bpo-23581](https://bugs.python.org/issue?@action=redirect&bpo=23581) and [bpo-23568](https://bugs.python.org/issue?@action=redirect&bpo=23568).)

It is no longer necessary to explicitly pass `create=True` to the
[`patch()`](https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch "unittest.mock.patch") function when patching builtin names.
(Contributed by Kushal Das in [bpo-17660](https://bugs.python.org/issue?@action=redirect&bpo=17660).)

### urllib [¶](https://docs.python.org/3/whatsnew/3.5.html\#urllib "Link to this heading")

A new
[`request.HTTPPasswordMgrWithPriorAuth`](https://docs.python.org/3/library/urllib.request.html#urllib.request.HTTPPasswordMgrWithPriorAuth "urllib.request.HTTPPasswordMgrWithPriorAuth")
class allows HTTP Basic Authentication credentials to be managed so as to
eliminate unnecessary `401` response handling, or to unconditionally send
credentials on the first request in order to communicate with servers that
return a `404` response instead of a `401` if the `Authorization` header
is not sent. (Contributed by Matej Cepl in [bpo-19494](https://bugs.python.org/issue?@action=redirect&bpo=19494) and Akshit Khurana in
[bpo-7159](https://bugs.python.org/issue?@action=redirect&bpo=7159).)

A new _quote\_via_ argument for the
[`parse.urlencode()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode "urllib.parse.urlencode")
function provides a way to control the encoding of query parts if needed.
(Contributed by Samwyse and Arnon Yaari in [bpo-13866](https://bugs.python.org/issue?@action=redirect&bpo=13866).)

The [`request.urlopen()`](https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen "urllib.request.urlopen") function accepts an
[`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") object as a _context_ argument, which will be used for
the HTTPS connection. (Contributed by Alex Gaynor in [bpo-22366](https://bugs.python.org/issue?@action=redirect&bpo=22366).)

The [`parse.urljoin()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urljoin "urllib.parse.urljoin") was updated to use the
[**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html) semantics for the resolution of relative URLs, rather than
[**RFC 1808**](https://datatracker.ietf.org/doc/html/rfc1808.html) and [**RFC 2396**](https://datatracker.ietf.org/doc/html/rfc2396.html).
(Contributed by Demian Brecht and Senthil Kumaran in [bpo-22118](https://bugs.python.org/issue?@action=redirect&bpo=22118).)

### wsgiref [¶](https://docs.python.org/3/whatsnew/3.5.html\#wsgiref "Link to this heading")

The _headers_ argument of the [`headers.Headers`](https://docs.python.org/3/library/wsgiref.html#wsgiref.headers.Headers "wsgiref.headers.Headers")
class constructor is now optional.
(Contributed by Pablo Torres Navarrete and SilentGhost in [bpo-5800](https://bugs.python.org/issue?@action=redirect&bpo=5800).)

### xmlrpc [¶](https://docs.python.org/3/whatsnew/3.5.html\#xmlrpc "Link to this heading")

The [`client.ServerProxy`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ServerProxy "xmlrpc.client.ServerProxy") class now supports
the [context manager](https://docs.python.org/3/glossary.html#term-context-manager) protocol.
(Contributed by Claudiu Popa in [bpo-20627](https://bugs.python.org/issue?@action=redirect&bpo=20627).)

The [`client.ServerProxy`](https://docs.python.org/3/library/xmlrpc.client.html#xmlrpc.client.ServerProxy "xmlrpc.client.ServerProxy") constructor now accepts
an optional [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") instance.
(Contributed by Alex Gaynor in [bpo-22960](https://bugs.python.org/issue?@action=redirect&bpo=22960).)

### xml.sax [¶](https://docs.python.org/3/whatsnew/3.5.html\#xml-sax "Link to this heading")

SAX parsers now support a character stream of the
[`xmlreader.InputSource`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") object.
(Contributed by Serhiy Storchaka in [bpo-2175](https://bugs.python.org/issue?@action=redirect&bpo=2175).)

[`parseString()`](https://docs.python.org/3/library/xml.sax.html#xml.sax.parseString "xml.sax.parseString") now accepts a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") instance.
(Contributed by Serhiy Storchaka in [bpo-10590](https://bugs.python.org/issue?@action=redirect&bpo=10590).)

### zipfile [¶](https://docs.python.org/3/whatsnew/3.5.html\#zipfile "Link to this heading")

ZIP output can now be written to unseekable streams.
(Contributed by Serhiy Storchaka in [bpo-23252](https://bugs.python.org/issue?@action=redirect&bpo=23252).)

The _mode_ argument of [`ZipFile.open()`](https://docs.python.org/3/library/zipfile.html#zipfile.ZipFile.open "zipfile.ZipFile.open") method now
accepts `"x"` to request exclusive creation.
(Contributed by Serhiy Storchaka in [bpo-21717](https://bugs.python.org/issue?@action=redirect&bpo=21717).)

## Other module-level changes [¶](https://docs.python.org/3/whatsnew/3.5.html\#other-module-level-changes "Link to this heading")

Many functions in the [`mmap`](https://docs.python.org/3/library/mmap.html#module-mmap "mmap: Interface to memory-mapped files for Unix and Windows."), `ossaudiodev`, [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface."),
[`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects"), and [`codecs`](https://docs.python.org/3/library/codecs.html#module-codecs "codecs: Encode and decode data and streams.") modules now accept writable
[bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object).
(Contributed by Serhiy Storchaka in [bpo-23001](https://bugs.python.org/issue?@action=redirect&bpo=23001).)

## Optimizations [¶](https://docs.python.org/3/whatsnew/3.5.html\#optimizations "Link to this heading")

The [`os.walk()`](https://docs.python.org/3/library/os.html#os.walk "os.walk") function has been sped up by 3 to 5 times on POSIX systems,
and by 7 to 20 times on Windows. This was done using the new [`os.scandir()`](https://docs.python.org/3/library/os.html#os.scandir "os.scandir")
function, which exposes file information from the underlying `readdir` or
`FindFirstFile`/`FindNextFile` system calls. (Contributed by
Ben Hoyt with help from Victor Stinner in [bpo-23605](https://bugs.python.org/issue?@action=redirect&bpo=23605).)

Construction of `bytes(int)` (filled by zero bytes) is faster and uses less
memory for large objects. `calloc()` is used instead of `malloc()` to
allocate memory for these objects.
(Contributed by Victor Stinner in [bpo-21233](https://bugs.python.org/issue?@action=redirect&bpo=21233).)

Some operations on [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.") [`IPv4Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network "ipaddress.IPv4Network") and
[`IPv6Network`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Network "ipaddress.IPv6Network") have been massively sped up, such as
[`subnets()`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.subnets "ipaddress.IPv4Network.subnets"), [`supernet()`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv4Network.supernet "ipaddress.IPv4Network.supernet"),
[`summarize_address_range()`](https://docs.python.org/3/library/ipaddress.html#ipaddress.summarize_address_range "ipaddress.summarize_address_range"), [`collapse_addresses()`](https://docs.python.org/3/library/ipaddress.html#ipaddress.collapse_addresses "ipaddress.collapse_addresses").
The speed up can range from 3 to 15 times.
(Contributed by Antoine Pitrou, Michel Albert, and Markus in
[bpo-21486](https://bugs.python.org/issue?@action=redirect&bpo=21486), [bpo-21487](https://bugs.python.org/issue?@action=redirect&bpo=21487), [bpo-20826](https://bugs.python.org/issue?@action=redirect&bpo=20826), [bpo-23266](https://bugs.python.org/issue?@action=redirect&bpo=23266).)

Pickling of [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.") objects was optimized to produce significantly
smaller output. (Contributed by Serhiy Storchaka in [bpo-23133](https://bugs.python.org/issue?@action=redirect&bpo=23133).)

Many operations on [`io.BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") are now 50% to 100% faster.
(Contributed by Serhiy Storchaka in [bpo-15381](https://bugs.python.org/issue?@action=redirect&bpo=15381) and David Wilson in
[bpo-22003](https://bugs.python.org/issue?@action=redirect&bpo=22003).)

The [`marshal.dumps()`](https://docs.python.org/3/library/marshal.html#marshal.dumps "marshal.dumps") function is now faster: 65–85% with versions 3
and 4, 20–25% with versions 0 to 2 on typical data, and up to 5 times in
best cases.
(Contributed by Serhiy Storchaka in [bpo-20416](https://bugs.python.org/issue?@action=redirect&bpo=20416) and [bpo-23344](https://bugs.python.org/issue?@action=redirect&bpo=23344).)

The UTF-32 encoder is now 3 to 7 times faster.
(Contributed by Serhiy Storchaka in [bpo-15027](https://bugs.python.org/issue?@action=redirect&bpo=15027).)

Regular expressions are now parsed up to 10% faster.
(Contributed by Serhiy Storchaka in [bpo-19380](https://bugs.python.org/issue?@action=redirect&bpo=19380).)

The [`json.dumps()`](https://docs.python.org/3/library/json.html#json.dumps "json.dumps") function was optimized to run with
`ensure_ascii=False` as fast as with `ensure_ascii=True`.
(Contributed by Naoki Inada in [bpo-23206](https://bugs.python.org/issue?@action=redirect&bpo=23206).)

The [`PyObject_IsInstance()`](https://docs.python.org/3/c-api/object.html#c.PyObject_IsInstance "PyObject_IsInstance") and [`PyObject_IsSubclass()`](https://docs.python.org/3/c-api/object.html#c.PyObject_IsSubclass "PyObject_IsSubclass")
functions have been sped up in the common case that the second argument
has [`type`](https://docs.python.org/3/library/functions.html#type "type") as its metaclass.
(Contributed Georg Brandl by in [bpo-22540](https://bugs.python.org/issue?@action=redirect&bpo=22540).)

Method caching was slightly improved, yielding up to 5% performance
improvement in some benchmarks.
(Contributed by Antoine Pitrou in [bpo-22847](https://bugs.python.org/issue?@action=redirect&bpo=22847).)

Objects from the [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") module now use 50% less memory on 64-bit
builds. (Contributed by Serhiy Storchaka in [bpo-23488](https://bugs.python.org/issue?@action=redirect&bpo=23488).)

The [`property()`](https://docs.python.org/3/library/functions.html#property "property") getter calls are up to 25% faster.
(Contributed by Joe Jevnik in [bpo-23910](https://bugs.python.org/issue?@action=redirect&bpo=23910).)

Instantiation of [`fractions.Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction") is now up to 30% faster.
(Contributed by Stefan Behnel in [bpo-22464](https://bugs.python.org/issue?@action=redirect&bpo=22464).)

String methods [`find()`](https://docs.python.org/3/library/stdtypes.html#str.find "str.find"), [`rfind()`](https://docs.python.org/3/library/stdtypes.html#str.rfind "str.rfind"), [`split()`](https://docs.python.org/3/library/stdtypes.html#str.split "str.split"),
[`partition()`](https://docs.python.org/3/library/stdtypes.html#str.partition "str.partition") and the [`in`](https://docs.python.org/3/reference/expressions.html#in) string operator are now significantly
faster for searching 1-character substrings.
(Contributed by Serhiy Storchaka in [bpo-23573](https://bugs.python.org/issue?@action=redirect&bpo=23573).)

## Build and C API Changes [¶](https://docs.python.org/3/whatsnew/3.5.html\#build-and-c-api-changes "Link to this heading")

New `calloc` functions were added:

- [`PyMem_RawCalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawCalloc "PyMem_RawCalloc"),

- [`PyMem_Calloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Calloc "PyMem_Calloc"),

- [`PyObject_Calloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Calloc "PyObject_Calloc").


(Contributed by Victor Stinner in [bpo-21233](https://bugs.python.org/issue?@action=redirect&bpo=21233).)

New encoding/decoding helper functions:

- [`Py_DecodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_DecodeLocale "Py_DecodeLocale") (replaced `_Py_char2wchar()`),

- [`Py_EncodeLocale()`](https://docs.python.org/3/c-api/sys.html#c.Py_EncodeLocale "Py_EncodeLocale") (replaced `_Py_wchar2char()`).


(Contributed by Victor Stinner in [bpo-18395](https://bugs.python.org/issue?@action=redirect&bpo=18395).)

A new [`PyCodec_NameReplaceErrors()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_NameReplaceErrors "PyCodec_NameReplaceErrors") function to replace the unicode
encode error with `\N{...}` escapes.
(Contributed by Serhiy Storchaka in [bpo-19676](https://bugs.python.org/issue?@action=redirect&bpo=19676).)

A new [`PyErr_FormatV()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_FormatV "PyErr_FormatV") function similar to [`PyErr_Format()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Format "PyErr_Format"),
but accepts a `va_list` argument.
(Contributed by Antoine Pitrou in [bpo-18711](https://bugs.python.org/issue?@action=redirect&bpo=18711).)

A new [`PyExc_RecursionError`](https://docs.python.org/3/c-api/exceptions.html#c.PyExc_RecursionError "PyExc_RecursionError") exception.
(Contributed by Georg Brandl in [bpo-19235](https://bugs.python.org/issue?@action=redirect&bpo=19235).)

New [`PyModule_FromDefAndSpec()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromDefAndSpec "PyModule_FromDefAndSpec"), [`PyModule_FromDefAndSpec2()`](https://docs.python.org/3/c-api/module.html#c.PyModule_FromDefAndSpec2 "PyModule_FromDefAndSpec2"),
and [`PyModule_ExecDef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_ExecDef "PyModule_ExecDef") functions introduced by [**PEP 489**](https://peps.python.org/pep-0489/) –
multi-phase extension module initialization.
(Contributed by Petr Viktorin in [bpo-24268](https://bugs.python.org/issue?@action=redirect&bpo=24268).)

New [`PyNumber_MatrixMultiply()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_MatrixMultiply "PyNumber_MatrixMultiply") and
[`PyNumber_InPlaceMatrixMultiply()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceMatrixMultiply "PyNumber_InPlaceMatrixMultiply") functions to perform matrix
multiplication.
(Contributed by Benjamin Peterson in [bpo-21176](https://bugs.python.org/issue?@action=redirect&bpo=21176). See also [**PEP 465**](https://peps.python.org/pep-0465/)
for details.)

The [`PyTypeObject.tp_finalize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_finalize "PyTypeObject.tp_finalize") slot is now part of the stable ABI.

Windows builds now require Microsoft Visual C++ 14.0, which
is available as part of [Visual Studio 2015](https://visualstudio.microsoft.com/en/vs/older-downloads/#visual-studio-2015-and-other-products).

Extension modules now include a platform information tag in their filename on
some platforms (the tag is optional, and CPython will import extensions without
it, although if the tag is present and mismatched, the extension won’t be
loaded):

- On Linux, extension module filenames end with
`.cpython-<major><minor>m-<architecture>-<os>.pyd`:

  - `<major>` is the major number of the Python version;
    for Python 3.5 this is `3`.

  - `<minor>` is the minor number of the Python version;
    for Python 3.5 this is `5`.

  - `<architecture>` is the hardware architecture the extension module
    was built to run on. It’s most commonly either `i386` for 32-bit Intel
    platforms or `x86_64` for 64-bit Intel (and AMD) platforms.

  - `<os>` is always `linux-gnu`, except for extensions built to
    talk to the 32-bit ABI on 64-bit platforms, in which case it is
    `linux-gnu32` (and `<architecture>` will be `x86_64`).
- On Windows, extension module filenames end with
`<debug>.cp<major><minor>-<platform>.pyd`:

  - `<major>` is the major number of the Python version;
    for Python 3.5 this is `3`.

  - `<minor>` is the minor number of the Python version;
    for Python 3.5 this is `5`.

  - `<platform>` is the platform the extension module was built for,
    either `win32` for Win32, `win_amd64` for Win64, `win_ia64` for
    Windows Itanium 64, and `win_arm` for Windows on ARM.

  - If built in debug mode, `<debug>` will be `_d`,
    otherwise it will be blank.
- On OS X platforms, extension module filenames now end with `-darwin.so`.

- On all other platforms, extension module filenames are the same as they were
with Python 3.4.


## Deprecated [¶](https://docs.python.org/3/whatsnew/3.5.html\#deprecated "Link to this heading")

### New Keywords [¶](https://docs.python.org/3/whatsnew/3.5.html\#new-keywords "Link to this heading")

`async` and `await` are not recommended to be used as variable, class,
function or module names. Introduced by [**PEP 492**](https://peps.python.org/pep-0492/) in Python 3.5, they will
become proper keywords in Python 3.7.

### Deprecated Python Behavior [¶](https://docs.python.org/3/whatsnew/3.5.html\#deprecated-python-behavior "Link to this heading")

Raising the [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration") exception inside a generator will now generate a silent
[`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning"), which will become a non-silent deprecation
warning in Python 3.6 and will trigger a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") in Python 3.7.
See [PEP 479: Change StopIteration handling inside generators](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-479)
for details.

### Unsupported Operating Systems [¶](https://docs.python.org/3/whatsnew/3.5.html\#unsupported-operating-systems "Link to this heading")

Windows XP is no longer supported by Microsoft, thus, per [**PEP 11**](https://peps.python.org/pep-0011/), CPython
3.5 is no longer officially supported on this OS.

### Deprecated Python modules, functions and methods [¶](https://docs.python.org/3/whatsnew/3.5.html\#deprecated-python-modules-functions-and-methods "Link to this heading")

The `formatter` module has now graduated to full deprecation and is still
slated for removal in Python 3.6.

The `asyncio.async()` function is deprecated in favor of
[`ensure_future()`](https://docs.python.org/3/library/asyncio-future.html#asyncio.ensure_future "asyncio.ensure_future").

The `smtpd` module has in the past always decoded the DATA portion of
email messages using the `utf-8` codec. This can now be controlled by the
new _decode\_data_ keyword to `SMTPServer`. The default value is
`True`, but this default is deprecated. Specify the _decode\_data_ keyword
with an appropriate value to avoid the deprecation warning.

Directly assigning values to the [`key`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.key "http.cookies.Morsel.key"),
[`value`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.value "http.cookies.Morsel.value") and
[`coded_value`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.coded_value "http.cookies.Morsel.coded_value") of [`http.cookies.Morsel`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "http.cookies.Morsel")
objects is deprecated. Use the [`set()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.set "http.cookies.Morsel.set") method
instead. In addition, the undocumented _LegalChars_ parameter of
[`set()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.set "http.cookies.Morsel.set") is deprecated, and is now ignored.

Passing a format string as keyword argument _format\_string_ to the
[`format()`](https://docs.python.org/3/library/string.html#string.Formatter.format "string.Formatter.format") method of the [`string.Formatter`](https://docs.python.org/3/library/string.html#string.Formatter "string.Formatter")
class has been deprecated.
(Contributed by Serhiy Storchaka in [bpo-23671](https://bugs.python.org/issue?@action=redirect&bpo=23671).)

The `platform.dist()` and `platform.linux_distribution()` functions
are now deprecated. Linux distributions use too many different ways of
describing themselves, so the functionality is left to a package.
(Contributed by Vajrasky Kok and Berker Peksag in [bpo-1322](https://bugs.python.org/issue?@action=redirect&bpo=1322).)

The previously undocumented `from_function` and `from_builtin` methods of
[`inspect.Signature`](https://docs.python.org/3/library/inspect.html#inspect.Signature "inspect.Signature") are deprecated. Use the new
[`Signature.from_callable()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.from_callable "inspect.Signature.from_callable")
method instead. (Contributed by Yury Selivanov in [bpo-24248](https://bugs.python.org/issue?@action=redirect&bpo=24248).)

The `inspect.getargspec()` function is deprecated and scheduled to be
removed in Python 3.6. (See [bpo-20438](https://bugs.python.org/issue?@action=redirect&bpo=20438) for details.)

The [`inspect`](https://docs.python.org/3/library/inspect.html#module-inspect "inspect: Extract information and source code from live objects.") [`getfullargspec()`](https://docs.python.org/3/library/inspect.html#inspect.getfullargspec "inspect.getfullargspec"),
[`getcallargs()`](https://docs.python.org/3/library/inspect.html#inspect.getcallargs "inspect.getcallargs"), and `formatargspec()` functions are
deprecated in favor of the [`inspect.signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature") API. (Contributed by Yury
Selivanov in [bpo-20438](https://bugs.python.org/issue?@action=redirect&bpo=20438).)

[`getargvalues()`](https://docs.python.org/3/library/inspect.html#inspect.getargvalues "inspect.getargvalues") and [`formatargvalues()`](https://docs.python.org/3/library/inspect.html#inspect.formatargvalues "inspect.formatargvalues") functions
were inadvertently marked as deprecated with the release of Python 3.5.0.

Use of [`re.LOCALE`](https://docs.python.org/3/library/re.html#re.LOCALE "re.LOCALE") flag with str patterns or [`re.ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") is now
deprecated. (Contributed by Serhiy Storchaka in [bpo-22407](https://bugs.python.org/issue?@action=redirect&bpo=22407).)

Use of unrecognized special sequences consisting of `'\'` and an ASCII letter
in regular expression patterns and replacement patterns now raises a
deprecation warning and will be forbidden in Python 3.6.
(Contributed by Serhiy Storchaka in [bpo-23622](https://bugs.python.org/issue?@action=redirect&bpo=23622).)

The undocumented and unofficial _use\_load\_tests_ default argument of the
[`unittest.TestLoader.loadTestsFromModule()`](https://docs.python.org/3/library/unittest.html#unittest.TestLoader.loadTestsFromModule "unittest.TestLoader.loadTestsFromModule") method now is
deprecated and ignored.
(Contributed by Robert Collins and Barry A. Warsaw in [bpo-16662](https://bugs.python.org/issue?@action=redirect&bpo=16662).)

## Removed [¶](https://docs.python.org/3/whatsnew/3.5.html\#removed "Link to this heading")

### API and Feature Removals [¶](https://docs.python.org/3/whatsnew/3.5.html\#api-and-feature-removals "Link to this heading")

The following obsolete and previously deprecated APIs and features have been
removed:

- The `__version__` attribute has been dropped from the email package. The
email code hasn’t been shipped separately from the stdlib for a long time,
and the `__version__` string was not updated in the last few releases.

- The internal `Netrc` class in the [`ftplib`](https://docs.python.org/3/library/ftplib.html#module-ftplib "ftplib: FTP protocol client (requires sockets).") module was deprecated in
3.4, and has now been removed.
(Contributed by Matt Chaput in [bpo-6623](https://bugs.python.org/issue?@action=redirect&bpo=6623).)

- The concept of `.pyo` files has been removed.

- The JoinableQueue class in the provisional [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") module was
deprecated in 3.4.4 and is now removed.
(Contributed by A. Jesse Jiryu Davis in [bpo-23464](https://bugs.python.org/issue?@action=redirect&bpo=23464).)


## Porting to Python 3.5 [¶](https://docs.python.org/3/whatsnew/3.5.html\#porting-to-python-3-5 "Link to this heading")

This section lists previously described changes and other bugfixes
that may require changes to your code.

### Changes in Python behavior [¶](https://docs.python.org/3/whatsnew/3.5.html\#changes-in-python-behavior "Link to this heading")

- Due to an oversight, earlier Python versions erroneously accepted the
following syntax:



Copy

```
f(1 for x in [1], *args)
f(1 for x in [1], **kwargs)
```





Python 3.5 now correctly raises a [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError"), as generator
expressions must be put in parentheses if not a sole argument to a function.


### Changes in the Python API [¶](https://docs.python.org/3/whatsnew/3.5.html\#changes-in-the-python-api "Link to this heading")

- [**PEP 475**](https://peps.python.org/pep-0475/): System calls are now retried when interrupted by a signal instead
of raising [`InterruptedError`](https://docs.python.org/3/library/exceptions.html#InterruptedError "InterruptedError") if the Python signal handler does not
raise an exception.

- Before Python 3.5, a [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object was considered to be false
if it represented midnight in UTC. This behavior was considered obscure and
error-prone and has been removed in Python 3.5. See [bpo-13936](https://bugs.python.org/issue?@action=redirect&bpo=13936) for full
details.

- The `ssl.SSLSocket.send()` method now raises either
[`ssl.SSLWantReadError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantReadError "ssl.SSLWantReadError") or [`ssl.SSLWantWriteError`](https://docs.python.org/3/library/ssl.html#ssl.SSLWantWriteError "ssl.SSLWantWriteError")
on a non-blocking socket if the operation would block. Previously,
it would return `0`. (Contributed by Nikolaus Rath in [bpo-20951](https://bugs.python.org/issue?@action=redirect&bpo=20951).)

- The `__name__` attribute of generators is now set from the function name,
instead of being set from the code name. Use `gen.gi_code.co_name` to
retrieve the code name. Generators also have a new `__qualname__`
attribute, the qualified name, which is now used for the representation
of a generator (`repr(gen)`).
(Contributed by Victor Stinner in [bpo-21205](https://bugs.python.org/issue?@action=redirect&bpo=21205).)

- The deprecated “strict” mode and argument of [`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser"),
`HTMLParser.error()`, and the `HTMLParserError` exception have been
removed. (Contributed by Ezio Melotti in [bpo-15114](https://bugs.python.org/issue?@action=redirect&bpo=15114).)
The _convert\_charrefs_ argument of [`HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser") is
now `True` by default. (Contributed by Berker Peksag in [bpo-21047](https://bugs.python.org/issue?@action=redirect&bpo=21047).)

- Although it is not formally part of the API, it is worth noting for porting
purposes (ie: fixing tests) that error messages that were previously of the
form “‘sometype’ does not support the buffer protocol” are now of the form “a
[bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) is required, not ‘sometype’”.
(Contributed by Ezio Melotti in [bpo-16518](https://bugs.python.org/issue?@action=redirect&bpo=16518).)

- If the current directory is set to a directory that no longer exists then
[`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") will no longer be raised and instead
[`find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder.find_spec "importlib.machinery.FileFinder.find_spec") will return `None` **without** caching `None` in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache"), which is
different than the typical case ( [bpo-22834](https://bugs.python.org/issue?@action=redirect&bpo=22834)).

- HTTP status code and messages from [`http.client`](https://docs.python.org/3/library/http.client.html#module-http.client "http.client: HTTP and HTTPS protocol client (requires sockets).") and [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.")
were refactored into a common [`HTTPStatus`](https://docs.python.org/3/library/http.html#http.HTTPStatus "http.HTTPStatus") enum. The values in
[`http.client`](https://docs.python.org/3/library/http.client.html#module-http.client "http.client: HTTP and HTTPS protocol client (requires sockets).") and [`http.server`](https://docs.python.org/3/library/http.server.html#module-http.server "http.server: HTTP server and request handlers.") remain available for backwards
compatibility. (Contributed by Demian Brecht in [bpo-21793](https://bugs.python.org/issue?@action=redirect&bpo=21793).)

- When an import loader defines [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module")
it is now expected to also define
[`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module") (raises a
[`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") now, will be an error in Python 3.6). If the loader
inherits from [`importlib.abc.Loader`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader "importlib.abc.Loader") then there is nothing to do, else
simply define [`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module") to return
`None`. (Contributed by Brett Cannon in [bpo-23014](https://bugs.python.org/issue?@action=redirect&bpo=23014).)

- The [`re.split()`](https://docs.python.org/3/library/re.html#re.split "re.split") function always ignored empty pattern matches, so the
`"x*"` pattern worked the same as `"x+"`, and the `"\b"` pattern never
worked. Now [`re.split()`](https://docs.python.org/3/library/re.html#re.split "re.split") raises a warning if the pattern could match
an empty string. For compatibility, use patterns that never match an empty
string (e.g. `"x+"` instead of `"x*"`). Patterns that could only match
an empty string (such as `"\b"`) now raise an error.
(Contributed by Serhiy Storchaka in [bpo-22818](https://bugs.python.org/issue?@action=redirect&bpo=22818).)

- The [`http.cookies.Morsel`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "http.cookies.Morsel") dict-like interface has been made self
consistent: morsel comparison now takes the [`key`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.key "http.cookies.Morsel.key")
and [`value`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.value "http.cookies.Morsel.value") into account,
[`copy()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.copy "http.cookies.Morsel.copy") now results in a
[`Morsel`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel "http.cookies.Morsel") instance rather than a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), and
[`update()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.update "http.cookies.Morsel.update") will now raise an exception if any of the
keys in the update dictionary are invalid. In addition, the undocumented
_LegalChars_ parameter of [`set()`](https://docs.python.org/3/library/http.cookies.html#http.cookies.Morsel.set "http.cookies.Morsel.set") is deprecated and
is now ignored. (Contributed by Demian Brecht in [bpo-2211](https://bugs.python.org/issue?@action=redirect&bpo=2211).)

- [**PEP 488**](https://peps.python.org/pep-0488/) has removed `.pyo` files from Python and introduced the optional
`opt-` tag in `.pyc` file names. The
[`importlib.util.cache_from_source()`](https://docs.python.org/3/library/importlib.html#importlib.util.cache_from_source "importlib.util.cache_from_source") has gained an _optimization_
parameter to help control the `opt-` tag. Because of this, the
_debug\_override_ parameter of the function is now deprecated. `.pyo` files
are also no longer supported as a file argument to the Python interpreter and
thus serve no purpose when distributed on their own (i.e. sourceless code
distribution). Due to the fact that the magic number for bytecode has changed
in Python 3.5, all old `.pyo` files from previous versions of Python are
invalid regardless of this PEP.

- The [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") module now exports the [`CAN_RAW_FD_FRAMES`](https://docs.python.org/3/library/socket.html#socket.CAN_RAW_FD_FRAMES "socket.CAN_RAW_FD_FRAMES")
constant on linux 3.6 and greater.

- The [`ssl.cert_time_to_seconds()`](https://docs.python.org/3/library/ssl.html#ssl.cert_time_to_seconds "ssl.cert_time_to_seconds") function now interprets the input time
as UTC and not as local time, per [**RFC 5280**](https://datatracker.ietf.org/doc/html/rfc5280.html). Additionally, the return
value is always an [`int`](https://docs.python.org/3/library/functions.html#int "int"). (Contributed by Akira Li in [bpo-19940](https://bugs.python.org/issue?@action=redirect&bpo=19940).)

- The `pygettext.py` Tool now uses the standard +NNNN format for timezones in
the POT-Creation-Date header.

- The [`smtplib`](https://docs.python.org/3/library/smtplib.html#module-smtplib "smtplib: SMTP protocol client (requires sockets).") module now uses [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") instead of the previous
module-level `stderr` variable for debug output. If your (test)
program depends on patching the module-level variable to capture the debug
output, you will need to update it to capture sys.stderr instead.

- The [`str.startswith()`](https://docs.python.org/3/library/stdtypes.html#str.startswith "str.startswith") and [`str.endswith()`](https://docs.python.org/3/library/stdtypes.html#str.endswith "str.endswith") methods no longer return
`True` when finding the empty string and the indexes are completely out of
range. (Contributed by Serhiy Storchaka in [bpo-24284](https://bugs.python.org/issue?@action=redirect&bpo=24284).)

- The [`inspect.getdoc()`](https://docs.python.org/3/library/inspect.html#inspect.getdoc "inspect.getdoc") function now returns documentation strings
inherited from base classes. Documentation strings no longer need to be
duplicated if the inherited documentation is appropriate. To suppress an
inherited string, an empty string must be specified (or the documentation
may be filled in). This change affects the output of the [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.")
module and the [`help()`](https://docs.python.org/3/library/functions.html#help "help") function.
(Contributed by Serhiy Storchaka in [bpo-15582](https://bugs.python.org/issue?@action=redirect&bpo=15582).)

- Nested [`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") calls are now flattened. If you were
relying on the previous behavior, you can now either add an attribute to a
[`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial") object or you can create a subclass of
[`functools.partial()`](https://docs.python.org/3/library/functools.html#functools.partial "functools.partial").
(Contributed by Alexander Belopolsky in [bpo-7830](https://bugs.python.org/issue?@action=redirect&bpo=7830).)


### Changes in the C API [¶](https://docs.python.org/3/whatsnew/3.5.html\#changes-in-the-c-api "Link to this heading")

- The undocumented `format` member of the
(non-public) `PyMemoryViewObject` structure has been removed.
All extensions relying on the relevant parts in `memoryobject.h`
must be rebuilt.

- The `PyMemAllocator` structure was renamed to
[`PyMemAllocatorEx`](https://docs.python.org/3/c-api/memory.html#c.PyMemAllocatorEx "PyMemAllocatorEx") and a new `calloc` field was added.

- Removed non-documented macro `PyObject_REPR()` which leaked references.
Use format character `%R` in [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")-like functions
to format the [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") of the object.
(Contributed by Serhiy Storchaka in [bpo-22453](https://bugs.python.org/issue?@action=redirect&bpo=22453).)

- Because the lack of the [`__module__`](https://docs.python.org/3/reference/datamodel.html#type.__module__ "type.__module__") attribute breaks pickling and
introspection, a deprecation warning is now raised for builtin types without
the [`__module__`](https://docs.python.org/3/reference/datamodel.html#type.__module__ "type.__module__") attribute. This will be an [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") in
the future.
(Contributed by Serhiy Storchaka in [bpo-20204](https://bugs.python.org/issue?@action=redirect&bpo=20204).)

- As part of the [**PEP 492**](https://peps.python.org/pep-0492/) implementation, the `tp_reserved` slot of
[`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject") was replaced with a
[`tp_as_async`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_async "PyTypeObject.tp_as_async") slot. Refer to [Coroutine Objects](https://docs.python.org/3/c-api/coro.html#coro-objects) for
new types, structures and functions.


## Notable changes in Python 3.5.4 [¶](https://docs.python.org/3/whatsnew/3.5.html\#notable-changes-in-python-3-5-4 "Link to this heading")

### New `make regen-all` build target [¶](https://docs.python.org/3/whatsnew/3.5.html\#new-make-regen-all-build-target "Link to this heading")

To simplify cross-compilation, and to ensure that CPython can reliably be
compiled without requiring an existing version of Python to already be
available, the autotools-based build system no longer attempts to implicitly
recompile generated files based on file modification times.

Instead, a new `make regen-all` command has been added to force regeneration
of these files when desired (e.g. after an initial version of Python has
already been built based on the pregenerated versions).

More selective regeneration targets are also defined - see
[Makefile.pre.in](https://github.com/python/cpython/tree/3.14/Makefile.pre.in) for details.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Added in version 3.5.4.

### Removal of `make touch` build target [¶](https://docs.python.org/3/whatsnew/3.5.html\#removal-of-make-touch-build-target "Link to this heading")

The `make touch` build target previously used to request implicit regeneration
of generated files by updating their modification times has been removed.

It has been replaced by the new `make regen-all` target.

(Contributed by Victor Stinner in [bpo-23404](https://bugs.python.org/issue?@action=redirect&bpo=23404).)

Changed in version 3.5.4.

### [Table of Contents](https://docs.python.org/3/contents.html)

- [What’s New In Python 3.5](https://docs.python.org/3/whatsnew/3.5.html#)
  - [Summary – Release highlights](https://docs.python.org/3/whatsnew/3.5.html#summary-release-highlights)
  - [New Features](https://docs.python.org/3/whatsnew/3.5.html#new-features)
    - [PEP 492 - Coroutines with async and await syntax](https://docs.python.org/3/whatsnew/3.5.html#pep-492-coroutines-with-async-and-await-syntax)
    - [PEP 465 - A dedicated infix operator for matrix multiplication](https://docs.python.org/3/whatsnew/3.5.html#pep-465-a-dedicated-infix-operator-for-matrix-multiplication)
    - [PEP 448 - Additional Unpacking Generalizations](https://docs.python.org/3/whatsnew/3.5.html#pep-448-additional-unpacking-generalizations)
    - [PEP 461 - percent formatting support for bytes and bytearray](https://docs.python.org/3/whatsnew/3.5.html#pep-461-percent-formatting-support-for-bytes-and-bytearray)
    - [PEP 484 - Type Hints](https://docs.python.org/3/whatsnew/3.5.html#pep-484-type-hints)
    - [PEP 471 - os.scandir() function – a better and faster directory iterator](https://docs.python.org/3/whatsnew/3.5.html#pep-471-os-scandir-function-a-better-and-faster-directory-iterator)
    - [PEP 475: Retry system calls failing with EINTR](https://docs.python.org/3/whatsnew/3.5.html#pep-475-retry-system-calls-failing-with-eintr)
    - [PEP 479: Change StopIteration handling inside generators](https://docs.python.org/3/whatsnew/3.5.html#pep-479-change-stopiteration-handling-inside-generators)
    - [PEP 485: A function for testing approximate equality](https://docs.python.org/3/whatsnew/3.5.html#pep-485-a-function-for-testing-approximate-equality)
    - [PEP 486: Make the Python Launcher aware of virtual environments](https://docs.python.org/3/whatsnew/3.5.html#pep-486-make-the-python-launcher-aware-of-virtual-environments)
    - [PEP 488: Elimination of PYO files](https://docs.python.org/3/whatsnew/3.5.html#pep-488-elimination-of-pyo-files)
    - [PEP 489: Multi-phase extension module initialization](https://docs.python.org/3/whatsnew/3.5.html#pep-489-multi-phase-extension-module-initialization)
  - [Other Language Changes](https://docs.python.org/3/whatsnew/3.5.html#other-language-changes)
  - [New Modules](https://docs.python.org/3/whatsnew/3.5.html#new-modules)
    - [typing](https://docs.python.org/3/whatsnew/3.5.html#typing)
    - [zipapp](https://docs.python.org/3/whatsnew/3.5.html#zipapp)
  - [Improved Modules](https://docs.python.org/3/whatsnew/3.5.html#improved-modules)
    - [argparse](https://docs.python.org/3/whatsnew/3.5.html#argparse)
    - [asyncio](https://docs.python.org/3/whatsnew/3.5.html#asyncio)
    - [bz2](https://docs.python.org/3/whatsnew/3.5.html#bz2)
    - [cgi](https://docs.python.org/3/whatsnew/3.5.html#cgi)
    - [cmath](https://docs.python.org/3/whatsnew/3.5.html#cmath)
    - [code](https://docs.python.org/3/whatsnew/3.5.html#code)
    - [collections](https://docs.python.org/3/whatsnew/3.5.html#collections)
    - [collections.abc](https://docs.python.org/3/whatsnew/3.5.html#collections-abc)
    - [compileall](https://docs.python.org/3/whatsnew/3.5.html#compileall)
    - [concurrent.futures](https://docs.python.org/3/whatsnew/3.5.html#concurrent-futures)
    - [configparser](https://docs.python.org/3/whatsnew/3.5.html#configparser)
    - [contextlib](https://docs.python.org/3/whatsnew/3.5.html#contextlib)
    - [csv](https://docs.python.org/3/whatsnew/3.5.html#csv)
    - [curses](https://docs.python.org/3/whatsnew/3.5.html#curses)
    - [dbm](https://docs.python.org/3/whatsnew/3.5.html#dbm)
    - [difflib](https://docs.python.org/3/whatsnew/3.5.html#difflib)
    - [distutils](https://docs.python.org/3/whatsnew/3.5.html#distutils)
    - [doctest](https://docs.python.org/3/whatsnew/3.5.html#doctest)
    - [email](https://docs.python.org/3/whatsnew/3.5.html#email)
    - [enum](https://docs.python.org/3/whatsnew/3.5.html#enum)
    - [faulthandler](https://docs.python.org/3/whatsnew/3.5.html#faulthandler)
    - [functools](https://docs.python.org/3/whatsnew/3.5.html#functools)
    - [glob](https://docs.python.org/3/whatsnew/3.5.html#glob)
    - [gzip](https://docs.python.org/3/whatsnew/3.5.html#gzip)
    - [heapq](https://docs.python.org/3/whatsnew/3.5.html#heapq)
    - [http](https://docs.python.org/3/whatsnew/3.5.html#http)
    - [http.client](https://docs.python.org/3/whatsnew/3.5.html#http-client)
    - [idlelib and IDLE](https://docs.python.org/3/whatsnew/3.5.html#idlelib-and-idle)
    - [imaplib](https://docs.python.org/3/whatsnew/3.5.html#imaplib)
    - [imghdr](https://docs.python.org/3/whatsnew/3.5.html#imghdr)
    - [importlib](https://docs.python.org/3/whatsnew/3.5.html#importlib)
    - [inspect](https://docs.python.org/3/whatsnew/3.5.html#inspect)
    - [io](https://docs.python.org/3/whatsnew/3.5.html#io)
    - [ipaddress](https://docs.python.org/3/whatsnew/3.5.html#ipaddress)
    - [json](https://docs.python.org/3/whatsnew/3.5.html#json)
    - [linecache](https://docs.python.org/3/whatsnew/3.5.html#linecache)
    - [locale](https://docs.python.org/3/whatsnew/3.5.html#locale)
    - [logging](https://docs.python.org/3/whatsnew/3.5.html#logging)
    - [lzma](https://docs.python.org/3/whatsnew/3.5.html#lzma)
    - [math](https://docs.python.org/3/whatsnew/3.5.html#math)
    - [multiprocessing](https://docs.python.org/3/whatsnew/3.5.html#multiprocessing)
    - [operator](https://docs.python.org/3/whatsnew/3.5.html#operator)
    - [os](https://docs.python.org/3/whatsnew/3.5.html#os)
    - [pathlib](https://docs.python.org/3/whatsnew/3.5.html#pathlib)
    - [pickle](https://docs.python.org/3/whatsnew/3.5.html#pickle)
    - [poplib](https://docs.python.org/3/whatsnew/3.5.html#poplib)
    - [re](https://docs.python.org/3/whatsnew/3.5.html#re)
    - [readline](https://docs.python.org/3/whatsnew/3.5.html#readline)
    - [selectors](https://docs.python.org/3/whatsnew/3.5.html#selectors)
    - [shutil](https://docs.python.org/3/whatsnew/3.5.html#shutil)
    - [signal](https://docs.python.org/3/whatsnew/3.5.html#signal)
    - [smtpd](https://docs.python.org/3/whatsnew/3.5.html#smtpd)
    - [smtplib](https://docs.python.org/3/whatsnew/3.5.html#smtplib)
    - [sndhdr](https://docs.python.org/3/whatsnew/3.5.html#sndhdr)
    - [socket](https://docs.python.org/3/whatsnew/3.5.html#socket)
    - [ssl](https://docs.python.org/3/whatsnew/3.5.html#ssl)
      - [Memory BIO Support](https://docs.python.org/3/whatsnew/3.5.html#memory-bio-support)
      - [Application-Layer Protocol Negotiation Support](https://docs.python.org/3/whatsnew/3.5.html#application-layer-protocol-negotiation-support)
      - [Other Changes](https://docs.python.org/3/whatsnew/3.5.html#other-changes)
    - [sqlite3](https://docs.python.org/3/whatsnew/3.5.html#sqlite3)
    - [subprocess](https://docs.python.org/3/whatsnew/3.5.html#subprocess)
    - [sys](https://docs.python.org/3/whatsnew/3.5.html#sys)
    - [sysconfig](https://docs.python.org/3/whatsnew/3.5.html#sysconfig)
    - [tarfile](https://docs.python.org/3/whatsnew/3.5.html#tarfile)
    - [threading](https://docs.python.org/3/whatsnew/3.5.html#threading)
    - [time](https://docs.python.org/3/whatsnew/3.5.html#time)
    - [timeit](https://docs.python.org/3/whatsnew/3.5.html#timeit)
    - [tkinter](https://docs.python.org/3/whatsnew/3.5.html#tkinter)
    - [traceback](https://docs.python.org/3/whatsnew/3.5.html#traceback)
    - [types](https://docs.python.org/3/whatsnew/3.5.html#types)
    - [unicodedata](https://docs.python.org/3/whatsnew/3.5.html#unicodedata)
    - [unittest](https://docs.python.org/3/whatsnew/3.5.html#unittest)
    - [unittest.mock](https://docs.python.org/3/whatsnew/3.5.html#unittest-mock)
    - [urllib](https://docs.python.org/3/whatsnew/3.5.html#urllib)
    - [wsgiref](https://docs.python.org/3/whatsnew/3.5.html#wsgiref)
    - [xmlrpc](https://docs.python.org/3/whatsnew/3.5.html#xmlrpc)
    - [xml.sax](https://docs.python.org/3/whatsnew/3.5.html#xml-sax)
    - [zipfile](https://docs.python.org/3/whatsnew/3.5.html#zipfile)
  - [Other module-level changes](https://docs.python.org/3/whatsnew/3.5.html#other-module-level-changes)
  - [Optimizations](https://docs.python.org/3/whatsnew/3.5.html#optimizations)
  - [Build and C API Changes](https://docs.python.org/3/whatsnew/3.5.html#build-and-c-api-changes)
  - [Deprecated](https://docs.python.org/3/whatsnew/3.5.html#deprecated)
    - [New Keywords](https://docs.python.org/3/whatsnew/3.5.html#new-keywords)
    - [Deprecated Python Behavior](https://docs.python.org/3/whatsnew/3.5.html#deprecated-python-behavior)
    - [Unsupported Operating Systems](https://docs.python.org/3/whatsnew/3.5.html#unsupported-operating-systems)
    - [Deprecated Python modules, functions and methods](https://docs.python.org/3/whatsnew/3.5.html#deprecated-python-modules-functions-and-methods)
  - [Removed](https://docs.python.org/3/whatsnew/3.5.html#removed)
    - [API and Feature Removals](https://docs.python.org/3/whatsnew/3.5.html#api-and-feature-removals)
  - [Porting to Python 3.5](https://docs.python.org/3/whatsnew/3.5.html#porting-to-python-3-5)
    - [Changes in Python behavior](https://docs.python.org/3/whatsnew/3.5.html#changes-in-python-behavior)
    - [Changes in the Python API](https://docs.python.org/3/whatsnew/3.5.html#changes-in-the-python-api)
    - [Changes in the C API](https://docs.python.org/3/whatsnew/3.5.html#changes-in-the-c-api)
  - [Notable changes in Python 3.5.4](https://docs.python.org/3/whatsnew/3.5.html#notable-changes-in-python-3-5-4)
    - [New `make regen-all` build target](https://docs.python.org/3/whatsnew/3.5.html#new-make-regen-all-build-target)
    - [Removal of `make touch` build target](https://docs.python.org/3/whatsnew/3.5.html#removal-of-make-touch-build-target)

#### Previous topic

[What’s New In Python 3.6](https://docs.python.org/3/whatsnew/3.6.html "previous chapter")

#### Next topic

[What’s New In Python 3.4](https://docs.python.org/3/whatsnew/3.4.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/whatsnew/3.5.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/whatsnew/3.4.html "What’s New In Python 3.4") \|
- [previous](https://docs.python.org/3/whatsnew/3.6.html "What’s New In Python 3.6") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [What’s New in Python](https://docs.python.org/3/whatsnew/index.html) »
- [What’s New In Python 3.5](https://docs.python.org/3/whatsnew/3.5.html)
- \|

- Theme
AutoLightDark \|