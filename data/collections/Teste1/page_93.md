### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/slice.html "Slice Objects") \|
- [previous](https://docs.python.org/3/c-api/iterator.html "Iterator Objects") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html) »
- [Descriptor Objects](https://docs.python.org/3/c-api/descriptor.html)
- \|

- Theme
AutoLightDark \|

# Descriptor Objects [¶](https://docs.python.org/3/c-api/descriptor.html\#descriptor-objects "Link to this heading")

“Descriptors” are objects that describe some attribute of an object. They are
found in the dictionary of type objects.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject") PyProperty\_Type [¶](https://docs.python.org/3/c-api/descriptor.html#c.PyProperty_Type "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

The type object for the built-in descriptor types.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyDescr\_NewGetSet( [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")\*type, struct [PyGetSetDef](https://docs.python.org/3/c-api/structures.html#c.PyGetSetDef "PyGetSetDef")\*getset) [¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewGetSet "Link to this definition")

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyDescr\_NewMember( [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")\*type, struct [PyMemberDef](https://docs.python.org/3/c-api/structures.html#c.PyMemberDef "PyMemberDef")\*meth) [¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewMember "Link to this definition")

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyDescr\_NewMethod( [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")\*type, struct [PyMethodDef](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")\*meth) [¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewMethod "Link to this definition")

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyDescr\_NewWrapper( [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")\*type, structwrapperbase\*wrapper, void\*wrapped) [¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewWrapper "Link to this definition")

_Return value: New reference._[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyDescr\_NewClassMethod( [PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject")\*type, [PyMethodDef](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")\*method) [¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_NewClassMethod "Link to this definition")

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._intPyDescr\_IsData( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*descr) [¶](https://docs.python.org/3/c-api/descriptor.html#c.PyDescr_IsData "Link to this definition")

Return non-zero if the descriptor object _descr_ describes a data attribute, or
`0` if it describes a method. _descr_ must be a descriptor object; there is
no error checking.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyWrapper\_New( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*) [¶](https://docs.python.org/3/c-api/descriptor.html#c.PyWrapper_New "Link to this definition")

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

## Built-in descriptors [¶](https://docs.python.org/3/c-api/descriptor.html\#built-in-descriptors "Link to this heading")

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject") PySuper\_Type [¶](https://docs.python.org/3/c-api/descriptor.html#c.PySuper_Type "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

The type object for super objects. This is the same object as
[`super`](https://docs.python.org/3/library/functions.html#super "super") in the Python layer.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject") PyClassMethod\_Type [¶](https://docs.python.org/3/c-api/descriptor.html#c.PyClassMethod_Type "Link to this definition")

The type of class method objects. This is the same object as
[`classmethod`](https://docs.python.org/3/library/functions.html#classmethod "classmethod") in the Python layer.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyClassMethod\_New( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*callable) [¶](https://docs.python.org/3/c-api/descriptor.html#c.PyClassMethod_New "Link to this definition")

Create a new [`classmethod`](https://docs.python.org/3/library/functions.html#classmethod "classmethod") object wrapping _callable_.
_callable_ must be a callable object and must not be `NULL`.

On success, this function returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference) to a new class
method descriptor. On failure, this function returns `NULL` with an
exception set.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject") PyStaticMethod\_Type [¶](https://docs.python.org/3/c-api/descriptor.html#c.PyStaticMethod_Type "Link to this definition")

The type of static method objects. This is the same object as
[`staticmethod`](https://docs.python.org/3/library/functions.html#staticmethod "staticmethod") in the Python layer.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyStaticMethod\_New( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*callable) [¶](https://docs.python.org/3/c-api/descriptor.html#c.PyStaticMethod_New "Link to this definition")

Create a new [`staticmethod`](https://docs.python.org/3/library/functions.html#staticmethod "staticmethod") object wrapping _callable_.
_callable_ must be a callable object and must not be `NULL`.

On success, this function returns a [strong reference](https://docs.python.org/3/glossary.html#term-strong-reference) to a new static
method descriptor. On failure, this function returns `NULL` with an
exception set.

### [Table of Contents](https://docs.python.org/3/contents.html)

- [Descriptor Objects](https://docs.python.org/3/c-api/descriptor.html#)
  - [Built-in descriptors](https://docs.python.org/3/c-api/descriptor.html#built-in-descriptors)

#### Previous topic

[Iterator Objects](https://docs.python.org/3/c-api/iterator.html "previous chapter")

#### Next topic

[Slice Objects](https://docs.python.org/3/c-api/slice.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/c-api/descriptor.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/slice.html "Slice Objects") \|
- [previous](https://docs.python.org/3/c-api/iterator.html "Iterator Objects") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html) »
- [Descriptor Objects](https://docs.python.org/3/c-api/descriptor.html)
- \|

- Theme
AutoLightDark \|