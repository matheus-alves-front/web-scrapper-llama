### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/buffer.html "Buffer Protocol") \|
- [previous](https://docs.python.org/3/c-api/mapping.html "Mapping Protocol") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html) »
- [Iterator Protocol](https://docs.python.org/3/c-api/iter.html)
- \|

- Theme
AutoLightDark \|

# Iterator Protocol [¶](https://docs.python.org/3/c-api/iter.html\#iterator-protocol "Link to this heading")

There are two functions specifically for working with iterators.

intPyIter\_Check( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*o) [¶](https://docs.python.org/3/c-api/iter.html#c.PyIter_Check "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable) since version 3.8._

Return non-zero if the object _o_ can be safely passed to
[`PyIter_NextItem()`](https://docs.python.org/3/c-api/iter.html#c.PyIter_NextItem "PyIter_NextItem") and `0` otherwise.
This function always succeeds.

intPyAIter\_Check( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*o) [¶](https://docs.python.org/3/c-api/iter.html#c.PyAIter_Check "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable) since version 3.10._

Return non-zero if the object _o_ provides the `AsyncIterator`
protocol, and `0` otherwise. This function always succeeds.

Added in version 3.10.

intPyIter\_NextItem( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*iter, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*\*item) [¶](https://docs.python.org/3/c-api/iter.html#c.PyIter_NextItem "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable) since version 3.14._

Return `1` and set _item_ to a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference) of the
next value of the iterator _iter_ on success.
Return `0` and set _item_ to `NULL` if there are no remaining values.
Return `-1`, set _item_ to `NULL` and set an exception on error.

Added in version 3.14.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyIter\_Next( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*o) [¶](https://docs.python.org/3/c-api/iter.html#c.PyIter_Next "Link to this definition")

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

This is an older version of `PyIter_NextItem()`,
which is retained for backwards compatibility.
Prefer [`PyIter_NextItem()`](https://docs.python.org/3/c-api/iter.html#c.PyIter_NextItem "PyIter_NextItem").

Return the next value from the iterator _o_. The object must be an iterator
according to [`PyIter_Check()`](https://docs.python.org/3/c-api/iter.html#c.PyIter_Check "PyIter_Check") (it is up to the caller to check this).
If there are no remaining values, returns `NULL` with no exception set.
If an error occurs while retrieving the item, returns `NULL` and passes
along the exception.

typePySendResult [¶](https://docs.python.org/3/c-api/iter.html#c.PySendResult "Link to this definition")

The enum value used to represent different results of [`PyIter_Send()`](https://docs.python.org/3/c-api/iter.html#c.PyIter_Send "PyIter_Send").

Added in version 3.10.

[PySendResult](https://docs.python.org/3/c-api/iter.html#c.PySendResult "PySendResult") PyIter\_Send( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*iter, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*arg, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*\*presult) [¶](https://docs.python.org/3/c-api/iter.html#c.PyIter_Send "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable) since version 3.10._

Sends the _arg_ value into the iterator _iter_. Returns:

- `PYGEN_RETURN` if iterator returns. Return value is returned via _presult_.

- `PYGEN_NEXT` if iterator yields. Yielded value is returned via _presult_.

- `PYGEN_ERROR` if iterator has raised and exception. _presult_ is set to `NULL`.


Added in version 3.10.

#### Previous topic

[Mapping Protocol](https://docs.python.org/3/c-api/mapping.html "previous chapter")

#### Next topic

[Buffer Protocol](https://docs.python.org/3/c-api/buffer.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/c-api/iter.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/buffer.html "Buffer Protocol") \|
- [previous](https://docs.python.org/3/c-api/mapping.html "Mapping Protocol") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Abstract Objects Layer](https://docs.python.org/3/c-api/abstract.html) »
- [Iterator Protocol](https://docs.python.org/3/c-api/iter.html)
- \|

- Theme
AutoLightDark \|