### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/email.headerregistry.html "email.headerregistry: Custom Header Objects") \|
- [previous](https://docs.python.org/3/library/email.policy.html "email.policy: Policy Objects") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
- [`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html) »
- [`email.errors`: Exception and Defect classes](https://docs.python.org/3/library/email.errors.html)
- \|

- Theme
AutoLightDark \|

# `email.errors`: Exception and Defect classes [¶](https://docs.python.org/3/library/email.errors.html\#module-email.errors "Link to this heading")

**Source code:** [Lib/email/errors.py](https://github.com/python/cpython/tree/3.14/Lib/email/errors.py)

* * *

The following exception classes are defined in the [`email.errors`](https://docs.python.org/3/library/email.errors.html#module-email.errors "email.errors: The exception classes used by the email package.") module:

_exception_ email.errors.MessageError [¶](https://docs.python.org/3/library/email.errors.html#email.errors.MessageError "Link to this definition")

This is the base class for all exceptions that the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.") package can
raise. It is derived from the standard [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") class and defines no
additional methods.

_exception_ email.errors.MessageParseError [¶](https://docs.python.org/3/library/email.errors.html#email.errors.MessageParseError "Link to this definition")

This is the base class for exceptions raised by the
[`Parser`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser "email.parser.Parser") class. It is derived from
[`MessageError`](https://docs.python.org/3/library/email.errors.html#email.errors.MessageError "email.errors.MessageError"). This class is also used internally by the parser used
by [`headerregistry`](https://docs.python.org/3/library/email.headerregistry.html#module-email.headerregistry "email.headerregistry: Automatic Parsing of headers based on the field name").

_exception_ email.errors.HeaderParseError [¶](https://docs.python.org/3/library/email.errors.html#email.errors.HeaderParseError "Link to this definition")

Raised under some error conditions when parsing the [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) headers of a
message, this class is derived from [`MessageParseError`](https://docs.python.org/3/library/email.errors.html#email.errors.MessageParseError "email.errors.MessageParseError"). The
[`set_boundary()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_boundary "email.message.EmailMessage.set_boundary") method will raise this
error if the content type is unknown when the method is called.
[`Header`](https://docs.python.org/3/library/email.header.html#email.header.Header "email.header.Header") may raise this error for certain base64
decoding errors, and when an attempt is made to create a header that appears
to contain an embedded header (that is, there is what is supposed to be a
continuation line that has no leading whitespace and looks like a header).

_exception_ email.errors.BoundaryError [¶](https://docs.python.org/3/library/email.errors.html#email.errors.BoundaryError "Link to this definition")

Deprecated and no longer used.

_exception_ email.errors.MultipartConversionError [¶](https://docs.python.org/3/library/email.errors.html#email.errors.MultipartConversionError "Link to this definition")

Raised if the [`attach()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.attach "email.message.Message.attach") method is called
on an instance of a class derived from
[`MIMENonMultipart`](https://docs.python.org/3/library/email.mime.html#email.mime.nonmultipart.MIMENonMultipart "email.mime.nonmultipart.MIMENonMultipart") (e.g.
[`MIMEImage`](https://docs.python.org/3/library/email.mime.html#email.mime.image.MIMEImage "email.mime.image.MIMEImage")).
[`MultipartConversionError`](https://docs.python.org/3/library/email.errors.html#email.errors.MultipartConversionError "email.errors.MultipartConversionError") multiply
inherits from [`MessageError`](https://docs.python.org/3/library/email.errors.html#email.errors.MessageError "email.errors.MessageError") and the built-in [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").

_exception_ email.errors.HeaderWriteError [¶](https://docs.python.org/3/library/email.errors.html#email.errors.HeaderWriteError "Link to this definition")

Raised when an error occurs when the [`generator`](https://docs.python.org/3/library/email.generator.html#module-email.generator "email.generator: Generate flat text email messages from a message structure.") outputs
headers.

_exception_ email.errors.MessageDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.MessageDefect "Link to this definition")

This is the base class for all defects found when parsing email messages.
It is derived from [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

_exception_ email.errors.HeaderDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.HeaderDefect "Link to this definition")

This is the base class for all defects found when parsing email headers.
It is derived from [`MessageDefect`](https://docs.python.org/3/library/email.errors.html#email.errors.MessageDefect "email.errors.MessageDefect").

Here is the list of the defects that the [`FeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.FeedParser "email.parser.FeedParser")
can find while parsing messages. Note that the defects are added to the message
where the problem was found, so for example, if a message nested inside a
_multipart/alternative_ had a malformed header, that nested message
object would have a defect, but the containing messages would not.

All defect classes are subclassed from [`email.errors.MessageDefect`](https://docs.python.org/3/library/email.errors.html#email.errors.MessageDefect "email.errors.MessageDefect").

_exception_ email.errors.NoBoundaryInMultipartDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.NoBoundaryInMultipartDefect "Link to this definition")

A message claimed to be a multipart, but had no _boundary_
parameter.

_exception_ email.errors.StartBoundaryNotFoundDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.StartBoundaryNotFoundDefect "Link to this definition")

The start boundary claimed in the _Content-Type_ header was
never found.

_exception_ email.errors.CloseBoundaryNotFoundDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.CloseBoundaryNotFoundDefect "Link to this definition")

A start boundary was found, but no corresponding close boundary was ever
found.

Added in version 3.3.

_exception_ email.errors.FirstHeaderLineIsContinuationDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.FirstHeaderLineIsContinuationDefect "Link to this definition")

The message had a continuation line as its first header line.

_exception_ email.errors.MisplacedEnvelopeHeaderDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.MisplacedEnvelopeHeaderDefect "Link to this definition")

