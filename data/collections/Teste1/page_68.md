### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/faq/windows.html "Python on Windows FAQ") \|
- [previous](https://docs.python.org/3/faq/library.html "Library and Extension FAQ") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python Frequently Asked Questions](https://docs.python.org/3/faq/index.html) »
- [Extending/Embedding FAQ](https://docs.python.org/3/faq/extending.html)
- \|

- Theme
AutoLightDark \|

# [Extending/Embedding FAQ](https://docs.python.org/3/faq/extending.html\#id2) [¶](https://docs.python.org/3/faq/extending.html\#extending-embedding-faq "Link to this heading")

## [Can I create my own functions in C?](https://docs.python.org/3/faq/extending.html\#id3) [¶](https://docs.python.org/3/faq/extending.html\#can-i-create-my-own-functions-in-c "Link to this heading")

Yes, you can create built-in modules containing functions, variables, exceptions
and even new types in C. This is explained in the document
[Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html#extending-index).

Most intermediate or advanced Python books will also cover this topic.

## [Can I create my own functions in C++?](https://docs.python.org/3/faq/extending.html\#id4) [¶](https://docs.python.org/3/faq/extending.html\#id1 "Link to this heading")

Yes, using the C compatibility features found in C++. Place `extern "C" {
... }` around the Python include files and put `extern "C"` before each
function that is going to be called by the Python interpreter. Global or static
C++ objects with constructors are probably not a good idea.

## [Writing C is hard; are there any alternatives?](https://docs.python.org/3/faq/extending.html\#id5) [¶](https://docs.python.org/3/faq/extending.html\#writing-c-is-hard-are-there-any-alternatives "Link to this heading")

There are a number of alternatives to writing your own C extensions, depending
on what you’re trying to do. [Recommended third party tools](https://docs.python.org/3/c-api/intro.html#c-api-tools)
offer both simpler and more sophisticated approaches to creating C and C++
extensions for Python.

## [How can I execute arbitrary Python statements from C?](https://docs.python.org/3/faq/extending.html\#id6) [¶](https://docs.python.org/3/faq/extending.html\#how-can-i-execute-arbitrary-python-statements-from-c "Link to this heading")

The highest-level function to do this is [`PyRun_SimpleString()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_SimpleString "PyRun_SimpleString") which takes
a single string argument to be executed in the context of the module
`__main__` and returns `0` for success and `-1` when an exception occurred
(including [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError")). If you want more control, use
[`PyRun_String()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_String "PyRun_String"); see the source for [`PyRun_SimpleString()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_SimpleString "PyRun_SimpleString") in
`Python/pythonrun.c`.

## [How can I evaluate an arbitrary Python expression from C?](https://docs.python.org/3/faq/extending.html\#id7) [¶](https://docs.python.org/3/faq/extending.html\#how-can-i-evaluate-an-arbitrary-python-expression-from-c "Link to this heading")

Call the function [`PyRun_String()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_String "PyRun_String") from the previous question with the
start symbol [`Py_eval_input`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_eval_input "Py_eval_input"); it parses an expression, evaluates it and
returns its value.

## [How do I extract C values from a Python object?](https://docs.python.org/3/faq/extending.html\#id8) [¶](https://docs.python.org/3/faq/extending.html\#how-do-i-extract-c-values-from-a-python-object "Link to this heading")

That depends on the object’s type. If it’s a tuple, [`PyTuple_Size()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_Size "PyTuple_Size")
returns its length and [`PyTuple_GetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_GetItem "PyTuple_GetItem") returns the item at a specified
index. Lists have similar functions, [`PyList_Size()`](https://docs.python.org/3/c-api/list.html#c.PyList_Size "PyList_Size") and
[`PyList_GetItem()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItem "PyList_GetItem").

For bytes, [`PyBytes_Size()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Size "PyBytes_Size") returns its length and
[`PyBytes_AsStringAndSize()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_AsStringAndSize "PyBytes_AsStringAndSize") provides a pointer to its value and its
length. Note that Python bytes objects may contain null bytes so C’s
`strlen()` should not be used.

To test the type of an object, first make sure it isn’t `NULL`, and then use
[`PyBytes_Check()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_Check "PyBytes_Check"), [`PyTuple_Check()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_Check "PyTuple_Check"), [`PyList_Check()`](https://docs.python.org/3/c-api/list.html#c.PyList_Check "PyList_Check"), etc.

There is also a high-level API to Python objects which is provided by the
so-called ‘abstract’ interface – read `Include/abstract.h` for further
details. It allows interfacing with any kind of Python sequence using calls
like [`PySequence_Length()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_Length "PySequence_Length"), [`PySequence_GetItem()`](https://docs.python.org/3/c-api/sequence.html#c.PySequence_GetItem "PySequence_GetItem"), etc. as well
as many other useful protocols such as numbers ( [`PyNumber_Index()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Index "PyNumber_Index") et
al.) and mappings in the PyMapping APIs.

## [How do I use Py\_BuildValue() to create a tuple of arbitrary length?](https://docs.python.org/3/faq/extending.html\#id9) [¶](https://docs.python.org/3/faq/extending.html\#how-do-i-use-py-buildvalue-to-create-a-tuple-of-arbitrary-length "Link to this heading")

You can’t. Use [`PyTuple_Pack()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_Pack "PyTuple_Pack") instead.

## [How do I call an object’s method from C?](https://docs.python.org/3/faq/extending.html\#id10) [¶](https://docs.python.org/3/faq/extending.html\#how-do-i-call-an-object-s-method-from-c "Link to this heading")

The [`PyObject_CallMethod()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethod "PyObject_CallMethod") function can be used to call an arbitrary
method of an object. The parameters are the object, the name of the method to
call, a format string like that used with [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "Py_BuildValue"), and the
argument values:

```
PyObject *
PyObject_CallMethod(PyObject *object, const char *method_name,
                    const char *arg_format, ...);
```

This works for any object that has methods – whether built-in or user-defined.
You are responsible for eventually [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF")‘ing the return value.

To call, e.g., a file object’s “seek” method with arguments 10, 0 (assuming the
file object pointer is “f”):

```
res = PyObject_CallMethod(f, "seek", "(ii)", 10, 0);
if (res == NULL) {
        ... an exception occurred ...
}
else {
        Py_DECREF(res);
}
```

Note that since [`PyObject_CallObject()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallObject "PyObject_CallObject") _always_ wants a tuple for the
argument list, to call a function without arguments, pass “()” for the format,
and to call a function with one argument, surround the argument in parentheses,
e.g. “(i)”.

## [How do I catch the output from PyErr\_Print() (or anything that prints to stdout/stderr)?](https://docs.python.org/3/faq/extending.html\#id11) [¶](https://docs.python.org/3/faq/extending.html\#how-do-i-catch-the-output-from-pyerr-print-or-anything-that-prints-to-stdout-stderr "Link to this heading")

In Python code, define an object that supports the `write()` method. Assign
this object to [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") and [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr"). Call print\_error, or
just allow the standard traceback mechanism to work. Then, the output will go
wherever your `write()` method sends it.

The easiest way to do this is to use the [`io.StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") class:

Copy

```
>>> import io, sys
>>> sys.stdout = io.StringIO()
>>> print('foo')
>>> print('hello world!')
>>> sys.stderr.write(sys.stdout.getvalue())
foo
hello world!
```

A custom object to do the same would look like this:

Copy

```
>>> import io, sys
>>> class StdoutCatcher(io.TextIOBase):
...     def __init__(self):
...         self.data = []
...     def write(self, stuff):
...         self.data.append(stuff)
...
>>> import sys
>>> sys.stdout = StdoutCatcher()
>>> print('foo')
>>> print('hello world!')
>>> sys.stderr.write(''.join(sys.stdout.data))
foo
hello world!
```

## [How do I access a module written in Python from C?](https://docs.python.org/3/faq/extending.html\#id12) [¶](https://docs.python.org/3/faq/extending.html\#how-do-i-access-a-module-written-in-python-from-c "Link to this heading")

You can get a pointer to the module object as follows:

```
module = PyImport_ImportModule("<modulename>");
```

If the module hasn’t been imported yet (i.e. it is not yet present in
[`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")), this initializes the module; otherwise it simply returns
the value of `sys.modules["<modulename>"]`. Note that it doesn’t enter the
module into any namespace – it only ensures it has been initialized and is
stored in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules").

You can then access the module’s attributes (i.e. any name defined in the
module) as follows:

```
attr = PyObject_GetAttrString(module, "<attrname>");
```

Calling [`PyObject_SetAttrString()`](https://docs.python.org/3/c-api/object.html#c.PyObject_SetAttrString "PyObject_SetAttrString") to assign to variables in the module
also works.

## [How do I interface to C++ objects from Python?](https://docs.python.org/3/faq/extending.html\#id13) [¶](https://docs.python.org/3/faq/extending.html\#how-do-i-interface-to-c-objects-from-python "Link to this heading")

Depending on your requirements, there are many approaches. To do this manually,
begin by reading [the “Extending and Embedding” document](https://docs.python.org/3/extending/index.html#extending-index). Realize that for the Python run-time system, there isn’t a
whole lot of difference between C and C++ – so the strategy of building a new
Python type around a C structure (pointer) type will also work for C++ objects.

For C++ libraries, see [Writing C is hard; are there any alternatives?](https://docs.python.org/3/faq/extending.html#c-wrapper-software).

## [I added a module using the Setup file and the make fails; why?](https://docs.python.org/3/faq/extending.html\#id14) [¶](https://docs.python.org/3/faq/extending.html\#i-added-a-module-using-the-setup-file-and-the-make-fails-why "Link to this heading")

Setup must end in a newline, if there is no newline there, the build process
fails. (Fixing this requires some ugly shell script hackery, and this bug is so
minor that it doesn’t seem worth the effort.)

## [How do I debug an extension?](https://docs.python.org/3/faq/extending.html\#id15) [¶](https://docs.python.org/3/faq/extending.html\#how-do-i-debug-an-extension "Link to this heading")

When using GDB with dynamically loaded extensions, you can’t set a breakpoint in
your extension until your extension is loaded.

In your `.gdbinit` file (or interactively), add the command:

```
br _PyImport_LoadDynamicModule
```

Then, when you run GDB:

```
$ gdb /local/bin/python
gdb) run myscript.py
gdb) continue # repeat until your extension is loaded
gdb) finish   # so that your extension is loaded
gdb) br myfunction.c:50
gdb) continue
```

## [I want to compile a Python module on my Linux system, but some files are missing. Why?](https://docs.python.org/3/faq/extending.html\#id16) [¶](https://docs.python.org/3/faq/extending.html\#i-want-to-compile-a-python-module-on-my-linux-system-but-some-files-are-missing-why "Link to this heading")

Most packaged versions of Python omit some files
required for compiling Python extensions.

For Red Hat, install the python3-devel RPM to get the necessary files.

For Debian, run `apt-get install python3-dev`.

## [How do I tell “incomplete input” from “invalid input”?](https://docs.python.org/3/faq/extending.html\#id17) [¶](https://docs.python.org/3/faq/extending.html\#how-do-i-tell-incomplete-input-from-invalid-input "Link to this heading")

Sometimes you want to emulate the Python interactive interpreter’s behavior,
where it gives you a continuation prompt when the input is incomplete (e.g. you
typed the start of an “if” statement or you didn’t close your parentheses or
triple string quotes), but it gives you a syntax error message immediately when
the input is invalid.

In Python you can use the [`codeop`](https://docs.python.org/3/library/codeop.html#module-codeop "codeop: Compile (possibly incomplete) Python code.") module, which approximates the parser’s
behavior sufficiently. IDLE uses this, for example.

The easiest way to do it in C is to call [`PyRun_InteractiveLoop()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_InteractiveLoop "PyRun_InteractiveLoop") (perhaps
in a separate thread) and let the Python interpreter handle the input for
you. You can also set the [`PyOS_ReadlineFunctionPointer()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_ReadlineFunctionPointer "PyOS_ReadlineFunctionPointer") to point at your
custom input function. See `Modules/readline.c` and `Parser/myreadline.c`
for more hints.

## [How do I find undefined g++ symbols \_\_builtin\_new or \_\_pure\_virtual?](https://docs.python.org/3/faq/extending.html\#id18) [¶](https://docs.python.org/3/faq/extending.html\#how-do-i-find-undefined-g-symbols-builtin-new-or-pure-virtual "Link to this heading")

To dynamically load g++ extension modules, you must recompile Python, relink it
using g++ (change LINKCC in the Python Modules Makefile), and link your
extension module using g++ (e.g., `g++ -shared -o mymodule.so mymodule.o`).

## [Can I create an object class with some methods implemented in C and others in Python (e.g. through inheritance)?](https://docs.python.org/3/faq/extending.html\#id19) [¶](https://docs.python.org/3/faq/extending.html\#can-i-create-an-object-class-with-some-methods-implemented-in-c-and-others-in-python-e-g-through-inheritance "Link to this heading")

Yes, you can inherit from built-in classes such as [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"),
[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), etc.

The Boost Python Library (BPL, [https://www.boost.org/libs/python/doc/index.html](https://www.boost.org/libs/python/doc/index.html))
provides a way of doing this from C++ (i.e. you can inherit from an extension
class written in C++ using the BPL).

### [Table of Contents](https://docs.python.org/3/contents.html)

- [Extending/Embedding FAQ](https://docs.python.org/3/faq/extending.html#)
  - [Can I create my own functions in C?](https://docs.python.org/3/faq/extending.html#can-i-create-my-own-functions-in-c)
  - [Can I create my own functions in C++?](https://docs.python.org/3/faq/extending.html#id1)
  - [Writing C is hard; are there any alternatives?](https://docs.python.org/3/faq/extending.html#writing-c-is-hard-are-there-any-alternatives)
  - [How can I execute arbitrary Python statements from C?](https://docs.python.org/3/faq/extending.html#how-can-i-execute-arbitrary-python-statements-from-c)
  - [How can I evaluate an arbitrary Python expression from C?](https://docs.python.org/3/faq/extending.html#how-can-i-evaluate-an-arbitrary-python-expression-from-c)
  - [How do I extract C values from a Python object?](https://docs.python.org/3/faq/extending.html#how-do-i-extract-c-values-from-a-python-object)
  - [How do I use Py\_BuildValue() to create a tuple of arbitrary length?](https://docs.python.org/3/faq/extending.html#how-do-i-use-py-buildvalue-to-create-a-tuple-of-arbitrary-length)
  - [How do I call an object’s method from C?](https://docs.python.org/3/faq/extending.html#how-do-i-call-an-object-s-method-from-c)
  - [How do I catch the output from PyErr\_Print() (or anything that prints to stdout/stderr)?](https://docs.python.org/3/faq/extending.html#how-do-i-catch-the-output-from-pyerr-print-or-anything-that-prints-to-stdout-stderr)
  - [How do I access a module written in Python from C?](https://docs.python.org/3/faq/extending.html#how-do-i-access-a-module-written-in-python-from-c)
  - [How do I interface to C++ objects from Python?](https://docs.python.org/3/faq/extending.html#how-do-i-interface-to-c-objects-from-python)
  - [I added a module using the Setup file and the make fails; why?](https://docs.python.org/3/faq/extending.html#i-added-a-module-using-the-setup-file-and-the-make-fails-why)
  - [How do I debug an extension?](https://docs.python.org/3/faq/extending.html#how-do-i-debug-an-extension)
  - [I want to compile a Python module on my Linux system, but some files are missing. Why?](https://docs.python.org/3/faq/extending.html#i-want-to-compile-a-python-module-on-my-linux-system-but-some-files-are-missing-why)
  - [How do I tell “incomplete input” from “invalid input”?](https://docs.python.org/3/faq/extending.html#how-do-i-tell-incomplete-input-from-invalid-input)
  - [How do I find undefined g++ symbols \_\_builtin\_new or \_\_pure\_virtual?](https://docs.python.org/3/faq/extending.html#how-do-i-find-undefined-g-symbols-builtin-new-or-pure-virtual)
  - [Can I create an object class with some methods implemented in C and others in Python (e.g. through inheritance)?](https://docs.python.org/3/faq/extending.html#can-i-create-an-object-class-with-some-methods-implemented-in-c-and-others-in-python-e-g-through-inheritance)

#### Previous topic

[Library and Extension FAQ](https://docs.python.org/3/faq/library.html "previous chapter")

#### Next topic

[Python on Windows FAQ](https://docs.python.org/3/faq/windows.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/faq/extending.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/faq/windows.html "Python on Windows FAQ") \|
- [previous](https://docs.python.org/3/faq/library.html "Library and Extension FAQ") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python Frequently Asked Questions](https://docs.python.org/3/faq/index.html) »
- [Extending/Embedding FAQ](https://docs.python.org/3/faq/extending.html)
- \|

- Theme
AutoLightDark \|