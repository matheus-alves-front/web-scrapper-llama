### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/whatsnew/3.8.html "What’s New In Python 3.8") \|
- [previous](https://docs.python.org/3/whatsnew/3.10.html "What’s New In Python 3.10") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [What’s New in Python](https://docs.python.org/3/whatsnew/index.html) »
- [What’s New In Python 3.9](https://docs.python.org/3/whatsnew/3.9.html)
- \|

- Theme
AutoLightDark \|

# What’s New In Python 3.9 [¶](https://docs.python.org/3/whatsnew/3.9.html\#what-s-new-in-python-3-9 "Link to this heading")

Editor:

Łukasz Langa

This article explains the new features in Python 3.9, compared to 3.8.
Python 3.9 was released on October 5, 2020.
For full details, see the [changelog](https://docs.python.org/3/whatsnew/changelog.html#changelog).

See also

[**PEP 596**](https://peps.python.org/pep-0596/) \- Python 3.9 Release Schedule

## Summary – Release highlights [¶](https://docs.python.org/3/whatsnew/3.9.html\#summary-release-highlights "Link to this heading")

New syntax features:

- [**PEP 584**](https://peps.python.org/pep-0584/), union operators added to `dict`;

- [**PEP 585**](https://peps.python.org/pep-0585/), type hinting generics in standard collections;

- [**PEP 614**](https://peps.python.org/pep-0614/), relaxed grammar restrictions on decorators.


New built-in features:

- [**PEP 616**](https://peps.python.org/pep-0616/), string methods to remove prefixes and suffixes.


New features in the standard library:

- [**PEP 593**](https://peps.python.org/pep-0593/), flexible function and variable annotations;

- [`os.pidfd_open()`](https://docs.python.org/3/library/os.html#os.pidfd_open "os.pidfd_open") added that allows process management without races
and signals.


Interpreter improvements:

- [**PEP 573**](https://peps.python.org/pep-0573/), fast access to module state from methods of C extension
types;

- [**PEP 617**](https://peps.python.org/pep-0617/), CPython now uses a new parser based on PEG;

- a number of Python builtins (range, tuple, set, frozenset, list, dict) are
now sped up using [**PEP 590**](https://peps.python.org/pep-0590/) vectorcall;

- garbage collection does not block on resurrected objects;

- a number of Python modules (`_abc`, `audioop`, `_bz2`,
`_codecs`, `_contextvars`, `_crypt`, `_functools`,
`_json`, `_locale`, [`math`](https://docs.python.org/3/library/math.html#module-math "math: Mathematical functions (sin() etc.)."), [`operator`](https://docs.python.org/3/library/operator.html#module-operator "operator: Functions corresponding to the standard operators."), [`resource`](https://docs.python.org/3/library/resource.html#module-resource "resource: An interface to provide resource usage information on the current process. (Unix)"),
[`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions."), `_weakref`) now use multiphase initialization as defined
by PEP 489;

- a number of standard library modules (`audioop`, [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation."), [`grp`](https://docs.python.org/3/library/grp.html#module-grp "grp: The group database (getgrnam() and friends). (Unix)"),
`_hashlib`, [`pwd`](https://docs.python.org/3/library/pwd.html#module-pwd "pwd: The password database (getpwnam() and friends). (Unix)"), `_posixsubprocess`, [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions."),
[`select`](https://docs.python.org/3/library/select.html#module-select "select: Wait for I/O completion on multiple streams."), [`struct`](https://docs.python.org/3/library/struct.html#module-struct "struct: Interpret bytes as packed binary data."), [`termios`](https://docs.python.org/3/library/termios.html#module-termios "termios: POSIX style tty control. (Unix)"), [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")) are now using
the stable ABI defined by PEP 384.


New library modules:

- [**PEP 615**](https://peps.python.org/pep-0615/), the IANA Time Zone Database is now present in the standard
library in the [`zoneinfo`](https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo "zoneinfo: IANA time zone support") module;

- an implementation of a topological sort of a graph is now provided in
the new [`graphlib`](https://docs.python.org/3/library/graphlib.html#module-graphlib "graphlib: Functionality to operate with graph-like structures") module.


Release process changes:

- [**PEP 602**](https://peps.python.org/pep-0602/), CPython adopts an annual release cycle.


## You should check for DeprecationWarning in your code [¶](https://docs.python.org/3/whatsnew/3.9.html\#you-should-check-for-deprecationwarning-in-your-code "Link to this heading")

When Python 2.7 was still supported, a lot of functionality in Python 3
was kept for backward compatibility with Python 2.7. With the end of Python
2 support, these backward compatibility layers have been removed, or will
be removed soon. Most of them emitted a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") warning for
several years. For example, using `collections.Mapping` instead of
`collections.abc.Mapping` emits a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") since Python
3.3, released in 2012.

Test your application with the [`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W)`default` command-line option to see
[`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") and [`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning"), or even with
[`-W`](https://docs.python.org/3/using/cmdline.html#cmdoption-W)`error` to treat them as errors. [Warnings Filter](https://docs.python.org/3/library/warnings.html#warning-filter) can be used to ignore warnings from third-party code.

Python 3.9 is the last version providing those Python 2 backward compatibility
layers, to give more time to Python projects maintainers to organize the
removal of the Python 2 support and add support for Python 3.9.

Aliases to [Abstract Base Classes](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes) in
the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes") module, like `collections.Mapping` alias to
[`collections.abc.Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping"), are kept for one last release for backward
compatibility. They will be removed from Python 3.10.

More generally, try to run your tests in the [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode) which helps to prepare your code to make it compatible with the
next Python version.

Note: a number of pre-existing deprecations were removed in this version of
Python as well. Consult the [Removed](https://docs.python.org/3/whatsnew/3.9.html#removed-in-python-39) section.

## New Features [¶](https://docs.python.org/3/whatsnew/3.9.html\#new-features "Link to this heading")

### Dictionary Merge & Update Operators [¶](https://docs.python.org/3/whatsnew/3.9.html\#dictionary-merge-update-operators "Link to this heading")

Merge (`|`) and update (`|=`) operators have been added to the built-in
[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") class. Those complement the existing `dict.update` and
`{**d1, **d2}` methods of merging dictionaries.

Example:

Copy

```
>>> x = {"key1": "value1 from x", "key2": "value2 from x"}
>>> y = {"key2": "value2 from y", "key3": "value3 from y"}
>>> x | y
{'key1': 'value1 from x', 'key2': 'value2 from y', 'key3': 'value3 from y'}
>>> y | x
{'key2': 'value2 from x', 'key3': 'value3 from y', 'key1': 'value1 from x'}
```

See [**PEP 584**](https://peps.python.org/pep-0584/) for a full description.
(Contributed by Brandt Bucher in [bpo-36144](https://bugs.python.org/issue?@action=redirect&bpo=36144).)

### New String Methods to Remove Prefixes and Suffixes [¶](https://docs.python.org/3/whatsnew/3.9.html\#new-string-methods-to-remove-prefixes-and-suffixes "Link to this heading")

[`str.removeprefix(prefix)`](https://docs.python.org/3/library/stdtypes.html#str.removeprefix "str.removeprefix") and
[`str.removesuffix(suffix)`](https://docs.python.org/3/library/stdtypes.html#str.removesuffix "str.removesuffix") have been added
to easily remove an unneeded prefix or a suffix from a string. Corresponding
`bytes`, `bytearray`, and `collections.UserString` methods have also been
added. See [**PEP 616**](https://peps.python.org/pep-0616/) for a full description. (Contributed by Dennis Sweeney in
[bpo-39939](https://bugs.python.org/issue?@action=redirect&bpo=39939).)

### Type Hinting Generics in Standard Collections [¶](https://docs.python.org/3/whatsnew/3.9.html\#type-hinting-generics-in-standard-collections "Link to this heading")

In type annotations you can now use built-in collection types such as
`list` and `dict` as generic types instead of importing the
corresponding capitalized types (e.g. `List` or `Dict`) from
`typing`. Some other types in the standard library are also now generic,
for example `queue.Queue`.

Example:

Copy

```
def greet_all(names: list[str]) -> None:
    for name in names:
        print("Hello", name)
```

See [**PEP 585**](https://peps.python.org/pep-0585/) for more details. (Contributed by Guido van Rossum,
Ethan Smith, and Batuhan Taşkaya in [bpo-39481](https://bugs.python.org/issue?@action=redirect&bpo=39481).)

### New Parser [¶](https://docs.python.org/3/whatsnew/3.9.html\#new-parser "Link to this heading")

Python 3.9 uses a new parser, based on [PEG](https://en.wikipedia.org/wiki/Parsing_expression_grammar) instead
of [LL(1)](https://en.wikipedia.org/wiki/LL_parser). The new
parser’s performance is roughly comparable to that of the old parser,
but the PEG formalism is more flexible than LL(1) when it comes to
designing new language features. We’ll start using this flexibility
in Python 3.10 and later.

The [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.") module uses the new parser and produces the same AST as
the old parser.

In Python 3.10, the old parser will be deleted and so will all
functionality that depends on it (primarily the `parser` module,
which has long been deprecated). In Python 3.9 _only_, you can switch
back to the LL(1) parser using a command line switch (`-X
oldparser`) or an environment variable (`PYTHONOLDPARSER=1`).

See [**PEP 617**](https://peps.python.org/pep-0617/) for more details. (Contributed by Guido van Rossum,
Pablo Galindo and Lysandros Nikolaou in [bpo-40334](https://bugs.python.org/issue?@action=redirect&bpo=40334).)

## Other Language Changes [¶](https://docs.python.org/3/whatsnew/3.9.html\#other-language-changes "Link to this heading")

- [`__import__()`](https://docs.python.org/3/library/functions.html#import__ "__import__") now raises [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") instead of
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"), which used to occur when a relative import went past
its top-level package.
(Contributed by Ngalim Siregar in [bpo-37444](https://bugs.python.org/issue?@action=redirect&bpo=37444).)

- Python now gets the absolute path of the script filename specified on
the command line (ex: `python3 script.py`): the `__file__` attribute of
the [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") module became an absolute path, rather than a relative
path. These paths now remain valid after the current directory is changed
by [`os.chdir()`](https://docs.python.org/3/library/os.html#os.chdir "os.chdir"). As a side effect, the traceback also displays the
absolute path for [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.") module frames in this case.
(Contributed by Victor Stinner in [bpo-20443](https://bugs.python.org/issue?@action=redirect&bpo=20443).)

- In the [Python Development Mode](https://docs.python.org/3/library/devmode.html#devmode) and in [debug build](https://docs.python.org/3/using/configure.html#debug-build), the
_encoding_ and _errors_ arguments are now checked for string encoding and
decoding operations. Examples: [`open()`](https://docs.python.org/3/library/functions.html#open "open"), [`str.encode()`](https://docs.python.org/3/library/stdtypes.html#str.encode "str.encode") and
[`bytes.decode()`](https://docs.python.org/3/library/stdtypes.html#bytes.decode "bytes.decode").

By default, for best performance, the _errors_ argument is only checked at
the first encoding/decoding error and the _encoding_ argument is sometimes
ignored for empty strings.
(Contributed by Victor Stinner in [bpo-37388](https://bugs.python.org/issue?@action=redirect&bpo=37388).)

- `"".replace("", s, n)` now returns `s` instead of an empty string for
all non-zero `n`. It is now consistent with `"".replace("", s)`.
There are similar changes for [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") objects.
(Contributed by Serhiy Storchaka in [bpo-28029](https://bugs.python.org/issue?@action=redirect&bpo=28029).)

- Any valid expression can now be used as a [decorator](https://docs.python.org/3/glossary.html#term-decorator). Previously, the
grammar was much more restrictive. See [**PEP 614**](https://peps.python.org/pep-0614/) for details.
(Contributed by Brandt Bucher in [bpo-39702](https://bugs.python.org/issue?@action=redirect&bpo=39702).)

- Improved help for the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") module. Docstrings are now shown for
all special forms and special generic aliases (like `Union` and `List`).
Using [`help()`](https://docs.python.org/3/library/functions.html#help "help") with generic alias like `List[int]` will show the help
for the correspondent concrete type (`list` in this case).
(Contributed by Serhiy Storchaka in [bpo-40257](https://bugs.python.org/issue?@action=redirect&bpo=40257).)

- Parallel running of [`aclose()`](https://docs.python.org/3/reference/expressions.html#agen.aclose "agen.aclose") / [`asend()`](https://docs.python.org/3/reference/expressions.html#agen.asend "agen.asend") /
[`athrow()`](https://docs.python.org/3/reference/expressions.html#agen.athrow "agen.athrow") is now prohibited, and `ag_running` now reflects
the actual running status of the async generator.
(Contributed by Yury Selivanov in [bpo-30773](https://bugs.python.org/issue?@action=redirect&bpo=30773).)

- Unexpected errors in calling the `__iter__` method are no longer masked by
`TypeError` in the [`in`](https://docs.python.org/3/reference/expressions.html#in) operator and functions
[`contains()`](https://docs.python.org/3/library/operator.html#operator.contains "operator.contains"), [`indexOf()`](https://docs.python.org/3/library/operator.html#operator.indexOf "operator.indexOf") and
[`countOf()`](https://docs.python.org/3/library/operator.html#operator.countOf "operator.countOf") of the [`operator`](https://docs.python.org/3/library/operator.html#module-operator "operator: Functions corresponding to the standard operators.") module.
(Contributed by Serhiy Storchaka in [bpo-40824](https://bugs.python.org/issue?@action=redirect&bpo=40824).)

- Unparenthesized lambda expressions can no longer be the expression part in an
`if` clause in comprehensions and generator expressions. See [bpo-41848](https://bugs.python.org/issue?@action=redirect&bpo=41848)
and [bpo-43755](https://bugs.python.org/issue?@action=redirect&bpo=43755) for details.


## New Modules [¶](https://docs.python.org/3/whatsnew/3.9.html\#new-modules "Link to this heading")

### zoneinfo [¶](https://docs.python.org/3/whatsnew/3.9.html\#zoneinfo "Link to this heading")

The [`zoneinfo`](https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo "zoneinfo: IANA time zone support") module brings support for the IANA time zone database to
the standard library. It adds [`zoneinfo.ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo"), a concrete
[`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") implementation backed by the system’s time zone data.

Example:

Copy

```
>>> from zoneinfo import ZoneInfo
>>> from datetime import datetime, timedelta

>>> # Daylight saving time
>>> dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
>>> print(dt)
2020-10-31 12:00:00-07:00
>>> dt.tzname()
'PDT'

>>> # Standard time
>>> dt += timedelta(days=7)
>>> print(dt)
2020-11-07 12:00:00-08:00
>>> print(dt.tzname())
PST
```

As a fall-back source of data for platforms that don’t ship the IANA database,
the [tzdata](https://pypi.org/project/tzdata/) module was released as a first-party package – distributed via
PyPI and maintained by the CPython core team.

See also

[**PEP 615**](https://peps.python.org/pep-0615/) – Support for the IANA Time Zone Database in the Standard Library

PEP written and implemented by Paul Ganssle

### graphlib [¶](https://docs.python.org/3/whatsnew/3.9.html\#graphlib "Link to this heading")

A new module, [`graphlib`](https://docs.python.org/3/library/graphlib.html#module-graphlib "graphlib: Functionality to operate with graph-like structures"), was added that contains the
[`graphlib.TopologicalSorter`](https://docs.python.org/3/library/graphlib.html#graphlib.TopologicalSorter "graphlib.TopologicalSorter") class to offer functionality to perform
topological sorting of graphs. (Contributed by Pablo Galindo, Tim Peters and
Larry Hastings in [bpo-17005](https://bugs.python.org/issue?@action=redirect&bpo=17005).)

## Improved Modules [¶](https://docs.python.org/3/whatsnew/3.9.html\#improved-modules "Link to this heading")

### ast [¶](https://docs.python.org/3/whatsnew/3.9.html\#ast "Link to this heading")

Added the _indent_ option to [`dump()`](https://docs.python.org/3/library/ast.html#ast.dump "ast.dump") which allows it to produce a
multiline indented output.
(Contributed by Serhiy Storchaka in [bpo-37995](https://bugs.python.org/issue?@action=redirect&bpo=37995).)

Added [`ast.unparse()`](https://docs.python.org/3/library/ast.html#ast.unparse "ast.unparse") as a function in the [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.") module that can
be used to unparse an [`ast.AST`](https://docs.python.org/3/library/ast.html#ast.AST "ast.AST") object and produce a string with code
that would produce an equivalent [`ast.AST`](https://docs.python.org/3/library/ast.html#ast.AST "ast.AST") object when parsed.
(Contributed by Pablo Galindo and Batuhan Taskaya in [bpo-38870](https://bugs.python.org/issue?@action=redirect&bpo=38870).)

Added docstrings to AST nodes that contains the ASDL signature used to
construct that node. (Contributed by Batuhan Taskaya in [bpo-39638](https://bugs.python.org/issue?@action=redirect&bpo=39638).)

### asyncio [¶](https://docs.python.org/3/whatsnew/3.9.html\#asyncio "Link to this heading")

Due to significant security concerns, the _reuse\_address_ parameter of
[`asyncio.loop.create_datagram_endpoint()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_datagram_endpoint "asyncio.loop.create_datagram_endpoint") is no longer supported. This is
because of the behavior of the socket option `SO_REUSEADDR` in UDP. For more
details, see the documentation for `loop.create_datagram_endpoint()`.
(Contributed by Kyle Stanley, Antoine Pitrou, and Yury Selivanov in
[bpo-37228](https://bugs.python.org/issue?@action=redirect&bpo=37228).)

Added a new [coroutine](https://docs.python.org/3/glossary.html#term-coroutine) [`shutdown_default_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.shutdown_default_executor "asyncio.loop.shutdown_default_executor")
that schedules a shutdown for the default executor that waits on the
[`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor") to finish closing. Also,
[`asyncio.run()`](https://docs.python.org/3/library/asyncio-runner.html#asyncio.run "asyncio.run") has been updated to use the new [coroutine](https://docs.python.org/3/glossary.html#term-coroutine).
(Contributed by Kyle Stanley in [bpo-34037](https://bugs.python.org/issue?@action=redirect&bpo=34037).)

Added `asyncio.PidfdChildWatcher`, a Linux-specific child watcher
implementation that polls process file descriptors. ( [bpo-38692](https://bugs.python.org/issue?@action=redirect&bpo=38692))

Added a new [coroutine](https://docs.python.org/3/glossary.html#term-coroutine) [`asyncio.to_thread()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.to_thread "asyncio.to_thread"). It is mainly used for
running IO-bound functions in a separate thread to avoid blocking the event
loop, and essentially works as a high-level version of
[`run_in_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor "asyncio.loop.run_in_executor") that can directly take keyword arguments.
(Contributed by Kyle Stanley and Yury Selivanov in [bpo-32309](https://bugs.python.org/issue?@action=redirect&bpo=32309).)

When cancelling the task due to a timeout, [`asyncio.wait_for()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait_for "asyncio.wait_for") will now
wait until the cancellation is complete also in the case when _timeout_ is
<= 0, like it does with positive timeouts.
(Contributed by Elvis Pranskevichus in [bpo-32751](https://bugs.python.org/issue?@action=redirect&bpo=32751).)

[`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.") now raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") when calling incompatible
methods with an [`ssl.SSLSocket`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket "ssl.SSLSocket") socket.
(Contributed by Ido Michael in [bpo-37404](https://bugs.python.org/issue?@action=redirect&bpo=37404).)

### compileall [¶](https://docs.python.org/3/whatsnew/3.9.html\#compileall "Link to this heading")

Added new possibility to use hardlinks for duplicated `.pyc` files: _hardlink\_dupes_ parameter and –hardlink-dupes command line option.
(Contributed by Lumír ‘Frenzy’ Balhar in [bpo-40495](https://bugs.python.org/issue?@action=redirect&bpo=40495).)

Added new options for path manipulation in resulting `.pyc` files: _stripdir_, _prependdir_, _limit\_sl\_dest_ parameters and -s, -p, -e command line options.
Added the possibility to specify the option for an optimization level multiple times.
(Contributed by Lumír ‘Frenzy’ Balhar in [bpo-38112](https://bugs.python.org/issue?@action=redirect&bpo=38112).)

### concurrent.futures [¶](https://docs.python.org/3/whatsnew/3.9.html\#concurrent-futures "Link to this heading")

Added a new _cancel\_futures_ parameter to
[`concurrent.futures.Executor.shutdown()`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.Executor.shutdown "concurrent.futures.Executor.shutdown") that cancels all pending futures
which have not started running, instead of waiting for them to complete before
shutting down the executor.
(Contributed by Kyle Stanley in [bpo-39349](https://bugs.python.org/issue?@action=redirect&bpo=39349).)

Removed daemon threads from [`ThreadPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor "concurrent.futures.ThreadPoolExecutor")
and [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor"). This improves
compatibility with subinterpreters and predictability in their shutdown
processes. (Contributed by Kyle Stanley in [bpo-39812](https://bugs.python.org/issue?@action=redirect&bpo=39812).)

Workers in [`ProcessPoolExecutor`](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor "concurrent.futures.ProcessPoolExecutor") are now spawned on
demand, only when there are no available idle workers to reuse. This optimizes
startup overhead and reduces the amount of lost CPU time to idle workers.
(Contributed by Kyle Stanley in [bpo-39207](https://bugs.python.org/issue?@action=redirect&bpo=39207).)

### curses [¶](https://docs.python.org/3/whatsnew/3.9.html\#curses "Link to this heading")

Added [`curses.get_escdelay()`](https://docs.python.org/3/library/curses.html#curses.get_escdelay "curses.get_escdelay"), [`curses.set_escdelay()`](https://docs.python.org/3/library/curses.html#curses.set_escdelay "curses.set_escdelay"),
[`curses.get_tabsize()`](https://docs.python.org/3/library/curses.html#curses.get_tabsize "curses.get_tabsize"), and [`curses.set_tabsize()`](https://docs.python.org/3/library/curses.html#curses.set_tabsize "curses.set_tabsize") functions.
(Contributed by Anthony Sottile in [bpo-38312](https://bugs.python.org/issue?@action=redirect&bpo=38312).)

### datetime [¶](https://docs.python.org/3/whatsnew/3.9.html\#datetime "Link to this heading")

The [`isocalendar()`](https://docs.python.org/3/library/datetime.html#datetime.date.isocalendar "datetime.date.isocalendar") of [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date")
and [`isocalendar()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.isocalendar "datetime.datetime.isocalendar") of [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime")
methods now returns a [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") instead of a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple").
(Contributed by Donghee Na in [bpo-24416](https://bugs.python.org/issue?@action=redirect&bpo=24416).)

### distutils [¶](https://docs.python.org/3/whatsnew/3.9.html\#distutils "Link to this heading")

The **upload** command now creates SHA2-256 and Blake2b-256 hash
digests. It skips MD5 on platforms that block MD5 digest.
(Contributed by Christian Heimes in [bpo-40698](https://bugs.python.org/issue?@action=redirect&bpo=40698).)

### fcntl [¶](https://docs.python.org/3/whatsnew/3.9.html\#fcntl "Link to this heading")

Added constants `fcntl.F_OFD_GETLK`, `fcntl.F_OFD_SETLK`
and `fcntl.F_OFD_SETLKW`.
(Contributed by Donghee Na in [bpo-38602](https://bugs.python.org/issue?@action=redirect&bpo=38602).)

### ftplib [¶](https://docs.python.org/3/whatsnew/3.9.html\#ftplib "Link to this heading")

[`FTP`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP "ftplib.FTP") and [`FTP_TLS`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP_TLS "ftplib.FTP_TLS") now raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError")
if the given timeout for their constructor is zero to prevent the creation of
a non-blocking socket. (Contributed by Donghee Na in [bpo-39259](https://bugs.python.org/issue?@action=redirect&bpo=39259).)

### gc [¶](https://docs.python.org/3/whatsnew/3.9.html\#gc "Link to this heading")

When the garbage collector makes a collection in which some objects resurrect
(they are reachable from outside the isolated cycles after the finalizers have
been executed), do not block the collection of all objects that are still
unreachable. (Contributed by Pablo Galindo and Tim Peters in [bpo-38379](https://bugs.python.org/issue?@action=redirect&bpo=38379).)

Added a new function [`gc.is_finalized()`](https://docs.python.org/3/library/gc.html#gc.is_finalized "gc.is_finalized") to check if an object has been
finalized by the garbage collector. (Contributed by Pablo Galindo in
[bpo-39322](https://bugs.python.org/issue?@action=redirect&bpo=39322).)

### hashlib [¶](https://docs.python.org/3/whatsnew/3.9.html\#hashlib "Link to this heading")

The [`hashlib`](https://docs.python.org/3/library/hashlib.html#module-hashlib "hashlib: Secure hash and message digest algorithms.") module can now use SHA3 hashes and SHAKE XOF from OpenSSL
when available.
(Contributed by Christian Heimes in [bpo-37630](https://bugs.python.org/issue?@action=redirect&bpo=37630).)

Builtin hash modules can now be disabled with
`./configure --without-builtin-hashlib-hashes` or selectively enabled with
e.g. `./configure --with-builtin-hashlib-hashes=sha3,blake2` to force use
of OpenSSL based implementation.
(Contributed by Christian Heimes in [bpo-40479](https://bugs.python.org/issue?@action=redirect&bpo=40479))

### http [¶](https://docs.python.org/3/whatsnew/3.9.html\#http "Link to this heading")

HTTP status codes `103 EARLY_HINTS`, `418 IM_A_TEAPOT` and `425 TOO_EARLY` are added to
[`http.HTTPStatus`](https://docs.python.org/3/library/http.html#http.HTTPStatus "http.HTTPStatus"). (Contributed by Donghee Na in [bpo-39509](https://bugs.python.org/issue?@action=redirect&bpo=39509) and Ross Rhodes in [bpo-39507](https://bugs.python.org/issue?@action=redirect&bpo=39507).)

### IDLE and idlelib [¶](https://docs.python.org/3/whatsnew/3.9.html\#idle-and-idlelib "Link to this heading")

Added option to toggle cursor blink off. (Contributed by Zackery Spytz
in [bpo-4603](https://bugs.python.org/issue?@action=redirect&bpo=4603).)

Escape key now closes IDLE completion windows. (Contributed by Johnny
Najera in [bpo-38944](https://bugs.python.org/issue?@action=redirect&bpo=38944).)

Added keywords to module name completion list. (Contributed by Terry J.
Reedy in [bpo-37765](https://bugs.python.org/issue?@action=redirect&bpo=37765).)

New in 3.9 maintenance releases

Make IDLE invoke [`sys.excepthook()`](https://docs.python.org/3/library/sys.html#sys.excepthook "sys.excepthook") (when started without ‘-n’).
User hooks were previously ignored. (Contributed by Ken Hilton in
[bpo-43008](https://bugs.python.org/issue?@action=redirect&bpo=43008).)

The changes above have been backported to 3.8 maintenance releases.

Rearrange the settings dialog. Split the General tab into Windows
and Shell/Ed tabs. Move help sources, which extend the Help menu, to the
Extensions tab. Make space for new options and shorten the dialog. The
latter makes the dialog better fit small screens. (Contributed by Terry Jan
Reedy in [bpo-40468](https://bugs.python.org/issue?@action=redirect&bpo=40468).) Move the indent space setting from the Font tab to
the new Windows tab. (Contributed by Mark Roseman and Terry Jan Reedy in
[bpo-33962](https://bugs.python.org/issue?@action=redirect&bpo=33962).)

Apply syntax highlighting to `.pyi` files. (Contributed by Alex
Waygood and Terry Jan Reedy in [bpo-45447](https://bugs.python.org/issue?@action=redirect&bpo=45447).)

### imaplib [¶](https://docs.python.org/3/whatsnew/3.9.html\#imaplib "Link to this heading")

[`IMAP4`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4 "imaplib.IMAP4") and [`IMAP4_SSL`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4_SSL "imaplib.IMAP4_SSL") now have
an optional _timeout_ parameter for their constructors.
Also, the [`open()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.open "imaplib.IMAP4.open") method now has an optional _timeout_ parameter
with this change. The overridden methods of [`IMAP4_SSL`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4_SSL "imaplib.IMAP4_SSL") and
[`IMAP4_stream`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4_stream "imaplib.IMAP4_stream") were applied to this change.
(Contributed by Donghee Na in [bpo-38615](https://bugs.python.org/issue?@action=redirect&bpo=38615).)

[`imaplib.IMAP4.unselect()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.unselect "imaplib.IMAP4.unselect") is added.
[`imaplib.IMAP4.unselect()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.unselect "imaplib.IMAP4.unselect") frees server’s resources associated with the
selected mailbox and returns the server to the authenticated
state. This command performs the same actions as [`imaplib.IMAP4.close()`](https://docs.python.org/3/library/imaplib.html#imaplib.IMAP4.close "imaplib.IMAP4.close"), except
that no messages are permanently removed from the currently
selected mailbox. (Contributed by Donghee Na in [bpo-40375](https://bugs.python.org/issue?@action=redirect&bpo=40375).)

### importlib [¶](https://docs.python.org/3/whatsnew/3.9.html\#importlib "Link to this heading")

To improve consistency with import statements, [`importlib.util.resolve_name()`](https://docs.python.org/3/library/importlib.html#importlib.util.resolve_name "importlib.util.resolve_name")
now raises [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") instead of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") for invalid relative
import attempts.
(Contributed by Ngalim Siregar in [bpo-37444](https://bugs.python.org/issue?@action=redirect&bpo=37444).)

Import loaders which publish immutable module objects can now publish
immutable packages in addition to individual modules.
(Contributed by Dino Viehland in [bpo-39336](https://bugs.python.org/issue?@action=redirect&bpo=39336).)

Added [`importlib.resources.files()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files "importlib.resources.files") function with support for
subdirectories in package data, matching backport in `importlib_resources`
version 1.5.
(Contributed by Jason R. Coombs in [bpo-39791](https://bugs.python.org/issue?@action=redirect&bpo=39791).)

Refreshed `importlib.metadata` from `importlib_metadata` version 1.6.1.

### inspect [¶](https://docs.python.org/3/whatsnew/3.9.html\#inspect "Link to this heading")

[`inspect.BoundArguments.arguments`](https://docs.python.org/3/library/inspect.html#inspect.BoundArguments.arguments "inspect.BoundArguments.arguments") is changed from `OrderedDict` to regular
dict. (Contributed by Inada Naoki in [bpo-36350](https://bugs.python.org/issue?@action=redirect&bpo=36350) and [bpo-39775](https://bugs.python.org/issue?@action=redirect&bpo=39775).)

### ipaddress [¶](https://docs.python.org/3/whatsnew/3.9.html\#ipaddress "Link to this heading")

[`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.") now supports IPv6 Scoped Addresses (IPv6 address with suffix `%<scope_id>`).

Scoped IPv6 addresses can be parsed using [`ipaddress.IPv6Address`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address "ipaddress.IPv6Address").
If present, scope zone ID is available through the [`scope_id`](https://docs.python.org/3/library/ipaddress.html#ipaddress.IPv6Address.scope_id "ipaddress.IPv6Address.scope_id") attribute.
(Contributed by Oleksandr Pavliuk in [bpo-34788](https://bugs.python.org/issue?@action=redirect&bpo=34788).)

Starting with Python 3.9.5 the [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.") module no longer
accepts any leading zeros in IPv4 address strings.
(Contributed by Christian Heimes in [bpo-36384](https://bugs.python.org/issue?@action=redirect&bpo=36384)).

### math [¶](https://docs.python.org/3/whatsnew/3.9.html\#math "Link to this heading")

Expanded the [`math.gcd()`](https://docs.python.org/3/library/math.html#math.gcd "math.gcd") function to handle multiple arguments.
Formerly, it only supported two arguments.
(Contributed by Serhiy Storchaka in [bpo-39648](https://bugs.python.org/issue?@action=redirect&bpo=39648).)

Added [`math.lcm()`](https://docs.python.org/3/library/math.html#math.lcm "math.lcm"): return the least common multiple of specified arguments.
(Contributed by Mark Dickinson, Ananthakrishnan and Serhiy Storchaka in
[bpo-39479](https://bugs.python.org/issue?@action=redirect&bpo=39479) and [bpo-39648](https://bugs.python.org/issue?@action=redirect&bpo=39648).)

Added [`math.nextafter()`](https://docs.python.org/3/library/math.html#math.nextafter "math.nextafter"): return the next floating-point value after _x_
towards _y_.
(Contributed by Victor Stinner in [bpo-39288](https://bugs.python.org/issue?@action=redirect&bpo=39288).)

Added [`math.ulp()`](https://docs.python.org/3/library/math.html#math.ulp "math.ulp"): return the value of the least significant bit
of a float.
(Contributed by Victor Stinner in [bpo-39310](https://bugs.python.org/issue?@action=redirect&bpo=39310).)

### multiprocessing [¶](https://docs.python.org/3/whatsnew/3.9.html\#multiprocessing "Link to this heading")

The [`multiprocessing.SimpleQueue`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.SimpleQueue "multiprocessing.SimpleQueue") class has a new
[`close()`](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.SimpleQueue.close "multiprocessing.SimpleQueue.close") method to explicitly close the
queue.
(Contributed by Victor Stinner in [bpo-30966](https://bugs.python.org/issue?@action=redirect&bpo=30966).)

### nntplib [¶](https://docs.python.org/3/whatsnew/3.9.html\#nntplib "Link to this heading")

`NNTP` and `NNTP_SSL` now raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError")
if the given timeout for their constructor is zero to prevent the creation of
a non-blocking socket. (Contributed by Donghee Na in [bpo-39259](https://bugs.python.org/issue?@action=redirect&bpo=39259).)

### os [¶](https://docs.python.org/3/whatsnew/3.9.html\#os "Link to this heading")

Added [`CLD_KILLED`](https://docs.python.org/3/library/os.html#os.CLD_KILLED "os.CLD_KILLED") and [`CLD_STOPPED`](https://docs.python.org/3/library/os.html#os.CLD_STOPPED "os.CLD_STOPPED") for `si_code`.
(Contributed by Donghee Na in [bpo-38493](https://bugs.python.org/issue?@action=redirect&bpo=38493).)

Exposed the Linux-specific [`os.pidfd_open()`](https://docs.python.org/3/library/os.html#os.pidfd_open "os.pidfd_open") ( [bpo-38692](https://bugs.python.org/issue?@action=redirect&bpo=38692)) and
[`os.P_PIDFD`](https://docs.python.org/3/library/os.html#os.P_PIDFD "os.P_PIDFD") ( [bpo-38713](https://bugs.python.org/issue?@action=redirect&bpo=38713)) for process management with file
descriptors.

The [`os.unsetenv()`](https://docs.python.org/3/library/os.html#os.unsetenv "os.unsetenv") function is now also available on Windows.
(Contributed by Victor Stinner in [bpo-39413](https://bugs.python.org/issue?@action=redirect&bpo=39413).)

The [`os.putenv()`](https://docs.python.org/3/library/os.html#os.putenv "os.putenv") and [`os.unsetenv()`](https://docs.python.org/3/library/os.html#os.unsetenv "os.unsetenv") functions are now always
available.
(Contributed by Victor Stinner in [bpo-39395](https://bugs.python.org/issue?@action=redirect&bpo=39395).)

Added [`os.waitstatus_to_exitcode()`](https://docs.python.org/3/library/os.html#os.waitstatus_to_exitcode "os.waitstatus_to_exitcode") function:
convert a wait status to an exit code.
(Contributed by Victor Stinner in [bpo-40094](https://bugs.python.org/issue?@action=redirect&bpo=40094).)

### pathlib [¶](https://docs.python.org/3/whatsnew/3.9.html\#pathlib "Link to this heading")

Added [`pathlib.Path.readlink()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.readlink "pathlib.Path.readlink") which acts similarly to
[`os.readlink()`](https://docs.python.org/3/library/os.html#os.readlink "os.readlink").
(Contributed by Girts Folkmanis in [bpo-30618](https://bugs.python.org/issue?@action=redirect&bpo=30618))

### pdb [¶](https://docs.python.org/3/whatsnew/3.9.html\#pdb "Link to this heading")

On Windows now [`Pdb`](https://docs.python.org/3/library/pdb.html#pdb.Pdb "pdb.Pdb") supports `~/.pdbrc`.
(Contributed by Tim Hopper and Dan Lidral-Porter in [bpo-20523](https://bugs.python.org/issue?@action=redirect&bpo=20523).)

### poplib [¶](https://docs.python.org/3/whatsnew/3.9.html\#poplib "Link to this heading")

[`POP3`](https://docs.python.org/3/library/poplib.html#poplib.POP3 "poplib.POP3") and [`POP3_SSL`](https://docs.python.org/3/library/poplib.html#poplib.POP3_SSL "poplib.POP3_SSL") now raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError")
if the given timeout for their constructor is zero to prevent the creation of
a non-blocking socket. (Contributed by Donghee Na in [bpo-39259](https://bugs.python.org/issue?@action=redirect&bpo=39259).)

### pprint [¶](https://docs.python.org/3/whatsnew/3.9.html\#pprint "Link to this heading")

[`pprint`](https://docs.python.org/3/library/pprint.html#module-pprint "pprint: Data pretty printer.") can now pretty-print [`types.SimpleNamespace`](https://docs.python.org/3/library/types.html#types.SimpleNamespace "types.SimpleNamespace").
(Contributed by Carl Bordum Hansen in [bpo-37376](https://bugs.python.org/issue?@action=redirect&bpo=37376).)

### pydoc [¶](https://docs.python.org/3/whatsnew/3.9.html\#pydoc "Link to this heading")

The documentation string is now shown not only for class, function,
method etc, but for any object that has its own [`__doc__`](https://docs.python.org/3/library/stdtypes.html#definition.__doc__ "definition.__doc__")
attribute.
(Contributed by Serhiy Storchaka in [bpo-40257](https://bugs.python.org/issue?@action=redirect&bpo=40257).)

### random [¶](https://docs.python.org/3/whatsnew/3.9.html\#random "Link to this heading")

Added a new [`random.Random.randbytes()`](https://docs.python.org/3/library/random.html#random.Random.randbytes "random.Random.randbytes") method: generate random bytes.
(Contributed by Victor Stinner in [bpo-40286](https://bugs.python.org/issue?@action=redirect&bpo=40286).)

### signal [¶](https://docs.python.org/3/whatsnew/3.9.html\#signal "Link to this heading")

Exposed the Linux-specific [`signal.pidfd_send_signal()`](https://docs.python.org/3/library/signal.html#signal.pidfd_send_signal "signal.pidfd_send_signal") for sending to
signals to a process using a file descriptor instead of a pid. ( [bpo-38712](https://bugs.python.org/issue?@action=redirect&bpo=38712))

### smtplib [¶](https://docs.python.org/3/whatsnew/3.9.html\#smtplib "Link to this heading")

[`SMTP`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP "smtplib.SMTP") and [`SMTP_SSL`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP_SSL "smtplib.SMTP_SSL") now raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError")
if the given timeout for their constructor is zero to prevent the creation of
a non-blocking socket. (Contributed by Donghee Na in [bpo-39259](https://bugs.python.org/issue?@action=redirect&bpo=39259).)

[`LMTP`](https://docs.python.org/3/library/smtplib.html#smtplib.LMTP "smtplib.LMTP") constructor now has an optional _timeout_ parameter.
(Contributed by Donghee Na in [bpo-39329](https://bugs.python.org/issue?@action=redirect&bpo=39329).)

### socket [¶](https://docs.python.org/3/whatsnew/3.9.html\#socket "Link to this heading")

The [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") module now exports the [`CAN_RAW_JOIN_FILTERS`](https://docs.python.org/3/library/socket.html#socket.CAN_RAW_JOIN_FILTERS "socket.CAN_RAW_JOIN_FILTERS")
constant on Linux 4.1 and greater.
(Contributed by Stefan Tatschner and Zackery Spytz in [bpo-25780](https://bugs.python.org/issue?@action=redirect&bpo=25780).)

The socket module now supports the [`CAN_J1939`](https://docs.python.org/3/library/socket.html#socket.CAN_J1939 "socket.CAN_J1939") protocol on
platforms that support it. (Contributed by Karl Ding in [bpo-40291](https://bugs.python.org/issue?@action=redirect&bpo=40291).)

The socket module now has the [`socket.send_fds()`](https://docs.python.org/3/library/socket.html#socket.send_fds "socket.send_fds") and
[`socket.recv_fds()`](https://docs.python.org/3/library/socket.html#socket.recv_fds "socket.recv_fds") functions. (Contributed by Joannah Nanjekye, Shinya
Okano and Victor Stinner in [bpo-28724](https://bugs.python.org/issue?@action=redirect&bpo=28724).)

### time [¶](https://docs.python.org/3/whatsnew/3.9.html\#time "Link to this heading")

On AIX, [`thread_time()`](https://docs.python.org/3/library/time.html#time.thread_time "time.thread_time") is now implemented with `thread_cputime()`
which has nanosecond resolution, rather than
`clock_gettime(CLOCK_THREAD_CPUTIME_ID)` which has a resolution of 10 milliseconds.
(Contributed by Batuhan Taskaya in [bpo-40192](https://bugs.python.org/issue?@action=redirect&bpo=40192))

### sys [¶](https://docs.python.org/3/whatsnew/3.9.html\#sys "Link to this heading")

Added a new [`sys.platlibdir`](https://docs.python.org/3/library/sys.html#sys.platlibdir "sys.platlibdir") attribute: name of the platform-specific
library directory. It is used to build the path of standard library and the
paths of installed extension modules. It is equal to `"lib"` on most
platforms. On Fedora and SuSE, it is equal to `"lib64"` on 64-bit platforms.
(Contributed by Jan Matějek, Matěj Cepl, Charalampos Stratakis and Victor Stinner in [bpo-1294959](https://bugs.python.org/issue?@action=redirect&bpo=1294959).)

Previously, [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr") was block-buffered when non-interactive. Now
`stderr` defaults to always being line-buffered.
(Contributed by Jendrik Seipp in [bpo-13601](https://bugs.python.org/issue?@action=redirect&bpo=13601).)

### tracemalloc [¶](https://docs.python.org/3/whatsnew/3.9.html\#tracemalloc "Link to this heading")

Added [`tracemalloc.reset_peak()`](https://docs.python.org/3/library/tracemalloc.html#tracemalloc.reset_peak "tracemalloc.reset_peak") to set the peak size of traced memory
blocks to the current size, to measure the peak of specific pieces of code.
(Contributed by Huon Wilson in [bpo-40630](https://bugs.python.org/issue?@action=redirect&bpo=40630).)

### typing [¶](https://docs.python.org/3/whatsnew/3.9.html\#typing "Link to this heading")

[**PEP 593**](https://peps.python.org/pep-0593/) introduced an [`typing.Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated "typing.Annotated") type to decorate existing
types with context-specific metadata and new `include_extras` parameter to
[`typing.get_type_hints()`](https://docs.python.org/3/library/typing.html#typing.get_type_hints "typing.get_type_hints") to access the metadata at runtime. (Contributed
by Till Varoquaux and Konstantin Kashin.)

### unicodedata [¶](https://docs.python.org/3/whatsnew/3.9.html\#unicodedata "Link to this heading")

The Unicode database has been updated to version 13.0.0. ( [bpo-39926](https://bugs.python.org/issue?@action=redirect&bpo=39926)).

### venv [¶](https://docs.python.org/3/whatsnew/3.9.html\#venv "Link to this heading")

The activation scripts provided by [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.") now all specify their prompt
customization consistently by always using the value specified by
`__VENV_PROMPT__`. Previously some scripts unconditionally used
`__VENV_PROMPT__`, others only if it happened to be set (which was the default
case), and one used `__VENV_NAME__` instead.
(Contributed by Brett Cannon in [bpo-37663](https://bugs.python.org/issue?@action=redirect&bpo=37663).)

### xml [¶](https://docs.python.org/3/whatsnew/3.9.html\#xml "Link to this heading")

White space characters within attributes are now preserved when serializing
[`xml.etree.ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.") to XML file. EOLNs are no longer normalized
to “n”. This is the result of discussion about how to interpret
section 2.11 of XML spec.
(Contributed by Mefistotelis in [bpo-39011](https://bugs.python.org/issue?@action=redirect&bpo=39011).)

## Optimizations [¶](https://docs.python.org/3/whatsnew/3.9.html\#optimizations "Link to this heading")

- Optimized the idiom for assignment a temporary variable in comprehensions.
Now `for y in [expr]` in comprehensions is as fast as a simple assignment
`y = expr`. For example:


> sums = \[s for s in \[0\] for x in data for s in \[s + x\]\]


Unlike the `:=` operator this idiom does not leak a variable to the
outer scope.

(Contributed by Serhiy Storchaka in [bpo-32856](https://bugs.python.org/issue?@action=redirect&bpo=32856).)

- Optimized signal handling in multithreaded applications. If a thread different
than the main thread gets a signal, the bytecode evaluation loop is no longer
interrupted at each bytecode instruction to check for pending signals which
cannot be handled. Only the main thread of the main interpreter can handle
signals.

Previously, the bytecode evaluation loop was interrupted at each instruction
until the main thread handles signals.
(Contributed by Victor Stinner in [bpo-40010](https://bugs.python.org/issue?@action=redirect&bpo=40010).)

- Optimized the [`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") module on FreeBSD using `closefrom()`.
(Contributed by Ed Maste, Conrad Meyer, Kyle Evans, Kubilay Kocak and Victor
Stinner in [bpo-38061](https://bugs.python.org/issue?@action=redirect&bpo=38061).)

- [`PyLong_FromDouble()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromDouble "PyLong_FromDouble") is now up to 1.87x faster for values that
fit into long.
(Contributed by Sergey Fedoseev in [bpo-37986](https://bugs.python.org/issue?@action=redirect&bpo=37986).)

- A number of Python builtins ( [`range`](https://docs.python.org/3/library/stdtypes.html#range "range"), [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"), [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"),
[`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict")) are now sped up by using
[**PEP 590**](https://peps.python.org/pep-0590/) vectorcall protocol.
(Contributed by Donghee Na, Mark Shannon, Jeroen Demeyer and Petr Viktorin in [bpo-37207](https://bugs.python.org/issue?@action=redirect&bpo=37207).)

- Optimized `set.difference_update()` for the case when the other set
is much larger than the base set.
(Suggested by Evgeny Kapun with code contributed by Michele Orrù in [bpo-8425](https://bugs.python.org/issue?@action=redirect&bpo=8425).)

- Python’s small object allocator (`obmalloc.c`) now allows (no more than)
one empty arena to remain available for immediate reuse, without returning
it to the OS. This prevents thrashing in simple loops where an arena could
be created and destroyed anew on each iteration.
(Contributed by Tim Peters in [bpo-37257](https://bugs.python.org/issue?@action=redirect&bpo=37257).)

- [floor division](https://docs.python.org/3/glossary.html#term-floor-division) of float operation now has a better performance. Also
the message of [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError "ZeroDivisionError") for this operation is updated.
(Contributed by Donghee Na in [bpo-39434](https://bugs.python.org/issue?@action=redirect&bpo=39434).)

- Decoding short ASCII strings with UTF-8 and ascii codecs is now about
15% faster. (Contributed by Inada Naoki in [bpo-37348](https://bugs.python.org/issue?@action=redirect&bpo=37348).)


Here’s a summary of performance improvements from Python 3.4 through Python 3.9:

```
Python version                       3.4     3.5     3.6     3.7     3.8    3.9
--------------                       ---     ---     ---     ---     ---    ---

Variable and attribute read access:
    read_local                       7.1     7.1     5.4     5.1     3.9    3.9
    read_nonlocal                    7.1     8.1     5.8     5.4     4.4    4.5
    read_global                     15.5    19.0    14.3    13.6     7.6    7.8
    read_builtin                    21.1    21.6    18.5    19.0     7.5    7.8
    read_classvar_from_class        25.6    26.5    20.7    19.5    18.4   17.9
    read_classvar_from_instance     22.8    23.5    18.8    17.1    16.4   16.9
    read_instancevar                32.4    33.1    28.0    26.3    25.4   25.3
    read_instancevar_slots          27.8    31.3    20.8    20.8    20.2   20.5
    read_namedtuple                 73.8    57.5    45.0    46.8    18.4   18.7
    read_boundmethod                37.6    37.9    29.6    26.9    27.7   41.1

Variable and attribute write access:
    write_local                      8.7     9.3     5.5     5.3     4.3    4.3
    write_nonlocal                  10.5    11.1     5.6     5.5     4.7    4.8
    write_global                    19.7    21.2    18.0    18.0    15.8   16.7
    write_classvar                  92.9    96.0   104.6   102.1    39.2   39.8
    write_instancevar               44.6    45.8    40.0    38.9    35.5   37.4
    write_instancevar_slots         35.6    36.1    27.3    26.6    25.7   25.8

Data structure read access:
    read_list                       24.2    24.5    20.8    20.8    19.0   19.5
    read_deque                      24.7    25.5    20.2    20.6    19.8   20.2
    read_dict                       24.3    25.7    22.3    23.0    21.0   22.4
    read_strdict                    22.6    24.3    19.5    21.2    18.9   21.5

Data structure write access:
    write_list                      27.1    28.5    22.5    21.6    20.0   20.0
    write_deque                     28.7    30.1    22.7    21.8    23.5   21.7
    write_dict                      31.4    33.3    29.3    29.2    24.7   25.4
    write_strdict                   28.4    29.9    27.5    25.2    23.1   24.5

Stack (or queue) operations:
    list_append_pop                 93.4   112.7    75.4    74.2    50.8   50.6
    deque_append_pop                43.5    57.0    49.4    49.2    42.5   44.2
    deque_append_popleft            43.7    57.3    49.7    49.7    42.8   46.4

Timing loop:
    loop_overhead                    0.5     0.6     0.4     0.3     0.3    0.3
```

These results were generated from the variable access benchmark script at:
`Tools/scripts/var_access_benchmark.py`. The benchmark script displays timings
in nanoseconds. The benchmarks were measured on an
[Intel® Core™ i7-4960HQ processor](https://ark.intel.com/content/www/us/en/ark/products/76088/intel-core-i7-4960hq-processor-6m-cache-up-to-3-80-ghz.html)
running the macOS 64-bit builds found at
[python.org](https://www.python.org/downloads/macos/).

## Deprecated [¶](https://docs.python.org/3/whatsnew/3.9.html\#deprecated "Link to this heading")

- The distutils `bdist_msi` command is now deprecated, use
`bdist_wheel` (wheel packages) instead.
(Contributed by Hugo van Kemenade in [bpo-39586](https://bugs.python.org/issue?@action=redirect&bpo=39586).)

- Currently [`math.factorial()`](https://docs.python.org/3/library/math.html#math.factorial "math.factorial") accepts [`float`](https://docs.python.org/3/library/functions.html#float "float") instances with
non-negative integer values (like `5.0`). It raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError")
for non-integral and negative floats. It is now deprecated. In future
Python versions it will raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") for all floats.
(Contributed by Serhiy Storchaka in [bpo-37315](https://bugs.python.org/issue?@action=redirect&bpo=37315).)

- The `parser` and `symbol` modules are deprecated and will be
removed in future versions of Python. For the majority of use cases,
users can leverage the Abstract Syntax Tree (AST) generation and compilation
stage, using the [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.") module.

- The Public C API functions `PyParser_SimpleParseStringFlags()`,
`PyParser_SimpleParseStringFlagsFilename()`,
`PyParser_SimpleParseFileFlags()` and `PyNode_Compile()`
are deprecated and will be removed in Python 3.10 together with the old parser.

- Using [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented") in a boolean context has been deprecated,
as it is almost exclusively the result of incorrect rich comparator
implementations. It will be made a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") in a future version
of Python.
(Contributed by Josh Rosenberg in [bpo-35712](https://bugs.python.org/issue?@action=redirect&bpo=35712).)

- The [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") module currently accepts any hashable type as a
possible seed value. Unfortunately, some of those types are not
guaranteed to have a deterministic hash value. After Python 3.9,
the module will restrict its seeds to [`None`](https://docs.python.org/3/library/constants.html#None "None"), [`int`](https://docs.python.org/3/library/functions.html#int "int"),
[`float`](https://docs.python.org/3/library/functions.html#float "float"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), and [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray").

- Opening the [`GzipFile`](https://docs.python.org/3/library/gzip.html#gzip.GzipFile "gzip.GzipFile") file for writing without specifying
the _mode_ argument is deprecated. In future Python versions it will always
be opened for reading by default. Specify the _mode_ argument for opening
it for writing and silencing a warning.
(Contributed by Serhiy Storchaka in [bpo-28286](https://bugs.python.org/issue?@action=redirect&bpo=28286).)

- Deprecated the `split()` method of `_tkinter.TkappType` in
favour of the `splitlist()` method which has more consistent and
predictable behavior.
(Contributed by Serhiy Storchaka in [bpo-38371](https://bugs.python.org/issue?@action=redirect&bpo=38371).)

- The explicit passing of coroutine objects to [`asyncio.wait()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.wait "asyncio.wait") has been
deprecated and will be removed in version 3.11.
(Contributed by Yury Selivanov and Kyle Stanley in [bpo-34790](https://bugs.python.org/issue?@action=redirect&bpo=34790).)

- binhex4 and hexbin4 standards are now deprecated. The `binhex` module
and the following [`binascii`](https://docs.python.org/3/library/binascii.html#module-binascii "binascii: Tools for converting between binary and various ASCII-encoded binary representations.") functions are now deprecated:


  - `b2a_hqx()`, `a2b_hqx()`

  - `rlecode_hqx()`, `rledecode_hqx()`


(Contributed by Victor Stinner in [bpo-39353](https://bugs.python.org/issue?@action=redirect&bpo=39353).)

- [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.") classes `slice`, `Index` and `ExtSlice` are considered deprecated
and will be removed in future Python versions. `value` itself should be
used instead of `Index(value)`. `Tuple(slices, Load())` should be
used instead of `ExtSlice(slices)`.
(Contributed by Serhiy Storchaka in [bpo-34822](https://bugs.python.org/issue?@action=redirect&bpo=34822).)

- [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.") classes `Suite`, `Param`, `AugLoad` and `AugStore`
are considered deprecated and will be removed in future Python versions.
They were not generated by the parser and not accepted by the code
generator in Python 3.
(Contributed by Batuhan Taskaya in [bpo-39639](https://bugs.python.org/issue?@action=redirect&bpo=39639) and [bpo-39969](https://bugs.python.org/issue?@action=redirect&bpo=39969)
and Serhiy Storchaka in [bpo-39988](https://bugs.python.org/issue?@action=redirect&bpo=39988).)

- The `PyEval_InitThreads()` and `PyEval_ThreadsInitialized()`
functions are now deprecated and will be removed in Python 3.11. Calling
`PyEval_InitThreads()` now does nothing. The [GIL](https://docs.python.org/3/glossary.html#term-GIL) is initialized
by [`Py_Initialize()`](https://docs.python.org/3/c-api/init.html#c.Py_Initialize "Py_Initialize") since Python 3.7.
(Contributed by Victor Stinner in [bpo-39877](https://bugs.python.org/issue?@action=redirect&bpo=39877).)

- Passing `None` as the first argument to the [`shlex.split()`](https://docs.python.org/3/library/shlex.html#shlex.split "shlex.split") function
has been deprecated. (Contributed by Zackery Spytz in [bpo-33262](https://bugs.python.org/issue?@action=redirect&bpo=33262).)

- `smtpd.MailmanProxy()` is now deprecated as it is unusable without
an external module, `mailman`. (Contributed by Samuel Colvin in [bpo-35800](https://bugs.python.org/issue?@action=redirect&bpo=35800).)

- The `lib2to3` module now emits a [`PendingDeprecationWarning`](https://docs.python.org/3/library/exceptions.html#PendingDeprecationWarning "PendingDeprecationWarning").
Python 3.9 switched to a PEG parser (see [**PEP 617**](https://peps.python.org/pep-0617/)), and Python 3.10 may
include new language syntax that is not parsable by lib2to3’s LL(1) parser.
The `lib2to3` module may be removed from the standard library in a future
Python version. Consider third-party alternatives such as [LibCST](https://libcst.readthedocs.io/) or
[parso](https://parso.readthedocs.io/).
(Contributed by Carl Meyer in [bpo-40360](https://bugs.python.org/issue?@action=redirect&bpo=40360).)

- The _random_ parameter of [`random.shuffle()`](https://docs.python.org/3/library/random.html#random.shuffle "random.shuffle") has been deprecated.
(Contributed by Raymond Hettinger in [bpo-40465](https://bugs.python.org/issue?@action=redirect&bpo=40465))


## Removed [¶](https://docs.python.org/3/whatsnew/3.9.html\#removed "Link to this heading")

- The erroneous version at `unittest.mock.__version__` has been removed.

- `nntplib.NNTP`: `xpath()` and `xgtitle()` methods have been removed.
These methods are deprecated since Python 3.3. Generally, these extensions
are not supported or not enabled by NNTP server administrators.
For `xgtitle()`, please use `nntplib.NNTP.descriptions()` or
`nntplib.NNTP.description()` instead.
(Contributed by Donghee Na in [bpo-39366](https://bugs.python.org/issue?@action=redirect&bpo=39366).)

- [`array.array`](https://docs.python.org/3/library/array.html#array.array "array.array"): `tostring()` and `fromstring()` methods have been
removed. They were aliases to `tobytes()` and `frombytes()`, deprecated
since Python 3.2.
(Contributed by Victor Stinner in [bpo-38916](https://bugs.python.org/issue?@action=redirect&bpo=38916).)

- The undocumented `sys.callstats()` function has been removed. Since Python
3.7, it was deprecated and always returned [`None`](https://docs.python.org/3/library/constants.html#None "None"). It required a special
build option `CALL_PROFILE` which was already removed in Python 3.7.
(Contributed by Victor Stinner in [bpo-37414](https://bugs.python.org/issue?@action=redirect&bpo=37414).)

- The `sys.getcheckinterval()` and `sys.setcheckinterval()` functions have
been removed. They were deprecated since Python 3.2. Use
[`sys.getswitchinterval()`](https://docs.python.org/3/library/sys.html#sys.getswitchinterval "sys.getswitchinterval") and [`sys.setswitchinterval()`](https://docs.python.org/3/library/sys.html#sys.setswitchinterval "sys.setswitchinterval") instead.
(Contributed by Victor Stinner in [bpo-37392](https://bugs.python.org/issue?@action=redirect&bpo=37392).)

- The C function `PyImport_Cleanup()` has been removed. It was documented as:
“Empty the module table. For internal use only.”
(Contributed by Victor Stinner in [bpo-36710](https://bugs.python.org/issue?@action=redirect&bpo=36710).)

- `_dummy_thread` and `dummy_threading` modules have been removed. These
modules were deprecated since Python 3.7 which requires threading support.
(Contributed by Victor Stinner in [bpo-37312](https://bugs.python.org/issue?@action=redirect&bpo=37312).)

- `aifc.openfp()` alias to `aifc.open()`, `sunau.openfp()` alias to
`sunau.open()`, and `wave.openfp()` alias to [`wave.open()`](https://docs.python.org/3/library/wave.html#wave.open "wave.open") have been
removed. They were deprecated since Python 3.7.
(Contributed by Victor Stinner in [bpo-37320](https://bugs.python.org/issue?@action=redirect&bpo=37320).)

- The `isAlive()` method of [`threading.Thread`](https://docs.python.org/3/library/threading.html#threading.Thread "threading.Thread")
has been removed. It was deprecated since Python 3.8.
Use [`is_alive()`](https://docs.python.org/3/library/threading.html#threading.Thread.is_alive "threading.Thread.is_alive") instead.
(Contributed by Donghee Na in [bpo-37804](https://bugs.python.org/issue?@action=redirect&bpo=37804).)

- Methods `getchildren()` and `getiterator()` of classes
[`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.ElementTree "xml.etree.ElementTree.ElementTree") and
[`Element`](https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element "xml.etree.ElementTree.Element") in the [`ElementTree`](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree "xml.etree.ElementTree: Implementation of the ElementTree API.")
module have been removed. They were deprecated in Python 3.2.
Use `iter(x)` or `list(x)` instead of `x.getchildren()` and
`x.iter()` or `list(x.iter())` instead of `x.getiterator()`.
(Contributed by Serhiy Storchaka in [bpo-36543](https://bugs.python.org/issue?@action=redirect&bpo=36543).)

- The old [`plistlib`](https://docs.python.org/3/library/plistlib.html#module-plistlib "plistlib: Generate and parse Apple plist files.") API has been removed, it was deprecated since Python
3.4. Use the [`load()`](https://docs.python.org/3/library/plistlib.html#plistlib.load "plistlib.load"), [`loads()`](https://docs.python.org/3/library/plistlib.html#plistlib.loads "plistlib.loads"), [`dump()`](https://docs.python.org/3/library/plistlib.html#plistlib.dump "plistlib.dump"), and
[`dumps()`](https://docs.python.org/3/library/plistlib.html#plistlib.dumps "plistlib.dumps") functions. Additionally, the _use\_builtin\_types_ parameter was
removed, standard [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects are always used instead.
(Contributed by Jon Janzen in [bpo-36409](https://bugs.python.org/issue?@action=redirect&bpo=36409).)

- The C function `PyGen_NeedsFinalizing` has been removed. It was not
documented, tested, or used anywhere within CPython after the implementation
of [**PEP 442**](https://peps.python.org/pep-0442/). Patch by Joannah Nanjekye.
(Contributed by Joannah Nanjekye in [bpo-15088](https://bugs.python.org/issue?@action=redirect&bpo=15088))

- `base64.encodestring()` and `base64.decodestring()`, aliases deprecated
since Python 3.1, have been removed: use [`base64.encodebytes()`](https://docs.python.org/3/library/base64.html#base64.encodebytes "base64.encodebytes") and
[`base64.decodebytes()`](https://docs.python.org/3/library/base64.html#base64.decodebytes "base64.decodebytes") instead.
(Contributed by Victor Stinner in [bpo-39351](https://bugs.python.org/issue?@action=redirect&bpo=39351).)

- `fractions.gcd()` function has been removed, it was deprecated since Python
3.5 ( [bpo-22486](https://bugs.python.org/issue?@action=redirect&bpo=22486)): use [`math.gcd()`](https://docs.python.org/3/library/math.html#math.gcd "math.gcd") instead.
(Contributed by Victor Stinner in [bpo-39350](https://bugs.python.org/issue?@action=redirect&bpo=39350).)

- The _buffering_ parameter of [`bz2.BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File") has been removed. Since
Python 3.0, it was ignored and using it emitted a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning").
Pass an open file object to control how the file is opened.
(Contributed by Victor Stinner in [bpo-39357](https://bugs.python.org/issue?@action=redirect&bpo=39357).)

- The _encoding_ parameter of [`json.loads()`](https://docs.python.org/3/library/json.html#json.loads "json.loads") has been removed.
As of Python 3.1, it was deprecated and ignored; using it has emitted a
[`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") since Python 3.8.
(Contributed by Inada Naoki in [bpo-39377](https://bugs.python.org/issue?@action=redirect&bpo=39377))

- `with (await asyncio.lock):` and `with (yield from asyncio.lock):` statements are
not longer supported, use `async with lock` instead. The same is correct for
`asyncio.Condition` and `asyncio.Semaphore`.
(Contributed by Andrew Svetlov in [bpo-34793](https://bugs.python.org/issue?@action=redirect&bpo=34793).)

- The `sys.getcounts()` function, the `-X showalloccount` command line
option and the `show_alloc_count` field of the C structure
[`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig") have been removed. They required a special Python build by
defining `COUNT_ALLOCS` macro.
(Contributed by Victor Stinner in [bpo-39489](https://bugs.python.org/issue?@action=redirect&bpo=39489).)

- The `_field_types` attribute of the [`typing.NamedTuple`](https://docs.python.org/3/library/typing.html#typing.NamedTuple "typing.NamedTuple") class
has been removed. It was deprecated since Python 3.8. Use
the `__annotations__` attribute instead.
(Contributed by Serhiy Storchaka in [bpo-40182](https://bugs.python.org/issue?@action=redirect&bpo=40182).)

- The `symtable.SymbolTable.has_exec()` method has been removed. It was
deprecated since 2006, and only returning `False` when it’s called.
(Contributed by Batuhan Taskaya in [bpo-40208](https://bugs.python.org/issue?@action=redirect&bpo=40208))

- The `asyncio.Task.current_task()` and `asyncio.Task.all_tasks()`
have been removed. They were deprecated since Python 3.7 and you can use
[`asyncio.current_task()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.current_task "asyncio.current_task") and [`asyncio.all_tasks()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.all_tasks "asyncio.all_tasks") instead.
(Contributed by Rémi Lapeyre in [bpo-40967](https://bugs.python.org/issue?@action=redirect&bpo=40967))

- The `unescape()` method in the [`html.parser.HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser") class
has been removed (it was deprecated since Python 3.4). [`html.unescape()`](https://docs.python.org/3/library/html.html#html.unescape "html.unescape")
should be used for converting character references to the corresponding
unicode characters.


## Porting to Python 3.9 [¶](https://docs.python.org/3/whatsnew/3.9.html\#porting-to-python-3-9 "Link to this heading")

This section lists previously described changes and other bugfixes
that may require changes to your code.

### Changes in the Python API [¶](https://docs.python.org/3/whatsnew/3.9.html\#changes-in-the-python-api "Link to this heading")

- [`__import__()`](https://docs.python.org/3/library/functions.html#import__ "__import__") and [`importlib.util.resolve_name()`](https://docs.python.org/3/library/importlib.html#importlib.util.resolve_name "importlib.util.resolve_name") now raise
[`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") where it previously raised [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"). Callers
catching the specific exception type and supporting both Python 3.9 and
earlier versions will need to catch both using `except (ImportError, ValueError):`.

- The [`venv`](https://docs.python.org/3/library/venv.html#module-venv "venv: Creation of virtual environments.") activation scripts no longer special-case when
`__VENV_PROMPT__` is set to `""`.

- The [`select.epoll.unregister()`](https://docs.python.org/3/library/select.html#select.epoll.unregister "select.epoll.unregister") method no longer ignores the
[`EBADF`](https://docs.python.org/3/library/errno.html#errno.EBADF "errno.EBADF") error.
(Contributed by Victor Stinner in [bpo-39239](https://bugs.python.org/issue?@action=redirect&bpo=39239).)

- The _compresslevel_ parameter of [`bz2.BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File") became keyword-only,
since the _buffering_ parameter has been removed.
(Contributed by Victor Stinner in [bpo-39357](https://bugs.python.org/issue?@action=redirect&bpo=39357).)

- Simplified AST for subscription. Simple indices will be represented by
their value, extended slices will be represented as tuples.
`Index(value)` will return a `value` itself, `ExtSlice(slices)`
will return `Tuple(slices, Load())`.
(Contributed by Serhiy Storchaka in [bpo-34822](https://bugs.python.org/issue?@action=redirect&bpo=34822).)

- The [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.") module now ignores the [`PYTHONCASEOK`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONCASEOK)
environment variable when the [`-E`](https://docs.python.org/3/using/cmdline.html#cmdoption-E) or [`-I`](https://docs.python.org/3/using/cmdline.html#cmdoption-I) command line
options are being used.

- The _encoding_ parameter has been added to the classes [`ftplib.FTP`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP "ftplib.FTP") and
[`ftplib.FTP_TLS`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP_TLS "ftplib.FTP_TLS") as a keyword-only parameter, and the default encoding
is changed from Latin-1 to UTF-8 to follow [**RFC 2640**](https://datatracker.ietf.org/doc/html/rfc2640.html).

- [`asyncio.loop.shutdown_default_executor()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.shutdown_default_executor "asyncio.loop.shutdown_default_executor") has been added to
[`AbstractEventLoop`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.AbstractEventLoop "asyncio.AbstractEventLoop"), meaning alternative event loops that
inherit from it should have this method defined.
(Contributed by Kyle Stanley in [bpo-34037](https://bugs.python.org/issue?@action=redirect&bpo=34037).)

- The constant values of future flags in the [`__future__`](https://docs.python.org/3/library/__future__.html#module-__future__ "__future__: Future statement definitions") module
is updated in order to prevent collision with compiler flags. Previously
`PyCF_ALLOW_TOP_LEVEL_AWAIT` was clashing with `CO_FUTURE_DIVISION`.
(Contributed by Batuhan Taskaya in [bpo-39562](https://bugs.python.org/issue?@action=redirect&bpo=39562))

- `array('u')` now uses `wchar_t` as C type instead of `Py_UNICODE`.
This change doesn’t affect to its behavior because `Py_UNICODE` is alias
of `wchar_t` since Python 3.3.
(Contributed by Inada Naoki in [bpo-34538](https://bugs.python.org/issue?@action=redirect&bpo=34538).)

- The [`logging.getLogger()`](https://docs.python.org/3/library/logging.html#logging.getLogger "logging.getLogger") API now returns the root logger when passed
the name `'root'`, whereas previously it returned a non-root logger named
`'root'`. This could affect cases where user code explicitly wants a
non-root logger named `'root'`, or instantiates a logger using
`logging.getLogger(__name__)` in some top-level module called `'root.py'`.
(Contributed by Vinay Sajip in [bpo-37742](https://bugs.python.org/issue?@action=redirect&bpo=37742).)

- Division handling of [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath") now returns [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented")
instead of raising a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") when passed something other than an
instance of `str` or [`PurePath`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath "pathlib.PurePath"). This allows creating
compatible classes that don’t inherit from those mentioned types.
(Contributed by Roger Aiudi in [bpo-34775](https://bugs.python.org/issue?@action=redirect&bpo=34775)).

- Starting with Python 3.9.5 the [`ipaddress`](https://docs.python.org/3/library/ipaddress.html#module-ipaddress "ipaddress: IPv4/IPv6 manipulation library.") module no longer
accepts any leading zeros in IPv4 address strings. Leading zeros are
ambiguous and interpreted as octal notation by some libraries. For example
the legacy function [`socket.inet_aton()`](https://docs.python.org/3/library/socket.html#socket.inet_aton "socket.inet_aton") treats leading zeros as octal
notatation. glibc implementation of modern [`inet_pton()`](https://docs.python.org/3/library/socket.html#socket.inet_pton "socket.inet_pton") does
not accept any leading zeros.
(Contributed by Christian Heimes in [bpo-36384](https://bugs.python.org/issue?@action=redirect&bpo=36384)).

- [`codecs.lookup()`](https://docs.python.org/3/library/codecs.html#codecs.lookup "codecs.lookup") now normalizes the encoding name the same way as
[`encodings.normalize_encoding()`](https://docs.python.org/3/library/codecs.html#encodings.normalize_encoding "encodings.normalize_encoding"), except that [`codecs.lookup()`](https://docs.python.org/3/library/codecs.html#codecs.lookup "codecs.lookup") also
converts the name to lower case. For example, `"latex+latin1"` encoding
name is now normalized to `"latex_latin1"`.
(Contributed by Jordon Xu in [bpo-37751](https://bugs.python.org/issue?@action=redirect&bpo=37751).)


### Changes in the C API [¶](https://docs.python.org/3/whatsnew/3.9.html\#changes-in-the-c-api "Link to this heading")

- Instances of [heap-allocated types](https://docs.python.org/3/c-api/typeobj.html#heap-types) (such as those created with
[`PyType_FromSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpec "PyType_FromSpec") and similar APIs) hold a reference to their type
object since Python 3.8. As indicated in the “Changes in the C API” of Python
3.8, for the vast majority of cases, there should be no side effect but for
types that have a custom [`tp_traverse`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_traverse "PyTypeObject.tp_traverse") function,
ensure that all custom `tp_traverse` functions of heap-allocated types
visit the object’s type.


> Example:
>
> ```
> int
> foo_traverse(PyObject *self, visitproc visit, void *arg)
> {
> // Rest of the traverse function
> #if PY_VERSION_HEX >= 0x03090000
>     // This was not needed before Python 3.9 (Python issue 35810 and 40217)
>     Py_VISIT(Py_TYPE(self));
> #endif
> }
> ```


If your traverse function delegates to `tp_traverse` of its base class
(or another type), ensure that `Py_TYPE(self)` is visited only once.
Note that only [heap type](https://docs.python.org/3/c-api/typeobj.html#heap-types) are expected to visit the type
in `tp_traverse`.


> For example, if your `tp_traverse` function includes:
>
> ```
> base->tp_traverse(self, visit, arg)
> ```
>
> then add:
>
> ```
> #if PY_VERSION_HEX >= 0x03090000
>     // This was not needed before Python 3.9 (bpo-35810 and bpo-40217)
>     if (base->tp_flags & Py_TPFLAGS_HEAPTYPE) {
>         // a heap type's tp_traverse already visited Py_TYPE(self)
>     } else {
>         Py_VISIT(Py_TYPE(self));
>     }
> #else
> ```


(See [bpo-35810](https://bugs.python.org/issue?@action=redirect&bpo=35810) and [bpo-40217](https://bugs.python.org/issue?@action=redirect&bpo=40217) for more information.)

- The functions `PyEval_CallObject`, `PyEval_CallFunction`,
`PyEval_CallMethod` and `PyEval_CallObjectWithKeywords` are deprecated.
Use [`PyObject_Call()`](https://docs.python.org/3/c-api/call.html#c.PyObject_Call "PyObject_Call") and its variants instead.
(See more details in [bpo-29548](https://bugs.python.org/issue?@action=redirect&bpo=29548).)


### CPython bytecode changes [¶](https://docs.python.org/3/whatsnew/3.9.html\#cpython-bytecode-changes "Link to this heading")

- The `LOAD_ASSERTION_ERROR` opcode was added for handling the
[`assert`](https://docs.python.org/3/reference/simple_stmts.html#assert) statement. Previously, the assert statement would not work
correctly if the [`AssertionError`](https://docs.python.org/3/library/exceptions.html#AssertionError "AssertionError") exception was being shadowed.
(Contributed by Zackery Spytz in [bpo-34880](https://bugs.python.org/issue?@action=redirect&bpo=34880).)

- The [`COMPARE_OP`](https://docs.python.org/3/library/dis.html#opcode-COMPARE_OP) opcode was split into four distinct instructions:


  - `COMPARE_OP` for rich comparisons

  - `IS_OP` for ‘is’ and ‘is not’ tests

  - `CONTAINS_OP` for ‘in’ and ‘not in’ tests

  - `JUMP_IF_NOT_EXC_MATCH` for checking exceptions in ‘try-except’
    statements.


(Contributed by Mark Shannon in [bpo-39156](https://bugs.python.org/issue?@action=redirect&bpo=39156).)

## Build Changes [¶](https://docs.python.org/3/whatsnew/3.9.html\#build-changes "Link to this heading")

- Added `--with-platlibdir` option to the `configure` script: name of the
platform-specific library directory, stored in the new [`sys.platlibdir`](https://docs.python.org/3/library/sys.html#sys.platlibdir "sys.platlibdir")
attribute. See [`sys.platlibdir`](https://docs.python.org/3/library/sys.html#sys.platlibdir "sys.platlibdir") attribute for more information.
(Contributed by Jan Matějek, Matěj Cepl, Charalampos Stratakis
and Victor Stinner in [bpo-1294959](https://bugs.python.org/issue?@action=redirect&bpo=1294959).)

- The `COUNT_ALLOCS` special build macro has been removed.
(Contributed by Victor Stinner in [bpo-39489](https://bugs.python.org/issue?@action=redirect&bpo=39489).)

- On non-Windows platforms, the `setenv()` and `unsetenv()`
functions are now required to build Python.
(Contributed by Victor Stinner in [bpo-39395](https://bugs.python.org/issue?@action=redirect&bpo=39395).)

- On non-Windows platforms, creating `bdist_wininst` installers is now
officially unsupported. (See [bpo-10945](https://bugs.python.org/issue?@action=redirect&bpo=10945) for more details.)

- When building Python on macOS from source, `_tkinter` now links with
non-system Tcl and Tk frameworks if they are installed in
`/Library/Frameworks`, as had been the case on older releases
of macOS. If a macOS SDK is explicitly configured, by using
[`--enable-universalsdk`](https://docs.python.org/3/using/configure.html#cmdoption-enable-universalsdk) or `-isysroot`, only the SDK itself is
searched. The default behavior can still be overridden with
`--with-tcltk-includes` and `--with-tcltk-libs`.
(Contributed by Ned Deily in [bpo-34956](https://bugs.python.org/issue?@action=redirect&bpo=34956).)

- Python can now be built for Windows 10 ARM64.
(Contributed by Steve Dower in [bpo-33125](https://bugs.python.org/issue?@action=redirect&bpo=33125).)

- Some individual tests are now skipped when `--pgo` is used. The tests
in question increased the PGO task time significantly and likely
didn’t help improve optimization of the final executable. This
speeds up the task by a factor of about 15x. Running the full unit test
suite is slow. This change may result in a slightly less optimized build
since not as many code branches will be executed. If you are willing to
wait for the much slower build, the old behavior can be restored using
`./configure [..] PROFILE_TASK="-m test --pgo-extended"`. We make no
guarantees as to which PGO task set produces a faster build. Users who care
should run their own relevant benchmarks as results can depend on the
environment, workload, and compiler tool chain.
(See [bpo-36044](https://bugs.python.org/issue?@action=redirect&bpo=36044) and [bpo-37707](https://bugs.python.org/issue?@action=redirect&bpo=37707) for more details.)


## C API Changes [¶](https://docs.python.org/3/whatsnew/3.9.html\#c-api-changes "Link to this heading")

### New Features [¶](https://docs.python.org/3/whatsnew/3.9.html\#id1 "Link to this heading")

- [**PEP 573**](https://peps.python.org/pep-0573/): Added [`PyType_FromModuleAndSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromModuleAndSpec "PyType_FromModuleAndSpec") to associate
a module with a class; [`PyType_GetModule()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModule "PyType_GetModule") and
[`PyType_GetModuleState()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetModuleState "PyType_GetModuleState") to retrieve the module and its state; and
[`PyCMethod`](https://docs.python.org/3/c-api/structures.html#c.PyCMethod "PyCMethod") and [`METH_METHOD`](https://docs.python.org/3/c-api/structures.html#c.METH_METHOD "METH_METHOD") to allow a method to
access the class it was defined in.
(Contributed by Marcel Plch and Petr Viktorin in [bpo-38787](https://bugs.python.org/issue?@action=redirect&bpo=38787).)

- Added [`PyFrame_GetCode()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetCode "PyFrame_GetCode") function: get a frame code.
Added [`PyFrame_GetBack()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetBack "PyFrame_GetBack") function: get the frame next outer frame.
(Contributed by Victor Stinner in [bpo-40421](https://bugs.python.org/issue?@action=redirect&bpo=40421).)

- Added [`PyFrame_GetLineNumber()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLineNumber "PyFrame_GetLineNumber") to the limited C API.
(Contributed by Victor Stinner in [bpo-40421](https://bugs.python.org/issue?@action=redirect&bpo=40421).)

- Added [`PyThreadState_GetInterpreter()`](https://docs.python.org/3/c-api/init.html#c.PyThreadState_GetInterpreter "PyThreadState_GetInterpreter") and
[`PyInterpreterState_Get()`](https://docs.python.org/3/c-api/init.html#c.PyInterpreterState_Get "PyInterpreterState_Get") functions to get the interpreter.
Added [`PyThreadState_GetFrame()`](https://docs.python.org/3/c-api/init.html#c.PyThreadState_GetFrame "PyThreadState_GetFrame") function to get the current frame of a
Python thread state.
Added [`PyThreadState_GetID()`](https://docs.python.org/3/c-api/init.html#c.PyThreadState_GetID "PyThreadState_GetID") function: get the unique identifier of a
Python thread state.
(Contributed by Victor Stinner in [bpo-39947](https://bugs.python.org/issue?@action=redirect&bpo=39947).)

- Added a new public [`PyObject_CallNoArgs()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallNoArgs "PyObject_CallNoArgs") function to the C API, which
calls a callable Python object without any arguments. It is the most efficient
way to call a callable Python object without any argument.
(Contributed by Victor Stinner in [bpo-37194](https://bugs.python.org/issue?@action=redirect&bpo=37194).)

- Changes in the limited C API (if `Py_LIMITED_API` macro is defined):


  - Provide [`Py_EnterRecursiveCall()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_EnterRecursiveCall "Py_EnterRecursiveCall") and [`Py_LeaveRecursiveCall()`](https://docs.python.org/3/c-api/exceptions.html#c.Py_LeaveRecursiveCall "Py_LeaveRecursiveCall")
    as regular functions for the limited API. Previously, there were defined as
    macros, but these macros didn’t compile with the limited C API which cannot
    access `PyThreadState.recursion_depth` field (the structure is opaque in
    the limited C API).

  - `PyObject_INIT()` and `PyObject_INIT_VAR()` become regular “opaque”
    function to hide implementation details.


(Contributed by Victor Stinner in [bpo-38644](https://bugs.python.org/issue?@action=redirect&bpo=38644) and [bpo-39542](https://bugs.python.org/issue?@action=redirect&bpo=39542).)

- The [`PyModule_AddType()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddType "PyModule_AddType") function is added to help adding a type
to a module.
(Contributed by Donghee Na in [bpo-40024](https://bugs.python.org/issue?@action=redirect&bpo=40024).)

- Added the functions [`PyObject_GC_IsTracked()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_IsTracked "PyObject_GC_IsTracked") and
[`PyObject_GC_IsFinalized()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_GC_IsFinalized "PyObject_GC_IsFinalized") to the public API to allow to query if
Python objects are being currently tracked or have been already finalized by
the garbage collector respectively.
(Contributed by Pablo Galindo Salgado in [bpo-40241](https://bugs.python.org/issue?@action=redirect&bpo=40241).)

- Added `_PyObject_FunctionStr()` to get a user-friendly string
representation of a function-like object.
(Patch by Jeroen Demeyer in [bpo-37645](https://bugs.python.org/issue?@action=redirect&bpo=37645).)

- Added [`PyObject_CallOneArg()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallOneArg "PyObject_CallOneArg") for calling an object with one
positional argument
(Patch by Jeroen Demeyer in [bpo-37483](https://bugs.python.org/issue?@action=redirect&bpo=37483).)


### Porting to Python 3.9 [¶](https://docs.python.org/3/whatsnew/3.9.html\#id2 "Link to this heading")

- `PyInterpreterState.eval_frame` ( [**PEP 523**](https://peps.python.org/pep-0523/)) now requires a new mandatory
_tstate_ parameter (`PyThreadState*`).
(Contributed by Victor Stinner in [bpo-38500](https://bugs.python.org/issue?@action=redirect&bpo=38500).)

- Extension modules: [`m_traverse`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_traverse "PyModuleDef.m_traverse"),
[`m_clear`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_clear "PyModuleDef.m_clear") and [`m_free`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_free "PyModuleDef.m_free")
functions of [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef") are no longer called if the module state
was requested but is not allocated yet. This is the case immediately after
the module is created and before the module is executed
( [`Py_mod_exec`](https://docs.python.org/3/c-api/module.html#c.Py_mod_exec "Py_mod_exec") function). More precisely, these functions are not called
if [`m_size`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_size "PyModuleDef.m_size") is greater than 0 and the module state (as
returned by [`PyModule_GetState()`](https://docs.python.org/3/c-api/module.html#c.PyModule_GetState "PyModule_GetState")) is `NULL`.

Extension modules without module state (`m_size <= 0`) are not affected.

- If [`Py_AddPendingCall()`](https://docs.python.org/3/c-api/init.html#c.Py_AddPendingCall "Py_AddPendingCall") is called in a subinterpreter, the function is
now scheduled to be called from the subinterpreter, rather than being called
from the main interpreter. Each subinterpreter now has its own list of
scheduled calls.
(Contributed by Victor Stinner in [bpo-39984](https://bugs.python.org/issue?@action=redirect&bpo=39984).)

- The Windows registry is no longer used to initialize [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") when
the `-E` option is used (if [`PyConfig.use_environment`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.use_environment "PyConfig.use_environment") is set to
`0`). This is significant when embedding Python on Windows.
(Contributed by Zackery Spytz in [bpo-8901](https://bugs.python.org/issue?@action=redirect&bpo=8901).)

- The global variable [`PyStructSequence_UnnamedField`](https://docs.python.org/3/c-api/tuple.html#c.PyStructSequence_UnnamedField "PyStructSequence_UnnamedField") is now a constant
and refers to a constant string.
(Contributed by Serhiy Storchaka in [bpo-38650](https://bugs.python.org/issue?@action=redirect&bpo=38650).)

- The `PyGC_Head` structure is now opaque. It is only defined in the
internal C API (`pycore_gc.h`).
(Contributed by Victor Stinner in [bpo-40241](https://bugs.python.org/issue?@action=redirect&bpo=40241).)

- The `Py_UNICODE_COPY`, `Py_UNICODE_FILL`, `PyUnicode_WSTR_LENGTH`,
`PyUnicode_FromUnicode()`, `PyUnicode_AsUnicode()`,
`_PyUnicode_AsUnicode`, and `PyUnicode_AsUnicodeAndSize()` are
marked as deprecated in C. They have been deprecated by [**PEP 393**](https://peps.python.org/pep-0393/) since
Python 3.3.
(Contributed by Inada Naoki in [bpo-36346](https://bugs.python.org/issue?@action=redirect&bpo=36346).)

- The [`Py_FatalError()`](https://docs.python.org/3/c-api/sys.html#c.Py_FatalError "Py_FatalError") function is replaced with a macro which logs
automatically the name of the current function, unless the
`Py_LIMITED_API` macro is defined.
(Contributed by Victor Stinner in [bpo-39882](https://bugs.python.org/issue?@action=redirect&bpo=39882).)

- The vectorcall protocol now requires that the caller passes only strings as
keyword names. (See [bpo-37540](https://bugs.python.org/issue?@action=redirect&bpo=37540) for more information.)

- Implementation details of a number of macros and functions are now hidden:


  - [`PyObject_IS_GC()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyObject_IS_GC "PyObject_IS_GC") macro was converted to a function.

  - The `PyObject_NEW()` macro becomes an alias to the
    [`PyObject_New`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_New "PyObject_New") macro, and the `PyObject_NEW_VAR()` macro
    becomes an alias to the [`PyObject_NewVar`](https://docs.python.org/3/c-api/allocation.html#c.PyObject_NewVar "PyObject_NewVar") macro. They no longer
    access directly the [`PyTypeObject.tp_basicsize`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_basicsize "PyTypeObject.tp_basicsize") member.

  - `PyObject_GET_WEAKREFS_LISTPTR()` macro was converted to a function:
    the macro accessed directly the [`PyTypeObject.tp_weaklistoffset`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_weaklistoffset "PyTypeObject.tp_weaklistoffset")
    member.

  - [`PyObject_CheckBuffer()`](https://docs.python.org/3/c-api/buffer.html#c.PyObject_CheckBuffer "PyObject_CheckBuffer") macro was converted to a function: the macro
    accessed directly the [`PyTypeObject.tp_as_buffer`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_buffer "PyTypeObject.tp_as_buffer") member.

  - [`PyIndex_Check()`](https://docs.python.org/3/c-api/number.html#c.PyIndex_Check "PyIndex_Check") is now always declared as an opaque function to hide
    implementation details: removed the `PyIndex_Check()` macro. The macro accessed
    directly the [`PyTypeObject.tp_as_number`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_as_number "PyTypeObject.tp_as_number") member.


(See [bpo-40170](https://bugs.python.org/issue?@action=redirect&bpo=40170) for more details.)

### Removed [¶](https://docs.python.org/3/whatsnew/3.9.html\#id3 "Link to this heading")

- Excluded `PyFPE_START_PROTECT()` and `PyFPE_END_PROTECT()` macros of
`pyfpe.h` from the limited C API.
(Contributed by Victor Stinner in [bpo-38835](https://bugs.python.org/issue?@action=redirect&bpo=38835).)

- The `tp_print` slot of [PyTypeObject](https://docs.python.org/3/c-api/typeobj.html#type-structs) has been removed.
It was used for printing objects to files in Python 2.7 and before. Since
Python 3.0, it has been ignored and unused.
(Contributed by Jeroen Demeyer in [bpo-36974](https://bugs.python.org/issue?@action=redirect&bpo=36974).)

- Changes in the limited C API (if `Py_LIMITED_API` macro is defined):


  - Excluded the following functions from the limited C API:

    - `PyThreadState_DeleteCurrent()`
      (Contributed by Joannah Nanjekye in [bpo-37878](https://bugs.python.org/issue?@action=redirect&bpo=37878).)

    - `_Py_CheckRecursionLimit`

    - `_Py_NewReference()`

    - `_Py_ForgetReference()`

    - `_PyTraceMalloc_NewReference()`

    - `_Py_GetRefTotal()`

    - The trashcan mechanism which never worked in the limited C API.

    - `PyTrash_UNWIND_LEVEL`

    - `Py_TRASHCAN_BEGIN_CONDITION`

    - `Py_TRASHCAN_BEGIN`

    - `Py_TRASHCAN_END`

    - `Py_TRASHCAN_SAFE_BEGIN`

    - `Py_TRASHCAN_SAFE_END`
  - Moved following functions and definitions to the internal C API:

    - `_PyDebug_PrintTotalRefs()`

    - `_Py_PrintReferences()`

    - `_Py_PrintReferenceAddresses()`

    - `_Py_tracemalloc_config`

    - `_Py_AddToAllObjects()` (specific to `Py_TRACE_REFS` build)

(Contributed by Victor Stinner in [bpo-38644](https://bugs.python.org/issue?@action=redirect&bpo=38644) and [bpo-39542](https://bugs.python.org/issue?@action=redirect&bpo=39542).)

- Removed `_PyRuntime.getframe` hook and removed `_PyThreadState_GetFrame`
macro which was an alias to `_PyRuntime.getframe`. They were only exposed
by the internal C API. Removed also `PyThreadFrameGetter` type.
(Contributed by Victor Stinner in [bpo-39946](https://bugs.python.org/issue?@action=redirect&bpo=39946).)

- Removed the following functions from the C API. Call [`PyGC_Collect()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyGC_Collect "PyGC_Collect")
explicitly to clear all free lists.
(Contributed by Inada Naoki and Victor Stinner in [bpo-37340](https://bugs.python.org/issue?@action=redirect&bpo=37340),
[bpo-38896](https://bugs.python.org/issue?@action=redirect&bpo=38896) and [bpo-40428](https://bugs.python.org/issue?@action=redirect&bpo=40428).)

  - `PyAsyncGen_ClearFreeLists()`

  - `PyContext_ClearFreeList()`

  - `PyDict_ClearFreeList()`

  - `PyFloat_ClearFreeList()`

  - `PyFrame_ClearFreeList()`

  - `PyList_ClearFreeList()`

  - `PyMethod_ClearFreeList()` and `PyCFunction_ClearFreeList()`:
    the free lists of bound method objects have been removed.

  - `PySet_ClearFreeList()`: the set free list has been removed
    in Python 3.4.

  - `PyTuple_ClearFreeList()`

  - `PyUnicode_ClearFreeList()`: the Unicode free list has been removed in
    Python 3.3.
- Removed `_PyUnicode_ClearStaticStrings()` function.
(Contributed by Victor Stinner in [bpo-39465](https://bugs.python.org/issue?@action=redirect&bpo=39465).)

- Removed `Py_UNICODE_MATCH`. It has been deprecated by [**PEP 393**](https://peps.python.org/pep-0393/), and
broken since Python 3.3. The [`PyUnicode_Tailmatch()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Tailmatch "PyUnicode_Tailmatch") function can be
used instead.
(Contributed by Inada Naoki in [bpo-36346](https://bugs.python.org/issue?@action=redirect&bpo=36346).)

- Cleaned header files of interfaces defined but with no implementation.
The public API symbols being removed are:
`_PyBytes_InsertThousandsGroupingLocale`,
`_PyBytes_InsertThousandsGrouping`, `_Py_InitializeFromArgs`,
`_Py_InitializeFromWideArgs`, `_PyFloat_Repr`, `_PyFloat_Digits`,
`_PyFloat_DigitsInit`, `PyFrame_ExtendStack`, `_PyAIterWrapper_Type`,
`PyNullImporter_Type`, `PyCmpWrapper_Type`, `PySortWrapper_Type`,
`PyNoArgsFunction`.
(Contributed by Pablo Galindo Salgado in [bpo-39372](https://bugs.python.org/issue?@action=redirect&bpo=39372).)


## Notable changes in Python 3.9.1 [¶](https://docs.python.org/3/whatsnew/3.9.html\#notable-changes-in-python-3-9-1 "Link to this heading")

### typing [¶](https://docs.python.org/3/whatsnew/3.9.html\#id4 "Link to this heading")

The behavior of [`typing.Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal") was changed to conform with [**PEP 586**](https://peps.python.org/pep-0586/)
and to match the behavior of static type checkers specified in the PEP.

1. `Literal` now de-duplicates parameters.

2. Equality comparisons between `Literal` objects are now order independent.

3. `Literal` comparisons now respect types. For example,
`Literal[0] == Literal[False]` previously evaluated to `True`. It is
now `False`. To support this change, the internally used type cache now
supports differentiating types.

4. `Literal` objects will now raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception during
equality comparisons if any of their parameters are not [hashable](https://docs.python.org/3/glossary.html#term-hashable).
Note that declaring `Literal` with mutable parameters will not throw
an error:



Copy

```
>>> from typing import Literal
>>> Literal[{0}]
>>> Literal[{0}] == Literal[{False}]
Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
```


(Contributed by Yurii Karabas in [bpo-42345](https://bugs.python.org/issue?@action=redirect&bpo=42345).)

### macOS 11.0 (Big Sur) and Apple Silicon Mac support [¶](https://docs.python.org/3/whatsnew/3.9.html\#macos-11-0-big-sur-and-apple-silicon-mac-support "Link to this heading")

As of 3.9.1, Python now fully supports building and running on macOS 11.0
(Big Sur) and on Apple Silicon Macs (based on the `ARM64` architecture).
A new universal build variant, `universal2`, is now available to natively
support both `ARM64` and `Intel 64` in one set of executables. Binaries
can also now be built on current versions of macOS to be deployed on a range
of older macOS versions (tested to 10.9) while making some newer OS
functions and options conditionally available based on the operating system
version in use at runtime (“weaklinking”).

(Contributed by Ronald Oussoren and Lawrence D’Anna in [bpo-41100](https://bugs.python.org/issue?@action=redirect&bpo=41100).)

## Notable changes in Python 3.9.2 [¶](https://docs.python.org/3/whatsnew/3.9.html\#notable-changes-in-python-3-9-2 "Link to this heading")

### collections.abc [¶](https://docs.python.org/3/whatsnew/3.9.html\#collections-abc "Link to this heading")

[`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") generic now flattens type parameters, similar
to what [`typing.Callable`](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable") currently does. This means that
`collections.abc.Callable[[int, str], str]` will have `__args__` of
`(int, str, str)`; previously this was `([int, str], str)`. To allow this
change, [`types.GenericAlias`](https://docs.python.org/3/library/types.html#types.GenericAlias "types.GenericAlias") can now be subclassed, and a subclass will
be returned when subscripting the [`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") type.
Code which accesses the arguments via [`typing.get_args()`](https://docs.python.org/3/library/typing.html#typing.get_args "typing.get_args") or `__args__`
need to account for this change. A [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") may be emitted for
invalid forms of parameterizing [`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") which may have
passed silently in Python 3.9.1. This [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") will
become a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") in Python 3.10.
(Contributed by Ken Jin in [bpo-42195](https://bugs.python.org/issue?@action=redirect&bpo=42195).)

### urllib.parse [¶](https://docs.python.org/3/whatsnew/3.9.html\#urllib-parse "Link to this heading")

Earlier Python versions allowed using both `;` and `&` as
query parameter separators in [`urllib.parse.parse_qs()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qs "urllib.parse.parse_qs") and
[`urllib.parse.parse_qsl()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qsl "urllib.parse.parse_qsl"). Due to security concerns, and to conform with
newer W3C recommendations, this has been changed to allow only a single
separator key, with `&` as the default. This change also affects
`cgi.parse()` and `cgi.parse_multipart()` as they use the affected
functions internally. For more details, please see their respective
documentation.
(Contributed by Adam Goldschmidt, Senthil Kumaran and Ken Jin in [bpo-42967](https://bugs.python.org/issue?@action=redirect&bpo=42967).)

## Notable changes in Python 3.9.3 [¶](https://docs.python.org/3/whatsnew/3.9.html\#notable-changes-in-python-3-9-3 "Link to this heading")

A security fix alters the [`ftplib.FTP`](https://docs.python.org/3/library/ftplib.html#ftplib.FTP "ftplib.FTP") behavior to not trust the
IPv4 address sent from the remote server when setting up a passive data
channel. We reuse the ftp server IP address instead. For unusual code
requiring the old behavior, set a `trust_server_pasv_ipv4_address`
attribute on your FTP instance to `True`. (See [gh-87451](https://github.com/python/cpython/issues/87451))

## Notable changes in Python 3.9.5 [¶](https://docs.python.org/3/whatsnew/3.9.html\#notable-changes-in-python-3-9-5 "Link to this heading")

### urllib.parse [¶](https://docs.python.org/3/whatsnew/3.9.html\#id5 "Link to this heading")

The presence of newline or tab characters in parts of a URL allows for some
forms of attacks. Following the WHATWG specification that updates [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html),
ASCII newline `\n`, `\r` and tab `\t` characters are stripped from the
URL by the parser in [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse "urllib.parse: Parse URLs into or assemble them from components.") preventing such attacks. The removal
characters are controlled by a new module level variable
`urllib.parse._UNSAFE_URL_BYTES_TO_REMOVE`. (See [gh-88048](https://github.com/python/cpython/issues/88048))

## Notable security feature in 3.9.14 [¶](https://docs.python.org/3/whatsnew/3.9.html\#notable-security-feature-in-3-9-14 "Link to this heading")

Converting between [`int`](https://docs.python.org/3/library/functions.html#int "int") and [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") in bases other than 2
(binary), 4, 8 (octal), 16 (hexadecimal), or 32 such as base 10 (decimal)
now raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the number of digits in string form is
above a limit to avoid potential denial of service attacks due to the
algorithmic complexity. This is a mitigation for [**CVE 2020-10735**](https://www.cve.org/CVERecord?id=CVE-2020-10735).
This limit can be configured or disabled by environment variable, command
line flag, or [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.") APIs. See the [integer string conversion\\
length limitation](https://docs.python.org/3/library/stdtypes.html#int-max-str-digits) documentation. The default limit
is 4300 digits in string form.

## Notable changes in 3.9.17 [¶](https://docs.python.org/3/whatsnew/3.9.html\#notable-changes-in-3-9-17 "Link to this heading")

### tarfile [¶](https://docs.python.org/3/whatsnew/3.9.html\#tarfile "Link to this heading")

- The extraction methods in [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files."), and [`shutil.unpack_archive()`](https://docs.python.org/3/library/shutil.html#shutil.unpack_archive "shutil.unpack_archive"),
have a new a _filter_ argument that allows limiting tar features than may be
surprising or dangerous, such as creating files outside the destination
directory.
See [Extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter) for details.
In Python 3.12, use without the _filter_ argument will show a
[`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning").
In Python 3.14, the default will switch to `'data'`.
(Contributed by Petr Viktorin in [**PEP 706**](https://peps.python.org/pep-0706/).)


### [Table of Contents](https://docs.python.org/3/contents.html)

- [What’s New In Python 3.9](https://docs.python.org/3/whatsnew/3.9.html#)
  - [Summary – Release highlights](https://docs.python.org/3/whatsnew/3.9.html#summary-release-highlights)
  - [You should check for DeprecationWarning in your code](https://docs.python.org/3/whatsnew/3.9.html#you-should-check-for-deprecationwarning-in-your-code)
  - [New Features](https://docs.python.org/3/whatsnew/3.9.html#new-features)
    - [Dictionary Merge & Update Operators](https://docs.python.org/3/whatsnew/3.9.html#dictionary-merge-update-operators)
    - [New String Methods to Remove Prefixes and Suffixes](https://docs.python.org/3/whatsnew/3.9.html#new-string-methods-to-remove-prefixes-and-suffixes)
    - [Type Hinting Generics in Standard Collections](https://docs.python.org/3/whatsnew/3.9.html#type-hinting-generics-in-standard-collections)
    - [New Parser](https://docs.python.org/3/whatsnew/3.9.html#new-parser)
  - [Other Language Changes](https://docs.python.org/3/whatsnew/3.9.html#other-language-changes)
  - [New Modules](https://docs.python.org/3/whatsnew/3.9.html#new-modules)
    - [zoneinfo](https://docs.python.org/3/whatsnew/3.9.html#zoneinfo)
    - [graphlib](https://docs.python.org/3/whatsnew/3.9.html#graphlib)
  - [Improved Modules](https://docs.python.org/3/whatsnew/3.9.html#improved-modules)
    - [ast](https://docs.python.org/3/whatsnew/3.9.html#ast)
    - [asyncio](https://docs.python.org/3/whatsnew/3.9.html#asyncio)
    - [compileall](https://docs.python.org/3/whatsnew/3.9.html#compileall)
    - [concurrent.futures](https://docs.python.org/3/whatsnew/3.9.html#concurrent-futures)
    - [curses](https://docs.python.org/3/whatsnew/3.9.html#curses)
    - [datetime](https://docs.python.org/3/whatsnew/3.9.html#datetime)
    - [distutils](https://docs.python.org/3/whatsnew/3.9.html#distutils)
    - [fcntl](https://docs.python.org/3/whatsnew/3.9.html#fcntl)
    - [ftplib](https://docs.python.org/3/whatsnew/3.9.html#ftplib)
    - [gc](https://docs.python.org/3/whatsnew/3.9.html#gc)
    - [hashlib](https://docs.python.org/3/whatsnew/3.9.html#hashlib)
    - [http](https://docs.python.org/3/whatsnew/3.9.html#http)
    - [IDLE and idlelib](https://docs.python.org/3/whatsnew/3.9.html#idle-and-idlelib)
    - [imaplib](https://docs.python.org/3/whatsnew/3.9.html#imaplib)
    - [importlib](https://docs.python.org/3/whatsnew/3.9.html#importlib)
    - [inspect](https://docs.python.org/3/whatsnew/3.9.html#inspect)
    - [ipaddress](https://docs.python.org/3/whatsnew/3.9.html#ipaddress)
    - [math](https://docs.python.org/3/whatsnew/3.9.html#math)
    - [multiprocessing](https://docs.python.org/3/whatsnew/3.9.html#multiprocessing)
    - [nntplib](https://docs.python.org/3/whatsnew/3.9.html#nntplib)
    - [os](https://docs.python.org/3/whatsnew/3.9.html#os)
    - [pathlib](https://docs.python.org/3/whatsnew/3.9.html#pathlib)
    - [pdb](https://docs.python.org/3/whatsnew/3.9.html#pdb)
    - [poplib](https://docs.python.org/3/whatsnew/3.9.html#poplib)
    - [pprint](https://docs.python.org/3/whatsnew/3.9.html#pprint)
    - [pydoc](https://docs.python.org/3/whatsnew/3.9.html#pydoc)
    - [random](https://docs.python.org/3/whatsnew/3.9.html#random)
    - [signal](https://docs.python.org/3/whatsnew/3.9.html#signal)
    - [smtplib](https://docs.python.org/3/whatsnew/3.9.html#smtplib)
    - [socket](https://docs.python.org/3/whatsnew/3.9.html#socket)
    - [time](https://docs.python.org/3/whatsnew/3.9.html#time)
    - [sys](https://docs.python.org/3/whatsnew/3.9.html#sys)
    - [tracemalloc](https://docs.python.org/3/whatsnew/3.9.html#tracemalloc)
    - [typing](https://docs.python.org/3/whatsnew/3.9.html#typing)
    - [unicodedata](https://docs.python.org/3/whatsnew/3.9.html#unicodedata)
    - [venv](https://docs.python.org/3/whatsnew/3.9.html#venv)
    - [xml](https://docs.python.org/3/whatsnew/3.9.html#xml)
  - [Optimizations](https://docs.python.org/3/whatsnew/3.9.html#optimizations)
  - [Deprecated](https://docs.python.org/3/whatsnew/3.9.html#deprecated)
  - [Removed](https://docs.python.org/3/whatsnew/3.9.html#removed)
  - [Porting to Python 3.9](https://docs.python.org/3/whatsnew/3.9.html#porting-to-python-3-9)
    - [Changes in the Python API](https://docs.python.org/3/whatsnew/3.9.html#changes-in-the-python-api)
    - [Changes in the C API](https://docs.python.org/3/whatsnew/3.9.html#changes-in-the-c-api)
    - [CPython bytecode changes](https://docs.python.org/3/whatsnew/3.9.html#cpython-bytecode-changes)
  - [Build Changes](https://docs.python.org/3/whatsnew/3.9.html#build-changes)
  - [C API Changes](https://docs.python.org/3/whatsnew/3.9.html#c-api-changes)
    - [New Features](https://docs.python.org/3/whatsnew/3.9.html#id1)
    - [Porting to Python 3.9](https://docs.python.org/3/whatsnew/3.9.html#id2)
    - [Removed](https://docs.python.org/3/whatsnew/3.9.html#id3)
  - [Notable changes in Python 3.9.1](https://docs.python.org/3/whatsnew/3.9.html#notable-changes-in-python-3-9-1)
    - [typing](https://docs.python.org/3/whatsnew/3.9.html#id4)
    - [macOS 11.0 (Big Sur) and Apple Silicon Mac support](https://docs.python.org/3/whatsnew/3.9.html#macos-11-0-big-sur-and-apple-silicon-mac-support)
  - [Notable changes in Python 3.9.2](https://docs.python.org/3/whatsnew/3.9.html#notable-changes-in-python-3-9-2)
    - [collections.abc](https://docs.python.org/3/whatsnew/3.9.html#collections-abc)
    - [urllib.parse](https://docs.python.org/3/whatsnew/3.9.html#urllib-parse)
  - [Notable changes in Python 3.9.3](https://docs.python.org/3/whatsnew/3.9.html#notable-changes-in-python-3-9-3)
  - [Notable changes in Python 3.9.5](https://docs.python.org/3/whatsnew/3.9.html#notable-changes-in-python-3-9-5)
    - [urllib.parse](https://docs.python.org/3/whatsnew/3.9.html#id5)
  - [Notable security feature in 3.9.14](https://docs.python.org/3/whatsnew/3.9.html#notable-security-feature-in-3-9-14)
  - [Notable changes in 3.9.17](https://docs.python.org/3/whatsnew/3.9.html#notable-changes-in-3-9-17)
    - [tarfile](https://docs.python.org/3/whatsnew/3.9.html#tarfile)

#### Previous topic

[What’s New In Python 3.10](https://docs.python.org/3/whatsnew/3.10.html "previous chapter")

#### Next topic

[What’s New In Python 3.8](https://docs.python.org/3/whatsnew/3.8.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/whatsnew/3.9.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/whatsnew/3.8.html "What’s New In Python 3.8") \|
- [previous](https://docs.python.org/3/whatsnew/3.10.html "What’s New In Python 3.10") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [What’s New in Python](https://docs.python.org/3/whatsnew/index.html) »
- [What’s New In Python 3.9](https://docs.python.org/3/whatsnew/3.9.html)
- \|

- Theme
AutoLightDark \|