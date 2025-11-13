### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/doctest.html "doctest — Test interactive Python examples") \|
- [previous](https://docs.python.org/3/library/pydoc.html "pydoc — Documentation generator and online help system") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Development Tools](https://docs.python.org/3/library/development.html) »
- [Python Development Mode](https://docs.python.org/3/library/devmode.html)
- \|

- Theme
AutoLightDark \|

# Python Development Mode [¶](https://docs.python.org/3/library/devmode.html\#python-development-mode "Link to this heading")

Added in version 3.7.

The Python Development Mode introduces additional runtime checks that are too
expensive to be enabled by default. It should not be more verbose than the
default if the code is correct; new warnings are only emitted when an issue is
detected.

It can be enabled using the [`-X dev`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) command line option or by
setting the [`PYTHONDEVMODE`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONDEVMODE) environment variable to `1`.

See also [Python debug build](https://docs.python.org/3/using/configure.html#debug-build).

## Effects of the Python Development Mode [¶](https://docs.python.org/3/library/devmode.html\#effects-of-the-python-development-mode "Link to this heading")

Enabling the Python Development Mode is similar to the following command, but
with additional effects described below:

Copy

```
PYTHONMALLOC=debug PYTHONASYNCIODEBUG=1 python -W default -X faulthandler
```

Effects of the Python Development Mode:

- Add `default` [warning filter](https://docs.python.org/3/library/warnings.html#describing-warning-filters). The
following warnings are shown:


  - [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning")

  - [`ImportWarning`](https://docs.python.org/3/library/exceptions.html#ImportWarning "ImportWarning")

  - [`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning")

  - [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning")


Normally, the above warnings are filtered by the default [warning\\
filters](https://docs.python.org/3/library/warnings.html#describing-warning-filters).

It behaves as if the [`-W default`](https://docs.python.org/3/using/cmdline.html#cmdoption-W) command line option is used.

Use the [`-W error`](https://docs.python.org/3/using/cmdline.html#cmdoption-W) command line option or set the
[`PYTHONWARNINGS`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNINGS) environment variable to `error` to treat warnings
as errors.

- Install debug hooks on memory allocators to check for:


  - Buffer underflow

  - Buffer overflow

  - Memory allocator API violation

  - Unsafe usage of the GIL


See the [`PyMem_SetupDebugHooks()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_SetupDebugHooks "PyMem_SetupDebugHooks") C function.

It behaves as if the [`PYTHONMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOC) environment variable is set to
`debug`.

To enable the Python Development Mode without installing debug hooks on
memory allocators, set the [`PYTHONMALLOC`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONMALLOC) environment variable to
`default`.

- Call [`faulthandler.enable()`](https://docs.python.org/3/library/faulthandler.html#faulthandler.enable "faulthandler.enable") at Python startup to install handlers for
the [`SIGSEGV`](https://docs.python.org/3/library/signal.html#signal.SIGSEGV "signal.SIGSEGV"), [`SIGFPE`](https://docs.python.org/3/library/signal.html#signal.SIGFPE "signal.SIGFPE"),
[`SIGABRT`](https://docs.python.org/3/library/signal.html#signal.SIGABRT "signal.SIGABRT"), [`SIGBUS`](https://docs.python.org/3/library/signal.html#signal.SIGBUS "signal.SIGBUS") and
[`SIGILL`](https://docs.python.org/3/library/signal.html#signal.SIGILL "signal.SIGILL") signals to dump the Python traceback on a crash.

It behaves as if the [`-X faulthandler`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) command line option is
used or if the [`PYTHONFAULTHANDLER`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONFAULTHANDLER) environment variable is set to
`1`.

- Enable [asyncio debug mode](https://docs.python.org/3/library/asyncio-dev.html#asyncio-debug-mode). For example,
[`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") checks for coroutines that were not awaited and logs them.

It behaves as if the [`PYTHONASYNCIODEBUG`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONASYNCIODEBUG) environment variable is set
to `1`.

- Check the _encoding_ and _errors_ arguments for string encoding and decoding
operations. Examples: [`open()`](https://docs.python.org/3/library/functions.html#open "open"), [`str.encode()`](https://docs.python.org/3/library/stdtypes.html#str.encode "str.encode") and
[`bytes.decode()`](https://docs.python.org/3/library/stdtypes.html#bytes.decode "bytes.decode").

By default, for best performance, the _errors_ argument is only checked at
the first encoding/decoding error and the _encoding_ argument is sometimes
ignored for empty strings.

- The [`io.IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") destructor logs `close()` exceptions.

- Set the [`dev_mode`](https://docs.python.org/3/library/sys.html#sys.flags.dev_mode "sys.flags.dev_mode") attribute of [`sys.flags`](https://docs.python.org/3/library/sys.html#sys.flags "sys.flags") to
`True`.


The Python Development Mode does not enable the [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.") module by
default, because the overhead cost (to performance and memory) would be too
large. Enabling the [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.") module provides additional information
on the origin of some errors. For example, [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning") logs the
traceback where the resource was allocated, and a buffer overflow error logs
the traceback where the memory block was allocated.

The Python Development Mode does not prevent the [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O) command line
option from removing [`assert`](https://docs.python.org/3/reference/simple_stmts.html#assert) statements nor from setting
[`__debug__`](https://docs.python.org/3/library/constants.html#debug__ "__debug__") to `False`.

The Python Development Mode can only be enabled at the Python startup. Its
value can be read from [`sys.flags.dev_mode`](https://docs.python.org/3/library/sys.html#sys.flags "sys.flags").

Changed in version 3.8: The [`io.IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") destructor now logs `close()` exceptions.

Changed in version 3.9: The _encoding_ and _errors_ arguments are now checked for string encoding
and decoding operations.

## ResourceWarning Example [¶](https://docs.python.org/3/library/devmode.html\#resourcewarning-example "Link to this heading")

Example of a script counting the number of lines of the text file specified in
the command line:

Copy

```
import sys

def main():
    fp = open(sys.argv[1])
    nlines = len(fp.readlines())
    print(nlines)
    # The file is closed implicitly

if __name__ == "__main__":
    main()
```

The script does not close the file explicitly. By default, Python does not emit
any warning. Example using README.txt, which has 269 lines:

```
$ python script.py README.txt
269
```

Enabling the Python Development Mode displays a [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning") warning:

```
$ python -X dev script.py README.txt
269
script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='README.rst' mode='r' encoding='UTF-8'>
  main()
ResourceWarning: Enable tracemalloc to get the object allocation traceback
```

In addition, enabling [`tracemalloc`](https://docs.python.org/3/library/tracemalloc.html#module-tracemalloc "tracemalloc: Trace memory allocations.") shows the line where the file was
opened:

```
$ python -X dev -X tracemalloc=5 script.py README.rst
269
script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='README.rst' mode='r' encoding='UTF-8'>
  main()
Object allocated at (most recent call last):
  File "script.py", lineno 10
    main()
  File "script.py", lineno 4
    fp = open(sys.argv[1])
```

The fix is to close explicitly the file. Example using a context manager:

Copy

```
def main():
    # Close the file explicitly when exiting the with block
    with open(sys.argv[1]) as fp:
        nlines = len(fp.readlines())
    print(nlines)
```

Not closing a resource explicitly can leave a resource open for way longer than
expected; it can cause severe issues upon exiting Python. It is bad in
CPython, but it is even worse in PyPy. Closing resources explicitly makes an
application more deterministic and more reliable.

## Bad file descriptor error example [¶](https://docs.python.org/3/library/devmode.html\#bad-file-descriptor-error-example "Link to this heading")

Script displaying the first line of itself:

Copy

```
import os

def main():
    fp = open(__file__)
    firstline = fp.readline()
    print(firstline.rstrip())
    os.close(fp.fileno())
    # The file is closed implicitly

main()
```

By default, Python does not emit any warning:

```
$ python script.py
import os
```

The Python Development Mode shows a [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning") and logs a “Bad file
descriptor” error when finalizing the file object:

```
$ python -X dev script.py
import os
script.py:10: ResourceWarning: unclosed file <_io.TextIOWrapper name='script.py' mode='r' encoding='UTF-8'>
  main()
ResourceWarning: Enable tracemalloc to get the object allocation traceback
Exception ignored in: <_io.TextIOWrapper name='script.py' mode='r' encoding='UTF-8'>
Traceback (most recent call last):
  File "script.py", line 10, in <module>
    main()
OSError: [Errno 9] Bad file descriptor
```

`os.close(fp.fileno())` closes the file descriptor. When the file object
finalizer tries to close the file descriptor again, it fails with the `Bad
file descriptor` error. A file descriptor must be closed only once. In the
worst case scenario, closing it twice can lead to a crash (see [bpo-18748](https://bugs.python.org/issue?@action=redirect&bpo=18748)
for an example).

The fix is to remove the `os.close(fp.fileno())` line, or open the file with
`closefd=False`.

### [Table of Contents](https://docs.python.org/3/contents.html)

- [Python Development Mode](https://docs.python.org/3/library/devmode.html#)
  - [Effects of the Python Development Mode](https://docs.python.org/3/library/devmode.html#effects-of-the-python-development-mode)
  - [ResourceWarning Example](https://docs.python.org/3/library/devmode.html#resourcewarning-example)
  - [Bad file descriptor error example](https://docs.python.org/3/library/devmode.html#bad-file-descriptor-error-example)

#### Previous topic

[`pydoc` — Documentation generator and online help system](https://docs.python.org/3/library/pydoc.html "previous chapter")

#### Next topic

[`doctest` — Test interactive Python examples](https://docs.python.org/3/library/doctest.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/devmode.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/doctest.html "doctest — Test interactive Python examples") \|
- [previous](https://docs.python.org/3/library/pydoc.html "pydoc — Documentation generator and online help system") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Development Tools](https://docs.python.org/3/library/development.html) »
- [Python Development Mode](https://docs.python.org/3/library/devmode.html)
- \|

- Theme
AutoLightDark \|