A “Unix From” header was found in the middle of a header block.

_exception_ email.errors.MissingHeaderBodySeparatorDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.MissingHeaderBodySeparatorDefect "Link to this definition")

A line was found while parsing headers that had no leading white space but
contained no ‘:’. Parsing continues assuming that the line represents the
first line of the body.

Added in version 3.3.

_exception_ email.errors.MalformedHeaderDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.MalformedHeaderDefect "Link to this definition")

A header was found that was missing a colon, or was otherwise malformed.

Deprecated since version 3.3: This defect has not been used for several Python versions.

_exception_ email.errors.MultipartInvariantViolationDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.MultipartInvariantViolationDefect "Link to this definition")

A message claimed to be a _multipart_, but no subparts were found.
Note that when a message has this defect, its
[`is_multipart()`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message.is_multipart "email.message.Message.is_multipart") method may return `False`
even though its content type claims to be _multipart_.

_exception_ email.errors.InvalidBase64PaddingDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.InvalidBase64PaddingDefect "Link to this definition")

When decoding a block of base64 encoded bytes, the padding was not correct.
Enough padding is added to perform the decode, but the resulting decoded
bytes may be invalid.

_exception_ email.errors.InvalidBase64CharactersDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.InvalidBase64CharactersDefect "Link to this definition")

When decoding a block of base64 encoded bytes, characters outside the base64
alphabet were encountered. The characters are ignored, but the resulting
decoded bytes may be invalid.

_exception_ email.errors.InvalidBase64LengthDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.InvalidBase64LengthDefect "Link to this definition")

When decoding a block of base64 encoded bytes, the number of non-padding
base64 characters was invalid (1 more than a multiple of 4). The encoded
block was kept as-is.

_exception_ email.errors.InvalidDateDefect [¶](https://docs.python.org/3/library/email.errors.html#email.errors.InvalidDateDefect "Link to this definition")

When decoding an invalid or unparsable date field. The original value is
kept as-is.

#### Previous topic

[`email.policy`: Policy Objects](https://docs.python.org/3/library/email.policy.html "previous chapter")

#### Next topic

[`email.headerregistry`: Custom Header Objects](https://docs.python.org/3/library/email.headerregistry.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/email.errors.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/email.headerregistry.html "email.headerregistry: Custom Header Objects") \|
- [previous](https://docs.python.org/3/library/email.policy.html "email.policy: Policy Objects") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
- [`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html) »
- [`email.errors`: Exception and Defect classes](https://docs.python.org/3/library/email.errors.html)
- \|

- Theme
AutoLightDark \|