### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/time.html "time — Time access and conversions") \|
- [previous](https://docs.python.org/3/library/os.html "os — Miscellaneous operating system interfaces") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Generic Operating System Services](https://docs.python.org/3/library/allos.html) »
- [`io` — Core tools for working with streams](https://docs.python.org/3/library/io.html)
- \|

- Theme
AutoLightDark \|

# `io` — Core tools for working with streams [¶](https://docs.python.org/3/library/io.html\#module-io "Link to this heading")

**Source code:** [Lib/io.py](https://github.com/python/cpython/tree/3.14/Lib/io.py)

* * *

## Overview [¶](https://docs.python.org/3/library/io.html\#overview "Link to this heading")

The [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.") module provides Python’s main facilities for dealing with various
types of I/O. There are three main types of I/O: _text I/O_, _binary I/O_
and _raw I/O_. These are generic categories, and various backing stores can
be used for each of them. A concrete object belonging to any of these
categories is called a [file object](https://docs.python.org/3/glossary.html#term-file-object). Other common terms are _stream_
and _file-like object_.

Independent of its category, each concrete stream object will also have
various capabilities: it can be read-only, write-only, or read-write. It can
also allow arbitrary random access (seeking forwards or backwards to any
location), or only sequential access (for example in the case of a socket or
pipe).

All streams are careful about the type of data you give to them. For example
giving a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") object to the `write()` method of a binary stream
will raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). So will giving a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object to the
`write()` method of a text stream.

Changed in version 3.3: Operations that used to raise [`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") now raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError"), since
[`IOError`](https://docs.python.org/3/library/exceptions.html#IOError "IOError") is now an alias of [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

### Text I/O [¶](https://docs.python.org/3/library/io.html\#text-i-o "Link to this heading")

Text I/O expects and produces [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") objects. This means that whenever
the backing store is natively made of bytes (such as in the case of a file),
encoding and decoding of data is made transparently as well as optional
translation of platform-specific newline characters.

The easiest way to create a text stream is with [`open()`](https://docs.python.org/3/library/functions.html#open "open"), optionally
specifying an encoding:

Copy

```
f = open("myfile.txt", "r", encoding="utf-8")
```

In-memory text streams are also available as [`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") objects:

Copy

```
f = io.StringIO("some initial text data")
```

Note

When working with a non-blocking stream, be aware that read operations on text I/O objects
might raise a [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") if the stream cannot perform the operation
immediately.

The text stream API is described in detail in the documentation of
[`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase").

### Binary I/O [¶](https://docs.python.org/3/library/io.html\#binary-i-o "Link to this heading")

Binary I/O (also called _buffered I/O_) expects
[bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) and produces [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")
objects. No encoding, decoding, or newline translation is performed. This
category of streams can be used for all kinds of non-text data, and also when
manual control over the handling of text data is desired.

The easiest way to create a binary stream is with [`open()`](https://docs.python.org/3/library/functions.html#open "open") with `'b'` in
the mode string:

Copy

```
f = open("myfile.jpg", "rb")
```

In-memory binary streams are also available as [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") objects:

Copy

```
f = io.BytesIO(b"some initial binary data: \x00\x01")
```

The binary stream API is described in detail in the docs of
[`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase").

Other library modules may provide additional ways to create text or binary
streams. See [`socket.socket.makefile()`](https://docs.python.org/3/library/socket.html#socket.socket.makefile "socket.socket.makefile") for example.

### Raw I/O [¶](https://docs.python.org/3/library/io.html\#raw-i-o "Link to this heading")

Raw I/O (also called _unbuffered I/O_) is generally used as a low-level
building-block for binary and text streams; it is rarely useful to directly
manipulate a raw stream from user code. Nevertheless, you can create a raw
stream by opening a file in binary mode with buffering disabled:

Copy

```
f = open("myfile.jpg", "rb", buffering=0)
```

The raw stream API is described in detail in the docs of [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase").

## Text Encoding [¶](https://docs.python.org/3/library/io.html\#text-encoding "Link to this heading")

The default encoding of [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") and [`open()`](https://docs.python.org/3/library/functions.html#open "open") is
locale-specific ( [`locale.getencoding()`](https://docs.python.org/3/library/locale.html#locale.getencoding "locale.getencoding")).

However, many developers forget to specify the encoding when opening text files
encoded in UTF-8 (e.g. JSON, TOML, Markdown, etc…) since most Unix
platforms use UTF-8 locale by default. This causes bugs because the locale
encoding is not UTF-8 for most Windows users. For example:

Copy

```
# May not work on Windows when non-ASCII characters in the file.
with open("README.md") as f:
    long_description = f.read()
```

Accordingly, it is highly recommended that you specify the encoding
explicitly when opening text files. If you want to use UTF-8, pass
`encoding="utf-8"`. To use the current locale encoding,
`encoding="locale"` is supported since Python 3.10.

See also

[Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode)

Python UTF-8 Mode can be used to change the default encoding to
UTF-8 from locale-specific encoding.

[**PEP 686**](https://peps.python.org/pep-0686/)

Python 3.15 will make [Python UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode) default.

### Opt-in EncodingWarning [¶](https://docs.python.org/3/library/io.html\#opt-in-encodingwarning "Link to this heading")

Added in version 3.10: See [**PEP 597**](https://peps.python.org/pep-0597/) for more details.

To find where the default locale encoding is used, you can enable
the [`-X warn_default_encoding`](https://docs.python.org/3/using/cmdline.html#cmdoption-X) command line option or set the
[`PYTHONWARNDEFAULTENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNDEFAULTENCODING) environment variable, which will
emit an [`EncodingWarning`](https://docs.python.org/3/library/exceptions.html#EncodingWarning "EncodingWarning") when the default encoding is used.

If you are providing an API that uses [`open()`](https://docs.python.org/3/library/functions.html#open "open") or
[`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") and passes `encoding=None` as a parameter, you
can use [`text_encoding()`](https://docs.python.org/3/library/io.html#io.text_encoding "io.text_encoding") so that callers of the API will emit an
[`EncodingWarning`](https://docs.python.org/3/library/exceptions.html#EncodingWarning "EncodingWarning") if they don’t pass an `encoding`. However,
please consider using UTF-8 by default (i.e. `encoding="utf-8"`) for
new APIs.

## High-level Module Interface [¶](https://docs.python.org/3/library/io.html\#high-level-module-interface "Link to this heading")

io.DEFAULT\_BUFFER\_SIZE [¶](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE "Link to this definition")

An int containing the default buffer size used by the module’s buffered I/O
classes. [`open()`](https://docs.python.org/3/library/functions.html#open "open") uses the file’s blksize (as obtained by
[`os.stat()`](https://docs.python.org/3/library/os.html#os.stat "os.stat")) if possible.

io.open( _file_, _mode='r'_, _buffering=-1_, _encoding=None_, _errors=None_, _newline=None_, _closefd=True_, _opener=None_) [¶](https://docs.python.org/3/library/io.html#io.open "Link to this definition")

This is an alias for the builtin [`open()`](https://docs.python.org/3/library/functions.html#open "open") function.

This function raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)`open` with
arguments _path_, _mode_ and _flags_. The _mode_ and _flags_
arguments may have been modified or inferred from the original call.

io.open\_code( _path_) [¶](https://docs.python.org/3/library/io.html#io.open_code "Link to this definition")

Opens the provided file with mode `'rb'`. This function should be used
when the intent is to treat the contents as executable code.

_path_ should be a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") and an absolute path.

The behavior of this function may be overridden by an earlier call to the
[`PyFile_SetOpenCodeHook()`](https://docs.python.org/3/c-api/file.html#c.PyFile_SetOpenCodeHook "PyFile_SetOpenCodeHook"). However, assuming that _path_ is a
[`str`](https://docs.python.org/3/library/stdtypes.html#str "str") and an absolute path, `open_code(path)` should always behave
the same as `open(path, 'rb')`. Overriding the behavior is intended for
additional validation or preprocessing of the file.

Added in version 3.8.

io.text\_encoding( _encoding_, _stacklevel=2_, _/_) [¶](https://docs.python.org/3/library/io.html#io.text_encoding "Link to this definition")

This is a helper function for callables that use [`open()`](https://docs.python.org/3/library/functions.html#open "open") or
[`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") and have an `encoding=None` parameter.

This function returns _encoding_ if it is not `None`.
Otherwise, it returns `"locale"` or `"utf-8"` depending on
[UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode).

This function emits an [`EncodingWarning`](https://docs.python.org/3/library/exceptions.html#EncodingWarning "EncodingWarning") if
[`sys.flags.warn_default_encoding`](https://docs.python.org/3/library/sys.html#sys.flags "sys.flags") is true and _encoding_
is `None`. _stacklevel_ specifies where the warning is emitted.
For example:

Copy

```
def read_text(path, encoding=None):
    encoding = io.text_encoding(encoding)  # stacklevel=2
    with open(path, encoding) as f:
        return f.read()
```

In this example, an [`EncodingWarning`](https://docs.python.org/3/library/exceptions.html#EncodingWarning "EncodingWarning") is emitted for the caller of
`read_text()`.

See [Text Encoding](https://docs.python.org/3/library/io.html#io-text-encoding) for more information.

Added in version 3.10.

Changed in version 3.11: [`text_encoding()`](https://docs.python.org/3/library/io.html#io.text_encoding "io.text_encoding") returns “utf-8” when UTF-8 mode is enabled and
_encoding_ is `None`.

_exception_ io.BlockingIOError [¶](https://docs.python.org/3/library/io.html#io.BlockingIOError "Link to this definition")

This is a compatibility alias for the builtin [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError")
exception.

_exception_ io.UnsupportedOperation [¶](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "Link to this definition")

An exception inheriting [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") and [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") that is raised
when an unsupported operation is called on a stream.

See also

[`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.")

contains the standard IO streams: [`sys.stdin`](https://docs.python.org/3/library/sys.html#sys.stdin "sys.stdin"), [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout"),
and [`sys.stderr`](https://docs.python.org/3/library/sys.html#sys.stderr "sys.stderr").

## Class hierarchy [¶](https://docs.python.org/3/library/io.html\#class-hierarchy "Link to this heading")

The implementation of I/O streams is organized as a hierarchy of classes. First
[abstract base classes](https://docs.python.org/3/glossary.html#term-abstract-base-class) (ABCs), which are used to
specify the various categories of streams, then concrete classes providing the
standard stream implementations.

Note

The abstract base classes also provide default implementations of some
methods in order to help implementation of concrete stream classes. For
example, [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") provides unoptimized implementations of
`readinto()` and `readline()`.

At the top of the I/O hierarchy is the abstract base class [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"). It
defines the basic interface to a stream. Note, however, that there is no
separation between reading and writing to streams; implementations are allowed
to raise [`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation") if they do not support a given operation.

The [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") ABC extends [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"). It deals with the reading
and writing of bytes to a stream. [`FileIO`](https://docs.python.org/3/library/io.html#io.FileIO "io.FileIO") subclasses [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase")
to provide an interface to files in the machine’s file system.

The [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") ABC extends [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"). It deals with
buffering on a raw binary stream ( [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase")). Its subclasses,
[`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter"), [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader"), and [`BufferedRWPair`](https://docs.python.org/3/library/io.html#io.BufferedRWPair "io.BufferedRWPair")
buffer raw binary streams that are writable, readable, and both readable and writable,
respectively. [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") provides a buffered interface to seekable streams.
Another [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") subclass, [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO"), is a stream of
in-memory bytes.

The [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") ABC extends [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"). It deals with
streams whose bytes represent text, and handles encoding and decoding to and
from strings. [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper"), which extends [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase"), is a buffered text
interface to a buffered raw stream ( [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")). Finally,
[`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") is an in-memory stream for text.

Argument names are not part of the specification, and only the arguments of
[`open()`](https://docs.python.org/3/library/functions.html#open "open") are intended to be used as keyword arguments.

The following table summarizes the ABCs provided by the [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.") module:

| ABC | Inherits | Stub Methods | Mixin Methods and Properties |
| --- | --- | --- | --- |
| [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") |  | `fileno`, `seek`,<br>and `truncate` | `close`, `closed`, `__enter__`,<br>`__exit__`, `flush`, `isatty`, `__iter__`,<br>`__next__`, `readable`, `readline`,<br>`readlines`, `seekable`, `tell`,<br>`writable`, and `writelines` |
| [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") | [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") | `readinto` and<br>`write` | Inherited [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") methods, `read`,<br>and `readall` |
| [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") | [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") | `detach`, `read`,<br>`read1`, and `write` | Inherited [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") methods, `readinto`,<br>and `readinto1` |
| [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") | [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") | `detach`, `read`,<br>`readline`, and<br>`write` | Inherited [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") methods, `encoding`,<br>`errors`, and `newlines` |

### I/O Base Classes [¶](https://docs.python.org/3/library/io.html\#i-o-base-classes "Link to this heading")

_class_ io.IOBase [¶](https://docs.python.org/3/library/io.html#io.IOBase "Link to this definition")

The abstract base class for all I/O classes.

This class provides empty abstract implementations for many methods
that derived classes can override selectively; the default
implementations represent a file that cannot be read, written or
seeked.

Even though [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") does not declare `read()`
or `write()` because their signatures will vary, implementations and
clients should consider those methods part of the interface. Also,
implementations may raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") (or [`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation"))
when operations they do not support are called.

The basic type used for binary data read from or written to a file is
[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"). Other [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) are
accepted as method arguments too. Text I/O classes work with [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") data.

Note that calling any method (even inquiries) on a closed stream is
undefined. Implementations may raise [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") in this case.

[`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") (and its subclasses) supports the iterator protocol, meaning
that an [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") object can be iterated over yielding the lines in a
stream. Lines are defined slightly differently depending on whether the
stream is a binary stream (yielding bytes), or a text stream (yielding
character strings). See [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline") below.

[`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") is also a context manager and therefore supports the
[`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement. In this example, _file_ is closed after the
`with` statement’s suite is finished—even if an exception occurs:

Copy

```
with open('spam.txt', 'w') as file:
    file.write('Spam and eggs!')
```

[`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") provides these data attributes and methods:

close() [¶](https://docs.python.org/3/library/io.html#io.IOBase.close "Link to this definition")

Flush and close this stream. This method has no effect if the file is
already closed. Once the file is closed, any operation on the file
(e.g. reading or writing) will raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

As a convenience, it is allowed to call this method more than once;
only the first call, however, will have an effect.

closed [¶](https://docs.python.org/3/library/io.html#io.IOBase.closed "Link to this definition")

`True` if the stream is closed.

fileno() [¶](https://docs.python.org/3/library/io.html#io.IOBase.fileno "Link to this definition")

Return the underlying file descriptor (an integer) of the stream if it
exists. An [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised if the IO object does not use a file
descriptor.

flush() [¶](https://docs.python.org/3/library/io.html#io.IOBase.flush "Link to this definition")

Flush the write buffers of the stream if applicable. This does nothing
for read-only and non-blocking streams.

isatty() [¶](https://docs.python.org/3/library/io.html#io.IOBase.isatty "Link to this definition")

Return `True` if the stream is interactive (i.e., connected to
a terminal/tty device).

readable() [¶](https://docs.python.org/3/library/io.html#io.IOBase.readable "Link to this definition")

Return `True` if the stream can be read from.
If `False`, `read()` will raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

readline( _size=-1_, _/_) [¶](https://docs.python.org/3/library/io.html#io.IOBase.readline "Link to this definition")

Read and return one line from the stream. If _size_ is specified, at
most _size_ bytes will be read.

The line terminator is always `b'\n'` for binary files; for text files,
the _newline_ argument to [`open()`](https://docs.python.org/3/library/functions.html#open "open") can be used to select the line
terminator(s) recognized.

readlines( _hint=-1_, _/_) [¶](https://docs.python.org/3/library/io.html#io.IOBase.readlines "Link to this definition")

Read and return a list of lines from the stream. _hint_ can be specified
to control the number of lines read: no more lines will be read if the
total size (in bytes/characters) of all lines so far exceeds _hint_.

_hint_ values of `0` or less, as well as `None`, are treated as no
hint.

Note that it’s already possible to iterate on file objects using `for
line in file: ...` without calling `file.readlines()`.

seek( _offset_, _whence=os.SEEK\_SET_, _/_) [¶](https://docs.python.org/3/library/io.html#io.IOBase.seek "Link to this definition")

Change the stream position to the given byte _offset_,
interpreted relative to the position indicated by _whence_,
and return the new absolute position.
Values for _whence_ are:

- [`os.SEEK_SET`](https://docs.python.org/3/library/os.html#os.SEEK_SET "os.SEEK_SET") or `0` – start of the stream (the default);
_offset_ should be zero or positive

- [`os.SEEK_CUR`](https://docs.python.org/3/library/os.html#os.SEEK_CUR "os.SEEK_CUR") or `1` – current stream position;
_offset_ may be negative

- [`os.SEEK_END`](https://docs.python.org/3/library/os.html#os.SEEK_END "os.SEEK_END") or `2` – end of the stream;
_offset_ is usually negative


Added in version 3.1: The `SEEK_*` constants.

Added in version 3.3: Some operating systems could support additional values, like
[`os.SEEK_HOLE`](https://docs.python.org/3/library/os.html#os.SEEK_HOLE "os.SEEK_HOLE") or [`os.SEEK_DATA`](https://docs.python.org/3/library/os.html#os.SEEK_DATA "os.SEEK_DATA"). The valid values
for a file could depend on it being open in text or binary mode.

seekable() [¶](https://docs.python.org/3/library/io.html#io.IOBase.seekable "Link to this definition")

Return `True` if the stream supports random access. If `False`,
[`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek"), [`tell()`](https://docs.python.org/3/library/io.html#io.IOBase.tell "io.IOBase.tell") and [`truncate()`](https://docs.python.org/3/library/io.html#io.IOBase.truncate "io.IOBase.truncate") will raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

tell() [¶](https://docs.python.org/3/library/io.html#io.IOBase.tell "Link to this definition")

Return the current stream position.

truncate( _size=None_, _/_) [¶](https://docs.python.org/3/library/io.html#io.IOBase.truncate "Link to this definition")

Resize the stream to the given _size_ in bytes (or the current position
if _size_ is not specified). The current stream position isn’t changed.
This resizing can extend or reduce the current file size. In case of
extension, the contents of the new file area depend on the platform
(on most systems, additional bytes are zero-filled). The new file size
is returned.

Changed in version 3.5: Windows will now zero-fill files when extending.

writable() [¶](https://docs.python.org/3/library/io.html#io.IOBase.writable "Link to this definition")

Return `True` if the stream supports writing. If `False`,
`write()` and [`truncate()`](https://docs.python.org/3/library/io.html#io.IOBase.truncate "io.IOBase.truncate") will raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError").

writelines( _lines_, _/_) [¶](https://docs.python.org/3/library/io.html#io.IOBase.writelines "Link to this definition")

Write a list of lines to the stream. Line separators are not added, so it
is usual for each of the lines provided to have a line separator at the
end.

\_\_del\_\_() [¶](https://docs.python.org/3/library/io.html#io.IOBase.__del__ "Link to this definition")

Prepare for object destruction. [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase") provides a default
implementation of this method that calls the instance’s
[`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close") method.

_class_ io.RawIOBase [¶](https://docs.python.org/3/library/io.html#io.RawIOBase "Link to this definition")

Base class for raw binary streams. It inherits from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase").

Raw binary streams typically provide low-level access to an underlying OS
device or API, and do not try to encapsulate it in high-level primitives
(this functionality is done at a higher-level in buffered binary streams and text streams, described later
in this page).

[`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") provides these methods in addition to those from
[`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

read( _size=-1_, _/_) [¶](https://docs.python.org/3/library/io.html#io.RawIOBase.read "Link to this definition")

Read up to _size_ bytes from the object and return them. As a convenience,
if _size_ is unspecified or -1, all bytes until EOF are returned.
Otherwise, only one system call is ever made. Fewer than _size_ bytes may
be returned if the operating system call returns fewer than _size_ bytes.

If 0 bytes are returned, and _size_ was not 0, this indicates end of file.
If the object is in non-blocking mode and no bytes are available,
`None` is returned.

The default implementation defers to [`readall()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readall "io.RawIOBase.readall") and
[`readinto()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto "io.RawIOBase.readinto").

readall() [¶](https://docs.python.org/3/library/io.html#io.RawIOBase.readall "Link to this definition")

Read and return all the bytes from the stream until EOF, using multiple
calls to the stream if necessary.

readinto( _b_, _/_) [¶](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto "Link to this definition")

Read bytes into a pre-allocated, writable
[bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _b_, and return the
number of bytes read. For example, _b_ might be a [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray").
If the object is in non-blocking mode and no bytes
are available, `None` is returned.

write( _b_, _/_) [¶](https://docs.python.org/3/library/io.html#io.RawIOBase.write "Link to this definition")

Write the given [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object), _b_, to the
underlying raw stream, and return the number of
bytes written. This can be less than the length of _b_ in
bytes, depending on specifics of the underlying raw
stream, and especially if it is in non-blocking mode. `None` is
returned if the raw stream is set not to block and no single byte could
be readily written to it. The caller may release or mutate _b_ after
this method returns, so the implementation should only access _b_
during the method call.

_class_ io.BufferedIOBase [¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase "Link to this definition")

Base class for binary streams that support some kind of buffering.
It inherits from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase").

The main difference with [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") is that methods [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read"),
[`readinto()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto") and [`write()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.write "io.BufferedIOBase.write") will try (respectively) to read
as much input as requested or to emit all provided data.

In addition, if the underlying raw stream is in non-blocking mode, when the
system returns would block [`write()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.write "io.BufferedIOBase.write") will raise [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError")
with [`BlockingIOError.characters_written`](https://docs.python.org/3/library/exceptions.html#BlockingIOError.characters_written "BlockingIOError.characters_written") and [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read") will return
data read so far or `None` if no data is available.

Besides, the [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read") method does not have a default
implementation that defers to [`readinto()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto").

A typical [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") implementation should not inherit from a
[`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") implementation, but wrap one, like
[`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter") and [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader") do.

[`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") provides or overrides these data attributes and
methods in addition to those from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

raw [¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.raw "Link to this definition")

The underlying raw stream (a [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") instance) that
[`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") deals with. This is not part of the
[`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") API and may not exist on some implementations.

detach() [¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.detach "Link to this definition")

Separate the underlying raw stream from the buffer and return it.

After the raw stream has been detached, the buffer is in an unusable
state.

Some buffers, like [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO"), do not have the concept of a single
raw stream to return from this method. They raise
[`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation").

Added in version 3.1.

read( _size=-1_, _/_) [¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "Link to this definition")

Read and return up to _size_ bytes. If the argument is omitted, `None`,
or negative read as much as possible.

Fewer bytes may be returned than requested. An empty [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object
is returned if the stream is already at EOF. More than one read may be
made and calls may be retried if specific errors are encountered, see
[`os.read()`](https://docs.python.org/3/library/os.html#os.read "os.read") and [**PEP 475**](https://peps.python.org/pep-0475/) for more details. Less than size bytes
being returned does not imply that EOF is imminent.

When reading as much as possible the default implementation will use
`raw.readall` if available (which should implement
[`RawIOBase.readall()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readall "io.RawIOBase.readall")), otherwise will read in a loop until read
returns `None`, an empty [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), or a non-retryable error. For
most streams this is to EOF, but for non-blocking streams more data may
become available.

Note

When the underlying raw stream is non-blocking, implementations may
either raise [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") or return `None` if no data is
available. [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.") implementations return `None`.

read1( _size=-1_, _/_) [¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read1 "Link to this definition")

Read and return up to _size_ bytes, calling [`readinto()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto "io.RawIOBase.readinto")
which may retry if [`EINTR`](https://docs.python.org/3/library/errno.html#errno.EINTR "errno.EINTR") is encountered per
[**PEP 475**](https://peps.python.org/pep-0475/). If _size_ is `-1` or not provided, the implementation will
choose an arbitrary value for _size_.

Note

When the underlying raw stream is non-blocking, implementations may
either raise [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") or return `None` if no data is
available. [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.") implementations return `None`.

readinto( _b_, _/_) [¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto "Link to this definition")

Read bytes into a pre-allocated, writable
[bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _b_ and return the number of bytes read.
For example, _b_ might be a [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray").

Like [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read"), multiple reads may be issued to the underlying raw
stream, unless the latter is interactive.

A [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") is raised if the underlying raw stream is in non
blocking-mode, and has no data available at the moment.

readinto1( _b_, _/_) [¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto1 "Link to this definition")

Read bytes into a pre-allocated, writable
[bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) _b_, using at most one call to
the underlying raw stream’s [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read") (or
[`readinto()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto "io.RawIOBase.readinto")) method. Return the number of bytes read.

A [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") is raised if the underlying raw stream is in non
blocking-mode, and has no data available at the moment.

Added in version 3.5.

write( _b_, _/_) [¶](https://docs.python.org/3/library/io.html#io.BufferedIOBase.write "Link to this definition")

Write the given [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object), _b_, and return the number
of bytes written (always equal to the length of _b_ in bytes, since if
the write fails an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") will be raised). Depending on the
actual implementation, these bytes may be readily written to the
underlying stream, or held in a buffer for performance and latency
reasons.

When in non-blocking mode, a [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") is raised if the
data needed to be written to the raw stream but it couldn’t accept
all the data without blocking.

The caller may release or mutate _b_ after this method returns,
so the implementation should only access _b_ during the method call.

### Raw File I/O [¶](https://docs.python.org/3/library/io.html\#raw-file-i-o "Link to this heading")

_class_ io.FileIO( _name_, _mode='r'_, _closefd=True_, _opener=None_) [¶](https://docs.python.org/3/library/io.html#io.FileIO "Link to this definition")

A raw binary stream representing an OS-level file containing bytes data. It
inherits from [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase").

The _name_ can be one of two things:

- a character string or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object representing the path to the
file which will be opened. In this case closefd must be `True` (the default)
otherwise an error will be raised.

- an integer representing the number of an existing OS-level file descriptor
to which the resulting [`FileIO`](https://docs.python.org/3/library/io.html#io.FileIO "io.FileIO") object will give access. When the
FileIO object is closed this fd will be closed as well, unless _closefd_
is set to `False`.


The _mode_ can be `'r'`, `'w'`, `'x'` or `'a'` for reading
(default), writing, exclusive creation or appending. The file will be
created if it doesn’t exist when opened for writing or appending; it will be
truncated when opened for writing. [`FileExistsError`](https://docs.python.org/3/library/exceptions.html#FileExistsError "FileExistsError") will be raised if
it already exists when opened for creating. Opening a file for creating
implies writing, so this mode behaves in a similar way to `'w'`. Add a
`'+'` to the mode to allow simultaneous reading and writing.

The [`read()`](https://docs.python.org/3/library/io.html#io.RawIOBase.read "io.RawIOBase.read") (when called with a positive argument),
[`readinto()`](https://docs.python.org/3/library/io.html#io.RawIOBase.readinto "io.RawIOBase.readinto") and [`write()`](https://docs.python.org/3/library/io.html#io.RawIOBase.write "io.RawIOBase.write") methods on this
class will only make one system call.

A custom opener can be used by passing a callable as _opener_. The underlying
file descriptor for the file object is then obtained by calling _opener_ with
( _name_, _flags_). _opener_ must return an open file descriptor (passing
[`os.open`](https://docs.python.org/3/library/os.html#os.open "os.open") as _opener_ results in functionality similar to passing
`None`).

The newly created file is [non-inheritable](https://docs.python.org/3/library/os.html#fd-inheritance).

See the [`open()`](https://docs.python.org/3/library/functions.html#open "open") built-in function for examples on using the _opener_
parameter.

Changed in version 3.3: The _opener_ parameter was added.
The `'x'` mode was added.

Changed in version 3.4: The file is now non-inheritable.

[`FileIO`](https://docs.python.org/3/library/io.html#io.FileIO "io.FileIO") provides these data attributes in addition to those from
[`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

mode [¶](https://docs.python.org/3/library/io.html#io.FileIO.mode "Link to this definition")

The mode as given in the constructor.

name [¶](https://docs.python.org/3/library/io.html#io.FileIO.name "Link to this definition")

The file name. This is the file descriptor of the file when no name is
given in the constructor.

### Buffered Streams [¶](https://docs.python.org/3/library/io.html\#buffered-streams "Link to this heading")

Buffered I/O streams provide a higher-level interface to an I/O device
than raw I/O does.

_class_ io.BytesIO( _initial\_bytes=b''_) [¶](https://docs.python.org/3/library/io.html#io.BytesIO "Link to this definition")

A binary stream using an in-memory bytes buffer. It inherits from
[`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase"). The buffer is discarded when the
[`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close") method is called.

The optional argument _initial\_bytes_ is a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) that
contains initial data.

[`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") provides or overrides these methods in addition to those
from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

getbuffer() [¶](https://docs.python.org/3/library/io.html#io.BytesIO.getbuffer "Link to this definition")

Return a readable and writable view over the contents of the buffer
without copying them. Also, mutating the view will transparently
update the contents of the buffer:

Copy

```
>>> b = io.BytesIO(b"abcdef")
>>> view = b.getbuffer()
>>> view[2:4] = b"56"
>>> b.getvalue()
b'ab56ef'
```

Note

As long as the view exists, the [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") object cannot be
resized or closed.

Added in version 3.2.

getvalue() [¶](https://docs.python.org/3/library/io.html#io.BytesIO.getvalue "Link to this definition")

Return [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") containing the entire contents of the buffer.

read1( _size=-1_, _/_) [¶](https://docs.python.org/3/library/io.html#io.BytesIO.read1 "Link to this definition")

In [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO"), this is the same as [`read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read").

Changed in version 3.7: The _size_ argument is now optional.

readinto1( _b_, _/_) [¶](https://docs.python.org/3/library/io.html#io.BytesIO.readinto1 "Link to this definition")

In [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO"), this is the same as [`readinto()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.readinto "io.BufferedIOBase.readinto").

Added in version 3.5.

_class_ io.BufferedReader( _raw_, _buffer\_size=DEFAULT\_BUFFER\_SIZE_) [¶](https://docs.python.org/3/library/io.html#io.BufferedReader "Link to this definition")

A buffered binary stream providing higher-level access to a readable, non
seekable [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") raw binary stream. It inherits from
[`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase").

When reading data from this object, a larger amount of data may be
requested from the underlying raw stream, and kept in an internal buffer.
The buffered data can then be returned directly on subsequent reads.

The constructor creates a [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader") for the given readable
_raw_ stream and _buffer\_size_. If _buffer\_size_ is omitted,
[`DEFAULT_BUFFER_SIZE`](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE") is used.

[`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader") provides or overrides these methods in addition to
those from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

peek( _size=0_, _/_) [¶](https://docs.python.org/3/library/io.html#io.BufferedReader.peek "Link to this definition")

Return bytes from the stream without advancing the position. The number of
bytes returned may be less or more than requested. If the underlying raw
stream is non-blocking and the operation would block, returns empty bytes.

read( _size=-1_, _/_) [¶](https://docs.python.org/3/library/io.html#io.BufferedReader.read "Link to this definition")

In [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader") this is the same as [`io.BufferedIOBase.read()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read "io.BufferedIOBase.read")

read1( _size=-1_, _/_) [¶](https://docs.python.org/3/library/io.html#io.BufferedReader.read1 "Link to this definition")

In [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader") this is the same as [`io.BufferedIOBase.read1()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.read1 "io.BufferedIOBase.read1")

Changed in version 3.7: The _size_ argument is now optional.

_class_ io.BufferedWriter( _raw_, _buffer\_size=DEFAULT\_BUFFER\_SIZE_) [¶](https://docs.python.org/3/library/io.html#io.BufferedWriter "Link to this definition")

A buffered binary stream providing higher-level access to a writeable, non
seekable [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") raw binary stream. It inherits from
[`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase").

When writing to this object, data is normally placed into an internal
buffer. The buffer will be written out to the underlying [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase")
object under various conditions, including:

- when the buffer gets too small for all pending data;

- when [`flush()`](https://docs.python.org/3/library/io.html#io.BufferedWriter.flush "io.BufferedWriter.flush") is called;

- when a [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek") is requested (for [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") objects);

- when the [`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter") object is closed or destroyed.


The constructor creates a [`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter") for the given writeable
_raw_ stream. If the _buffer\_size_ is not given, it defaults to
[`DEFAULT_BUFFER_SIZE`](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE").

[`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter") provides or overrides these methods in addition to
those from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

flush() [¶](https://docs.python.org/3/library/io.html#io.BufferedWriter.flush "Link to this definition")

Force bytes held in the buffer into the raw stream. A
[`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") should be raised if the raw stream blocks.

write( _b_, _/_) [¶](https://docs.python.org/3/library/io.html#io.BufferedWriter.write "Link to this definition")

Write the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object), _b_, and return the
number of bytes written. When in non-blocking mode, a
[`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError") with [`BlockingIOError.characters_written`](https://docs.python.org/3/library/exceptions.html#BlockingIOError.characters_written "BlockingIOError.characters_written") set
is raised if the buffer needs to be written out but the raw stream blocks.

_class_ io.BufferedRandom( _raw_, _buffer\_size=DEFAULT\_BUFFER\_SIZE_) [¶](https://docs.python.org/3/library/io.html#io.BufferedRandom "Link to this definition")

A buffered binary stream providing higher-level access to a seekable
[`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") raw binary stream. It inherits from [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader")
and [`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter").

The constructor creates a reader and writer for a seekable raw stream, given
in the first argument. If the _buffer\_size_ is omitted it defaults to
[`DEFAULT_BUFFER_SIZE`](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE").

[`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") is capable of anything [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader") or
[`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter") can do. In addition, [`seek()`](https://docs.python.org/3/library/io.html#io.IOBase.seek "io.IOBase.seek") and
[`tell()`](https://docs.python.org/3/library/io.html#io.IOBase.tell "io.IOBase.tell") are guaranteed to be implemented.

_class_ io.BufferedRWPair( _reader_, _writer_, _buffer\_size=DEFAULT\_BUFFER\_SIZE_, _/_) [¶](https://docs.python.org/3/library/io.html#io.BufferedRWPair "Link to this definition")

A buffered binary stream providing higher-level access to two non seekable
[`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") raw binary streams—one readable, the other writeable.
It inherits from [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase").

_reader_ and _writer_ are [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") objects that are readable and
writeable respectively. If the _buffer\_size_ is omitted it defaults to
[`DEFAULT_BUFFER_SIZE`](https://docs.python.org/3/library/io.html#io.DEFAULT_BUFFER_SIZE "io.DEFAULT_BUFFER_SIZE").

[`BufferedRWPair`](https://docs.python.org/3/library/io.html#io.BufferedRWPair "io.BufferedRWPair") implements all of [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")'s methods
except for [`detach()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.detach "io.BufferedIOBase.detach"), which raises
[`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation").

Warning

[`BufferedRWPair`](https://docs.python.org/3/library/io.html#io.BufferedRWPair "io.BufferedRWPair") does not attempt to synchronize accesses to
its underlying raw streams. You should not pass it the same object
as reader and writer; use [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") instead.

### Text I/O [¶](https://docs.python.org/3/library/io.html\#id1 "Link to this heading")

_class_ io.TextIOBase [¶](https://docs.python.org/3/library/io.html#io.TextIOBase "Link to this definition")

Base class for text streams. This class provides a character and line based
interface to stream I/O. It inherits from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase").

[`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") provides or overrides these data attributes and
methods in addition to those from [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

encoding [¶](https://docs.python.org/3/library/io.html#io.TextIOBase.encoding "Link to this definition")

The name of the encoding used to decode the stream’s bytes into
strings, and to encode strings into bytes.

errors [¶](https://docs.python.org/3/library/io.html#io.TextIOBase.errors "Link to this definition")

The error setting of the decoder or encoder.

newlines [¶](https://docs.python.org/3/library/io.html#io.TextIOBase.newlines "Link to this definition")

A string, a tuple of strings, or `None`, indicating the newlines
translated so far. Depending on the implementation and the initial
constructor flags, this may not be available.

buffer [¶](https://docs.python.org/3/library/io.html#io.TextIOBase.buffer "Link to this definition")

The underlying binary buffer (a [`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase")
or [`RawIOBase`](https://docs.python.org/3/library/io.html#io.RawIOBase "io.RawIOBase") instance) that [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") deals with.
This is not part of the [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") API and may not exist
in some implementations.

detach() [¶](https://docs.python.org/3/library/io.html#io.TextIOBase.detach "Link to this definition")

Separate the underlying binary buffer from the [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") and
return it.

After the underlying buffer has been detached, the [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") is
in an unusable state.

Some [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") implementations, like [`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO"), may not
have the concept of an underlying buffer and calling this method will
raise [`UnsupportedOperation`](https://docs.python.org/3/library/io.html#io.UnsupportedOperation "io.UnsupportedOperation").

Added in version 3.1.

read( _size=-1_, _/_) [¶](https://docs.python.org/3/library/io.html#io.TextIOBase.read "Link to this definition")

Read and return at most _size_ characters from the stream as a single
[`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). If _size_ is negative or `None`, reads until EOF.

readline( _size=-1_, _/_) [¶](https://docs.python.org/3/library/io.html#io.TextIOBase.readline "Link to this definition")

Read until newline or EOF and return a single [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). If the stream is
already at EOF, an empty string is returned.

If _size_ is specified, at most _size_ characters will be read.

seek( _offset_, _whence=SEEK\_SET_, _/_) [¶](https://docs.python.org/3/library/io.html#io.TextIOBase.seek "Link to this definition")

Change the stream position to the given _offset_. Behaviour depends on
the _whence_ parameter. The default value for _whence_ is
`SEEK_SET`.

- `SEEK_SET` or `0`: seek from the start of the stream
(the default); _offset_ must either be a number returned by
[`TextIOBase.tell()`](https://docs.python.org/3/library/io.html#io.TextIOBase.tell "io.TextIOBase.tell"), or zero. Any other _offset_ value
produces undefined behaviour.

- `SEEK_CUR` or `1`: “seek” to the current position;
_offset_ must be zero, which is a no-operation (all other values
are unsupported).

- `SEEK_END` or `2`: seek to the end of the stream;
_offset_ must be zero (all other values are unsupported).


Return the new absolute position as an opaque number.

Added in version 3.1: The `SEEK_*` constants.

tell() [¶](https://docs.python.org/3/library/io.html#io.TextIOBase.tell "Link to this definition")

Return the current stream position as an opaque number. The number
does not usually represent a number of bytes in the underlying
binary storage.

write( _s_, _/_) [¶](https://docs.python.org/3/library/io.html#io.TextIOBase.write "Link to this definition")

Write the string _s_ to the stream and return the number of characters
written.

_class_ io.TextIOWrapper( _buffer_, _encoding=None_, _errors=None_, _newline=None_, _line\_buffering=False_, _write\_through=False_) [¶](https://docs.python.org/3/library/io.html#io.TextIOWrapper "Link to this definition")

A buffered text stream providing higher-level access to a
[`BufferedIOBase`](https://docs.python.org/3/library/io.html#io.BufferedIOBase "io.BufferedIOBase") buffered binary stream. It inherits from
[`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase").

_encoding_ gives the name of the encoding that the stream will be decoded or
encoded with. In [UTF-8 Mode](https://docs.python.org/3/library/os.html#utf8-mode), this defaults to UTF-8.
Otherwise, it defaults to [`locale.getencoding()`](https://docs.python.org/3/library/locale.html#locale.getencoding "locale.getencoding").
`encoding="locale"` can be used to specify the current locale’s encoding
explicitly. See [Text Encoding](https://docs.python.org/3/library/io.html#io-text-encoding) for more information.

_errors_ is an optional string that specifies how encoding and decoding
errors are to be handled. Pass `'strict'` to raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError")
exception if there is an encoding error (the default of `None` has the same
effect), or pass `'ignore'` to ignore errors. (Note that ignoring encoding
errors can lead to data loss.) `'replace'` causes a replacement marker
(such as `'?'`) to be inserted where there is malformed data.
`'backslashreplace'` causes malformed data to be replaced by a
backslashed escape sequence. When writing, `'xmlcharrefreplace'`
(replace with the appropriate XML character reference) or `'namereplace'`
(replace with `\N{...}` escape sequences) can be used. Any other error
handling name that has been registered with
[`codecs.register_error()`](https://docs.python.org/3/library/codecs.html#codecs.register_error "codecs.register_error") is also valid.

_newline_ controls how line endings are handled. It can be `None`,
`''`, `'\n'`, `'\r'`, and `'\r\n'`. It works as follows:

- When reading input from the stream, if _newline_ is `None`,
[universal newlines](https://docs.python.org/3/glossary.html#term-universal-newlines) mode is enabled. Lines in the input can end in
`'\n'`, `'\r'`, or `'\r\n'`, and these are translated into `'\n'`
before being returned to the caller. If _newline_ is `''`, universal
newlines mode is enabled, but line endings are returned to the caller
untranslated. If _newline_ has any of the other legal values, input lines
are only terminated by the given string, and the line ending is returned to
the caller untranslated.

- When writing output to the stream, if _newline_ is `None`, any `'\n'`
characters written are translated to the system default line separator,
[`os.linesep`](https://docs.python.org/3/library/os.html#os.linesep "os.linesep"). If _newline_ is `''` or `'\n'`, no translation
takes place. If _newline_ is any of the other legal values, any `'\n'`
characters written are translated to the given string.


If _line\_buffering_ is `True`, [`flush()`](https://docs.python.org/3/library/io.html#io.IOBase.flush "io.IOBase.flush") is implied when a call to
write contains a newline character or a carriage return.

If _write\_through_ is `True`, calls to [`write()`](https://docs.python.org/3/library/io.html#io.BufferedIOBase.write "io.BufferedIOBase.write") are guaranteed
not to be buffered: any data written on the [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper")
object is immediately handled to its underlying binary _buffer_.

Changed in version 3.3: The _write\_through_ argument has been added.

Changed in version 3.3: The default _encoding_ is now `locale.getpreferredencoding(False)`
instead of `locale.getpreferredencoding()`. Don’t change temporary the
locale encoding using [`locale.setlocale()`](https://docs.python.org/3/library/locale.html#locale.setlocale "locale.setlocale"), use the current locale
encoding instead of the user preferred encoding.

Changed in version 3.10: The _encoding_ argument now supports the `"locale"` dummy encoding name.

Note

When the underlying raw stream is non-blocking, a [`BlockingIOError`](https://docs.python.org/3/library/exceptions.html#BlockingIOError "BlockingIOError")
may be raised if a read operation cannot be completed immediately.

[`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") provides these data attributes and methods in
addition to those from [`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

line\_buffering [¶](https://docs.python.org/3/library/io.html#io.TextIOWrapper.line_buffering "Link to this definition")

Whether line buffering is enabled.

write\_through [¶](https://docs.python.org/3/library/io.html#io.TextIOWrapper.write_through "Link to this definition")

Whether writes are passed immediately to the underlying binary
buffer.

Added in version 3.7.

reconfigure( _\*_, _encoding=None_, _errors=None_, _newline=None_, _line\_buffering=None_, _write\_through=None_) [¶](https://docs.python.org/3/library/io.html#io.TextIOWrapper.reconfigure "Link to this definition")

Reconfigure this text stream using new settings for _encoding_,
_errors_, _newline_, _line\_buffering_ and _write\_through_.

Parameters not specified keep current settings, except
`errors='strict'` is used when _encoding_ is specified but
_errors_ is not specified.

It is not possible to change the encoding or newline if some data
has already been read from the stream. On the other hand, changing
encoding after write is possible.

This method does an implicit stream flush before setting the
new parameters.

Added in version 3.7.

Changed in version 3.11: The method supports `encoding="locale"` option.

seek( _cookie_, _whence=os.SEEK\_SET_, _/_) [¶](https://docs.python.org/3/library/io.html#io.TextIOWrapper.seek "Link to this definition")

Set the stream position.
Return the new stream position as an [`int`](https://docs.python.org/3/library/functions.html#int "int").

Four operations are supported,
given by the following argument combinations:

- `seek(0, SEEK_SET)`: Rewind to the start of the stream.

- `seek(cookie, SEEK_SET)`: Restore a previous position;
_cookie_ **must be** a number returned by [`tell()`](https://docs.python.org/3/library/io.html#io.TextIOWrapper.tell "io.TextIOWrapper.tell").

- `seek(0, SEEK_END)`: Fast-forward to the end of the stream.

- `seek(0, SEEK_CUR)`: Leave the current stream position unchanged.


Any other argument combinations are invalid,
and may raise exceptions.

See also

[`os.SEEK_SET`](https://docs.python.org/3/library/os.html#os.SEEK_SET "os.SEEK_SET"), [`os.SEEK_CUR`](https://docs.python.org/3/library/os.html#os.SEEK_CUR "os.SEEK_CUR"), and [`os.SEEK_END`](https://docs.python.org/3/library/os.html#os.SEEK_END "os.SEEK_END").

tell() [¶](https://docs.python.org/3/library/io.html#io.TextIOWrapper.tell "Link to this definition")

Return the stream position as an opaque number.
The return value of `tell()` can be given as input to [`seek()`](https://docs.python.org/3/library/io.html#io.TextIOWrapper.seek "io.TextIOWrapper.seek"),
to restore a previous stream position.

_class_ io.StringIO( _initial\_value=''_, _newline='\\n'_) [¶](https://docs.python.org/3/library/io.html#io.StringIO "Link to this definition")

A text stream using an in-memory text buffer. It inherits from
[`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase").

The text buffer is discarded when the [`close()`](https://docs.python.org/3/library/io.html#io.IOBase.close "io.IOBase.close") method is
called.

The initial value of the buffer can be set by providing _initial\_value_.
If newline translation is enabled, newlines will be encoded as if by
[`write()`](https://docs.python.org/3/library/io.html#io.TextIOBase.write "io.TextIOBase.write"). The stream is positioned at the start of the
buffer which emulates opening an existing file in a `w+` mode, making it
ready for an immediate write from the beginning or for a write that
would overwrite the initial value. To emulate opening a file in an `a+`
mode ready for appending, use `f.seek(0, io.SEEK_END)` to reposition the
stream at the end of the buffer.

The _newline_ argument works like that of [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper"),
except that when writing output to the stream, if _newline_ is `None`,
newlines are written as `\n` on all platforms.

[`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") provides this method in addition to those from
[`TextIOBase`](https://docs.python.org/3/library/io.html#io.TextIOBase "io.TextIOBase") and [`IOBase`](https://docs.python.org/3/library/io.html#io.IOBase "io.IOBase"):

getvalue() [¶](https://docs.python.org/3/library/io.html#io.StringIO.getvalue "Link to this definition")

Return a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") containing the entire contents of the buffer.
Newlines are decoded as if by [`read()`](https://docs.python.org/3/library/io.html#io.TextIOBase.read "io.TextIOBase.read"), although
the stream position is not changed.

Example usage:

Copy

```
import io

output = io.StringIO()
output.write('First line.\n')
print('Second line.', file=output)

# Retrieve file contents -- this will be
# 'First line.\nSecond line.\n'
contents = output.getvalue()

# Close object and discard memory buffer --
# .getvalue() will now raise an exception.
output.close()
```

_class_ io.IncrementalNewlineDecoder [¶](https://docs.python.org/3/library/io.html#io.IncrementalNewlineDecoder "Link to this definition")

A helper codec that decodes newlines for [universal newlines](https://docs.python.org/3/glossary.html#term-universal-newlines) mode.
It inherits from [`codecs.IncrementalDecoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder "codecs.IncrementalDecoder").

## Static Typing [¶](https://docs.python.org/3/library/io.html\#static-typing "Link to this heading")

The following protocols can be used for annotating function and method
arguments for simple stream reading or writing operations. They are decorated
with [`@typing.runtime_checkable`](https://docs.python.org/3/library/typing.html#typing.runtime_checkable "typing.runtime_checkable").

_class_ io.Reader\[ _T_\] [¶](https://docs.python.org/3/library/io.html#io.Reader "Link to this definition")

Generic protocol for reading from a file or other input stream. `T` will
usually be [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), but can be any type that is
read from the stream.

Added in version 3.14.

read() [¶](https://docs.python.org/3/library/io.html#io.Reader.read "Link to this definition")read( _size_, _/_)

Read data from the input stream and return it. If _size_ is
specified, it should be an integer, and at most _size_ items
(bytes/characters) will be read.

For example:

Copy

```
def read_it(reader: Reader[str]):
    data = reader.read(11)
    assert isinstance(data, str)
```

_class_ io.Writer\[ _T_\] [¶](https://docs.python.org/3/library/io.html#io.Writer "Link to this definition")

Generic protocol for writing to a file or other output stream. `T` will
usually be [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), but can be any type that can be
written to the stream.

Added in version 3.14.

write( _data_, _/_) [¶](https://docs.python.org/3/library/io.html#io.Writer.write "Link to this definition")

Write _data_ to the output stream and return the number of items
(bytes/characters) written.

For example:

Copy

```
def write_binary(writer: Writer[bytes]):
    writer.write(b"Hello world!\n")
```

See [ABCs and Protocols for working with I/O](https://docs.python.org/3/library/typing.html#typing-io) for other I/O related protocols and classes that can be
used for static type checking.

## Performance [¶](https://docs.python.org/3/library/io.html\#performance "Link to this heading")

This section discusses the performance of the provided concrete I/O
implementations.

### Binary I/O [¶](https://docs.python.org/3/library/io.html\#id2 "Link to this heading")

By reading and writing only large chunks of data even when the user asks for a
single byte, buffered I/O hides any inefficiency in calling and executing the
operating system’s unbuffered I/O routines. The gain depends on the OS and the
kind of I/O which is performed. For example, on some modern OSes such as Linux,
unbuffered disk I/O can be as fast as buffered I/O. The bottom line, however,
is that buffered I/O offers predictable performance regardless of the platform
and the backing device. Therefore, it is almost always preferable to use
buffered I/O rather than unbuffered I/O for binary data.

### Text I/O [¶](https://docs.python.org/3/library/io.html\#id3 "Link to this heading")

Text I/O over a binary storage (such as a file) is significantly slower than
binary I/O over the same storage, because it requires conversions between
unicode and binary data using a character codec. This can become noticeable
handling huge amounts of text data like large log files. Also,
[`tell()`](https://docs.python.org/3/library/io.html#io.TextIOBase.tell "io.TextIOBase.tell") and [`seek()`](https://docs.python.org/3/library/io.html#io.TextIOBase.seek "io.TextIOBase.seek") are both quite slow
due to the reconstruction algorithm used.

[`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO"), however, is a native in-memory unicode container and will
exhibit similar speed to [`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO").

### Multi-threading [¶](https://docs.python.org/3/library/io.html\#multi-threading "Link to this heading")

[`FileIO`](https://docs.python.org/3/library/io.html#io.FileIO "io.FileIO") objects are thread-safe to the extent that the operating system
calls (such as _[read(2)](https://manpages.debian.org/read(2))_ under Unix) they wrap are thread-safe too.

Binary buffered objects (instances of [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader"),
[`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter"), [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") and [`BufferedRWPair`](https://docs.python.org/3/library/io.html#io.BufferedRWPair "io.BufferedRWPair"))
protect their internal structures using a lock; it is therefore safe to call
them from multiple threads at once.

[`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") objects are not thread-safe.

### Reentrancy [¶](https://docs.python.org/3/library/io.html\#reentrancy "Link to this heading")

Binary buffered objects (instances of [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader"),
[`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter"), [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") and [`BufferedRWPair`](https://docs.python.org/3/library/io.html#io.BufferedRWPair "io.BufferedRWPair"))
are not reentrant. While reentrant calls will not happen in normal situations,
they can arise from doing I/O in a [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.") handler. If a thread tries to
re-enter a buffered object which it is already accessing, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError")
is raised. Note this doesn’t prohibit a different thread from entering the
buffered object.

The above implicitly extends to text files, since the [`open()`](https://docs.python.org/3/library/functions.html#open "open") function
will wrap a buffered object inside a [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper"). This includes
standard streams and therefore affects the built-in [`print()`](https://docs.python.org/3/library/functions.html#print "print") function as
well.

### [Table of Contents](https://docs.python.org/3/contents.html)

- [`io` — Core tools for working with streams](https://docs.python.org/3/library/io.html#)
  - [Overview](https://docs.python.org/3/library/io.html#overview)
    - [Text I/O](https://docs.python.org/3/library/io.html#text-i-o)
    - [Binary I/O](https://docs.python.org/3/library/io.html#binary-i-o)
    - [Raw I/O](https://docs.python.org/3/library/io.html#raw-i-o)
  - [Text Encoding](https://docs.python.org/3/library/io.html#text-encoding)
    - [Opt-in EncodingWarning](https://docs.python.org/3/library/io.html#opt-in-encodingwarning)
  - [High-level Module Interface](https://docs.python.org/3/library/io.html#high-level-module-interface)
  - [Class hierarchy](https://docs.python.org/3/library/io.html#class-hierarchy)
    - [I/O Base Classes](https://docs.python.org/3/library/io.html#i-o-base-classes)
    - [Raw File I/O](https://docs.python.org/3/library/io.html#raw-file-i-o)
    - [Buffered Streams](https://docs.python.org/3/library/io.html#buffered-streams)
    - [Text I/O](https://docs.python.org/3/library/io.html#id1)
  - [Static Typing](https://docs.python.org/3/library/io.html#static-typing)
  - [Performance](https://docs.python.org/3/library/io.html#performance)
    - [Binary I/O](https://docs.python.org/3/library/io.html#id2)
    - [Text I/O](https://docs.python.org/3/library/io.html#id3)
    - [Multi-threading](https://docs.python.org/3/library/io.html#multi-threading)
    - [Reentrancy](https://docs.python.org/3/library/io.html#reentrancy)

#### Previous topic

[`os` — Miscellaneous operating system interfaces](https://docs.python.org/3/library/os.html "previous chapter")

#### Next topic

[`time` — Time access and conversions](https://docs.python.org/3/library/time.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/io.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/time.html "time — Time access and conversions") \|
- [previous](https://docs.python.org/3/library/os.html "os — Miscellaneous operating system interfaces") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Generic Operating System Services](https://docs.python.org/3/library/allos.html) »
- [`io` — Core tools for working with streams](https://docs.python.org/3/library/io.html)
- \|

- Theme
AutoLightDark \|