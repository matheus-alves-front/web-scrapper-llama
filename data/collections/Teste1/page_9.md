### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/datetime.html "DateTime Objects") \|
- [previous](https://docs.python.org/3/c-api/typehints.html "Objects for Type Hinting") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html) »
- [Curses C API](https://docs.python.org/3/c-api/curses.html)
- \|

- Theme
AutoLightDark \|

# Curses C API [¶](https://docs.python.org/3/c-api/curses.html\#curses-c-api "Link to this heading")

[`curses`](https://docs.python.org/3/library/curses.html#module-curses "curses: An interface to the curses library, providing portable terminal handling. (Unix)") exposes a small C interface for extension modules.
Consumers must include the header file `py_curses.h` (which is not
included by default by `Python.h`) and [`import_curses()`](https://docs.python.org/3/c-api/curses.html#c.import_curses "import_curses") must
be invoked, usually as part of the module initialisation function, to populate
[`PyCurses_API`](https://docs.python.org/3/c-api/curses.html#c.PyCurses_API "PyCurses_API").

Warning

Neither the C API nor the pure Python [`curses`](https://docs.python.org/3/library/curses.html#module-curses "curses: An interface to the curses library, providing portable terminal handling. (Unix)") module are compatible
with subinterpreters.

import\_curses() [¶](https://docs.python.org/3/c-api/curses.html#c.import_curses "Link to this definition")

Import the curses C API. The macro does not need a semi-colon to be called.

On success, populate the [`PyCurses_API`](https://docs.python.org/3/c-api/curses.html#c.PyCurses_API "PyCurses_API") pointer.

On failure, set [`PyCurses_API`](https://docs.python.org/3/c-api/curses.html#c.PyCurses_API "PyCurses_API") to NULL and set an exception.
The caller must check if an error occurred via [`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred"):

```
import_curses();  // semi-colon is optional but recommended
if (PyErr_Occurred()) { /* cleanup */ }
```

void\*\*PyCurses\_API [¶](https://docs.python.org/3/c-api/curses.html#c.PyCurses_API "Link to this definition")

Dynamically allocated object containing the curses C API.
This variable is only available once [`import_curses`](https://docs.python.org/3/c-api/curses.html#c.import_curses "import_curses") succeeds.

`PyCurses_API[0]` corresponds to [`PyCursesWindow_Type`](https://docs.python.org/3/c-api/curses.html#c.PyCursesWindow_Type "PyCursesWindow_Type").

`PyCurses_API[1]`, `PyCurses_API[2]`, and `PyCurses_API[3]`
are pointers to predicate functions of type `int (*)(void)`.

When called, these predicates return whether [`curses.setupterm()`](https://docs.python.org/3/library/curses.html#curses.setupterm "curses.setupterm"),
[`curses.initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr"), and [`curses.start_color()`](https://docs.python.org/3/library/curses.html#curses.start_color "curses.start_color") have been called
respectively.

See also the convenience macros [`PyCursesSetupTermCalled`](https://docs.python.org/3/c-api/curses.html#c.PyCursesSetupTermCalled "PyCursesSetupTermCalled"),
[`PyCursesInitialised`](https://docs.python.org/3/c-api/curses.html#c.PyCursesInitialised "PyCursesInitialised"), and [`PyCursesInitialisedColor`](https://docs.python.org/3/c-api/curses.html#c.PyCursesInitialisedColor "PyCursesInitialisedColor").

Note

The number of entries in this structure is subject to changes.
Consider using [`PyCurses_API_pointers`](https://docs.python.org/3/c-api/curses.html#c.PyCurses_API_pointers "PyCurses_API_pointers") to check if
new fields are available or not.

PyCurses\_API\_pointers [¶](https://docs.python.org/3/c-api/curses.html#c.PyCurses_API_pointers "Link to this definition")

The number of accessible fields (`4`) in [`PyCurses_API`](https://docs.python.org/3/c-api/curses.html#c.PyCurses_API "PyCurses_API").
This number is incremented whenever new fields are added.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject") PyCursesWindow\_Type [¶](https://docs.python.org/3/c-api/curses.html#c.PyCursesWindow_Type "Link to this definition")

The [heap type](https://docs.python.org/3/c-api/typeobj.html#heap-types) corresponding to [`curses.window`](https://docs.python.org/3/library/curses.html#curses.window "curses.window").

intPyCursesWindow\_Check( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*op) [¶](https://docs.python.org/3/c-api/curses.html#c.PyCursesWindow_Check "Link to this definition")

Return true if _op_ is a [`curses.window`](https://docs.python.org/3/library/curses.html#curses.window "curses.window") instance, false otherwise.

The following macros are convenience macros expanding into C statements.
In particular, they can only be used as `macro;` or `macro`, but not
`macro()` or `macro();`.

PyCursesSetupTermCalled [¶](https://docs.python.org/3/c-api/curses.html#c.PyCursesSetupTermCalled "Link to this definition")

Macro checking if [`curses.setupterm()`](https://docs.python.org/3/library/curses.html#curses.setupterm "curses.setupterm") has been called.

The macro expansion is roughly equivalent to:

```
{
    typedef int (*predicate_t)(void);
    predicate_t was_setupterm_called = (predicate_t)PyCurses_API[1];
    if (!was_setupterm_called()) {
        return NULL;
    }
}
```

PyCursesInitialised [¶](https://docs.python.org/3/c-api/curses.html#c.PyCursesInitialised "Link to this definition")

Macro checking if [`curses.initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr") has been called.

The macro expansion is roughly equivalent to:

```
{
    typedef int (*predicate_t)(void);
    predicate_t was_initscr_called = (predicate_t)PyCurses_API[2];
    if (!was_initscr_called()) {
        return NULL;
    }
}
```

PyCursesInitialisedColor [¶](https://docs.python.org/3/c-api/curses.html#c.PyCursesInitialisedColor "Link to this definition")

Macro checking if [`curses.start_color()`](https://docs.python.org/3/library/curses.html#curses.start_color "curses.start_color") has been called.

The macro expansion is roughly equivalent to:

```
{
    typedef int (*predicate_t)(void);
    predicate_t was_start_color_called = (predicate_t)PyCurses_API[3];
    if (!was_start_color_called()) {
        return NULL;
    }
}
```

# Internal data [¶](https://docs.python.org/3/c-api/curses.html\#internal-data "Link to this heading")

The following objects are exposed by the C API but should be considered
internal-only.

PyCurses\_CAPSULE\_NAME [¶](https://docs.python.org/3/c-api/curses.html#c.PyCurses_CAPSULE_NAME "Link to this definition")

Name of the curses capsule to pass to [`PyCapsule_Import()`](https://docs.python.org/3/c-api/capsule.html#c.PyCapsule_Import "PyCapsule_Import").

Internal usage only. Use [`import_curses`](https://docs.python.org/3/c-api/curses.html#c.import_curses "import_curses") instead.

### [Table of Contents](https://docs.python.org/3/contents.html)

- [Curses C API](https://docs.python.org/3/c-api/curses.html#)
- [Internal data](https://docs.python.org/3/c-api/curses.html#internal-data)

#### Previous topic

[Objects for Type Hinting](https://docs.python.org/3/c-api/typehints.html "previous chapter")

#### Next topic

[DateTime Objects](https://docs.python.org/3/c-api/datetime.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/c-api/curses.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/datetime.html "DateTime Objects") \|
- [previous](https://docs.python.org/3/c-api/typehints.html "Objects for Type Hinting") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html) »
- [Curses C API](https://docs.python.org/3/c-api/curses.html)
- \|

- Theme
AutoLightDark \|