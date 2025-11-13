### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/whatsnew/2.2.html "What’s New in Python 2.2") \|
- [previous](https://docs.python.org/3/whatsnew/2.4.html "What’s New in Python 2.4") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [What’s New in Python](https://docs.python.org/3/whatsnew/index.html) »
- [What’s New in Python 2.3](https://docs.python.org/3/whatsnew/2.3.html)
- \|

- Theme
AutoLightDark \|

# What’s New in Python 2.3 [¶](https://docs.python.org/3/whatsnew/2.3.html\#what-s-new-in-python-2-3 "Link to this heading")

Author:

A.M. Kuchling

This article explains the new features in Python 2.3. Python 2.3 was released
on July 29, 2003.

The main themes for Python 2.3 are polishing some of the features added in 2.2,
adding various small but useful enhancements to the core language, and expanding
the standard library. The new object model introduced in the previous version
has benefited from 18 months of bugfixes and from optimization efforts that have
improved the performance of new-style classes. A few new built-in functions
have been added such as [`sum()`](https://docs.python.org/3/library/functions.html#sum "sum") and [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate "enumerate"). The [`in`](https://docs.python.org/3/reference/expressions.html#in)
operator can now be used for substring searches (e.g. `"ab" in "abc"` returns
[`True`](https://docs.python.org/3/library/constants.html#True "True")).

Some of the many new library features include Boolean, set, heap, and date/time
data types, the ability to import modules from ZIP-format archives, metadata
support for the long-awaited Python catalog, an updated version of IDLE, and
modules for logging messages, wrapping text, parsing CSV files, processing
command-line options, using BerkeleyDB databases… the list of new and
enhanced modules is lengthy.

This article doesn’t attempt to provide a complete specification of the new
features, but instead provides a convenient overview. For full details, you
should refer to the documentation for Python 2.3, such as the Python Library
Reference and the Python Reference Manual. If you want to understand the
complete implementation and design rationale, refer to the PEP for a particular
new feature.

## PEP 218: A Standard Set Datatype [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-218-a-standard-set-datatype "Link to this heading")

The new `sets` module contains an implementation of a set datatype. The
`Set` class is for mutable sets, sets that can have members added and
removed. The `ImmutableSet` class is for sets that can’t be modified,
and instances of `ImmutableSet` can therefore be used as dictionary keys.
Sets are built on top of dictionaries, so the elements within a set must be
hashable.

Here’s a simple example:

Copy

```
>>> import sets
>>> S = sets.Set([1,2,3])
>>> S
Set([1, 2, 3])
>>> 1 in S
True
>>> 0 in S
False
>>> S.add(5)
>>> S.remove(3)
>>> S
Set([1, 2, 5])
>>>
```

The union and intersection of sets can be computed with the [`union()`](https://docs.python.org/3/library/stdtypes.html#frozenset.union "frozenset.union") and
[`intersection()`](https://docs.python.org/3/library/stdtypes.html#frozenset.intersection "frozenset.intersection") methods; an alternative notation uses the bitwise operators
`&` and `|`. Mutable sets also have in-place versions of these methods,
`union_update()` and [`intersection_update()`](https://docs.python.org/3/library/stdtypes.html#frozenset.intersection_update "frozenset.intersection_update").

Copy

```
>>> S1 = sets.Set([1,2,3])
>>> S2 = sets.Set([4,5,6])
>>> S1.union(S2)
Set([1, 2, 3, 4, 5, 6])
>>> S1 | S2                  # Alternative notation
Set([1, 2, 3, 4, 5, 6])
>>> S1.intersection(S2)
Set([])
>>> S1 & S2                  # Alternative notation
Set([])
>>> S1.union_update(S2)
>>> S1
Set([1, 2, 3, 4, 5, 6])
>>>
```

It’s also possible to take the symmetric difference of two sets. This is the
set of all elements in the union that aren’t in the intersection. Another way
of putting it is that the symmetric difference contains all elements that are in
exactly one set. Again, there’s an alternative notation (`^`), and an
in-place version with the ungainly name [`symmetric_difference_update()`](https://docs.python.org/3/library/stdtypes.html#frozenset.symmetric_difference_update "frozenset.symmetric_difference_update").

Copy

```
>>> S1 = sets.Set([1,2,3,4])
>>> S2 = sets.Set([3,4,5,6])
>>> S1.symmetric_difference(S2)
Set([1, 2, 5, 6])
>>> S1 ^ S2
Set([1, 2, 5, 6])
>>>
```

There are also `issubset()` and `issuperset()` methods for checking
whether one set is a subset or superset of another:

Copy

```
>>> S1 = sets.Set([1,2,3])
>>> S2 = sets.Set([2,3])
>>> S2.issubset(S1)
True
>>> S1.issubset(S2)
False
>>> S1.issuperset(S2)
True
>>>
```

See also

[**PEP 218**](https://peps.python.org/pep-0218/) \- Adding a Built-In Set Object Type

PEP written by Greg V. Wilson. Implemented by Greg V. Wilson, Alex Martelli, and
GvR.

## PEP 255: Simple Generators [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-255-simple-generators "Link to this heading")

In Python 2.2, generators were added as an optional feature, to be enabled by a
`from __future__ import generators` directive. In 2.3 generators no longer
need to be specially enabled, and are now always present; this means that
[`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield) is now always a keyword. The rest of this section is a copy of
the description of generators from the “What’s New in Python 2.2” document; if
you read it back when Python 2.2 came out, you can skip the rest of this
section.

You’re doubtless familiar with how function calls work in Python or C. When you
call a function, it gets a private namespace where its local variables are
created. When the function reaches a [`return`](https://docs.python.org/3/reference/simple_stmts.html#return) statement, the local
variables are destroyed and the resulting value is returned to the caller. A
later call to the same function will get a fresh new set of local variables.
But, what if the local variables weren’t thrown away on exiting a function?
What if you could later resume the function where it left off? This is what
generators provide; they can be thought of as resumable functions.

Here’s the simplest example of a generator function:

Copy

```
def generate_ints(N):
    for i in range(N):
        yield i
```

A new keyword, [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield), was introduced for generators. Any function
containing a `yield` statement is a generator function; this is
detected by Python’s bytecode compiler which compiles the function specially as
a result.

When you call a generator function, it doesn’t return a single value; instead it
returns a generator object that supports the iterator protocol. On executing
the [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield) statement, the generator outputs the value of `i`,
similar to a [`return`](https://docs.python.org/3/reference/simple_stmts.html#return) statement. The big difference between
`yield` and a `return` statement is that on reaching a
`yield` the generator’s state of execution is suspended and local
variables are preserved. On the next call to the generator’s `.next()`
method, the function will resume executing immediately after the
`yield` statement. (For complicated reasons, the `yield`
statement isn’t allowed inside the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) block of a
`try`…`finally` statement; read [**PEP 255**](https://peps.python.org/pep-0255/) for a full
explanation of the interaction between `yield` and exceptions.)

Here’s a sample usage of the `generate_ints()` generator:

Copy

```
>>> gen = generate_ints(3)
>>> gen
<generator object at 0x8117f90>
>>> gen.next()
0
>>> gen.next()
1
>>> gen.next()
2
>>> gen.next()
Traceback (most recent call last):
  File "stdin", line 1, in ?
  File "stdin", line 2, in generate_ints
StopIteration
```

You could equally write `for i in generate_ints(5)`, or `a,b,c =
generate_ints(3)`.

Inside a generator function, the [`return`](https://docs.python.org/3/reference/simple_stmts.html#return) statement can only be used
without a value, and signals the end of the procession of values; afterwards the
generator cannot return any further values. `return` with a value, such
as `return 5`, is a syntax error inside a generator function. The end of the
generator’s results can also be indicated by raising [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration")
manually, or by just letting the flow of execution fall off the bottom of the
function.

You could achieve the effect of generators manually by writing your own class
and storing all the local variables of the generator as instance variables. For
example, returning a list of integers could be done by setting `self.count` to
0, and having the [`next()`](https://docs.python.org/3/library/functions.html#next "next") method increment `self.count` and return it.
However, for a moderately complicated generator, writing a corresponding class
would be much messier. `Lib/test/test_generators.py` contains a number of
more interesting examples. The simplest one implements an in-order traversal of
a tree using generators recursively.

Copy

```
# A recursive generator that generates Tree leaves in in-order.
def inorder(t):
    if t:
        for x in inorder(t.left):
            yield x
        yield t.label
        for x in inorder(t.right):
            yield x
```

Two other examples in `Lib/test/test_generators.py` produce solutions for
the N-Queens problem (placing $N$ queens on an $NxN$ chess board so that no
queen threatens another) and the Knight’s Tour (a route that takes a knight to
every square of an $NxN$ chessboard without visiting any square twice).

The idea of generators comes from other programming languages, especially Icon
( [https://www2.cs.arizona.edu/icon/](https://www2.cs.arizona.edu/icon/)), where the idea of generators is central. In
Icon, every expression and function call behaves like a generator. One example
from “An Overview of the Icon Programming Language” at
[https://www2.cs.arizona.edu/icon/docs/ipd266.htm](https://www2.cs.arizona.edu/icon/docs/ipd266.htm) gives an idea of what this looks
like:

Copy

```
sentence := "Store it in the neighboring harbor"
if (i := find("or", sentence)) > 5 then write(i)
```

In Icon the `find()` function returns the indexes at which the substring
“or” is found: 3, 23, 33. In the [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) statement, `i` is first
assigned a value of 3, but 3 is less than 5, so the comparison fails, and Icon
retries it with the second value of 23. 23 is greater than 5, so the comparison
now succeeds, and the code prints the value 23 to the screen.

Python doesn’t go nearly as far as Icon in adopting generators as a central
concept. Generators are considered part of the core Python language, but
learning or using them isn’t compulsory; if they don’t solve any problems that
you have, feel free to ignore them. One novel feature of Python’s interface as
compared to Icon’s is that a generator’s state is represented as a concrete
object (the iterator) that can be passed around to other functions or stored in
a data structure.

See also

[**PEP 255**](https://peps.python.org/pep-0255/) \- Simple Generators

Written by Neil Schemenauer, Tim Peters, Magnus Lie Hetland. Implemented mostly
by Neil Schemenauer and Tim Peters, with other fixes from the Python Labs crew.

## PEP 263: Source Code Encodings [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-263-source-code-encodings "Link to this heading")

Python source files can now be declared as being in different character set
encodings. Encodings are declared by including a specially formatted comment in
the first or second line of the source file. For example, a UTF-8 file can be
declared with:

Copy

```
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
```

Without such an encoding declaration, the default encoding used is 7-bit ASCII.
Executing or importing modules that contain string literals with 8-bit
characters and have no encoding declaration will result in a
[`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") being signalled by Python 2.3; in 2.4 this will be a
syntax error.

The encoding declaration only affects Unicode string literals, which will be
converted to Unicode using the specified encoding. Note that Python identifiers
are still restricted to ASCII characters, so you can’t have variable names that
use characters outside of the usual alphanumerics.

See also

[**PEP 263**](https://peps.python.org/pep-0263/) \- Defining Python Source Code Encodings

Written by Marc-André Lemburg and Martin von Löwis; implemented by Suzuki Hisao
and Martin von Löwis.

## PEP 273: Importing Modules from ZIP Archives [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-273-importing-modules-from-zip-archives "Link to this heading")

The new [`zipimport`](https://docs.python.org/3/library/zipimport.html#module-zipimport "zipimport: Support for importing Python modules from ZIP archives.") module adds support for importing modules from a
ZIP-format archive. You don’t need to import the module explicitly; it will be
automatically imported if a ZIP archive’s filename is added to `sys.path`.
For example:

```
amk@nyman:~/src/python$ unzip -l /tmp/example.zip
Archive:  /tmp/example.zip
  Length     Date   Time    Name
 --------    ----   ----    ----
     8467  11-26-02 22:30   jwzthreading.py
 --------                   -------
     8467                   1 file
amk@nyman:~/src/python$ ./python
Python 2.3 (#1, Aug 1 2003, 19:54:32)
>>> import sys
>>> sys.path.insert(0, '/tmp/example.zip')  # Add .zip file to front of path
>>> import jwzthreading
>>> jwzthreading.__file__
'/tmp/example.zip/jwzthreading.py'
>>>
```

An entry in `sys.path` can now be the filename of a ZIP archive. The ZIP
archive can contain any kind of files, but only files named `*.py`,
`*.pyc`, or `*.pyo` can be imported. If an archive only contains
`*.py` files, Python will not attempt to modify the archive by adding the
corresponding `*.pyc` file, meaning that if a ZIP archive doesn’t contain
`*.pyc` files, importing may be rather slow.

A path within the archive can also be specified to only import from a
subdirectory; for example, the path `/tmp/example.zip/lib/` would only
import from the `lib/` subdirectory within the archive.

See also

[**PEP 273**](https://peps.python.org/pep-0273/) \- Import Modules from Zip Archives

Written by James C. Ahlstrom, who also provided an implementation. Python 2.3
follows the specification in [**PEP 273**](https://peps.python.org/pep-0273/), but uses an implementation written by
Just van Rossum that uses the import hooks described in [**PEP 302**](https://peps.python.org/pep-0302/). See section
[PEP 302: New Import Hooks](https://docs.python.org/3/whatsnew/2.3.html#section-pep302) for a description of the new import hooks.

## PEP 277: Unicode file name support for Windows NT [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-277-unicode-file-name-support-for-windows-nt "Link to this heading")

On Windows NT, 2000, and XP, the system stores file names as Unicode strings.
Traditionally, Python has represented file names as byte strings, which is
inadequate because it renders some file names inaccessible.

Python now allows using arbitrary Unicode strings (within the limitations of the
file system) for all functions that expect file names, most notably the
[`open()`](https://docs.python.org/3/library/functions.html#open "open") built-in function. If a Unicode string is passed to
[`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir"), Python now returns a list of Unicode strings. A new
function, `os.getcwdu()`, returns the current directory as a Unicode string.

Byte strings still work as file names, and on Windows Python will transparently
convert them to Unicode using the `mbcs` encoding.

Other systems also allow Unicode strings as file names but convert them to byte
strings before passing them to the system, which can cause a [`UnicodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeError "UnicodeError")
to be raised. Applications can test whether arbitrary Unicode strings are
supported as file names by checking [`os.path.supports_unicode_filenames`](https://docs.python.org/3/library/os.path.html#os.path.supports_unicode_filenames "os.path.supports_unicode_filenames"),
a Boolean value.

Under MacOS, [`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir "os.listdir") may now return Unicode filenames.

See also

[**PEP 277**](https://peps.python.org/pep-0277/) \- Unicode file name support for Windows NT

Written by Neil Hodgson; implemented by Neil Hodgson, Martin von Löwis, and Mark
Hammond.

## PEP 278: Universal Newline Support [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-278-universal-newline-support "Link to this heading")

The three major operating systems used today are Microsoft Windows, Apple’s
Macintosh OS, and the various Unix derivatives. A minor irritation of
cross-platform work is that these three platforms all use different characters to
mark the ends of lines in text files. Unix uses the linefeed (ASCII character
10), MacOS uses the carriage return (ASCII character 13), and Windows uses a
two-character sequence of a carriage return plus a newline.

Python’s file objects can now support end of line conventions other than the
one followed by the platform on which Python is running. Opening a file with
the mode `'U'` or `'rU'` will open a file for reading in [universal\\
newlines](https://docs.python.org/3/glossary.html#term-universal-newlines) mode. All three line ending conventions will be translated to a
`'\n'` in the strings returned by the various file methods such as
`read()` and `readline()`.

Universal newline support is also used when importing modules and when executing
a file with the `execfile()` function. This means that Python modules can
be shared between all three operating systems without needing to convert the
line-endings.

This feature can be disabled when compiling Python by specifying the
`--without-universal-newlines` switch when running Python’s
**configure** script.

See also

[**PEP 278**](https://peps.python.org/pep-0278/) \- Universal Newline Support

Written and implemented by Jack Jansen.

## PEP 279: enumerate() [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-279-enumerate "Link to this heading")

A new built-in function, [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate "enumerate"), will make certain loops a bit
clearer. `enumerate(thing)`, where _thing_ is either an iterator or a
sequence, returns an iterator that will return `(0, thing[0])`, `(1,
thing[1])`, `(2, thing[2])`, and so forth.

A common idiom to change every element of a list looks like this:

Copy

```
for i in range(len(L)):
    item = L[i]
    # ... compute some result based on item ...
    L[i] = result
```

This can be rewritten using [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate "enumerate") as:

Copy

```
for i, item in enumerate(L):
    # ... compute some result based on item ...
    L[i] = result
```

See also

[**PEP 279**](https://peps.python.org/pep-0279/) \- The enumerate() built-in function

Written and implemented by Raymond D. Hettinger.

## PEP 282: The logging Package [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-282-the-logging-package "Link to this heading")

A standard package for writing logs, [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications."), has been added to Python
2.3. It provides a powerful and flexible mechanism for generating logging
output which can then be filtered and processed in various ways. A
configuration file written in a standard format can be used to control the
logging behavior of a program. Python includes handlers that will write log
records to standard error or to a file or socket, send them to the system log,
or even e-mail them to a particular address; of course, it’s also possible to
write your own handler classes.

The [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") class is the primary class. Most application code will deal
with one or more [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") objects, each one used by a particular
subsystem of the application. Each [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") is identified by a name, and
names are organized into a hierarchy using `.` as the component separator.
For example, you might have [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") instances named `server`,
`server.auth` and `server.network`. The latter two instances are below
`server` in the hierarchy. This means that if you turn up the verbosity for
`server` or direct `server` messages to a different handler, the changes
will also apply to records logged to `server.auth` and `server.network`.
There’s also a root [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") that’s the parent of all other loggers.

For simple uses, the [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.") package contains some convenience functions
that always use the root log:

Copy

```
import logging

logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')
```

This produces the following output:

Copy

```
WARNING:root:Warning:config file server.conf not found
ERROR:root:Error occurred
CRITICAL:root:Critical error -- shutting down
```

In the default configuration, informational and debugging messages are
suppressed and the output is sent to standard error. You can enable the display
of informational and debugging messages by calling the [`setLevel()`](https://docs.python.org/3/library/logging.html#logging.Logger.setLevel "logging.Logger.setLevel") method
on the root logger.

Notice the [`warning()`](https://docs.python.org/3/library/logging.html#logging.warning "logging.warning") call’s use of string formatting operators; all of the
functions for logging messages take the arguments `(msg, arg1, arg2, ...)` and
log the string resulting from `msg % (arg1, arg2, ...)`.

There’s also an [`exception()`](https://docs.python.org/3/library/logging.html#logging.exception "logging.exception") function that records the most recent
traceback. Any of the other functions will also record the traceback if you
specify a true value for the keyword argument _exc\_info_.

Copy

```
def f():
    try:    1/0
    except: logging.exception('Problem recorded')

f()
```

This produces the following output:

Copy

```
ERROR:root:Problem recorded
Traceback (most recent call last):
  File "t.py", line 6, in f
    1/0
ZeroDivisionError: integer division or modulo by zero
```

Slightly more advanced programs will use a logger other than the root logger.
The `getLogger(name)` function is used to get a particular log, creating
it if it doesn’t exist yet. `getLogger(None)` returns the root logger.

Copy

```
log = logging.getLogger('server')
 ...
log.info('Listening on port %i', port)
 ...
log.critical('Disk full')
 ...
```

Log records are usually propagated up the hierarchy, so a message logged to
`server.auth` is also seen by `server` and `root`, but a [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger")
can prevent this by setting its [`propagate`](https://docs.python.org/3/library/logging.html#logging.Logger.propagate "logging.Logger.propagate") attribute to [`False`](https://docs.python.org/3/library/constants.html#False "False").

There are more classes provided by the [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.") package that can be
customized. When a [`Logger`](https://docs.python.org/3/library/logging.html#logging.Logger "logging.Logger") instance is told to log a message, it
creates a [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") instance that is sent to any number of different
[`Handler`](https://docs.python.org/3/library/logging.html#logging.Handler "logging.Handler") instances. Loggers and handlers can also have an attached list
of filters, and each filter can cause the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") to be ignored or
can modify the record before passing it along. When they’re finally output,
[`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") instances are converted to text by a [`Formatter`](https://docs.python.org/3/library/logging.html#logging.Formatter "logging.Formatter")
class. All of these classes can be replaced by your own specially written
classes.

With all of these features the [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.") package should provide enough
flexibility for even the most complicated applications. This is only an
incomplete overview of its features, so please see the package’s reference
documentation for all of the details. Reading [**PEP 282**](https://peps.python.org/pep-0282/) will also be helpful.

See also

[**PEP 282**](https://peps.python.org/pep-0282/) \- A Logging System

Written by Vinay Sajip and Trent Mick; implemented by Vinay Sajip.

## PEP 285: A Boolean Type [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-285-a-boolean-type "Link to this heading")

A Boolean type was added to Python 2.3. Two new constants were added to the
`__builtin__` module, [`True`](https://docs.python.org/3/library/constants.html#True "True") and [`False`](https://docs.python.org/3/library/constants.html#False "False"). ( [`True`](https://docs.python.org/3/library/constants.html#True "True") and
[`False`](https://docs.python.org/3/library/constants.html#False "False") constants were added to the built-ins in Python 2.2.1, but the
2.2.1 versions are simply set to integer values of 1 and 0 and aren’t a
different type.)

The type object for this new type is named [`bool`](https://docs.python.org/3/library/functions.html#bool "bool"); the constructor for it
takes any Python value and converts it to [`True`](https://docs.python.org/3/library/constants.html#True "True") or [`False`](https://docs.python.org/3/library/constants.html#False "False").

Copy

```
>>> bool(1)
True
>>> bool(0)
False
>>> bool([])
False
>>> bool( (1,) )
True
```

Most of the standard library modules and built-in functions have been changed to
return Booleans.

Copy

```
>>> obj = []
>>> hasattr(obj, 'append')
True
>>> isinstance(obj, list)
True
>>> isinstance(obj, tuple)
False
```

Python’s Booleans were added with the primary goal of making code clearer. For
example, if you’re reading a function and encounter the statement `return 1`,
you might wonder whether the `1` represents a Boolean truth value, an index,
or a coefficient that multiplies some other quantity. If the statement is
`return True`, however, the meaning of the return value is quite clear.

Python’s Booleans were _not_ added for the sake of strict type-checking. A very
strict language such as Pascal would also prevent you performing arithmetic with
Booleans, and would require that the expression in an [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) statement
always evaluate to a Boolean result. Python is not this strict and never will
be, as [**PEP 285**](https://peps.python.org/pep-0285/) explicitly says. This means you can still use any expression
in an `if` statement, even ones that evaluate to a list or tuple or
some random object. The Boolean type is a subclass of the [`int`](https://docs.python.org/3/library/functions.html#int "int") class so
that arithmetic using a Boolean still works.

Copy

```
>>> True + 1
2
>>> False + 1
1
>>> False * 75
0
>>> True * 75
75
```

To sum up [`True`](https://docs.python.org/3/library/constants.html#True "True") and [`False`](https://docs.python.org/3/library/constants.html#False "False") in a sentence: they’re alternative
ways to spell the integer values 1 and 0, with the single difference that
[`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") and [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") return the strings `'True'` and `'False'`
instead of `'1'` and `'0'`.

See also

[**PEP 285**](https://peps.python.org/pep-0285/) \- Adding a bool type

Written and implemented by GvR.

## PEP 293: Codec Error Handling Callbacks [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-293-codec-error-handling-callbacks "Link to this heading")

When encoding a Unicode string into a byte string, unencodable characters may be
encountered. So far, Python has allowed specifying the error processing as
either “strict” (raising [`UnicodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeError "UnicodeError")), “ignore” (skipping the
character), or “replace” (using a question mark in the output string), with
“strict” being the default behavior. It may be desirable to specify alternative
processing of such errors, such as inserting an XML character reference or HTML
entity reference into the converted string.

Python now has a flexible framework to add different processing strategies. New
error handlers can be added with [`codecs.register_error()`](https://docs.python.org/3/library/codecs.html#codecs.register_error "codecs.register_error"), and codecs then
can access the error handler with [`codecs.lookup_error()`](https://docs.python.org/3/library/codecs.html#codecs.lookup_error "codecs.lookup_error"). An equivalent C
API has been added for codecs written in C. The error handler gets the necessary
state information such as the string being converted, the position in the string
where the error was detected, and the target encoding. The handler can then
either raise an exception or return a replacement string.

Two additional error handlers have been implemented using this framework:
“backslashreplace” uses Python backslash quoting to represent unencodable
characters and “xmlcharrefreplace” emits XML character references.

See also

[**PEP 293**](https://peps.python.org/pep-0293/) \- Codec Error Handling Callbacks

Written and implemented by Walter Dörwald.

## PEP 301: Package Index and Metadata for Distutils [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-301-package-index-and-metadata-for-distutils "Link to this heading")

Support for the long-requested Python catalog makes its first appearance in 2.3.

The heart of the catalog is the new Distutils **register** command.
Running `python setup.py register` will collect the metadata describing a
package, such as its name, version, maintainer, description, &c., and send it to
a central catalog server. The resulting catalog is available from
[https://pypi.org](https://pypi.org/).

To make the catalog a bit more useful, a new optional _classifiers_ keyword
argument has been added to the Distutils `setup()` function. A list of
[Trove](http://catb.org/~esr/trove/)-style strings can be supplied to help
classify the software.

Here’s an example `setup.py` with classifiers, written to be compatible
with older versions of the Distutils:

Copy

```
from distutils import core
kw = {'name': "Quixote",
      'version': "0.5.1",
      'description': "A highly Pythonic Web application framework",
      # ...
      }

if (hasattr(core, 'setup_keywords') and
    'classifiers' in core.setup_keywords):
    kw['classifiers'] = \
        ['Topic :: Internet :: WWW/HTTP :: Dynamic Content',\
         'Environment :: No Input/Output (Daemon)',\
         'Intended Audience :: Developers'],

core.setup(**kw)
```

The full list of classifiers can be obtained by running `python setup.py
register --list-classifiers`.

See also

[**PEP 301**](https://peps.python.org/pep-0301/) \- Package Index and Metadata for Distutils

Written and implemented by Richard Jones.

## PEP 302: New Import Hooks [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-302-new-import-hooks "Link to this heading")

While it’s been possible to write custom import hooks ever since the
`ihooks` module was introduced in Python 1.3, no one has ever been really
happy with it because writing new import hooks is difficult and messy. There
have been various proposed alternatives such as the `imputil` and `iu`
modules, but none of them has ever gained much acceptance, and none of them were
easily usable from C code.

[**PEP 302**](https://peps.python.org/pep-0302/) borrows ideas from its predecessors, especially from Gordon
McMillan’s `iu` module. Three new items are added to the [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")
module:

- `sys.path_hooks` is a list of callable objects; most often they’ll be
classes. Each callable takes a string containing a path and either returns an
importer object that will handle imports from this path or raises an
[`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") exception if it can’t handle this path.

- `sys.path_importer_cache` caches importer objects for each path, so
`sys.path_hooks` will only need to be traversed once for each path.

- `sys.meta_path` is a list of importer objects that will be traversed before
`sys.path` is checked. This list is initially empty, but user code can add
objects to it. Additional built-in and frozen modules can be imported by an
object added to this list.


Importer objects must have a single method, `find_module(fullname,
path=None)`. _fullname_ will be a module or package name, e.g. `string` or
`distutils.core`. `find_module()` must return a loader object that has a
single method, `load_module(fullname)`, that creates and returns the
corresponding module object.

Pseudo-code for Python’s new import logic, therefore, looks something like this
(simplified a bit; see [**PEP 302**](https://peps.python.org/pep-0302/) for the full details):

Copy

```
for mp in sys.meta_path:
    loader = mp(fullname)
    if loader is not None:
        <module> = loader.load_module(fullname)

for path in sys.path:
    for hook in sys.path_hooks:
        try:
            importer = hook(path)
        except ImportError:
            # ImportError, so try the other path hooks
            pass
        else:
            loader = importer.find_module(fullname)
            <module> = loader.load_module(fullname)

# Not found!
raise ImportError
```

See also

[**PEP 302**](https://peps.python.org/pep-0302/) \- New Import Hooks

Written by Just van Rossum and Paul Moore. Implemented by Just van Rossum.

## PEP 305: Comma-separated Files [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-305-comma-separated-files "Link to this heading")

Comma-separated files are a format frequently used for exporting data from
databases and spreadsheets. Python 2.3 adds a parser for comma-separated files.

Comma-separated format is deceptively simple at first glance:

Copy

```
Costs,150,200,3.95
```

Read a line and call `line.split(',')`: what could be simpler? But toss in
string data that can contain commas, and things get more complicated:

Copy

```
"Costs",150,200,3.95,"Includes taxes, shipping, and sundry items"
```

A big ugly regular expression can parse this, but using the new [`csv`](https://docs.python.org/3/library/csv.html#module-csv "csv: Write and read tabular data to and from delimited files.")
package is much simpler:

Copy

```
import csv

input = open('datafile', 'rb')
reader = csv.reader(input)
for line in reader:
    print line
```

The [`reader()`](https://docs.python.org/3/library/csv.html#csv.reader "csv.reader") function takes a number of different options. The field
separator isn’t limited to the comma and can be changed to any character, and so
can the quoting and line-ending characters.

Different dialects of comma-separated files can be defined and registered;
currently there are two dialects, both used by Microsoft Excel. A separate
[`csv.writer`](https://docs.python.org/3/library/csv.html#csv.writer "csv.writer") class will generate comma-separated files from a succession
of tuples or lists, quoting strings that contain the delimiter.

See also

[**PEP 305**](https://peps.python.org/pep-0305/) \- CSV File API

Written and implemented by Kevin Altis, Dave Cole, Andrew McNamara, Skip
Montanaro, Cliff Wells.

## PEP 307: Pickle Enhancements [¶](https://docs.python.org/3/whatsnew/2.3.html\#pep-307-pickle-enhancements "Link to this heading")

The [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and `cPickle` modules received some attention during the
2.3 development cycle. In 2.2, new-style classes could be pickled without
difficulty, but they weren’t pickled very compactly; [**PEP 307**](https://peps.python.org/pep-0307/) quotes a trivial
example where a new-style class results in a pickled string three times longer
than that for a classic class.

The solution was to invent a new pickle protocol. The [`pickle.dumps()`](https://docs.python.org/3/library/pickle.html#pickle.dumps "pickle.dumps")
function has supported a text-or-binary flag for a long time. In 2.3, this
flag is redefined from a Boolean to an integer: 0 is the old text-mode pickle
format, 1 is the old binary format, and now 2 is a new 2.3-specific format. A
new constant, [`pickle.HIGHEST_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.HIGHEST_PROTOCOL "pickle.HIGHEST_PROTOCOL"), can be used to select the
fanciest protocol available.

Unpickling is no longer considered a safe operation. 2.2’s [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.")
provided hooks for trying to prevent unsafe classes from being unpickled
(specifically, a `__safe_for_unpickling__` attribute), but none of this
code was ever audited and therefore it’s all been ripped out in 2.3. You should
not unpickle untrusted data in any version of Python.

To reduce the pickling overhead for new-style classes, a new interface for
customizing pickling was added using three special methods:
[`__getstate__()`](https://docs.python.org/3/library/pickle.html#object.__getstate__ "object.__getstate__"), [`__setstate__()`](https://docs.python.org/3/library/pickle.html#object.__setstate__ "object.__setstate__"), and [`__getnewargs__()`](https://docs.python.org/3/library/pickle.html#object.__getnewargs__ "object.__getnewargs__"). Consult
[**PEP 307**](https://peps.python.org/pep-0307/) for the full semantics of these methods.

As a way to compress pickles yet further, it’s now possible to use integer codes
instead of long strings to identify pickled classes. The Python Software
Foundation will maintain a list of standardized codes; there’s also a range of
codes for private use. Currently no codes have been specified.

See also

[**PEP 307**](https://peps.python.org/pep-0307/) \- Extensions to the pickle protocol

Written and implemented by Guido van Rossum and Tim Peters.

## Extended Slices [¶](https://docs.python.org/3/whatsnew/2.3.html\#extended-slices "Link to this heading")

Ever since Python 1.4, the slicing syntax has supported an optional third “step”
or “stride” argument. For example, these are all legal Python syntax:
`L[1:10:2]`, `L[:-1:1]`, `L[::-1]`. This was added to Python at the
request of the developers of Numerical Python, which uses the third argument
extensively. However, Python’s built-in list, tuple, and string sequence types
have never supported this feature, raising a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if you tried it.
Michael Hudson contributed a patch to fix this shortcoming.

For example, you can now easily extract the elements of a list that have even
indexes:

Copy

```
>>> L = range(10)
>>> L[::2]
[0, 2, 4, 6, 8]
```

Negative values also work to make a copy of the same list in reverse order:

Copy

```
>>> L[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

This also works for tuples, arrays, and strings:

Copy

```
>>> s='abcd'
>>> s[::2]
'ac'
>>> s[::-1]
'dcba'
```

If you have a mutable sequence such as a list or an array you can assign to or
delete an extended slice, but there are some differences between assignment to
extended and regular slices. Assignment to a regular slice can be used to
change the length of the sequence:

Copy

```
>>> a = range(3)
>>> a
[0, 1, 2]
>>> a[1:3] = [4, 5, 6]
>>> a
[0, 4, 5, 6]
```

Extended slices aren’t this flexible. When assigning to an extended slice, the
list on the right hand side of the statement must contain the same number of
items as the slice it is replacing:

Copy

```
>>> a = range(4)
>>> a
[0, 1, 2, 3]
>>> a[::2]
[0, 2]
>>> a[::2] = [0, -1]
>>> a
[0, 1, -1, 3]
>>> a[::2] = [0,1,2]
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ValueError: attempt to assign sequence of size 3 to extended slice of size 2
```

Deletion is more straightforward:

Copy

```
>>> a = range(4)
>>> a
[0, 1, 2, 3]
>>> a[::2]
[0, 2]
>>> del a[::2]
>>> a
[1, 3]
```

One can also now pass slice objects to the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__") methods of the
built-in sequences:

Copy

```
>>> range(10).__getitem__(slice(0, 5, 2))
[0, 2, 4]
```

Or use slice objects directly in subscripts:

Copy

```
>>> range(10)[slice(0, 5, 2)]
[0, 2, 4]
```

To simplify implementing sequences that support extended slicing, slice objects
now have a method `indices(length)` which, given the length of a sequence,
returns a `(start, stop, step)` tuple that can be passed directly to
[`range()`](https://docs.python.org/3/library/stdtypes.html#range "range"). `indices()` handles omitted and out-of-bounds indices in a
manner consistent with regular slices (and this innocuous phrase hides a welter
of confusing details!). The method is intended to be used like this:

Copy

```
class FakeSeq:
    ...
    def calc_item(self, i):
        ...
    def __getitem__(self, item):
        if isinstance(item, slice):
            indices = item.indices(len(self))
            return FakeSeq([self.calc_item(i) for i in range(*indices)])
        else:
            return self.calc_item(i)
```

From this example you can also see that the built-in [`slice`](https://docs.python.org/3/library/functions.html#slice "slice") object is
now the type object for the slice type, and is no longer a function. This is
consistent with Python 2.2, where [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), etc., underwent
the same change.

## Other Language Changes [¶](https://docs.python.org/3/whatsnew/2.3.html\#other-language-changes "Link to this heading")

Here are all of the changes that Python 2.3 makes to the core Python language.

- The [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield) statement is now always a keyword, as described in
section [PEP 255: Simple Generators](https://docs.python.org/3/whatsnew/2.3.html#section-generators) of this document.

- A new built-in function [`enumerate()`](https://docs.python.org/3/library/functions.html#enumerate "enumerate") was added, as described in section
[PEP 279: enumerate()](https://docs.python.org/3/whatsnew/2.3.html#section-enumerate) of this document.

- Two new constants, [`True`](https://docs.python.org/3/library/constants.html#True "True") and [`False`](https://docs.python.org/3/library/constants.html#False "False") were added along with the
built-in [`bool`](https://docs.python.org/3/library/functions.html#bool "bool") type, as described in section [PEP 285: A Boolean Type](https://docs.python.org/3/whatsnew/2.3.html#section-bool) of this
document.

- The [`int()`](https://docs.python.org/3/library/functions.html#int "int") type constructor will now return a long integer instead of
raising an [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") when a string or floating-point number is too
large to fit into an integer. This can lead to the paradoxical result that
`isinstance(int(expression), int)` is false, but that seems unlikely to cause
problems in practice.

- Built-in types now support the extended slicing syntax, as described in
section [Extended Slices](https://docs.python.org/3/whatsnew/2.3.html#section-slices) of this document.

- A new built-in function, `sum(iterable, start=0)`, adds up the numeric
items in the iterable object and returns their sum. [`sum()`](https://docs.python.org/3/library/functions.html#sum "sum") only accepts
numbers, meaning that you can’t use it to concatenate a bunch of strings.
(Contributed by Alex Martelli.)

- `list.insert(pos, value)` used to insert _value_ at the front of the list
when _pos_ was negative. The behaviour has now been changed to be consistent
with slice indexing, so when _pos_ is -1 the value will be inserted before the
last element, and so forth.

- `list.index(value)`, which searches for _value_ within the list and returns
its index, now takes optional _start_ and _stop_ arguments to limit the search
to only part of the list.

- Dictionaries have a new method, `pop(key[, *default*])`, that returns
the value corresponding to _key_ and removes that key/value pair from the
dictionary. If the requested key isn’t present in the dictionary, _default_ is
returned if it’s specified and [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") raised if it isn’t.



Copy

```
>>> d = {1:2}
>>> d
{1: 2}
>>> d.pop(4)
Traceback (most recent call last):
    File "stdin", line 1, in ?
KeyError: 4
>>> d.pop(1)
2
>>> d.pop(1)
Traceback (most recent call last):
    File "stdin", line 1, in ?
KeyError: 'pop(): dictionary is empty'
>>> d
{}
>>>
```





There’s also a new class method, `dict.fromkeys(iterable, value)`, that
creates a dictionary with keys taken from the supplied iterator _iterable_ and
all values set to _value_, defaulting to `None`.

(Patches contributed by Raymond Hettinger.)

Also, the [`dict()`](https://docs.python.org/3/library/stdtypes.html#dict "dict") constructor now accepts keyword arguments to simplify
creating small dictionaries:



Copy

```
>>> dict(red=1, blue=2, green=3, black=4)
{'blue': 2, 'black': 4, 'green': 3, 'red': 1}
```





(Contributed by Just van Rossum.)

- The [`assert`](https://docs.python.org/3/reference/simple_stmts.html#assert) statement no longer checks the `__debug__` flag, so
you can no longer disable assertions by assigning to `__debug__`. Running
Python with the [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O) switch will still generate code that doesn’t
execute any assertions.

- Most type objects are now callable, so you can use them to create new objects
such as functions, classes, and modules. (This means that the `new` module
can be deprecated in a future Python version, because you can now use the type
objects available in the [`types`](https://docs.python.org/3/library/types.html#module-types "types: Names for built-in types.") module.) For example, you can create a new
module object with the following code:



Copy

```
>>> import types
>>> m = types.ModuleType('abc','docstring')
>>> m
<module 'abc' (built-in)>
>>> m.__doc__
'docstring'
```

- A new warning, [`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning") was added to indicate features
which are in the process of being deprecated. The warning will _not_ be printed
by default. To check for use of features that will be deprecated in the future,
supply [`-Walways::PendingDeprecationWarning::`](https://docs.python.org/3/using/cmdline.html#cmdoption-W) on the command line or
use [`warnings.filterwarnings()`](https://docs.python.org/3/library/warnings.html#warnings.filterwarnings "warnings.filterwarnings").

- The process of deprecating string-based exceptions, as in `raise "Error
occurred"`, has begun. Raising a string will now trigger
[`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning").

- Using `None` as a variable name will now result in a [`SyntaxWarning`](https://docs.python.org/3/library/exceptions.html#SyntaxWarning "SyntaxWarning")
warning. In a future version of Python, `None` may finally become a keyword.

- The `xreadlines()` method of file objects, introduced in Python 2.1, is no
longer necessary because files now behave as their own iterator.
`xreadlines()` was originally introduced as a faster way to loop over all
the lines in a file, but now you can simply write `for line in file_obj`.
File objects also have a new read-only `encoding` attribute that gives the
encoding used by the file; Unicode strings written to the file will be
automatically converted to bytes using the given encoding.

- The method resolution order used by new-style classes has changed, though
you’ll only notice the difference if you have a really complicated inheritance
hierarchy. Classic classes are unaffected by this change. Python 2.2
originally used a topological sort of a class’s ancestors, but 2.3 now uses the
C3 algorithm as described in the paper [“A Monotonic Superclass Linearization\\
for Dylan”](https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.19.3910). To
understand the motivation for this change, read Michele Simionato’s article
[The Python 2.3 Method Resolution Order](https://docs.python.org/3/howto/mro.html#python-2-3-mro), or
read the thread on python-dev starting with the message at
[https://mail.python.org/pipermail/python-dev/2002-October/029035.html](https://mail.python.org/pipermail/python-dev/2002-October/029035.html). Samuele
Pedroni first pointed out the problem and also implemented the fix by coding the
C3 algorithm.

- Python runs multithreaded programs by switching between threads after
executing N bytecodes. The default value for N has been increased from 10 to
100 bytecodes, speeding up single-threaded applications by reducing the
switching overhead. Some multithreaded applications may suffer slower response
time, but that’s easily fixed by setting the limit back to a lower number using
`sys.setcheckinterval(N)`. The limit can be retrieved with the new
`sys.getcheckinterval()` function.

- One minor but far-reaching change is that the names of extension types defined
by the modules included with Python now contain the module and a `'.'` in
front of the type name. For example, in Python 2.2, if you created a socket and
printed its `__class__`, you’d get this output:



Copy

```
>>> s = socket.socket()
>>> s.__class__
<type 'socket'>
```





In 2.3, you get this:



Copy

```
>>> s.__class__
<type '_socket.socket'>
```

- One of the noted incompatibilities between old- and new-style classes has been
removed: you can now assign to the [`__name__`](https://docs.python.org/3/reference/datamodel.html#type.__name__ "type.__name__") and [`__bases__`](https://docs.python.org/3/reference/datamodel.html#type.__bases__ "type.__bases__")
attributes of new-style classes. There are some restrictions on what can be
assigned to `__bases__` along the lines of those relating to assigning to
an instance’s [`__class__`](https://docs.python.org/3/reference/datamodel.html#object.__class__ "object.__class__") attribute.


### String Changes [¶](https://docs.python.org/3/whatsnew/2.3.html\#string-changes "Link to this heading")

- The [`in`](https://docs.python.org/3/reference/expressions.html#in) operator now works differently for strings. Previously, when
evaluating `X in Y` where _X_ and _Y_ are strings, _X_ could only be a single
character. That’s now changed; _X_ can be a string of any length, and `X in Y`
will return [`True`](https://docs.python.org/3/library/constants.html#True "True") if _X_ is a substring of _Y_. If _X_ is the empty
string, the result is always [`True`](https://docs.python.org/3/library/constants.html#True "True").



Copy

```
>>> 'ab' in 'abcd'
True
>>> 'ad' in 'abcd'
False
>>> '' in 'abcd'
True
```





Note that this doesn’t tell you where the substring starts; if you need that
information, use the [`find()`](https://docs.python.org/3/library/stdtypes.html#str.find "str.find") string method.

- The [`strip()`](https://docs.python.org/3/library/stdtypes.html#str.strip "str.strip"), [`lstrip()`](https://docs.python.org/3/library/stdtypes.html#str.lstrip "str.lstrip"), and [`rstrip()`](https://docs.python.org/3/library/stdtypes.html#str.rstrip "str.rstrip") string methods now have
an optional argument for specifying the characters to strip. The default is
still to remove all whitespace characters:



Copy

```
>>> '   abc '.strip()
'abc'
>>> '><><abc<><><>'.strip('<>')
'abc'
>>> '><><abc<><><>\n'.strip('<>')
'abc<><><>\n'
>>> u'\u4000\u4001abc\u4000'.strip(u'\u4000')
u'\u4001abc'
>>>
```





(Suggested by Simon Brunning and implemented by Walter Dörwald.)

- The [`startswith()`](https://docs.python.org/3/library/stdtypes.html#str.startswith "str.startswith") and [`endswith()`](https://docs.python.org/3/library/stdtypes.html#str.endswith "str.endswith") string methods now accept negative
numbers for the _start_ and _end_ parameters.

- Another new string method is [`zfill()`](https://docs.python.org/3/library/stdtypes.html#str.zfill "str.zfill"), originally a function in the
[`string`](https://docs.python.org/3/library/string.html#module-string "string: Common string operations.") module. [`zfill()`](https://docs.python.org/3/library/stdtypes.html#str.zfill "str.zfill") pads a numeric string with zeros on the
left until it’s the specified width. Note that the `%` operator is still more
flexible and powerful than [`zfill()`](https://docs.python.org/3/library/stdtypes.html#str.zfill "str.zfill").



Copy

```
>>> '45'.zfill(4)
'0045'
>>> '12345'.zfill(4)
'12345'
>>> 'goofy'.zfill(6)
'0goofy'
```





(Contributed by Walter Dörwald.)

- A new type object, `basestring`, has been added. Both 8-bit strings and
Unicode strings inherit from this type, so `isinstance(obj, basestring)` will
return [`True`](https://docs.python.org/3/library/constants.html#True "True") for either kind of string. It’s a completely abstract
type, so you can’t create `basestring` instances.

- Interned strings are no longer immortal and will now be garbage-collected in
the usual way when the only reference to them is from the internal dictionary of
interned strings. (Implemented by Oren Tirosh.)


### Optimizations [¶](https://docs.python.org/3/whatsnew/2.3.html\#optimizations "Link to this heading")

- The creation of new-style class instances has been made much faster; they’re
now faster than classic classes!

- The [`sort()`](https://docs.python.org/3/library/stdtypes.html#list.sort "list.sort") method of list objects has been extensively rewritten by Tim
Peters, and the implementation is significantly faster.

- Multiplication of large long integers is now much faster thanks to an
implementation of Karatsuba multiplication, an algorithm that scales better than
the _O_( _n_ 2) required for the grade-school multiplication algorithm. (Original
patch by Christopher A. Craig, and significantly reworked by Tim Peters.)

- The `SET_LINENO` opcode is now gone. This may provide a small speed
increase, depending on your compiler’s idiosyncrasies. See section
[Other Changes and Fixes](https://docs.python.org/3/whatsnew/2.3.html#section-other) for a longer explanation. (Removed by Michael Hudson.)

- `xrange()` objects now have their own iterator, making `for i in
xrange(n)` slightly faster than `for i in range(n)`. (Patch by Raymond
Hettinger.)

- A number of small rearrangements have been made in various hotspots to improve
performance, such as inlining a function or removing some code. (Implemented
mostly by GvR, but lots of people have contributed single changes.)


The net result of the 2.3 optimizations is that Python 2.3 runs the pystone
benchmark around 25% faster than Python 2.2.

## New, Improved, and Deprecated Modules [¶](https://docs.python.org/3/whatsnew/2.3.html\#new-improved-and-deprecated-modules "Link to this heading")

As usual, Python’s standard library received a number of enhancements and bug
fixes. Here’s a partial list of the most notable changes, sorted alphabetically
by module name. Consult the `Misc/NEWS` file in the source tree for a more
complete list of changes, or look through the CVS logs for all the details.

- The [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.") module now supports arrays of Unicode characters using the
`'u'` format character. Arrays also now support using the `+=` assignment
operator to add another array’s contents, and the `*=` assignment operator to
repeat an array. (Contributed by Jason Orendorff.)

- The `bsddb` module has been replaced by version 4.1.6 of the [PyBSDDB](https://pybsddb.sourceforge.net/) package, providing a more complete interface
to the transactional features of the BerkeleyDB library.

The old version of the module has been renamed to `bsddb185` and is no
longer built automatically; you’ll have to edit `Modules/Setup` to enable
it. Note that the new `bsddb` package is intended to be compatible with
the old module, so be sure to file bugs if you discover any incompatibilities.
When upgrading to Python 2.3, if the new interpreter is compiled with a new
version of the underlying BerkeleyDB library, you will almost certainly have to
convert your database files to the new version. You can do this fairly easily
with the new scripts `db2pickle.py` and `pickle2db.py` which you
will find in the distribution’s `Tools/scripts` directory. If you’ve
already been using the PyBSDDB package and importing it as `bsddb3`, you
will have to change your `import` statements to import it as `bsddb`.

- The new [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") module is an interface to the bz2 data compression library.
bz2-compressed data is usually smaller than corresponding
[`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")-compressed data. (Contributed by Gustavo Niemeyer.)

- A set of standard date/time types has been added in the new [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
module. See the following section for more details.

- The Distutils `Extension` class now supports an extra constructor
argument named _depends_ for listing additional source files that an extension
depends on. This lets Distutils recompile the module if any of the dependency
files are modified. For example, if `sampmodule.c` includes the header
file `sample.h`, you would create the `Extension` object like
this:



Copy

```
ext = Extension("samp",
                  sources=["sampmodule.c"],
                  depends=["sample.h"])
```





Modifying `sample.h` would then cause the module to be recompiled.
(Contributed by Jeremy Hylton.)

- Other minor changes to Distutils: it now checks for the [`CC`](https://docs.python.org/3/using/configure.html#envvar-CC),
[`CFLAGS`](https://docs.python.org/3/using/configure.html#envvar-CFLAGS), `CPP`, [`LDFLAGS`](https://docs.python.org/3/using/configure.html#envvar-LDFLAGS), and [`CPPFLAGS`](https://docs.python.org/3/using/configure.html#envvar-CPPFLAGS)
environment variables, using them to override the settings in Python’s
configuration (contributed by Robert Weber).

- Previously the [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") module would only search the docstrings of
public methods and functions for test cases, but it now also examines private
ones as well. The [`DocTestSuite()`](https://docs.python.org/3/library/doctest.html#doctest.DocTestSuite "doctest.DocTestSuite") function creates a
[`unittest.TestSuite`](https://docs.python.org/3/library/unittest.html#unittest.TestSuite "unittest.TestSuite") object from a set of [`doctest`](https://docs.python.org/3/library/doctest.html#module-doctest "doctest: Test pieces of code within docstrings.") tests.

- The new `gc.get_referents(object)` function returns a list of all the
objects referenced by _object_.

- The [`getopt`](https://docs.python.org/3/library/getopt.html#module-getopt "getopt: Portable parser for command line options; support both short and long option names.") module gained a new function, [`gnu_getopt()`](https://docs.python.org/3/library/getopt.html#getopt.gnu_getopt "getopt.gnu_getopt"), that
supports the same arguments as the existing [`getopt()`](https://docs.python.org/3/library/getopt.html#getopt.getopt "getopt.getopt") function but uses
GNU-style scanning mode. The existing [`getopt()`](https://docs.python.org/3/library/getopt.html#getopt.getopt "getopt.getopt") stops processing options as
soon as a non-option argument is encountered, but in GNU-style mode processing
continues, meaning that options and arguments can be mixed. For example:



Copy

```
>>> getopt.getopt(['-f', 'filename', 'output', '-v'], 'f:v')
([('-f', 'filename')], ['output', '-v'])
>>> getopt.gnu_getopt(['-f', 'filename', 'output', '-v'], 'f:v')
([('-f', 'filename'), ('-v', '')], ['output'])
```





(Contributed by Peter Åstrand.)

- The [`grp`](https://docs.python.org/3/library/grp.html#module-grp "grp: The group database (getgrnam() and friends). (Unix)"), [`pwd`](https://docs.python.org/3/library/pwd.html#module-pwd "pwd: The password database (getpwnam() and friends). (Unix)"), and [`resource`](https://docs.python.org/3/library/resource.html#module-resource "resource: An interface to provide resource usage information on the current process. (Unix)") modules now return enhanced
tuples:



Copy

```
>>> import grp
>>> g = grp.getgrnam('amk')
>>> g.gr_name, g.gr_gid
('amk', 500)
```

- The [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.") module can now handle files exceeding 2 GiB.

- The new [`heapq`](https://docs.python.org/3/library/heapq.html#module-heapq "heapq: Heap queue algorithm (a.k.a. priority queue).") module contains an implementation of a heap queue
algorithm. A heap is an array-like data structure that keeps items in a
partially sorted order such that, for every index _k_, `heap[k] <=
heap[2*k+1]` and `heap[k] <= heap[2*k+2]`. This makes it quick to remove the
smallest item, and inserting a new item while maintaining the heap property is
_O_(log _n_). (See [https://xlinux.nist.gov/dads//HTML/priorityque.html](https://xlinux.nist.gov/dads//HTML/priorityque.html) for more
information about the priority queue data structure.)

The [`heapq`](https://docs.python.org/3/library/heapq.html#module-heapq "heapq: Heap queue algorithm (a.k.a. priority queue).") module provides [`heappush()`](https://docs.python.org/3/library/heapq.html#heapq.heappush "heapq.heappush") and [`heappop()`](https://docs.python.org/3/library/heapq.html#heapq.heappop "heapq.heappop") functions
for adding and removing items while maintaining the heap property on top of some
other mutable Python sequence type. Here’s an example that uses a Python list:



Copy

```
>>> import heapq
>>> heap = []
>>> for item in [3, 7, 5, 11, 1]:
...    heapq.heappush(heap, item)
...
>>> heap
[1, 3, 5, 11, 7]
>>> heapq.heappop(heap)
1
>>> heapq.heappop(heap)
3
>>> heap
[5, 7, 11]
```





(Contributed by Kevin O’Connor.)

- The IDLE integrated development environment has been updated using the code
from the IDLEfork project ( [https://idlefork.sourceforge.net](https://idlefork.sourceforge.net/)). The most notable feature is
that the code being developed is now executed in a subprocess, meaning that
there’s no longer any need for manual `reload()` operations. IDLE’s core code
has been incorporated into the standard library as the [`idlelib`](https://docs.python.org/3/library/idle.html#module-idlelib "idlelib: Implementation package for the IDLE shell/editor.") package.

- The [`imaplib`](https://docs.python.org/3/library/imaplib.html#module-imaplib "imaplib: IMAP4 protocol client (requires sockets).") module now supports IMAP over SSL. (Contributed by Piers
Lauder and Tino Lange.)

- The [`itertools`](https://docs.python.org/3/library/itertools.html#module-itertools "itertools: Functions creating iterators for efficient looping.") contains a number of useful functions for use with
iterators, inspired by various functions provided by the ML and Haskell
languages. For example, `itertools.ifilter(predicate, iterator)` returns all
elements in the iterator for which the function `predicate()` returns
[`True`](https://docs.python.org/3/library/constants.html#True "True"), and `itertools.repeat(obj, N)` returns `obj` _N_ times.
There are a number of other functions in the module; see the package’s reference
documentation for details.
(Contributed by Raymond Hettinger.)

- Two new functions in the [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).") module, `degrees(rads)` and
`radians(degs)`, convert between radians and degrees. Other functions in
the [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.).") module such as [`math.sin()`](https://docs.python.org/3/library/math.html#math.sin "math.sin") and [`math.cos()`](https://docs.python.org/3/library/math.html#math.cos "math.cos") have always
required input values measured in radians. Also, an optional _base_ argument
was added to [`math.log()`](https://docs.python.org/3/library/math.html#math.log "math.log") to make it easier to compute logarithms for bases
other than `e` and `10`. (Contributed by Raymond Hettinger.)

- Several new POSIX functions (`getpgid()`, `killpg()`, `lchown()`,
`loadavg()`, `major()`, `makedev()`, `minor()`, and
`mknod()`) were added to the [`posix`](https://docs.python.org/3/library/posix.html#module-posix "posix: The most common POSIX system calls (normally used via module os). (Unix)") module that underlies the
[`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") module. (Contributed by Gustavo Niemeyer, Geert Jansen, and Denis S.
Otkidach.)

- In the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") module, the `*stat()` family of functions can now report
fractions of a second in a timestamp. Such time stamps are represented as
floats, similar to the value returned by [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time").

During testing, it was found that some applications will break if time stamps
are floats. For compatibility, when using the tuple interface of the
[`stat_result`](https://docs.python.org/3/library/os.html#os.stat_result "os.stat_result") time stamps will be represented as integers. When using
named fields (a feature first introduced in Python 2.2), time stamps are still
represented as integers, unless `os.stat_float_times()` is invoked to enable
float return values:



Copy

```
>>> os.stat("/tmp").st_mtime
1034791200
>>> os.stat_float_times(True)
>>> os.stat("/tmp").st_mtime
1034791200.6335014
```





In Python 2.4, the default will change to always returning floats.

Application developers should enable this feature only if all their libraries
work properly when confronted with floating-point time stamps, or if they use
the tuple API. If used, the feature should be activated on an application level
instead of trying to enable it on a per-use basis.

- The [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.") module contains a new parser for command-line arguments
that can convert option values to a particular Python type and will
automatically generate a usage message. See the following section for more
details.

- The old and never-documented `linuxaudiodev` module has been deprecated,
and a new version named `ossaudiodev` has been added. The module was
renamed because the OSS sound drivers can be used on platforms other than Linux,
and the interface has also been tidied and brought up to date in various ways.
(Contributed by Greg Ward and Nicholas FitzRoy-Dale.)

- The new [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible.") module contains a number of functions that try to
determine various properties of the platform you’re running on. There are
functions for getting the architecture, CPU type, the Windows OS version, and
even the Linux distribution version. (Contributed by Marc-André Lemburg.)

- The parser objects provided by the [`pyexpat`](https://docs.python.org/3/library/pyexpat.html#module-xml.parsers.expat "xml.parsers.expat: An interface to the Expat non-validating XML parser.") module can now optionally
buffer character data, resulting in fewer calls to your character data handler
and therefore faster performance. Setting the parser object’s
[`buffer_text`](https://docs.python.org/3/library/pyexpat.html#xml.parsers.expat.xmlparser.buffer_text "xml.parsers.expat.xmlparser.buffer_text") attribute to [`True`](https://docs.python.org/3/library/constants.html#True "True") will enable buffering.

- The `sample(population, k)` function was added to the [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.")
module. _population_ is a sequence or `xrange` object containing the
elements of a population, and [`sample()`](https://docs.python.org/3/library/random.html#random.sample "random.sample") chooses _k_ elements from the
population without replacing chosen elements. _k_ can be any value up to
`len(population)`. For example:



Copy

```
>>> days = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'St', 'Sn']
>>> random.sample(days, 3)      # Choose 3 elements
['St', 'Sn', 'Th']
>>> random.sample(days, 7)      # Choose 7 elements
['Tu', 'Th', 'Mo', 'We', 'St', 'Fr', 'Sn']
>>> random.sample(days, 7)      # Choose 7 again
['We', 'Mo', 'Sn', 'Fr', 'Tu', 'St', 'Th']
>>> random.sample(days, 8)      # Can't choose eight
Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    File "random.py", line 414, in sample
        raise ValueError, "sample larger than population"
ValueError: sample larger than population
>>> random.sample(xrange(1,10000,2), 10)   # Choose ten odd nos. under 10000
[3407, 3805, 1505, 7023, 2401, 2267, 9733, 3151, 8083, 9195]
```





The [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") module now uses a new algorithm, the Mersenne Twister,
implemented in C. It’s faster and more extensively studied than the previous
algorithm.

(All changes contributed by Raymond Hettinger.)

- The [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python. (Unix)") module also gained a number of new functions:
[`get_history_item()`](https://docs.python.org/3/library/readline.html#readline.get_history_item "readline.get_history_item"), [`get_current_history_length()`](https://docs.python.org/3/library/readline.html#readline.get_current_history_length "readline.get_current_history_length"), and
[`redisplay()`](https://docs.python.org/3/library/readline.html#readline.redisplay "readline.redisplay").

- The `rexec` and `Bastion` modules have been declared dead, and
attempts to import them will fail with a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError"). New-style classes
provide new ways to break out of the restricted execution environment provided
by `rexec`, and no one has interest in fixing them or time to do so. If
you have applications using `rexec`, rewrite them to use something else.

(Sticking with Python 2.2 or 2.1 will not make your applications any safer
because there are known bugs in the `rexec` module in those versions. To
repeat: if you’re using `rexec`, stop using it immediately.)

- The `rotor` module has been deprecated because the algorithm it uses for
encryption is not believed to be secure. If you need encryption, use one of the
several AES Python modules that are available separately.

- The [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying.") module gained a `move(src, dest)` function that
recursively moves a file or directory to a new location.

- Support for more advanced POSIX signal handling was added to the [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.")
but then removed again as it proved impossible to make it work reliably across
platforms.

- The [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") module now supports timeouts. You can call the
`settimeout(t)` method on a socket object to set a timeout of _t_ seconds.
Subsequent socket operations that take longer than _t_ seconds to complete will
abort and raise a [`socket.timeout`](https://docs.python.org/3/library/socket.html#socket.timeout "socket.timeout") exception.

The original timeout implementation was by Tim O’Malley. Michael Gilfix
integrated it into the Python [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") module and shepherded it through a
lengthy review. After the code was checked in, Guido van Rossum rewrote parts
of it. (This is a good example of a collaborative development process in
action.)

- On Windows, the [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") module now ships with Secure Sockets Layer
(SSL) support.

- The value of the C `PYTHON_API_VERSION` macro is now exposed at the
Python level as `sys.api_version`. The current exception can be cleared by
calling the new `sys.exc_clear()` function.

- The new [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files.") module allows reading from and writing to
**tar**-format archive files. (Contributed by Lars Gustäbel.)

- The new [`textwrap`](https://docs.python.org/3/library/textwrap.html#module-textwrap "textwrap: Text wrapping and filling") module contains functions for wrapping strings
containing paragraphs of text. The `wrap(text, width)` function takes a
string and returns a list containing the text split into lines of no more than
the chosen width. The `fill(text, width)` function returns a single
string, reformatted to fit into lines no longer than the chosen width. (As you
can guess, [`fill()`](https://docs.python.org/3/library/textwrap.html#textwrap.fill "textwrap.fill") is built on top of [`wrap()`](https://docs.python.org/3/library/textwrap.html#textwrap.wrap "textwrap.wrap"). For example:



Copy

```
>>> import textwrap
>>> paragraph = "Not a whit, we defy augury: ... more text ..."
>>> textwrap.wrap(paragraph, 60)
["Not a whit, we defy augury: there's a special providence in",\
"the fall of a sparrow. If it be now, 'tis not to come; if it",\
...]
>>> print textwrap.fill(paragraph, 35)
Not a whit, we defy augury: there's
a special providence in the fall of
a sparrow. If it be now, 'tis not
to come; if it be not to come, it
will be now; if it be not now, yet
it will come: the readiness is all.
>>>
```





The module also contains a [`TextWrapper`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "textwrap.TextWrapper") class that actually implements
the text wrapping strategy. Both the [`TextWrapper`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "textwrap.TextWrapper") class and the
[`wrap()`](https://docs.python.org/3/library/textwrap.html#textwrap.wrap "textwrap.wrap") and [`fill()`](https://docs.python.org/3/library/textwrap.html#textwrap.fill "textwrap.fill") functions support a number of additional keyword
arguments for fine-tuning the formatting; consult the module’s documentation
for details. (Contributed by Greg Ward.)

- The `thread` and [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.") modules now have companion modules,
`dummy_thread` and `dummy_threading`, that provide a do-nothing
implementation of the `thread` module’s interface for platforms where
threads are not supported. The intention is to simplify thread-aware modules
(ones that _don’t_ rely on threads to run) by putting the following code at the
top:



Copy

```
try:
      import threading as _threading
except ImportError:
      import dummy_threading as _threading
```





In this example, `_threading` is used as the module name to make it clear
that the module being used is not necessarily the actual [`threading`](https://docs.python.org/3/library/threading.html#module-threading "threading: Thread-based parallelism.")
module. Code can call functions and use classes in `_threading` whether or
not threads are supported, avoiding an [`if`](https://docs.python.org/3/reference/compound_stmts.html#if) statement and making the
code slightly clearer. This module will not magically make multithreaded code
run without threads; code that waits for another thread to return or to do
something will simply hang forever.

- The [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.") module’s [`strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime") function has long been an annoyance
because it uses the platform C library’s [`strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime") implementation, and
different platforms sometimes have odd bugs. Brett Cannon contributed a
portable implementation that’s written in pure Python and should behave
identically on all platforms.

- The new [`timeit`](https://docs.python.org/3/library/timeit.html#module-timeit "timeit: Measure the execution time of small code snippets.") module helps measure how long snippets of Python code
take to execute. The `timeit.py` file can be run directly from the
command line, or the module’s [`Timer`](https://docs.python.org/3/library/timeit.html#timeit.Timer "timeit.Timer") class can be imported and used
directly. Here’s a short example that figures out whether it’s faster to
convert an 8-bit string to Unicode by appending an empty Unicode string to it or
by using the `unicode()` function:



Copy

```
import timeit

timer1 = timeit.Timer('unicode("abc")')
timer2 = timeit.Timer('"abc" + u""')

# Run three trials
print timer1.repeat(repeat=3, number=100000)
print timer2.repeat(repeat=3, number=100000)

# On my laptop this outputs:
# [0.36831796169281006, 0.37441694736480713, 0.35304892063140869]
# [0.17574405670166016, 0.18193507194519043, 0.17565798759460449]
```

- The `Tix` module has received various bug fixes and updates for the
current version of the Tix package.

- The `Tkinter` module now works with a thread-enabled version of Tcl.
Tcl’s threading model requires that widgets only be accessed from the thread in
which they’re created; accesses from another thread can cause Tcl to panic. For
certain Tcl interfaces, `Tkinter` will now automatically avoid this when a
widget is accessed from a different thread by marshalling a command, passing it
to the correct thread, and waiting for the results. Other interfaces can’t be
handled automatically but `Tkinter` will now raise an exception on such an
access so that you can at least find out about the problem. See
[https://mail.python.org/pipermail/python-dev/2002-December/031107.html](https://mail.python.org/pipermail/python-dev/2002-December/031107.html) for a more
detailed explanation of this change. (Implemented by Martin von Löwis.)

- Calling Tcl methods through `_tkinter` no longer returns only strings.
Instead, if Tcl returns other objects those objects are converted to their
Python equivalent, if one exists, or wrapped with a `_tkinter.Tcl_Obj`
object if no Python equivalent exists. This behavior can be controlled through
the `wantobjects()` method of `tkapp` objects.

When using `_tkinter` through the `Tkinter` module (as most Tkinter
applications will), this feature is always activated. It should not cause
compatibility problems, since Tkinter would always convert string results to
Python types where possible.

If any incompatibilities are found, the old behavior can be restored by setting
the `wantobjects` variable in the `Tkinter` module to false before
creating the first `tkapp` object.



Copy

```
import Tkinter
Tkinter.wantobjects = 0
```





Any breakage caused by this change should be reported as a bug.

- The `UserDict` module has a new `DictMixin` class which defines
all dictionary methods for classes that already have a minimum mapping
interface. This greatly simplifies writing classes that need to be
substitutable for dictionaries, such as the classes in the [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.")
module.

Adding the mix-in as a superclass provides the full dictionary interface
whenever the class defines [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__"), [`__setitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__setitem__ "object.__setitem__"),
[`__delitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__delitem__ "object.__delitem__"), and `keys()`. For example:



Copy

```
>>> import UserDict
>>> class SeqDict(UserDict.DictMixin):
...     """Dictionary lookalike implemented with lists."""
...     def __init__(self):
...         self.keylist = []
...         self.valuelist = []
...     def __getitem__(self, key):
...         try:
...             i = self.keylist.index(key)
...         except ValueError:
...             raise KeyError
...         return self.valuelist[i]
...     def __setitem__(self, key, value):
...         try:
...             i = self.keylist.index(key)
...             self.valuelist[i] = value
...         except ValueError:
...             self.keylist.append(key)
...             self.valuelist.append(value)
...     def __delitem__(self, key):
...         try:
...             i = self.keylist.index(key)
...         except ValueError:
...             raise KeyError
...         self.keylist.pop(i)
...         self.valuelist.pop(i)
...     def keys(self):
...         return list(self.keylist)
...
>>> s = SeqDict()
>>> dir(s)      # See that other dictionary methods are implemented
['__cmp__', '__contains__', '__delitem__', '__doc__', '__getitem__',\
'__init__', '__iter__', '__len__', '__module__', '__repr__',\
'__setitem__', 'clear', 'get', 'has_key', 'items', 'iteritems',\
'iterkeys', 'itervalues', 'keylist', 'keys', 'pop', 'popitem',\
'setdefault', 'update', 'valuelist', 'values']
```





(Contributed by Raymond Hettinger.)

- The DOM implementation in [`xml.dom.minidom`](https://docs.python.org/3/library/xml.dom.minidom.html#module-xml.dom.minidom "xml.dom.minidom: Minimal Document Object Model (DOM) implementation.") can now generate XML output
in a particular encoding by providing an optional encoding argument to the
[`toxml()`](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.Node.toxml "xml.dom.minidom.Node.toxml") and [`toprettyxml()`](https://docs.python.org/3/library/xml.dom.minidom.html#xml.dom.minidom.Node.toprettyxml "xml.dom.minidom.Node.toprettyxml") methods of DOM nodes.

- The `xmlrpclib` module now supports an XML-RPC extension for handling nil
data values such as Python’s `None`. Nil values are always supported on
unmarshalling an XML-RPC response. To generate requests containing `None`,
you must supply a true value for the _allow\_none_ parameter when creating a
`Marshaller` instance.

- The new `DocXMLRPCServer` module allows writing self-documenting XML-RPC
servers. Run it in demo mode (as a program) to see it in action. Pointing the
web browser to the RPC server produces pydoc-style documentation; pointing
xmlrpclib to the server allows invoking the actual methods. (Contributed by
Brian Quinlan.)

- Support for internationalized domain names (RFCs 3454, 3490, 3491, and 3492)
has been added. The “idna” encoding can be used to convert between a Unicode
domain name and the ASCII-compatible encoding (ACE) of that name.



Copy

```
>{}>{}> u"www.Alliancefrançaise.nu".encode("idna")
'www.xn--alliancefranaise-npb.nu'
```





The [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") module has also been extended to transparently convert
Unicode hostnames to the ACE version before passing them to the C library.
Modules that deal with hostnames such as `httplib` and [`ftplib`](https://docs.python.org/3/library/ftplib.html#module-ftplib "ftplib: FTP protocol client (requires sockets)."))
also support Unicode host names; `httplib` also sends HTTP `Host`
headers using the ACE version of the domain name. [`urllib`](https://docs.python.org/3/library/urllib.html#module-urllib "urllib") supports
Unicode URLs with non-ASCII host names as long as the `path` part of the URL
is ASCII only.

To implement this change, the [`stringprep`](https://docs.python.org/3/library/stringprep.html#module-stringprep "stringprep: String preparation, as per RFC 3453") module, the `mkstringprep`
tool and the `punycode` encoding have been added.


### Date/Time Type [¶](https://docs.python.org/3/whatsnew/2.3.html\#date-time-type "Link to this heading")

Date and time types suitable for expressing timestamps were added as the
[`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.") module. The types don’t support different calendars or many
fancy features, and just stick to the basics of representing time.

The three primary types are: [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date"), representing a day, month, and year;
[`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time"), consisting of hour, minute, and second; and [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime"),
which contains all the attributes of both [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") and [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time").
There’s also a [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") class representing differences between two
points in time, and time zone logic is implemented by classes inheriting from
the abstract [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") class.

You can create instances of [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") and [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") by either supplying
keyword arguments to the appropriate constructor, e.g.
`datetime.date(year=1972, month=10, day=15)`, or by using one of a number of
class methods. For example, the [`today()`](https://docs.python.org/3/library/datetime.html#datetime.date.today "datetime.date.today") class method returns the
current local date.

Once created, instances of the date/time classes are all immutable. There are a
number of methods for producing formatted strings from objects:

Copy

```
>>> import datetime
>>> now = datetime.datetime.now()
>>> now.isoformat()
'2002-12-30T21:27:03.994956'
>>> now.ctime()  # Only available on date, datetime
'Mon Dec 30 21:27:03 2002'
>>> now.strftime('%Y %d %b')
'2002 30 Dec'
```

The [`replace()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.replace "datetime.datetime.replace") method allows modifying one or more fields of a
[`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") or [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") instance, returning a new instance:

Copy

```
>>> d = datetime.datetime.now()
>>> d
datetime.datetime(2002, 12, 30, 22, 15, 38, 827738)
>>> d.replace(year=2001, hour = 12)
datetime.datetime(2001, 12, 30, 12, 15, 38, 827738)
>>>
```

Instances can be compared, hashed, and converted to strings (the result is the
same as that of [`isoformat()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.isoformat "datetime.datetime.isoformat")). [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") and [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
instances can be subtracted from each other, and added to [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
instances. The largest missing feature is that there’s no standard library
support for parsing strings and getting back a [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") or
[`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime").

For more information, refer to the module’s reference documentation.
(Contributed by Tim Peters.)

### The optparse Module [¶](https://docs.python.org/3/whatsnew/2.3.html\#the-optparse-module "Link to this heading")

The [`getopt`](https://docs.python.org/3/library/getopt.html#module-getopt "getopt: Portable parser for command line options; support both short and long option names.") module provides simple parsing of command-line arguments. The
new [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.") module (originally named Optik) provides more elaborate
command-line parsing that follows the Unix conventions, automatically creates
the output for `--help`, and can perform different actions for different
options.

You start by creating an instance of [`OptionParser`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "optparse.OptionParser") and telling it what
your program’s options are.

Copy

```
import sys
from optparse import OptionParser

op = OptionParser()
op.add_option('-i', '--input',
              action='store', type='string', dest='input',
              help='set input filename')
op.add_option('-l', '--length',
              action='store', type='int', dest='length',
              help='set maximum length of output')
```

Parsing a command line is then done by calling the [`parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args") method.

Copy

```
options, args = op.parse_args(sys.argv[1:])
print options
print args
```

This returns an object containing all of the option values, and a list of
strings containing the remaining arguments.

Invoking the script with the various arguments now works as you’d expect it to.
Note that the length argument is automatically converted to an integer.

```
$ ./python opt.py -i data arg1
<Values at 0x400cad4c: {'input': 'data', 'length': None}>
['arg1']
$ ./python opt.py --input=data --length=4
<Values at 0x400cad2c: {'input': 'data', 'length': 4}>
[]
$
```

The help message is automatically generated for you:

```
$ ./python opt.py --help
usage: opt.py [options]

options:
  -h, --help            show this help message and exit
  -iINPUT, --input=INPUT
                        set input filename
  -lLENGTH, --length=LENGTH
                        set maximum length of output
$
```

See the module’s documentation for more details.

Optik was written by Greg Ward, with suggestions from the readers of the Getopt
SIG.

## Pymalloc: A Specialized Object Allocator [¶](https://docs.python.org/3/whatsnew/2.3.html\#pymalloc-a-specialized-object-allocator "Link to this heading")

Pymalloc, a specialized object allocator written by Vladimir Marangozov, was a
feature added to Python 2.1. Pymalloc is intended to be faster than the system
`malloc()` and to have less memory overhead for allocation patterns typical
of Python programs. The allocator uses C’s `malloc()` function to get large
pools of memory and then fulfills smaller memory requests from these pools.

In 2.1 and 2.2, pymalloc was an experimental feature and wasn’t enabled by
default; you had to explicitly enable it when compiling Python by providing the
`--with-pymalloc` option to the **configure** script. In 2.3,
pymalloc has had further enhancements and is now enabled by default; you’ll have
to supply `--without-pymalloc` to disable it.

This change is transparent to code written in Python; however, pymalloc may
expose bugs in C extensions. Authors of C extension modules should test their
code with pymalloc enabled, because some incorrect code may cause core dumps at
runtime.

There’s one particularly common error that causes problems. There are a number
of memory allocation functions in Python’s C API that have previously just been
aliases for the C library’s `malloc()` and `free()`, meaning that if
you accidentally called mismatched functions the error wouldn’t be noticeable.
When the object allocator is enabled, these functions aren’t aliases of
`malloc()` and `free()` any more, and calling the wrong function to
free memory may get you a core dump. For example, if memory was allocated using
[`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc"), it has to be freed using [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free"), not
`free()`. A few modules included with Python fell afoul of this and had to
be fixed; doubtless there are more third-party modules that will have the same
problem.

As part of this change, the confusing multiple interfaces for allocating memory
have been consolidated down into two API families. Memory allocated with one
family must not be manipulated with functions from the other family. There is
one family for allocating chunks of memory and another family of functions
specifically for allocating Python objects.

- To allocate and free an undistinguished chunk of memory use the “raw memory”
family: [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc"), [`PyMem_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Realloc "PyMem_Realloc"), and [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free").

- The “object memory” family is the interface to the pymalloc facility described
above and is biased towards a large number of “small” allocations:
[`PyObject_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Malloc "PyObject_Malloc"), [`PyObject_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Realloc "PyObject_Realloc"), and [`PyObject_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyObject_Free "PyObject_Free").

- To allocate and free Python objects, use the “object” family
[`PyObject_New`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "PyObject_New"), [`PyObject_NewVar`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "PyObject_NewVar"), and [`PyObject_Del()`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_Del "PyObject_Del").


Thanks to lots of work by Tim Peters, pymalloc in 2.3 also provides debugging
features to catch memory overwrites and doubled frees in both extension modules
and in the interpreter itself. To enable this support, compile a debugging
version of the Python interpreter by running **configure** with
`--with-pydebug`.

To aid extension writers, a header file `Misc/pymemcompat.h` is
distributed with the source to Python 2.3 that allows Python extensions to use
the 2.3 interfaces to memory allocation while compiling against any version of
Python since 1.5.2. You would copy the file from Python’s source distribution
and bundle it with the source of your extension.

See also

[https://hg.python.org/cpython/file/default/Objects/obmalloc.c](https://hg.python.org/cpython/file/default/Objects/obmalloc.c)

For the full details of the pymalloc implementation, see the comments at
the top of the file `Objects/obmalloc.c` in the Python source code.
The above link points to the file within the python.org SVN browser.

## Build and C API Changes [¶](https://docs.python.org/3/whatsnew/2.3.html\#build-and-c-api-changes "Link to this heading")

Changes to Python’s build process and to the C API include:

- The cycle detection implementation used by the garbage collection has proven
to be stable, so it’s now been made mandatory. You can no longer compile Python
without it, and the `--with-cycle-gc` switch to **configure** has
been removed.

- Python can now optionally be built as a shared library
(`libpython2.3.so`) by supplying `--enable-shared` when running
Python’s **configure** script. (Contributed by Ondrej Palkovsky.)

- The `DL_EXPORT` and `DL_IMPORT` macros are now deprecated.
Initialization functions for Python extension modules should now be declared
using the new macro [`PyMODINIT_FUNC`](https://docs.python.org/3/c-api/extension-modules.html#c.PyMODINIT_FUNC "PyMODINIT_FUNC"), while the Python core will
generally use the `PyAPI_FUNC` and `PyAPI_DATA` macros.

- The interpreter can be compiled without any docstrings for the built-in
functions and modules by supplying `--without-doc-strings` to the
**configure** script. This makes the Python executable about 10% smaller,
but will also mean that you can’t get help for Python’s built-ins. (Contributed
by Gustavo Niemeyer.)

- The `PyArg_NoArgs()` macro is now deprecated, and code that uses it
should be changed. For Python 2.2 and later, the method definition table can
specify the [`METH_NOARGS`](https://docs.python.org/3/c-api/structures.html#c.METH_NOARGS "METH_NOARGS") flag, signalling that there are no arguments,
and the argument checking can then be removed. If compatibility with pre-2.2
versions of Python is important, the code could use `PyArg_ParseTuple(args,
"")` instead, but this will be slower than using [`METH_NOARGS`](https://docs.python.org/3/c-api/structures.html#c.METH_NOARGS "METH_NOARGS").

- [`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple") accepts new format characters for various sizes of
unsigned integers: `B` for unsignedchar, `H` for unsignedshortint, `I` for unsignedint, and `K` for unsignedlonglong.

- A new function, `PyObject_DelItemString(mapping, char *key)` was added
as shorthand for `PyObject_DelItem(mapping, PyString_New(key))`.

- File objects now manage their internal string buffer differently, increasing
it exponentially when needed. This results in the benchmark tests in
`Lib/test/test_bufio.py` speeding up considerably (from 57 seconds to 1.7
seconds, according to one measurement).

- It’s now possible to define class and static methods for a C extension type by
setting either the [`METH_CLASS`](https://docs.python.org/3/c-api/structures.html#c.METH_CLASS "METH_CLASS") or [`METH_STATIC`](https://docs.python.org/3/c-api/structures.html#c.METH_STATIC "METH_STATIC") flags in a
method’s [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef") structure.

- Python now includes a copy of the Expat XML parser’s source code, removing any
dependence on a system version or local installation of Expat.

- If you dynamically allocate type objects in your extension, you should be
aware of a change in the rules relating to the [`__module__`](https://docs.python.org/3/reference/datamodel.html#type.__module__ "type.__module__") and
[`__name__`](https://docs.python.org/3/reference/datamodel.html#type.__name__ "type.__name__") attributes. In summary, you will want to ensure the type’s
dictionary contains a `'__module__'` key; making the module name the part of
the type name leading up to the final period will no longer have the desired
effect. For more detail, read the API reference documentation or the source.


### Port-Specific Changes [¶](https://docs.python.org/3/whatsnew/2.3.html\#port-specific-changes "Link to this heading")

Support for a port to IBM’s OS/2 using the EMX runtime environment was merged
into the main Python source tree. EMX is a POSIX emulation layer over the OS/2
system APIs. The Python port for EMX tries to support all the POSIX-like
capability exposed by the EMX runtime, and mostly succeeds; `fork()` and
[`fcntl()`](https://docs.python.org/3/library/fcntl.html#module-fcntl "fcntl: The fcntl() and ioctl() system calls. (Unix)") are restricted by the limitations of the underlying emulation
layer. The standard OS/2 port, which uses IBM’s Visual Age compiler, also
gained support for case-sensitive import semantics as part of the integration of
the EMX port into CVS. (Contributed by Andrew MacIntyre.)

On MacOS, most toolbox modules have been weaklinked to improve backward
compatibility. This means that modules will no longer fail to load if a single
routine is missing on the current OS version. Instead calling the missing
routine will raise an exception. (Contributed by Jack Jansen.)

The RPM spec files, found in the `Misc/RPM/` directory in the Python
source distribution, were updated for 2.3. (Contributed by Sean Reifschneider.)

Other new platforms now supported by Python include AtheOS
( [http://www.atheos.cx/](http://www.atheos.cx/)), GNU/Hurd, and OpenVMS.

## Other Changes and Fixes [¶](https://docs.python.org/3/whatsnew/2.3.html\#other-changes-and-fixes "Link to this heading")

As usual, there were a bunch of other improvements and bugfixes scattered
throughout the source tree. A search through the CVS change logs finds there
were 523 patches applied and 514 bugs fixed between Python 2.2 and 2.3. Both
figures are likely to be underestimates.

Some of the more notable changes are:

- If the [`PYTHONINSPECT`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONINSPECT) environment variable is set, the Python
interpreter will enter the interactive prompt after running a Python program, as
if Python had been invoked with the [`-i`](https://docs.python.org/3/using/cmdline.html#cmdoption-i) option. The environment
variable can be set before running the Python interpreter, or it can be set by
the Python program as part of its execution.

- The `regrtest.py` script now provides a way to allow “all resources
except _foo_.” A resource name passed to the `-u` option can now be
prefixed with a hyphen (`'-'`) to mean “remove this resource.” For example,
the option ‘`-uall,-bsddb`’ could be used to enable the use of all resources
except `bsddb`.

- The tools used to build the documentation now work under Cygwin as well as
Unix.

- The `SET_LINENO` opcode has been removed. Back in the mists of time, this
opcode was needed to produce line numbers in tracebacks and support trace
functions (for, e.g., [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.")). Since Python 1.5, the line numbers in
tracebacks have been computed using a different mechanism that works with
“python -O”. For Python 2.3 Michael Hudson implemented a similar scheme to
determine when to call the trace function, removing the need for `SET_LINENO`
entirely.

It would be difficult to detect any resulting difference from Python code, apart
from a slight speed up when Python is run without [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O).

C extensions that access the [`f_lineno`](https://docs.python.org/3/reference/datamodel.html#frame.f_lineno "frame.f_lineno") field of frame objects should
instead call `PyCode_Addr2Line(f->f_code, f->f_lasti)`. This will have the
added effect of making the code work as desired under “python -O” in earlier
versions of Python.

A nifty new feature is that trace functions can now assign to the
[`f_lineno`](https://docs.python.org/3/reference/datamodel.html#frame.f_lineno "frame.f_lineno") attribute of frame objects, changing the line that will be
executed next. A `jump` command has been added to the [`pdb`](https://docs.python.org/3/library/pdb.html#module-pdb "pdb: The Python debugger for interactive interpreters.") debugger
taking advantage of this new feature. (Implemented by Richie Hindle.)


## Porting to Python 2.3 [¶](https://docs.python.org/3/whatsnew/2.3.html\#porting-to-python-2-3 "Link to this heading")

This section lists previously described changes that may require changes to your
code:

- [`yield`](https://docs.python.org/3/reference/simple_stmts.html#yield) is now always a keyword; if it’s used as a variable name in
your code, a different name must be chosen.

- For strings _X_ and _Y_, `X in Y` now works if _X_ is more than one
character long.

- The [`int()`](https://docs.python.org/3/library/functions.html#int "int") type constructor will now return a long integer instead of
raising an [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") when a string or floating-point number is too
large to fit into an integer.

- If you have Unicode strings that contain 8-bit characters, you must declare
the file’s encoding (UTF-8, Latin-1, or whatever) by adding a comment to the top
of the file. See section [PEP 263: Source Code Encodings](https://docs.python.org/3/whatsnew/2.3.html#section-encodings) for more information.

- Calling Tcl methods through `_tkinter` no longer returns only strings.
Instead, if Tcl returns other objects those objects are converted to their
Python equivalent, if one exists, or wrapped with a `_tkinter.Tcl_Obj`
object if no Python equivalent exists.

- Large octal and hex literals such as `0xffffffff` now trigger a
[`FutureWarning`](https://docs.python.org/3/library/exceptions.html#FutureWarning "FutureWarning"). Currently they’re stored as 32-bit numbers and result in a
negative value, but in Python 2.4 they’ll become positive long integers.

There are a few ways to fix this warning. If you really need a positive number,
just add an `L` to the end of the literal. If you’re trying to get a 32-bit
integer with low bits set and have previously used an expression such as `~(1
<< 31)`, it’s probably clearest to start with all bits set and clear the
desired upper bits. For example, to clear just the top bit (bit 31), you could
write `0xffffffffL &~(1L<<31)`.

- You can no longer disable assertions by assigning to `__debug__`.

- The Distutils `setup()` function has gained various new keyword arguments
such as _depends_. Old versions of the Distutils will abort if passed unknown
keywords. A solution is to check for the presence of the new
`get_distutil_options()` function in your `setup.py` and only uses the
new keywords with a version of the Distutils that supports them:



Copy

```
from distutils import core

kw = {'sources': 'foo.c', ...}
if hasattr(core, 'get_distutil_options'):
      kw['depends'] = ['foo.h']
ext = Extension(**kw)
```

- Using `None` as a variable name will now result in a [`SyntaxWarning`](https://docs.python.org/3/library/exceptions.html#SyntaxWarning "SyntaxWarning")
warning.

- Names of extension types defined by the modules included with Python now
contain the module and a `'.'` in front of the type name.


## Acknowledgements [¶](https://docs.python.org/3/whatsnew/2.3.html\#acknowledgements "Link to this heading")

The author would like to thank the following people for offering suggestions,
corrections and assistance with various drafts of this article: Jeff Bauer,
Simon Brunning, Brett Cannon, Michael Chermside, Andrew Dalke, Scott David
Daniels, Fred L. Drake, Jr., David Fraser, Kelly Gerber, Raymond Hettinger,
Michael Hudson, Chris Lambert, Detlef Lannert, Martin von Löwis, Andrew
MacIntyre, Lalo Martins, Chad Netzer, Gustavo Niemeyer, Neal Norwitz, Hans
Nowak, Chris Reedy, Francesco Ricciardi, Vinay Sajip, Neil Schemenauer, Roman
Suzi, Jason Tishler, Just van Rossum.

### [Table of Contents](https://docs.python.org/3/contents.html)

- [What’s New in Python 2.3](https://docs.python.org/3/whatsnew/2.3.html#)
  - [PEP 218: A Standard Set Datatype](https://docs.python.org/3/whatsnew/2.3.html#pep-218-a-standard-set-datatype)
  - [PEP 255: Simple Generators](https://docs.python.org/3/whatsnew/2.3.html#pep-255-simple-generators)
  - [PEP 263: Source Code Encodings](https://docs.python.org/3/whatsnew/2.3.html#pep-263-source-code-encodings)
  - [PEP 273: Importing Modules from ZIP Archives](https://docs.python.org/3/whatsnew/2.3.html#pep-273-importing-modules-from-zip-archives)
  - [PEP 277: Unicode file name support for Windows NT](https://docs.python.org/3/whatsnew/2.3.html#pep-277-unicode-file-name-support-for-windows-nt)
  - [PEP 278: Universal Newline Support](https://docs.python.org/3/whatsnew/2.3.html#pep-278-universal-newline-support)
  - [PEP 279: enumerate()](https://docs.python.org/3/whatsnew/2.3.html#pep-279-enumerate)
  - [PEP 282: The logging Package](https://docs.python.org/3/whatsnew/2.3.html#pep-282-the-logging-package)
  - [PEP 285: A Boolean Type](https://docs.python.org/3/whatsnew/2.3.html#pep-285-a-boolean-type)
  - [PEP 293: Codec Error Handling Callbacks](https://docs.python.org/3/whatsnew/2.3.html#pep-293-codec-error-handling-callbacks)
  - [PEP 301: Package Index and Metadata for Distutils](https://docs.python.org/3/whatsnew/2.3.html#pep-301-package-index-and-metadata-for-distutils)
  - [PEP 302: New Import Hooks](https://docs.python.org/3/whatsnew/2.3.html#pep-302-new-import-hooks)
  - [PEP 305: Comma-separated Files](https://docs.python.org/3/whatsnew/2.3.html#pep-305-comma-separated-files)
  - [PEP 307: Pickle Enhancements](https://docs.python.org/3/whatsnew/2.3.html#pep-307-pickle-enhancements)
  - [Extended Slices](https://docs.python.org/3/whatsnew/2.3.html#extended-slices)
  - [Other Language Changes](https://docs.python.org/3/whatsnew/2.3.html#other-language-changes)
    - [String Changes](https://docs.python.org/3/whatsnew/2.3.html#string-changes)
    - [Optimizations](https://docs.python.org/3/whatsnew/2.3.html#optimizations)
  - [New, Improved, and Deprecated Modules](https://docs.python.org/3/whatsnew/2.3.html#new-improved-and-deprecated-modules)
    - [Date/Time Type](https://docs.python.org/3/whatsnew/2.3.html#date-time-type)
    - [The optparse Module](https://docs.python.org/3/whatsnew/2.3.html#the-optparse-module)
  - [Pymalloc: A Specialized Object Allocator](https://docs.python.org/3/whatsnew/2.3.html#pymalloc-a-specialized-object-allocator)
  - [Build and C API Changes](https://docs.python.org/3/whatsnew/2.3.html#build-and-c-api-changes)
    - [Port-Specific Changes](https://docs.python.org/3/whatsnew/2.3.html#port-specific-changes)
  - [Other Changes and Fixes](https://docs.python.org/3/whatsnew/2.3.html#other-changes-and-fixes)
  - [Porting to Python 2.3](https://docs.python.org/3/whatsnew/2.3.html#porting-to-python-2-3)
  - [Acknowledgements](https://docs.python.org/3/whatsnew/2.3.html#acknowledgements)

#### Previous topic

[What’s New in Python 2.4](https://docs.python.org/3/whatsnew/2.4.html "previous chapter")

#### Next topic

[What’s New in Python 2.2](https://docs.python.org/3/whatsnew/2.2.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/whatsnew/2.3.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/whatsnew/2.2.html "What’s New in Python 2.2") \|
- [previous](https://docs.python.org/3/whatsnew/2.4.html "What’s New in Python 2.4") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [What’s New in Python](https://docs.python.org/3/whatsnew/index.html) »
- [What’s New in Python 2.3](https://docs.python.org/3/whatsnew/2.3.html)
- \|

- Theme
AutoLightDark \|