### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/function.html "Function Objects") \|
- [previous](https://docs.python.org/3/c-api/dict.html "Dictionary Objects") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html) »
- [Set Objects](https://docs.python.org/3/c-api/set.html)
- \|

- Theme
AutoLightDark \|

# Set Objects [¶](https://docs.python.org/3/c-api/set.html\#set-objects "Link to this heading")

This section details the public API for [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") and [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset")
objects. Any functionality not listed below is best accessed using either
the abstract object protocol (including [`PyObject_CallMethod()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethod "PyObject_CallMethod"),
[`PyObject_RichCompareBool()`](https://docs.python.org/3/c-api/object.html#c.PyObject_RichCompareBool "PyObject_RichCompareBool"), [`PyObject_Hash()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Hash "PyObject_Hash"),
[`PyObject_Repr()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Repr "PyObject_Repr"), [`PyObject_IsTrue()`](https://docs.python.org/3/c-api/object.html#c.PyObject_IsTrue "PyObject_IsTrue"), [`PyObject_Print()`](https://docs.python.org/3/c-api/object.html#c.PyObject_Print "PyObject_Print"), and
[`PyObject_GetIter()`](https://docs.python.org/3/c-api/object.html#c.PyObject_GetIter "PyObject_GetIter")) or the abstract number protocol (including
[`PyNumber_And()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_And "PyNumber_And"), [`PyNumber_Subtract()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Subtract "PyNumber_Subtract"), [`PyNumber_Or()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Or "PyNumber_Or"),
[`PyNumber_Xor()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Xor "PyNumber_Xor"), [`PyNumber_InPlaceAnd()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceAnd "PyNumber_InPlaceAnd"),
[`PyNumber_InPlaceSubtract()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceSubtract "PyNumber_InPlaceSubtract"), [`PyNumber_InPlaceOr()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceOr "PyNumber_InPlaceOr"), and
[`PyNumber_InPlaceXor()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_InPlaceXor "PyNumber_InPlaceXor")).

typePySetObject [¶](https://docs.python.org/3/c-api/set.html#c.PySetObject "Link to this definition")

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject") is used to hold the internal data for both
[`set`](https://docs.python.org/3/library/stdtypes.html#set "set") and [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") objects. It is like a [`PyDictObject`](https://docs.python.org/3/c-api/dict.html#c.PyDictObject "PyDictObject")
in that it is a fixed size for small sets (much like tuple storage) and will
point to a separate, variable sized block of memory for medium and large sized
sets (much like list storage). None of the fields of this structure should be
considered public and all are subject to change. All access should be done through
the documented API rather than by manipulating the values in the structure.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject") PySet\_Type [¶](https://docs.python.org/3/c-api/set.html#c.PySet_Type "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

This is an instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject") representing the Python
[`set`](https://docs.python.org/3/library/stdtypes.html#set "set") type.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject") PyFrozenSet\_Type [¶](https://docs.python.org/3/c-api/set.html#c.PyFrozenSet_Type "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

This is an instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject") representing the Python
[`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") type.

The following type check macros work on pointers to any Python object. Likewise,
the constructor functions work with any iterable Python object.

intPySet\_Check( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*p) [¶](https://docs.python.org/3/c-api/set.html#c.PySet_Check "Link to this definition")

Return true if _p_ is a [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") object or an instance of a subtype.
This function always succeeds.

intPyFrozenSet\_Check( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*p) [¶](https://docs.python.org/3/c-api/set.html#c.PyFrozenSet_Check "Link to this definition")

Return true if _p_ is a [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") object or an instance of a
subtype. This function always succeeds.

intPyAnySet\_Check( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*p) [¶](https://docs.python.org/3/c-api/set.html#c.PyAnySet_Check "Link to this definition")

Return true if _p_ is a [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") object, a [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") object, or an
instance of a subtype. This function always succeeds.

intPySet\_CheckExact( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*p) [¶](https://docs.python.org/3/c-api/set.html#c.PySet_CheckExact "Link to this definition")

Return true if _p_ is a [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") object but not an instance of a
subtype. This function always succeeds.

Added in version 3.10.

intPyAnySet\_CheckExact( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*p) [¶](https://docs.python.org/3/c-api/set.html#c.PyAnySet_CheckExact "Link to this definition")

Return true if _p_ is a [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") object or a [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") object but
not an instance of a subtype. This function always succeeds.

intPyFrozenSet\_CheckExact( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*p) [¶](https://docs.python.org/3/c-api/set.html#c.PyFrozenSet_CheckExact "Link to this definition")

Return true if _p_ is a [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") object but not an instance of a
subtype. This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PySet\_New( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*iterable) [¶](https://docs.python.org/3/c-api/set.html#c.PySet_New "Link to this definition")

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Return a new [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") containing objects returned by the _iterable_. The
_iterable_ may be `NULL` to create a new empty set. Return the new set on
success or `NULL` on failure. Raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if _iterable_ is not
actually iterable. The constructor is also useful for copying a set
(`c=set(s)`).

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyFrozenSet\_New( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*iterable) [¶](https://docs.python.org/3/c-api/set.html#c.PyFrozenSet_New "Link to this definition")

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Return a new [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") containing objects returned by the _iterable_.
The _iterable_ may be `NULL` to create a new empty frozenset. Return the new
set on success or `NULL` on failure. Raise [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if _iterable_ is
not actually iterable.

The following functions and macros are available for instances of [`set`](https://docs.python.org/3/library/stdtypes.html#set "set")
or [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") or instances of their subtypes.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") PySet\_Size( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*anyset) [¶](https://docs.python.org/3/c-api/set.html#c.PySet_Size "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Return the length of a [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") or [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") object. Equivalent to
`len(anyset)`. Raises a [`SystemError`](https://docs.python.org/3/library/exceptions.html#SystemError "SystemError") if _anyset_ is not a
[`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset"), or an instance of a subtype.

[Py\_ssize\_t](https://docs.python.org/3/c-api/intro.html#c.Py_ssize_t "Py_ssize_t") PySet\_GET\_SIZE( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*anyset) [¶](https://docs.python.org/3/c-api/set.html#c.PySet_GET_SIZE "Link to this definition")

Macro form of [`PySet_Size()`](https://docs.python.org/3/c-api/set.html#c.PySet_Size "PySet_Size") without error checking.

intPySet\_Contains( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*anyset, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*key) [¶](https://docs.python.org/3/c-api/set.html#c.PySet_Contains "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Return `1` if found, `0` if not found, and `-1` if an error is encountered. Unlike
the Python [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__") method, this function does not automatically
convert unhashable sets into temporary frozensets. Raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if
the _key_ is unhashable. Raise [`SystemError`](https://docs.python.org/3/library/exceptions.html#SystemError "SystemError") if _anyset_ is not a
[`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset"), or an instance of a subtype.

intPySet\_Add( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*set, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*key) [¶](https://docs.python.org/3/c-api/set.html#c.PySet_Add "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Add _key_ to a [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") instance. Also works with [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset")
instances (like [`PyTuple_SetItem()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SetItem "PyTuple_SetItem") it can be used to fill in the values
of brand new frozensets before they are exposed to other code). Return `0` on
success or `-1` on failure. Raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if the _key_ is
unhashable. Raise a [`MemoryError`](https://docs.python.org/3/library/exceptions.html#MemoryError "MemoryError") if there is no room to grow. Raise a
[`SystemError`](https://docs.python.org/3/library/exceptions.html#SystemError "SystemError") if _set_ is not an instance of [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") or its
subtype.

The following functions are available for instances of [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") or its
subtypes but not for instances of [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset") or its subtypes.

intPySet\_Discard( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*set, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*key) [¶](https://docs.python.org/3/c-api/set.html#c.PySet_Discard "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Return `1` if found and removed, `0` if not found (no action taken), and `-1` if an
error is encountered. Does not raise [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") for missing keys. Raise a
[`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if the _key_ is unhashable. Unlike the Python [`discard()`](https://docs.python.org/3/library/stdtypes.html#frozenset.discard "frozenset.discard")
method, this function does not automatically convert unhashable sets into
temporary frozensets. Raise [`SystemError`](https://docs.python.org/3/library/exceptions.html#SystemError "SystemError") if _set_ is not an
instance of [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") or its subtype.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PySet\_Pop( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*set) [¶](https://docs.python.org/3/c-api/set.html#c.PySet_Pop "Link to this definition")

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Return a new reference to an arbitrary object in the _set_, and removes the
object from the _set_. Return `NULL` on failure. Raise [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") if the
set is empty. Raise a [`SystemError`](https://docs.python.org/3/library/exceptions.html#SystemError "SystemError") if _set_ is not an instance of
[`set`](https://docs.python.org/3/library/stdtypes.html#set "set") or its subtype.

intPySet\_Clear( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*set) [¶](https://docs.python.org/3/c-api/set.html#c.PySet_Clear "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Empty an existing set of all elements. Return `0` on
success. Return `-1` and raise [`SystemError`](https://docs.python.org/3/library/exceptions.html#SystemError "SystemError") if _set_ is not an instance of
[`set`](https://docs.python.org/3/library/stdtypes.html#set "set") or its subtype.

#### Previous topic

[Dictionary Objects](https://docs.python.org/3/c-api/dict.html "previous chapter")

#### Next topic

[Function Objects](https://docs.python.org/3/c-api/function.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/c-api/set.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/function.html "Function Objects") \|
- [previous](https://docs.python.org/3/c-api/dict.html "Dictionary Objects") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html) »
- [Set Objects](https://docs.python.org/3/c-api/set.html)
- \|

- Theme
AutoLightDark \|