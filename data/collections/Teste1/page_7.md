### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/complex.html "Complex Number Objects") \|
- [previous](https://docs.python.org/3/c-api/bool.html "Boolean Objects") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html) »
- [Floating-Point Objects](https://docs.python.org/3/c-api/float.html)
- \|

- Theme
AutoLightDark \|

# Floating-Point Objects [¶](https://docs.python.org/3/c-api/float.html\#floating-point-objects "Link to this heading")

typePyFloatObject [¶](https://docs.python.org/3/c-api/float.html#c.PyFloatObject "Link to this definition")

This subtype of [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject") represents a Python floating-point object.

[PyTypeObject](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject") PyFloat\_Type [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_Type "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

This instance of [`PyTypeObject`](https://docs.python.org/3/c-api/type.html#c.PyTypeObject "PyTypeObject") represents the Python floating-point
type. This is the same object as [`float`](https://docs.python.org/3/library/functions.html#float "float") in the Python layer.

intPyFloat\_Check( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*p) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_Check "Link to this definition")

Return true if its argument is a [`PyFloatObject`](https://docs.python.org/3/c-api/float.html#c.PyFloatObject "PyFloatObject") or a subtype of
[`PyFloatObject`](https://docs.python.org/3/c-api/float.html#c.PyFloatObject "PyFloatObject"). This function always succeeds.

intPyFloat\_CheckExact( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*p) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_CheckExact "Link to this definition")

Return true if its argument is a [`PyFloatObject`](https://docs.python.org/3/c-api/float.html#c.PyFloatObject "PyFloatObject"), but not a subtype of
[`PyFloatObject`](https://docs.python.org/3/c-api/float.html#c.PyFloatObject "PyFloatObject"). This function always succeeds.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyFloat\_FromString( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*str) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_FromString "Link to this definition")

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Create a [`PyFloatObject`](https://docs.python.org/3/c-api/float.html#c.PyFloatObject "PyFloatObject") object based on the string value in _str_, or
`NULL` on failure.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyFloat\_FromDouble(doublev) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_FromDouble "Link to this definition")

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Create a [`PyFloatObject`](https://docs.python.org/3/c-api/float.html#c.PyFloatObject "PyFloatObject") object from _v_, or `NULL` on failure.

doublePyFloat\_AsDouble( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*pyfloat) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_AsDouble "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Return a C double representation of the contents of _pyfloat_. If
_pyfloat_ is not a Python floating-point object but has a [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__")
method, this method will first be called to convert _pyfloat_ into a float.
If `__float__()` is not defined then it falls back to [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__").
This method returns `-1.0` upon failure, so one should call
[`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred") to check for errors.

Changed in version 3.8: Use [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") if available.

doublePyFloat\_AS\_DOUBLE( [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*pyfloat) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_AS_DOUBLE "Link to this definition")

Return a C double representation of the contents of _pyfloat_, but
without error checking.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")\*PyFloat\_GetInfo(void) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_GetInfo "Link to this definition")

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Return a structseq instance which contains information about the
precision, minimum and maximum values of a float. It’s a thin wrapper
around the header file `float.h`.

doublePyFloat\_GetMax() [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_GetMax "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Return the maximum representable finite float _DBL\_MAX_ as C double.

doublePyFloat\_GetMin() [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_GetMin "Link to this definition")

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)._

Return the minimum normalized positive float _DBL\_MIN_ as C double.

Py\_INFINITY [¶](https://docs.python.org/3/c-api/float.html#c.Py_INFINITY "Link to this definition")

This macro expands a to constant expression of type double, that
represents the positive infinity.

On most platforms, this is equivalent to the `INFINITY` macro from
the C11 standard `<math.h>` header.

Py\_NAN [¶](https://docs.python.org/3/c-api/float.html#c.Py_NAN "Link to this definition")

This macro expands a to constant expression of type double, that
represents a quiet not-a-number (qNaN) value.

On most platforms, this is equivalent to the `NAN` macro from
the C11 standard `<math.h>` header.

Py\_MATH\_E [¶](https://docs.python.org/3/c-api/float.html#c.Py_MATH_E "Link to this definition")

The definition (accurate for a double type) of the [`math.e`](https://docs.python.org/3/library/math.html#math.e "math.e") constant.

Py\_MATH\_El [¶](https://docs.python.org/3/c-api/float.html#c.Py_MATH_El "Link to this definition")

High precision (long double) definition of [`e`](https://docs.python.org/3/library/math.html#math.e "math.e") constant.

Py\_MATH\_PI [¶](https://docs.python.org/3/c-api/float.html#c.Py_MATH_PI "Link to this definition")

The definition (accurate for a double type) of the [`math.pi`](https://docs.python.org/3/library/math.html#math.pi "math.pi") constant.

Py\_MATH\_PIl [¶](https://docs.python.org/3/c-api/float.html#c.Py_MATH_PIl "Link to this definition")

High precision (long double) definition of [`pi`](https://docs.python.org/3/library/math.html#math.pi "math.pi") constant.

Py\_MATH\_TAU [¶](https://docs.python.org/3/c-api/float.html#c.Py_MATH_TAU "Link to this definition")

The definition (accurate for a double type) of the [`math.tau`](https://docs.python.org/3/library/math.html#math.tau "math.tau") constant.

Added in version 3.6.

Py\_RETURN\_NAN [¶](https://docs.python.org/3/c-api/float.html#c.Py_RETURN_NAN "Link to this definition")

Return [`math.nan`](https://docs.python.org/3/library/math.html#math.nan "math.nan") from a function.

On most platforms, this is equivalent to `return PyFloat_FromDouble(NAN)`.

Py\_RETURN\_INF(sign) [¶](https://docs.python.org/3/c-api/float.html#c.Py_RETURN_INF "Link to this definition")

Return [`math.inf`](https://docs.python.org/3/library/math.html#math.inf "math.inf") or [`-math.inf`](https://docs.python.org/3/library/math.html#math.inf "math.inf") from a function,
depending on the sign of _sign_.

On most platforms, this is equivalent to the following:

```
return PyFloat_FromDouble(copysign(INFINITY, sign));
```

## Pack and Unpack functions [¶](https://docs.python.org/3/c-api/float.html\#pack-and-unpack-functions "Link to this heading")

The pack and unpack functions provide an efficient platform-independent way to
store floating-point values as byte strings. The Pack routines produce a bytes
string from a C double, and the Unpack routines produce a C
double from such a bytes string. The suffix (2, 4 or 8) specifies the
number of bytes in the bytes string.

On platforms that appear to use IEEE 754 formats these functions work by
copying bits. On other platforms, the 2-byte format is identical to the IEEE
754 binary16 half-precision format, the 4-byte format (32-bit) is identical to
the IEEE 754 binary32 single precision format, and the 8-byte format to the
IEEE 754 binary64 double precision format, although the packing of INFs and
NaNs (if such things exist on the platform) isn’t handled correctly, and
attempting to unpack a bytes string containing an IEEE INF or NaN will raise an
exception.

Note that NaNs type may not be preserved on IEEE platforms (signaling NaN become
quiet NaN), for example on x86 systems in 32-bit mode.

On non-IEEE platforms with more precision, or larger dynamic range, than IEEE
754 supports, not all values can be packed; on non-IEEE platforms with less
precision, or smaller dynamic range, not all values can be unpacked. What
happens in such cases is partly accidental (alas).

Added in version 3.11.

### Pack functions [¶](https://docs.python.org/3/c-api/float.html\#pack-functions "Link to this heading")

The pack routines write 2, 4 or 8 bytes, starting at _p_. _le_ is an
int argument, non-zero if you want the bytes string in little-endian
format (exponent last, at `p+1`, `p+3`, or `p+6``p+7`), zero if you
want big-endian format (exponent first, at _p_). The `PY_BIG_ENDIAN`
constant can be used to use the native endian: it is equal to `1` on big
endian processor, or `0` on little endian processor.

Return value: `0` if all is OK, `-1` if error (and an exception is set,
most likely [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError")).

There are two problems on non-IEEE platforms:

- What this does is undefined if _x_ is a NaN or infinity.

- `-0.0` and `+0.0` produce the same bytes string.


intPyFloat\_Pack2(doublex, char\*p, intle) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_Pack2 "Link to this definition")

Pack a C double as the IEEE 754 binary16 half-precision format.

intPyFloat\_Pack4(doublex, char\*p, intle) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_Pack4 "Link to this definition")

Pack a C double as the IEEE 754 binary32 single precision format.

intPyFloat\_Pack8(doublex, char\*p, intle) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_Pack8 "Link to this definition")

Pack a C double as the IEEE 754 binary64 double precision format.

### Unpack functions [¶](https://docs.python.org/3/c-api/float.html\#unpack-functions "Link to this heading")

The unpack routines read 2, 4 or 8 bytes, starting at _p_. _le_ is an
int argument, non-zero if the bytes string is in little-endian format
(exponent last, at `p+1`, `p+3` or `p+6` and `p+7`), zero if big-endian
(exponent first, at _p_). The `PY_BIG_ENDIAN` constant can be used to
use the native endian: it is equal to `1` on big endian processor, or `0`
on little endian processor.

Return value: The unpacked double. On error, this is `-1.0` and
[`PyErr_Occurred()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_Occurred "PyErr_Occurred") is true (and an exception is set, most likely
[`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError")).

Note that on a non-IEEE platform this will refuse to unpack a bytes string that
represents a NaN or infinity.

doublePyFloat\_Unpack2(constchar\*p, intle) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_Unpack2 "Link to this definition")

Unpack the IEEE 754 binary16 half-precision format as a C double.

doublePyFloat\_Unpack4(constchar\*p, intle) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_Unpack4 "Link to this definition")

Unpack the IEEE 754 binary32 single precision format as a C double.

doublePyFloat\_Unpack8(constchar\*p, intle) [¶](https://docs.python.org/3/c-api/float.html#c.PyFloat_Unpack8 "Link to this definition")

Unpack the IEEE 754 binary64 double precision format as a C double.

### [Table of Contents](https://docs.python.org/3/contents.html)

- [Floating-Point Objects](https://docs.python.org/3/c-api/float.html#)
  - [Pack and Unpack functions](https://docs.python.org/3/c-api/float.html#pack-and-unpack-functions)
    - [Pack functions](https://docs.python.org/3/c-api/float.html#pack-functions)
    - [Unpack functions](https://docs.python.org/3/c-api/float.html#unpack-functions)

#### Previous topic

[Boolean Objects](https://docs.python.org/3/c-api/bool.html "previous chapter")

#### Next topic

[Complex Number Objects](https://docs.python.org/3/c-api/complex.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/c-api/float.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/c-api/complex.html "Complex Number Objects") \|
- [previous](https://docs.python.org/3/c-api/bool.html "Boolean Objects") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [Python/C API Reference Manual](https://docs.python.org/3/c-api/index.html) »
- [Concrete Objects Layer](https://docs.python.org/3/c-api/concrete.html) »
- [Floating-Point Objects](https://docs.python.org/3/c-api/float.html)
- \|

- Theme
AutoLightDark \|