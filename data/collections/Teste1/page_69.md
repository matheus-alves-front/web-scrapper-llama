### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/curses.panel.html "curses.panel — A panel stack extension for curses") \|
- [previous](https://docs.python.org/3/library/curses.html "curses — Terminal handling for character-cell displays") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
- [`curses.ascii` — Utilities for ASCII characters](https://docs.python.org/3/library/curses.ascii.html)
- \|

- Theme
AutoLightDark \|

# `curses.ascii` — Utilities for ASCII characters [¶](https://docs.python.org/3/library/curses.ascii.html\#module-curses.ascii "Link to this heading")

**Source code:** [Lib/curses/ascii.py](https://github.com/python/cpython/tree/3.14/Lib/curses/ascii.py)

* * *

The [`curses.ascii`](https://docs.python.org/3/library/curses.ascii.html#module-curses.ascii "curses.ascii: Constants and set-membership functions for ASCII characters.") module supplies name constants for ASCII characters and
functions to test membership in various ASCII character classes. The constants
supplied are names for control characters as follows:

| Name | Meaning |
| --- | --- |
| curses.ascii.NUL [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.NUL "Link to this definition") |  |
| curses.ascii.SOH [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.SOH "Link to this definition") | Start of heading, console interrupt |
| curses.ascii.STX [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.STX "Link to this definition") | Start of text |
| curses.ascii.ETX [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.ETX "Link to this definition") | End of text |
| curses.ascii.EOT [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.EOT "Link to this definition") | End of transmission |
| curses.ascii.ENQ [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.ENQ "Link to this definition") | Enquiry, goes with [`ACK`](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.ACK "curses.ascii.ACK") flow control |
| curses.ascii.ACK [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.ACK "Link to this definition") | Acknowledgement |
| curses.ascii.BEL [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.BEL "Link to this definition") | Bell |
| curses.ascii.BS [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.BS "Link to this definition") | Backspace |
| curses.ascii.TAB [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.TAB "Link to this definition") | Tab |
| curses.ascii.HT [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.HT "Link to this definition") | Alias for [`TAB`](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.TAB "curses.ascii.TAB"): “Horizontal tab” |
| curses.ascii.LF [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.LF "Link to this definition") | Line feed |
| curses.ascii.NL [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.NL "Link to this definition") | Alias for [`LF`](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.LF "curses.ascii.LF"): “New line” |
| curses.ascii.VT [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.VT "Link to this definition") | Vertical tab |
| curses.ascii.FF [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.FF "Link to this definition") | Form feed |
| curses.ascii.CR [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.CR "Link to this definition") | Carriage return |
| curses.ascii.SO [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.SO "Link to this definition") | Shift-out, begin alternate character set |
| curses.ascii.SI [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.SI "Link to this definition") | Shift-in, resume default character set |
| curses.ascii.DLE [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.DLE "Link to this definition") | Data-link escape |
| curses.ascii.DC1 [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.DC1 "Link to this definition") | XON, for flow control |
| curses.ascii.DC2 [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.DC2 "Link to this definition") | Device control 2, block-mode flow control |
| curses.ascii.DC3 [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.DC3 "Link to this definition") | XOFF, for flow control |
| curses.ascii.DC4 [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.DC4 "Link to this definition") | Device control 4 |
| curses.ascii.NAK [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.NAK "Link to this definition") | Negative acknowledgement |
| curses.ascii.SYN [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.SYN "Link to this definition") | Synchronous idle |
| curses.ascii.ETB [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.ETB "Link to this definition") | End transmission block |
| curses.ascii.CAN [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.CAN "Link to this definition") | Cancel |
| curses.ascii.EM [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.EM "Link to this definition") | End of medium |
| curses.ascii.SUB [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.SUB "Link to this definition") | Substitute |
| curses.ascii.ESC [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.ESC "Link to this definition") | Escape |
| curses.ascii.FS [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.FS "Link to this definition") | File separator |
| curses.ascii.GS [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.GS "Link to this definition") | Group separator |
| curses.ascii.RS [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.RS "Link to this definition") | Record separator, block-mode terminator |
| curses.ascii.US [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.US "Link to this definition") | Unit separator |
| curses.ascii.SP [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.SP "Link to this definition") | Space |
| curses.ascii.DEL [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.DEL "Link to this definition") | Delete |

Note that many of these have little practical significance in modern usage. The
mnemonics derive from teleprinter conventions that predate digital computers.

The module supplies the following functions, patterned on those in the standard
C library:

curses.ascii.isalnum( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.isalnum "Link to this definition")

Checks for an ASCII alphanumeric character; it is equivalent to `isalpha(c) or
isdigit(c)`.

curses.ascii.isalpha( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.isalpha "Link to this definition")

Checks for an ASCII alphabetic character; it is equivalent to `isupper(c) or
islower(c)`.

curses.ascii.isascii( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.isascii "Link to this definition")

Checks for a character value that fits in the 7-bit ASCII set.

curses.ascii.isblank( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.isblank "Link to this definition")

Checks for an ASCII whitespace character; space or horizontal tab.

curses.ascii.iscntrl( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.iscntrl "Link to this definition")

Checks for an ASCII control character (in the range 0x00 to 0x1f or 0x7f).

curses.ascii.isdigit( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.isdigit "Link to this definition")

Checks for an ASCII decimal digit, `'0'` through `'9'`. This is equivalent
to `c in string.digits`.

curses.ascii.isgraph( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.isgraph "Link to this definition")

Checks for ASCII any printable character except space.

curses.ascii.islower( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.islower "Link to this definition")

Checks for an ASCII lower-case character.

curses.ascii.isprint( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.isprint "Link to this definition")

Checks for any ASCII printable character including space.

curses.ascii.ispunct( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.ispunct "Link to this definition")

Checks for any printable ASCII character which is not a space or an alphanumeric
character.

curses.ascii.isspace( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.isspace "Link to this definition")

Checks for ASCII white-space characters; space, line feed, carriage return, form
feed, horizontal tab, vertical tab.

curses.ascii.isupper( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.isupper "Link to this definition")

Checks for an ASCII uppercase letter.

curses.ascii.isxdigit( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.isxdigit "Link to this definition")

Checks for an ASCII hexadecimal digit. This is equivalent to `c in
string.hexdigits`.

curses.ascii.isctrl( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.isctrl "Link to this definition")

Checks for an ASCII control character (ordinal values 0 to 31).

curses.ascii.ismeta( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.ismeta "Link to this definition")

Checks for a non-ASCII character (ordinal values 0x80 and above).

These functions accept either integers or single-character strings; when the argument is a
string, it is first converted using the built-in function [`ord()`](https://docs.python.org/3/library/functions.html#ord "ord").

Note that all these functions check ordinal bit values derived from the
character of the string you pass in; they do not actually know anything about
the host machine’s character encoding.

The following two functions take either a single-character string or integer
byte value; they return a value of the same type.

curses.ascii.ascii( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.ascii "Link to this definition")

Return the ASCII value corresponding to the low 7 bits of _c_.

curses.ascii.ctrl( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.ctrl "Link to this definition")

Return the control character corresponding to the given character (the character
bit value is bitwise-anded with 0x1f).

curses.ascii.alt( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.alt "Link to this definition")

Return the 8-bit character corresponding to the given ASCII character (the
character bit value is bitwise-ored with 0x80).

The following function takes either a single-character string or integer value;
it returns a string.

curses.ascii.unctrl( _c_) [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.unctrl "Link to this definition")

Return a string representation of the ASCII character _c_. If _c_ is printable,
this string is the character itself. If the character is a control character
(0x00–0x1f) the string consists of a caret (`'^'`) followed by the
corresponding uppercase letter. If the character is an ASCII delete (0x7f) the
string is `'^?'`. If the character has its meta bit (0x80) set, the meta bit
is stripped, the preceding rules applied, and `'!'` prepended to the result.

curses.ascii.controlnames [¶](https://docs.python.org/3/library/curses.ascii.html#curses.ascii.controlnames "Link to this definition")

A 33-element string array that contains the ASCII mnemonics for the thirty-two
ASCII control characters from 0 (NUL) to 0x1f (US), in order, plus the mnemonic
`SP` for the space character.

#### Previous topic

[`curses` — Terminal handling for character-cell displays](https://docs.python.org/3/library/curses.html "previous chapter")

#### Next topic

[`curses.panel` — A panel stack extension for curses](https://docs.python.org/3/library/curses.panel.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/curses.ascii.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/curses.panel.html "curses.panel — A panel stack extension for curses") \|
- [previous](https://docs.python.org/3/library/curses.html "curses — Terminal handling for character-cell displays") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
- [`curses.ascii` — Utilities for ASCII characters](https://docs.python.org/3/library/curses.ascii.html)
- \|

- Theme
AutoLightDark \|