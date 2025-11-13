### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/abstract.html "Abstract Objects Layer") \|
- [previous](https://docs.python.org/3/c-api/time.html "PyTime C API") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Utilities](https://docs.python.org/3/c-api/utilities.html) »
- [Support for Perf Maps](https://docs.python.org/3/c-api/perfmaps.html)
- \|

- Theme
AutoLightDark \|

# Support for Perf Maps [¶](https://docs.python.org/3/c-api/perfmaps.html\#support-for-perf-maps "Link to this heading")

On supported platforms (as of this writing, only Linux), the runtime can take
advantage of _perf map files_ to make Python functions visible to an external
profiling tool (such as [perf](https://perf.wiki.kernel.org/index.php/Main_Page)).
A running process may create a file in the `/tmp` directory, which contains entries
that can map a section of executable code to a name. This interface is described in the
[documentation of the Linux Perf tool](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/tools/perf/Documentation/jit-interface.txt).

In Python, these helper APIs can be used by libraries and features that rely
on generating machine code on the fly.

Note that holding an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state) is not required for these APIs.

intPyUnstable\_PerfMapState\_Init(void) [¶](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_PerfMapState_Init "Link to this definition")

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api). It may change without warning in minor releases._

Open the `/tmp/perf-$pid.map` file, unless it’s already opened, and create
a lock to ensure thread-safe writes to the file (provided the writes are
done through [`PyUnstable_WritePerfMapEntry()`](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_WritePerfMapEntry "PyUnstable_WritePerfMapEntry")). Normally, there’s no need
to call this explicitly; just use [`PyUnstable_WritePerfMapEntry()`](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_WritePerfMapEntry "PyUnstable_WritePerfMapEntry")
and it will initialize the state on first call.

Returns `0` on success, `-1` on failure to create/open the perf map file,
or `-2` on failure to create a lock. Check `errno` for more information
about the cause of a failure.

intPyUnstable\_WritePerfMapEntry(constvoid\*code\_addr, unsignedintcode\_size, constchar\*entry\_name) [¶](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_WritePerfMapEntry "Link to this definition")

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api). It may change without warning in minor releases._

Write one single entry to the `/tmp/perf-$pid.map` file. This function is
thread safe. Here is what an example entry looks like:

```
# address      size  name
7f3529fcf759 b     py::bar:/run/t.py
```

Will call [`PyUnstable_PerfMapState_Init()`](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_PerfMapState_Init "PyUnstable_PerfMapState_Init") before writing the entry, if
the perf map file is not already opened. Returns `0` on success, or the
same error codes as [`PyUnstable_PerfMapState_Init()`](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_PerfMapState_Init "PyUnstable_PerfMapState_Init") on failure.

voidPyUnstable\_PerfMapState\_Fini(void) [¶](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_PerfMapState_Fini "Link to this definition")

_This is [Unstable API](https://docs.python.org/3/c-api/stable.html#unstable-c-api). It may change without warning in minor releases._

Close the perf map file opened by [`PyUnstable_PerfMapState_Init()`](https://docs.python.org/3/c-api/perfmaps.html#c.PyUnstable_PerfMapState_Init "PyUnstable_PerfMapState_Init").
This is called by the runtime itself during interpreter shut-down. In
general, there shouldn’t be a reason to explicitly call this, except to
handle specific scenarios such as forking.

#### Previous topic

[PyTime C API](https://docs.python.org/3/c-api/time.html "previous chapter")

#### Next topic

[Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/c-api/perfmaps.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/abstract.html "Abstract Objects Layer") \|
- [previous](https://docs.python.org/3/c-api/time.html "PyTime C API") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Utilities](https://docs.python.org/3/c-api/utilities.html) »
- [Support for Perf Maps](https://docs.python.org/3/c-api/perfmaps.html)
- \|

- Theme
AutoLightDark \|