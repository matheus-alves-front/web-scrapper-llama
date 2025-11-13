### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/utilities.html "Utilities") \|
- [previous](https://docs.python.org/3/c-api/exceptions.html "Exception Handling") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Defining extension modules](https://docs.python.org/3/c-api/extension-modules.html)
- \|

- Theme
AutoLightDark \|

# Defining extension modules [¶](https://docs.python.org/3/c-api/extension-modules.html\#defining-extension-modules "Link to this heading")

A C extension for CPython is a shared library (for example, a `.so` file
on Linux, `.pyd` DLL on Windows), which is loadable into the Python process
(for example, it is compiled with compatible compiler settings), and which
exports an [initialization function](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook).

To be importable by default (that is, by
[`importlib.machinery.ExtensionFileLoader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader "importlib.machinery.ExtensionFileLoader")),
the shared library must be available on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path"),
and must be named after the module name plus an extension listed in
[`importlib.machinery.EXTENSION_SUFFIXES`](https://docs.python.org/3/library/importlib.html#importlib.machinery.EXTENSION_SUFFIXES "importlib.machinery.EXTENSION_SUFFIXES").

Note

Building, packaging and distributing extension modules is best done with
third-party tools, and is out of scope of this document.
One suitable tool is Setuptools, whose documentation can be found at
[https://setuptools.pypa.io/en/latest/setuptools.html](https://setuptools.pypa.io/en/latest/setuptools.html).

Normally, the initialization function returns a module definition initialized
using [`PyModuleDef_Init()`](https://docs.python.org/3/c-api/extension-modules.html#c.PyModuleDef_Init "PyModuleDef_Init").
This allows splitting the creation process into several phases:

- Before any substantial code is executed, Python can determine which
capabilities the module supports, and it can adjust the environment or
refuse loading an incompatible extension.

- By default, Python itself creates the module object – that is, it does
the equivalent of [`object.__new__()`](https://docs.python.org/3/reference/datamodel.html#object.__new__ "object.__new__") for classes.
It also sets initial attributes like [`__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__") and
[`__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__").

- Afterwards, the module object is initialized using extension-specific
code – the equivalent of [`__init__()`](https://docs.python.org/3/reference/datamodel.html#object.__init__ "object.__init__") on classes.


This is called _multi-phase initialization_ to distinguish it from the legacy
(but still supported) _single-phase initialization_ scheme,
where the initialization function returns a fully constructed module.
See the [single-phase-initialization section below](https://docs.python.org/3/c-api/extension-modules.html#single-phase-initialization)
for details.

Changed in version 3.5: Added support for multi-phase initialization ( [**PEP 489**](https://peps.python.org/pep-0489/)).

## Multiple module instances [¶](https://docs.python.org/3/c-api/extension-modules.html\#multiple-module-instances "Link to this heading")

By default, extension modules are not singletons.
For example, if the [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules") entry is removed and the module
is re-imported, a new module object is created, and typically populated with
fresh method and type objects.
The old module is subject to normal garbage collection.
This mirrors the behavior of pure-Python modules.

Additional module instances may be created in
[sub-interpreters](https://docs.python.org/3/c-api/init.html#sub-interpreter-support)
or after Python runtime reinitialization
( [`Py_Finalize()`](https://docs.python.org/3/c-api/init.html#c.Py_Finalize "Py_Finalize") and [`Py_Initialize()`](https://docs.python.org/3/c-api/init.html#c.Py_Initialize "Py_Initialize")).
In these cases, sharing Python objects between module instances would likely
cause crashes or undefined behavior.

To avoid such issues, each instance of an extension module should
be _isolated_: changes to one instance should not implicitly affect the others,
and all state owned by the module, including references to Python objects,
should be specific to a particular module instance.
See [Isolating Extension Modules](https://docs.python.org/3/howto/isolating-extensions.html#isolating-extensions-howto) for more details and a practical guide.

A simpler way to avoid these issues is
[raising an error on repeated initialization](https://docs.python.org/3/howto/isolating-extensions.html#isolating-extensions-optout).

All modules are expected to support
[sub-interpreters](https://docs.python.org/3/c-api/init.html#sub-interpreter-support), or otherwise explicitly
signal a lack of support.
This is usually achieved by isolation or blocking repeated initialization,
as above.
A module may also be limited to the main interpreter using
the [`Py_mod_multiple_interpreters`](https://docs.python.org/3/c-api/module.html#c.Py_mod_multiple_interpreters "Py_mod_multiple_interpreters") slot.

## Initialization function [¶](https://docs.python.org/3/c-api/extension-modules.html\#initialization-function "Link to this heading")

The initialization function defined by an extension module has the
following signature:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyInit\_modulename(void) [¶](https://docs.python.org/3/c-api/extension-modules.html#c.PyInit_modulename "Link to this definition")

Its name should be `PyInit_<name>`, with `<name>` replaced by the
name of the module.

For modules with ASCII-only names, the function must instead be named
`PyInit_<name>`, with `<name>` replaced by the name of the module.
When using [Multi-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization), non-ASCII module names
are allowed. In this case, the initialization function name is
`PyInitU_<name>`, with `<name>` encoded using Python’s
_punycode_ encoding with hyphens replaced by underscores. In Python:

Copy

```
def initfunc_name(name):
    try:
        suffix = b'_' + name.encode('ascii')
    except UnicodeEncodeError:
        suffix = b'U_' + name.encode('punycode').replace(b'-', b'_')
    return b'PyInit' + suffix
```

It is recommended to define the initialization function using a helper macro:

PyMODINIT\_FUNC [¶](https://docs.python.org/3/c-api/extension-modules.html#c.PyMODINIT_FUNC "Link to this definition")

Declare an extension module initialization function.
This macro:

- specifies the [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\* return type,

- adds any special linkage declarations required by the platform, and

- for C++, declares the function as `extern "C"`.


For example, a module called `spam` would be defined like this:

```
static struct PyModuleDef spam_module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "spam",
    ...
};

PyMODINIT_FUNC
PyInit_spam(void)
{
    return PyModuleDef_Init(&spam_module);
}
```

It is possible to export multiple modules from a single shared library by
defining multiple initialization functions. However, importing them requires
using symbolic links or a custom importer, because by default only the
function corresponding to the filename is found.
See the [Multiple modules in one library](https://peps.python.org/pep-0489/#multiple-modules-in-one-library)
section in [**PEP 489**](https://peps.python.org/pep-0489/) for details.

The initialization function is typically the only non-`static`
item defined in the module’s C source.

## Multi-phase initialization [¶](https://docs.python.org/3/c-api/extension-modules.html\#multi-phase-initialization "Link to this heading")

Normally, the [initialization function](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
(`PyInit_modulename`) returns a [`PyModuleDef`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef") instance with
non-`NULL` [`m_slots`](https://docs.python.org/3/c-api/module.html#c.PyModuleDef.m_slots "PyModuleDef.m_slots").
Before it is returned, the `PyModuleDef` instance must be initialized
using the following function:

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyModuleDef\_Init( [PyModuleDef](https://docs.python.org/3/c-api/module.html#c.PyModuleDef "PyModuleDef")\*def) [¶](https://docs.python.org/3/c-api/extension-modules.html#c.PyModuleDef_Init "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable) since version 3.5._

Ensure a module definition is a properly initialized Python object that
correctly reports its type and a reference count.

Return _def_ cast to `PyObject*`, or `NULL` if an error occurred.

Calling this function is required for [Multi-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization).
It should not be used in other contexts.

Note that Python assumes that `PyModuleDef` structures are statically
allocated.
This function may return either a new reference or a borrowed one;
this reference must not be released.

Added in version 3.5.

## Legacy single-phase initialization [¶](https://docs.python.org/3/c-api/extension-modules.html\#legacy-single-phase-initialization "Link to this heading")

Attention

Single-phase initialization is a legacy mechanism to initialize extension
modules, with known drawbacks and design flaws. Extension module authors
are encouraged to use multi-phase initialization instead.

In single-phase initialization, the
[initialization function](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook) (`PyInit_modulename`)
should create, populate and return a module object.
This is typically done using [`PyModule_Create()`](https://docs.python.org/3/c-api/module.html#c.PyModule_Create "PyModule_Create") and functions like
[`PyModule_AddObjectRef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef").

Single-phase initialization differs from the [default](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
in the following ways:

- Single-phase modules are, or rather _contain_, “singletons”.

When the module is first initialized, Python saves the contents of
the module’s `__dict__` (that is, typically, the module’s functions and
types).

For subsequent imports, Python does not call the initialization function
again.
Instead, it creates a new module object with a new `__dict__`, and copies
the saved contents to it.
For example, given a single-phase module `_testsinglephase` [\[1\]](https://docs.python.org/3/c-api/extension-modules.html#testsinglephase) that defines a function `sum` and an exception class
`error`:



Copy

```
>>> import sys
>>> import _testsinglephase as one
>>> del sys.modules['_testsinglephase']
>>> import _testsinglephase as two
>>> one is two
False
>>> one.__dict__ is two.__dict__
False
>>> one.sum is two.sum
True
>>> one.error is two.error
True
```





The exact behavior should be considered a CPython implementation detail.

- To work around the fact that `PyInit_modulename` does not take a _spec_
argument, some state of the import machinery is saved and applied to the
first suitable module created during the `PyInit_modulename` call.
Specifically, when a sub-module is imported, this mechanism prepends the
parent package name to the name of the module.

A single-phase `PyInit_modulename` function should create “its” module
object as soon as possible, before any other module objects can be created.

- Non-ASCII module names (`PyInitU_modulename`) are not supported.

- Single-phase modules support module lookup functions like
[`PyState_FindModule()`](https://docs.python.org/3/c-api/module.html#c.PyState_FindModule "PyState_FindModule").


### [Table of Contents](https://docs.python.org/3/contents.html)

- [Defining extension modules](https://docs.python.org/3/c-api/extension-modules.html#)
  - [Multiple module instances](https://docs.python.org/3/c-api/extension-modules.html#multiple-module-instances)
  - [Initialization function](https://docs.python.org/3/c-api/extension-modules.html#initialization-function)
  - [Multi-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#multi-phase-initialization)
  - [Legacy single-phase initialization](https://docs.python.org/3/c-api/extension-modules.html#legacy-single-phase-initialization)

#### Previous topic

[Exception Handling](https://docs.python.org/3/c-api/exceptions.html "previous chapter")

#### Next topic

[Utilities](https://docs.python.org/3/c-api/utilities.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/c-api/extension-modules.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/utilities.html "Utilities") \|
- [previous](https://docs.python.org/3/c-api/exceptions.html "Exception Handling") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Defining extension modules](https://docs.python.org/3/c-api/extension-modules.html)
- \|

- Theme
AutoLightDark \|