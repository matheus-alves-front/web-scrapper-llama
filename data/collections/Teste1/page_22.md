### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/faq/extending.html "Extending/Embedding FAQ") \|
- [previous](https://docs.python.org/3/faq/design.html "Design and History FAQ") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python Frequently Asked Questions](https://docs.python.org/3/faq/index.html) »
- [Library and Extension FAQ](https://docs.python.org/3/faq/library.html)
- \|

- Theme
AutoLightDark \|

# [Library and Extension FAQ](https://docs.python.org/3/faq/library.html\#id1) [¶](https://docs.python.org/3/faq/library.html\#library-and-extension-faq "Link to this heading")

## [General Library Questions](https://docs.python.org/3/faq/library.html\#id2) [¶](https://docs.python.org/3/faq/library.html\#general-library-questions "Link to this heading")

### [How do I find a module or application to perform task X?](https://docs.python.org/3/faq/library.html\#id3) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-find-a-module-or-application-to-perform-task-x "Link to this heading")

Check [the Library Reference](https://docs.python.org/3/library/index.html#library-index) to see if there’s a relevant
standard library module. (Eventually you’ll learn what’s in the standard
library and will be able to skip this step.)

For third-party packages, search the [Python Package Index](https://pypi.org/) or try [Google](https://www.google.com/) or
another web search engine. Searching for “Python” plus a keyword or two for
your topic of interest will usually find something helpful.

### [Where is the math.py (socket.py, regex.py, etc.) source file?](https://docs.python.org/3/faq/library.html\#id4) [¶](https://docs.python.org/3/faq/library.html\#where-is-the-math-py-socket-py-regex-py-etc-source-file "Link to this heading")

If you can’t find a source file for a module it may be a built-in or
dynamically loaded module implemented in C, C++ or other compiled language.
In this case you may not have the source file or it may be something like
`mathmodule.c`, somewhere in a C source directory (not on the Python Path).

There are (at least) three kinds of modules in Python:

1. modules written in Python (.py);

2. modules written in C and dynamically loaded (.dll, .pyd, .so, .sl, etc);

3. modules written in C and linked with the interpreter; to get a list of these,
type:



Copy

```
import sys
print(sys.builtin_module_names)
```


### [How do I make a Python script executable on Unix?](https://docs.python.org/3/faq/library.html\#id5) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-make-a-python-script-executable-on-unix "Link to this heading")

You need to do two things: the script file’s mode must be executable and the
first line must begin with `#!` followed by the path of the Python
interpreter.

The first is done by executing `chmod +x scriptfile` or perhaps `chmod 755
scriptfile`.

The second can be done in a number of ways. The most straightforward way is to
write

Copy

```
#!/usr/local/bin/python
```

as the very first line of your file, using the pathname for where the Python
interpreter is installed on your platform.

If you would like the script to be independent of where the Python interpreter
lives, you can use the **env** program. Almost all Unix variants support
the following, assuming the Python interpreter is in a directory on the user’s
`PATH`:

Copy

```
#!/usr/bin/env python
```

_Don’t_ do this for CGI scripts. The `PATH` variable for CGI scripts is
often very minimal, so you need to use the actual absolute pathname of the
interpreter.

Occasionally, a user’s environment is so full that the **/usr/bin/env**
program fails; or there’s no env program at all. In that case, you can try the
following hack (due to Alex Rezinsky):

```
#! /bin/sh
""":"
exec python $0 ${1+"$@"}
"""
```

The minor disadvantage is that this defines the script’s \_\_doc\_\_ string.
However, you can fix that by adding

Copy

```
__doc__ = """...Whatever..."""
```

### [Is there a curses/termcap package for Python?](https://docs.python.org/3/faq/library.html\#id6) [¶](https://docs.python.org/3/faq/library.html\#is-there-a-curses-termcap-package-for-python "Link to this heading")

For Unix variants: The standard Python source distribution comes with a curses
module in the [Modules](https://github.com/python/cpython/tree/3.14/Modules) subdirectory, though it’s not compiled by default.
(Note that this is not available in the Windows distribution – there is no
curses module for Windows.)

The [`curses`](https://docs.python.org/3/library/curses.html#module-curses "curses: An interface to the curses library, providing portable terminal handling. (Unix)") module supports basic curses features as well as many additional
functions from ncurses and SYSV curses such as colour, alternative character set
support, pads, and mouse support. This means the module isn’t compatible with
operating systems that only have BSD curses, but there don’t seem to be any
currently maintained OSes that fall into this category.

### [Is there an equivalent to C’s onexit() in Python?](https://docs.python.org/3/faq/library.html\#id7) [¶](https://docs.python.org/3/faq/library.html\#is-there-an-equivalent-to-c-s-onexit-in-python "Link to this heading")

The [`atexit`](https://docs.python.org/3/library/atexit.html#module-atexit "atexit: Register and execute cleanup functions.") module provides a register function that is similar to C’s
`onexit()`.

### [Why don’t my signal handlers work?](https://docs.python.org/3/faq/library.html\#id8) [¶](https://docs.python.org/3/faq/library.html\#why-don-t-my-signal-handlers-work "Link to this heading")

The most common problem is that the signal handler is declared with the wrong
argument list. It is called as

Copy

```
handler(signum, frame)
```

so it should be declared with two parameters:

Copy

```
def handler(signum, frame):
    ...
```

## [Common tasks](https://docs.python.org/3/faq/library.html\#id9) [¶](https://docs.python.org/3/faq/library.html\#common-tasks "Link to this heading")

### [How do I test a Python program or component?](https://docs.python.org/3/faq/library.html\#id10) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-test-a-python-program-or-component "Link to this heading")

Python comes with two testing frameworks. The [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") module finds
examples in the docstrings for a module and runs them, comparing the output with
the expected output given in the docstring.

The [`unittest`](https://docs.python.org/3/library/unittest.html#module-unittest "unittest: Unit testing framework for Python.") module is a fancier testing framework modelled on Java and
Smalltalk testing frameworks.

To make testing easier, you should use good modular design in your program.
Your program should have almost all functionality
encapsulated in either functions or class methods – and this sometimes has the
surprising and delightful effect of making the program run faster (because local
variable accesses are faster than global accesses). Furthermore the program
should avoid depending on mutating global variables, since this makes testing
much more difficult to do.

The “global main logic” of your program may be as simple as

Copy

```
if __name__ == "__main__":
    main_logic()
```

at the bottom of the main module of your program.

Once your program is organized as a tractable collection of function and class
behaviours, you should write test functions that exercise the behaviours. A
test suite that automates a sequence of tests can be associated with each module.
This sounds like a lot of work, but since Python is so terse and flexible it’s
surprisingly easy. You can make coding much more pleasant and fun by writing
your test functions in parallel with the “production code”, since this makes it
easy to find bugs and even design flaws earlier.

“Support modules” that are not intended to be the main module of a program may
include a self-test of the module.

Copy

```
if __name__ == "__main__":
    self_test()
```

Even programs that interact with complex external interfaces may be tested when
the external interfaces are unavailable by using “fake” interfaces implemented
in Python.

### [How do I create documentation from doc strings?](https://docs.python.org/3/faq/library.html\#id11) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-create-documentation-from-doc-strings "Link to this heading")

The [`pydoc`](https://docs.python.org/3/library/pydoc.html#module-pydoc "pydoc: Documentation generator and online help system.") module can create HTML from the doc strings in your Python
source code. An alternative for creating API documentation purely from
docstrings is [epydoc](https://epydoc.sourceforge.net/). [Sphinx](https://www.sphinx-doc.org/) can also include docstring content.

### [How do I get a single keypress at a time?](https://docs.python.org/3/faq/library.html\#id12) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-get-a-single-keypress-at-a-time "Link to this heading")

For Unix variants there are several solutions. It’s straightforward to do this
using curses, but curses is a fairly large module to learn.

## [Threads](https://docs.python.org/3/faq/library.html\#id13) [¶](https://docs.python.org/3/faq/library.html\#threads "Link to this heading")

### [How do I program using threads?](https://docs.python.org/3/faq/library.html\#id14) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-program-using-threads "Link to this heading")

Be sure to use the [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.") module and not the [`_thread`](https://docs.python.org/3/library/_thread.html#module-_thread "_thread: Low-level threading API.") module.
The [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.") module builds convenient abstractions on top of the
low-level primitives provided by the [`_thread`](https://docs.python.org/3/library/_thread.html#module-_thread "_thread: Low-level threading API.") module.

### [None of my threads seem to run: why?](https://docs.python.org/3/faq/library.html\#id15) [¶](https://docs.python.org/3/faq/library.html\#none-of-my-threads-seem-to-run-why "Link to this heading")

As soon as the main thread exits, all threads are killed. Your main thread is
running too quickly, giving the threads no time to do any work.

A simple fix is to add a sleep to the end of the program that’s long enough for
all the threads to finish:

Copy

```
import threading, time

def thread_task(name, n):
    for i in range(n):
        print(name, i)

for i in range(10):
    T = threading.Thread(target=thread_task, args=(str(i), i))
    T.start()

time.sleep(10)  # <---------------------------!
```

But now (on many platforms) the threads don’t run in parallel, but appear to run
sequentially, one at a time! The reason is that the OS thread scheduler doesn’t
start a new thread until the previous thread is blocked.

A simple fix is to add a tiny sleep to the start of the run function:

Copy

```
def thread_task(name, n):
    time.sleep(0.001)  # <--------------------!
    for i in range(n):
        print(name, i)

for i in range(10):
    T = threading.Thread(target=thread_task, args=(str(i), i))
    T.start()

time.sleep(10)
```

Instead of trying to guess a good delay value for [`time.sleep()`](https://docs.python.org/3/library/time.html#time.sleep "time.sleep"),
it’s better to use some kind of semaphore mechanism. One idea is to use the
[`queue`](https://docs.python.org/3/library/queue.html#module-queue "queue: A synchronized queue class.") module to create a queue object, let each thread append a token to
the queue when it finishes, and let the main thread read as many tokens from the
queue as there are threads.

### [How do I parcel out work among a bunch of worker threads?](https://docs.python.org/3/faq/library.html\#id16) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-parcel-out-work-among-a-bunch-of-worker-threads "Link to this heading")

The easiest way is to use the [`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures "concurrent.futures: Execute computations concurrently using threads or processes.") module,
especially the [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor") class.

Or, if you want fine control over the dispatching algorithm, you can write
your own logic manually. Use the [`queue`](https://docs.python.org/3/library/queue.html#module-queue "queue: A synchronized queue class.") module to create a queue
containing a list of jobs. The [`Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue") class maintains a
list of objects and has a `.put(obj)` method that adds items to the queue and
a `.get()` method to return them. The class will take care of the locking
necessary to ensure that each job is handed out exactly once.

Here’s a trivial example:

Copy

```
import threading, queue, time

# The worker thread gets jobs off the queue.  When the queue is empty, it
# assumes there will be no more work and exits.
# (Realistically workers will run until terminated.)
def worker():
    print('Running worker')
    time.sleep(0.1)
    while True:
        try:
            arg = q.get(block=False)
        except queue.Empty:
            print('Worker', threading.current_thread(), end=' ')
            print('queue empty')
            break
        else:
            print('Worker', threading.current_thread(), end=' ')
            print('running with argument', arg)
            time.sleep(0.5)

# Create queue
q = queue.Queue()

# Start a pool of 5 workers
for i in range(5):
    t = threading.Thread(target=worker, name='worker %i' % (i+1))
    t.start()

# Begin adding work to the queue
for i in range(50):
    q.put(i)

# Give threads time to run
print('Main thread sleeping')
time.sleep(5)
```

When run, this will produce the following output:

```
Running worker
Running worker
Running worker
Running worker
Running worker
Main thread sleeping
Worker <Thread(worker 1, started 130283832797456)> running with argument 0
Worker <Thread(worker 2, started 130283824404752)> running with argument 1
Worker <Thread(worker 3, started 130283816012048)> running with argument 2
Worker <Thread(worker 4, started 130283807619344)> running with argument 3
Worker <Thread(worker 5, started 130283799226640)> running with argument 4
Worker <Thread(worker 1, started 130283832797456)> running with argument 5
...
```

Consult the module’s documentation for more details; the [`Queue`](https://docs.python.org/3/library/queue.html#queue.Queue "queue.Queue")
class provides a featureful interface.

### [What kinds of global value mutation are thread-safe?](https://docs.python.org/3/faq/library.html\#id17) [¶](https://docs.python.org/3/faq/library.html\#what-kinds-of-global-value-mutation-are-thread-safe "Link to this heading")

A [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock) (GIL) is used internally to ensure that only one
thread runs in the Python VM at a time. In general, Python offers to switch
among threads only between bytecode instructions; how frequently it switches can
be set via [`sys.setswitchinterval()`](https://docs.python.org/3/library/sys.html#sys.setswitchinterval "sys.setswitchinterval"). Each bytecode instruction and
therefore all the C implementation code reached from each instruction is
therefore atomic from the point of view of a Python program.

In theory, this means an exact accounting requires an exact understanding of the
PVM bytecode implementation. In practice, it means that operations on shared
variables of built-in data types (ints, lists, dicts, etc) that “look atomic”
really are.

For example, the following operations are all atomic (L, L1, L2 are lists, D,
D1, D2 are dicts, x, y are objects, i, j are ints):

Copy

```
L.append(x)
L1.extend(L2)
x = L[i]
x = L.pop()
L1[i:j] = L2
L.sort()
x = y
x.field = y
D[x] = y
D1.update(D2)
D.keys()
```

These aren’t:

Copy

```
i = i+1
L.append(L[-1])
L[i] = L[j]
D[x] = D[x] + 1
```

Operations that replace other objects may invoke those other objects’
[`__del__()`](https://docs.python.org/3/reference/datamodel.html#object.__del__ "object.__del__") method when their reference count reaches zero, and that can
affect things. This is especially true for the mass updates to dictionaries and
lists. When in doubt, use a mutex!

### [Can’t we get rid of the Global Interpreter Lock?](https://docs.python.org/3/faq/library.html\#id18) [¶](https://docs.python.org/3/faq/library.html\#can-t-we-get-rid-of-the-global-interpreter-lock "Link to this heading")

The [global interpreter lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock) (GIL) is often seen as a hindrance to Python’s
deployment on high-end multiprocessor server machines, because a multi-threaded
Python program effectively only uses one CPU, due to the insistence that
(almost) all Python code can only run while the GIL is held.

With the approval of [**PEP 703**](https://peps.python.org/pep-0703/) work is now underway to remove the GIL from the
CPython implementation of Python. Initially it will be implemented as an
optional compiler flag when building the interpreter, and so separate
builds will be available with and without the GIL. Long-term, the hope is
to settle on a single build, once the performance implications of removing the
GIL are fully understood. Python 3.13 is likely to be the first release
containing this work, although it may not be completely functional in this
release.

The current work to remove the GIL is based on a
[fork of Python 3.9 with the GIL removed](https://github.com/colesbury/nogil)
by Sam Gross.
Prior to that,
in the days of Python 1.5, Greg Stein actually implemented a comprehensive
patch set (the “free threading” patches) that removed the GIL and replaced it
with fine-grained locking. Adam Olsen did a similar experiment
in his [python-safethread](https://code.google.com/archive/p/python-safethread)
project. Unfortunately, both of these earlier experiments exhibited a sharp
drop in single-thread
performance (at least 30% slower), due to the amount of fine-grained locking
necessary to compensate for the removal of the GIL. The Python 3.9 fork
is the first attempt at removing the GIL with an acceptable performance
impact.

The presence of the GIL in current Python releases
doesn’t mean that you can’t make good use of Python on multi-CPU machines!
You just have to be creative with dividing the work up between multiple
_processes_ rather than multiple _threads_. The
[`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor") class in the new
[`concurrent.futures`](https://docs.python.org/3/library/concurrent.futures.html#module-concurrent.futures "concurrent.futures: Execute computations concurrently using threads or processes.") module provides an easy way of doing so; the
[`multiprocessing`](https://docs.python.org/3/library/multiprocessing.html#module-multiprocessing "multiprocessing: Process-based parallelism.") module provides a lower-level API in case you want
more control over dispatching of tasks.

Judicious use of C extensions will also help; if you use a C extension to
perform a time-consuming task, the extension can release the GIL while the
thread of execution is in the C code and allow other threads to get some work
done. Some standard library modules such as [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") and [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.")
already do this.

An alternative approach to reducing the impact of the GIL is
to make the GIL a per-interpreter-state lock rather than truly global.
This was [first implemented in Python 3.12](https://docs.python.org/3/whatsnew/3.12.html#whatsnew312-pep684) and is
available in the C API. A Python interface to it is expected in Python 3.13.
The main limitation to it at the moment is likely to be 3rd party extension
modules, since these must be written with multiple interpreters in mind in
order to be usable, so many older extension modules will not be usable.

## [Input and Output](https://docs.python.org/3/faq/library.html\#id19) [¶](https://docs.python.org/3/faq/library.html\#input-and-output "Link to this heading")

### [How do I delete a file? (And other file questions…)](https://docs.python.org/3/faq/library.html\#id20) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-delete-a-file-and-other-file-questions "Link to this heading")

Use `os.remove(filename)` or `os.unlink(filename)`; for documentation, see
the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") module. The two functions are identical; [`unlink()`](https://docs.python.org/3/library/os.html#os.unlink "os.unlink") is simply
the name of the Unix system call for this function.

To remove a directory, use [`os.rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir "os.rmdir"); use [`os.mkdir()`](https://docs.python.org/3/library/os.html#os.mkdir "os.mkdir") to create one.
`os.makedirs(path)` will create any intermediate directories in `path` that
don’t exist. `os.removedirs(path)` will remove intermediate directories as
long as they’re empty; if you want to delete an entire directory tree and its
contents, use [`shutil.rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree").

To rename a file, use `os.rename(old_path, new_path)`.

To truncate a file, open it using `f = open(filename, "rb+")`, and use
`f.truncate(offset)`; offset defaults to the current seek position. There’s
also `os.ftruncate(fd, offset)` for files opened with [`os.open()`](https://docs.python.org/3/library/os.html#os.open "os.open"), where
_fd_ is the file descriptor (a small integer).

The [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.") module also contains a number of functions to work on files
including [`copyfile()`](https://docs.python.org/3/library/shutil.html#shutil.copyfile "shutil.copyfile"), [`copytree()`](https://docs.python.org/3/library/shutil.html#shutil.copytree "shutil.copytree"), and
[`rmtree()`](https://docs.python.org/3/library/shutil.html#shutil.rmtree "shutil.rmtree").

### [How do I copy a file?](https://docs.python.org/3/faq/library.html\#id21) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-copy-a-file "Link to this heading")

The [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.") module contains a [`copyfile()`](https://docs.python.org/3/library/shutil.html#shutil.copyfile "shutil.copyfile") function.
Note that on Windows NTFS volumes, it does not copy
[alternate data streams](https://en.wikipedia.org/wiki/NTFS#Alternate_data_stream_(ADS))
nor [resource forks](https://en.wikipedia.org/wiki/Resource_fork)
on macOS HFS+ volumes, though both are now rarely used.
It also doesn’t copy file permissions and metadata, though using
[`shutil.copy2()`](https://docs.python.org/3/library/shutil.html#shutil.copy2 "shutil.copy2") instead will preserve most (though not all) of it.

### [How do I read (or write) binary data?](https://docs.python.org/3/faq/library.html\#id22) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-read-or-write-binary-data "Link to this heading")

To read or write complex binary data formats, it’s best to use the [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data.")
module. It allows you to take a string containing binary data (usually numbers)
and convert it to Python objects; and vice versa.

For example, the following code reads two 2-byte integers and one 4-byte integer
in big-endian format from a file:

Copy

```
import struct

with open(filename, "rb") as f:
    s = f.read(8)
    x, y, z = struct.unpack(">hhl", s)
```

The ‘>’ in the format string forces big-endian data; the letter ‘h’ reads one
“short integer” (2 bytes), and ‘l’ reads one “long integer” (4 bytes) from the
string.

For data that is more regular (e.g. a homogeneous list of ints or floats),
you can also use the [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.") module.

Note

To read and write binary data, it is mandatory to open the file in
binary mode (here, passing `"rb"` to [`open()`](https://docs.python.org/3/library/functions.html#open "open")). If you use
`"r"` instead (the default), the file will be open in text mode
and `f.read()` will return [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") objects rather than
[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects.

### [I can’t seem to use os.read() on a pipe created with os.popen(); why?](https://docs.python.org/3/faq/library.html\#id23) [¶](https://docs.python.org/3/faq/library.html\#i-can-t-seem-to-use-os-read-on-a-pipe-created-with-os-popen-why "Link to this heading")

[`os.read()`](https://docs.python.org/3/library/os.html#os.read "os.read") is a low-level function which takes a file descriptor, a small
integer representing the opened file. [`os.popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen") creates a high-level
file object, the same type returned by the built-in [`open()`](https://docs.python.org/3/library/functions.html#open "open") function.
Thus, to read _n_ bytes from a pipe _p_ created with [`os.popen()`](https://docs.python.org/3/library/os.html#os.popen "os.popen"), you need to
use `p.read(n)`.

### [How do I access the serial (RS232) port?](https://docs.python.org/3/faq/library.html\#id24) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-access-the-serial-rs232-port "Link to this heading")

For Win32, OSX, Linux, BSD, Jython, IronPython:

> [pyserial](https://pypi.org/project/pyserial/)

For Unix, see a Usenet post by Mitch Chapman:

> [https://groups.google.com/groups?selm=34A04430.CF9@ohioee.com](https://groups.google.com/groups?selm=34A04430.CF9@ohioee.com)

### [Why doesn’t closing sys.stdout (stdin, stderr) really close it?](https://docs.python.org/3/faq/library.html\#id25) [¶](https://docs.python.org/3/faq/library.html\#why-doesn-t-closing-sys-stdout-stdin-stderr-really-close-it "Link to this heading")

Python [file objects](https://docs.python.org/3/glossary.html#term-file-object) are a high-level layer of
abstraction on low-level C file descriptors.

For most file objects you create in Python via the built-in [`open()`](https://docs.python.org/3/library/functions.html#open "open")
function, `f.close()` marks the Python file object as being closed from
Python’s point of view, and also arranges to close the underlying C file
descriptor. This also happens automatically in `f`’s destructor, when
`f` becomes garbage.

But stdin, stdout and stderr are treated specially by Python, because of the
special status also given to them by C. Running `sys.stdout.close()` marks
the Python-level file object as being closed, but does _not_ close the
associated C file descriptor.

To close the underlying C file descriptor for one of these three, you should
first be sure that’s what you really want to do (e.g., you may confuse
extension modules trying to do I/O). If it is, use [`os.close()`](https://docs.python.org/3/library/os.html#os.close "os.close"):

Copy

```
os.close(stdin.fileno())
os.close(stdout.fileno())
os.close(stderr.fileno())
```

Or you can use the numeric constants 0, 1 and 2, respectively.

## [Network/Internet Programming](https://docs.python.org/3/faq/library.html\#id26) [¶](https://docs.python.org/3/faq/library.html\#network-internet-programming "Link to this heading")

### [What WWW tools are there for Python?](https://docs.python.org/3/faq/library.html\#id27) [¶](https://docs.python.org/3/faq/library.html\#what-www-tools-are-there-for-python "Link to this heading")

See the chapters titled [Internet Protocols and Support](https://docs.python.org/3/library/internet.html#internet) and [Internet Data Handling](https://docs.python.org/3/library/netdata.html#netdata) in the Library
Reference Manual. Python has many modules that will help you build server-side
and client-side web systems.

A summary of available frameworks is maintained by Paul Boddie at
[https://wiki.python.org/moin/WebProgramming](https://wiki.python.org/moin/WebProgramming).

### [What module should I use to help with generating HTML?](https://docs.python.org/3/faq/library.html\#id28) [¶](https://docs.python.org/3/faq/library.html\#what-module-should-i-use-to-help-with-generating-html "Link to this heading")

You can find a collection of useful links on the [Web Programming wiki page](https://wiki.python.org/moin/WebProgramming).

### [How do I send mail from a Python script?](https://docs.python.org/3/faq/library.html\#id29) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-send-mail-from-a-python-script "Link to this heading")

Use the standard library module [`smtplib`](https://docs.python.org/3/library/smtplib.html#module-smtplib "smtplib: SMTP protocol client (requires sockets).").

Here’s a very simple interactive mail sender that uses it. This method will
work on any host that supports an SMTP listener.

Copy

```
import sys, smtplib

fromaddr = input("From: ")
toaddrs  = input("To: ").split(',')
print("Enter message, end with ^D:")
msg = ''
while True:
    line = sys.stdin.readline()
    if not line:
        break
    msg += line

# The actual mail send
server = smtplib.SMTP('localhost')
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
```

A Unix-only alternative uses sendmail. The location of the sendmail program
varies between systems; sometimes it is `/usr/lib/sendmail`, sometimes
`/usr/sbin/sendmail`. The sendmail manual page will help you out. Here’s
some sample code:

Copy

```
import os

SENDMAIL = "/usr/sbin/sendmail"  # sendmail location
p = os.popen("%s -t -i" % SENDMAIL, "w")
p.write("To: receiver@example.com\n")
p.write("Subject: test\n")
p.write("\n")  # blank line separating headers from body
p.write("Some text\n")
p.write("some more text\n")
sts = p.close()
if sts != 0:
    print("Sendmail exit status", sts)
```

### [How do I avoid blocking in the connect() method of a socket?](https://docs.python.org/3/faq/library.html\#id30) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-avoid-blocking-in-the-connect-method-of-a-socket "Link to this heading")

The [`select`](https://docs.python.org/3/library/select.html#module-select "select: Wait for I/O completion on multiple streams.") module is commonly used to help with asynchronous I/O on
sockets.

To prevent the TCP connect from blocking, you can set the socket to non-blocking
mode. Then when you do the [`connect()`](https://docs.python.org/3/library/socket.html#socket.socket.connect "socket.socket.connect"),
you will either connect immediately
(unlikely) or get an exception that contains the error number as `.errno`.
`errno.EINPROGRESS` indicates that the connection is in progress, but hasn’t
finished yet. Different OSes will return different values, so you’re going to
have to check what’s returned on your system.

You can use the [`connect_ex()`](https://docs.python.org/3/library/socket.html#socket.socket.connect_ex "socket.socket.connect_ex") method
to avoid creating an exception.
It will just return the errno value.
To poll, you can call [`connect_ex()`](https://docs.python.org/3/library/socket.html#socket.socket.connect_ex "socket.socket.connect_ex") again later
– `0` or `errno.EISCONN` indicate that you’re connected – or you can pass this
socket to [`select.select()`](https://docs.python.org/3/library/select.html#select.select "select.select") to check if it’s writable.

Note

The [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") module provides a general purpose single-threaded and
concurrent asynchronous library, which can be used for writing non-blocking
network code.
The third-party [Twisted](https://twisted.org/) library is
a popular and feature-rich alternative.

## [Databases](https://docs.python.org/3/faq/library.html\#id31) [¶](https://docs.python.org/3/faq/library.html\#databases "Link to this heading")

### [Are there any interfaces to database packages in Python?](https://docs.python.org/3/faq/library.html\#id32) [¶](https://docs.python.org/3/faq/library.html\#are-there-any-interfaces-to-database-packages-in-python "Link to this heading")

Yes.

Interfaces to disk-based hashes such as [`DBM`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager (Unix)") and [`GDBM`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager (Unix)") are also included with standard Python. There is also the
[`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.") module, which provides a lightweight disk-based relational
database.

Support for most relational databases is available. See the
[DatabaseProgramming wiki page](https://wiki.python.org/moin/DatabaseProgramming) for details.

### [How do you implement persistent objects in Python?](https://docs.python.org/3/faq/library.html\#id33) [¶](https://docs.python.org/3/faq/library.html\#how-do-you-implement-persistent-objects-in-python "Link to this heading")

The [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") library module solves this in a very general way (though you
still can’t store things like open files, sockets or windows), and the
[`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.") library module uses pickle and (g)dbm to create persistent
mappings containing arbitrary Python objects.

## [Mathematics and Numerics](https://docs.python.org/3/faq/library.html\#id34) [¶](https://docs.python.org/3/faq/library.html\#mathematics-and-numerics "Link to this heading")

### [How do I generate random numbers in Python?](https://docs.python.org/3/faq/library.html\#id35) [¶](https://docs.python.org/3/faq/library.html\#how-do-i-generate-random-numbers-in-python "Link to this heading")

The standard module [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") implements a random number generator. Usage
is simple:

Copy

```
import random
random.random()
```

This returns a random floating-point number in the range \[0, 1).\
\
There are also many other specialized generators in this module, such as:\
\
- `randrange(a, b)` chooses an integer in the range \[a, b).\
\
- `uniform(a, b)` chooses a floating-point number in the range \[a, b).\
\
- `normalvariate(mean, sdev)` samples the normal (Gaussian) distribution.\
\
\
Some higher-level functions operate on sequences directly, such as:\
\
- `choice(S)` chooses a random element from a given sequence.\
\
- `shuffle(L)` shuffles a list in-place, i.e. permutes it randomly.\
\
\
There’s also a `Random` class you can instantiate to create independent\
multiple random number generators.\
\
### [Table of Contents](https://docs.python.org/3/contents.html)\
\
- [Library and Extension FAQ](https://docs.python.org/3/faq/library.html#)\
  - [General Library Questions](https://docs.python.org/3/faq/library.html#general-library-questions)\
  - [Common tasks](https://docs.python.org/3/faq/library.html#common-tasks)\
  - [Threads](https://docs.python.org/3/faq/library.html#threads)\
  - [Input and Output](https://docs.python.org/3/faq/library.html#input-and-output)\
  - [Network/Internet Programming](https://docs.python.org/3/faq/library.html#network-internet-programming)\
  - [Databases](https://docs.python.org/3/faq/library.html#databases)\
  - [Mathematics and Numerics](https://docs.python.org/3/faq/library.html#mathematics-and-numerics)\
\
#### Previous topic\
\
[Design and History FAQ](https://docs.python.org/3/faq/design.html "previous chapter")\
\
#### Next topic\
\
[Extending/Embedding FAQ](https://docs.python.org/3/faq/extending.html "next chapter")\
\
### This page\
\
- [Report a bug](https://docs.python.org/3/bugs.html)\
- [Show source](https://github.com/python/cpython/blob/main/Doc/faq/library.rst?plain=1)\
\
«\
\
### Navigation\
\
- [index](https://docs.python.org/3/genindex.html "General Index")\
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|\
- [next](https://docs.python.org/3/faq/extending.html "Extending/Embedding FAQ") \|\
- [previous](https://docs.python.org/3/faq/design.html "Design and History FAQ") \|\
- ![Python logo](https://docs.python.org/3/_static/py.svg)\
- [Python](https://www.python.org/) »\
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文\
\
dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6\
\
- [3.14.0 Documentation](https://docs.python.org/3/index.html) »\
\
- [Python Frequently Asked Questions](https://docs.python.org/3/faq/index.html) »\
- [Library and Extension FAQ](https://docs.python.org/3/faq/library.html)\
- \|\
\
- Theme\
AutoLightDark \|