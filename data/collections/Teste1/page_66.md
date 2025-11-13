### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/email.generator.html "email.generator: Generating MIME documents") \|
- [previous](https://docs.python.org/3/library/email.message.html "email.message: Representing an email message") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
- [`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html) »
- [`email.parser`: Parsing email messages](https://docs.python.org/3/library/email.parser.html)
- \|

- Theme
AutoLightDark \|

# `email.parser`: Parsing email messages [¶](https://docs.python.org/3/library/email.parser.html\#module-email.parser "Link to this heading")

**Source code:** [Lib/email/parser.py](https://github.com/python/cpython/tree/3.14/Lib/email/parser.py)

* * *

Message object structures can be created in one of two ways: they can be
created from whole cloth by creating an [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage")
object, adding headers using the dictionary interface, and adding payload(s)
using [`set_content()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.set_content "email.message.EmailMessage.set_content") and related methods, or
they can be created by parsing a serialized representation of the email
message.

The [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.") package provides a standard parser that understands most email
document structures, including MIME documents. You can pass the parser a
bytes, string or file object, and the parser will return to you the root
[`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage") instance of the object structure. For
simple, non-MIME messages the payload of this root object will likely be a
string containing the text of the message. For MIME messages, the root object
will return `True` from its [`is_multipart()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.is_multipart "email.message.EmailMessage.is_multipart")
method, and the subparts can be accessed via the payload manipulation methods,
such as [`get_body()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.get_body "email.message.EmailMessage.get_body"),
[`iter_parts()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.iter_parts "email.message.EmailMessage.iter_parts"), and
[`walk()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.walk "email.message.EmailMessage.walk").

There are actually two parser interfaces available for use, the [`Parser`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser "email.parser.Parser")
API and the incremental [`FeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.FeedParser "email.parser.FeedParser") API. The [`Parser`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser "email.parser.Parser") API is
most useful if you have the entire text of the message in memory, or if the
entire message lives in a file on the file system. [`FeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.FeedParser "email.parser.FeedParser") is more
appropriate when you are reading the message from a stream which might block
waiting for more input (such as reading an email message from a socket). The
[`FeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.FeedParser "email.parser.FeedParser") can consume and parse the message incrementally, and only
returns the root object when you close the parser.

Note that the parser can be extended in limited ways, and of course you can
implement your own parser completely from scratch. All of the logic that
connects the [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.") package’s bundled parser and the
[`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage") class is embodied in the [`Policy`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy "email.policy.Policy")
class, so a custom parser can create message object trees any way it finds
necessary by implementing custom versions of the appropriate `Policy`
methods.

## FeedParser API [¶](https://docs.python.org/3/library/email.parser.html\#feedparser-api "Link to this heading")

The [`BytesFeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser "email.parser.BytesFeedParser"), imported from the `email.feedparser` module,
provides an API that is conducive to incremental parsing of email messages,
such as would be necessary when reading the text of an email message from a
source that can block (such as a socket). The [`BytesFeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser "email.parser.BytesFeedParser") can of
course be used to parse an email message fully contained in a [bytes-like\\
object](https://docs.python.org/3/glossary.html#term-bytes-like-object), string, or file, but the [`BytesParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser "email.parser.BytesParser") API may be more
convenient for such use cases. The semantics and results of the two parser
APIs are identical.

The [`BytesFeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser "email.parser.BytesFeedParser")’s API is simple; you create an instance, feed it a
bunch of bytes until there’s no more to feed it, then close the parser to
retrieve the root message object. The [`BytesFeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser "email.parser.BytesFeedParser") is extremely
accurate when parsing standards-compliant messages, and it does a very good job
of parsing non-compliant messages, providing information about how a message
was deemed broken. It will populate a message object’s
[`defects`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.defects "email.message.EmailMessage.defects") attribute with a list of any
problems it found in a message. See the [`email.errors`](https://docs.python.org/3/library/email.errors.html#module-email.errors "email.errors: The exception classes used by the email package.") module for the
list of defects that it can find.

Here is the API for the [`BytesFeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser "email.parser.BytesFeedParser"):

_class_ email.parser.BytesFeedParser( _\_factory=None_, _\*_, _policy=policy.compat32_) [¶](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser "Link to this definition")

Create a [`BytesFeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser "email.parser.BytesFeedParser") instance. Optional _\_factory_ is a
no-argument callable; if not specified use the
[`message_factory`](https://docs.python.org/3/library/email.policy.html#email.policy.Policy.message_factory "email.policy.Policy.message_factory") from the _policy_. Call
_\_factory_ whenever a new message object is needed.

If _policy_ is specified use the rules it specifies to update the
representation of the message. If _policy_ is not set, use the
[`compat32`](https://docs.python.org/3/library/email.policy.html#email.policy.Compat32 "email.policy.Compat32") policy, which maintains backward
compatibility with the Python 3.2 version of the email package and provides
[`Message`](https://docs.python.org/3/library/email.compat32-message.html#email.message.Message "email.message.Message") as the default factory. All other policies
provide [`EmailMessage`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage "email.message.EmailMessage") as the default _\_factory_. For
more information on what else _policy_ controls, see the
[`policy`](https://docs.python.org/3/library/email.policy.html#module-email.policy "email.policy: Controlling the parsing and generating of messages") documentation.

Note: **The policy keyword should always be specified**; The default will
change to [`email.policy.default`](https://docs.python.org/3/library/email.policy.html#email.policy.default "email.policy.default") in a future version of Python.

Added in version 3.2.

Changed in version 3.3: Added the _policy_ keyword.

Changed in version 3.6: _\_factory_ defaults to the policy `message_factory`.

feed( _data_) [¶](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser.feed "Link to this definition")

Feed the parser some more data. _data_ should be a [bytes-like\\
object](https://docs.python.org/3/glossary.html#term-bytes-like-object) containing one or more lines. The lines can be partial and the
parser will stitch such partial lines together properly. The lines can
have any of the three common line endings: carriage return, newline, or
carriage return and newline (they can even be mixed).

close() [¶](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser.close "Link to this definition")

Complete the parsing of all previously fed data and return the root
message object. It is undefined what happens if [`feed()`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser.feed "email.parser.BytesFeedParser.feed") is called
after this method has been called.

_class_ email.parser.FeedParser( _\_factory=None_, _\*_, _policy=policy.compat32_) [¶](https://docs.python.org/3/library/email.parser.html#email.parser.FeedParser "Link to this definition")

Works like [`BytesFeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser "email.parser.BytesFeedParser") except that the input to the
[`feed()`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser.feed "email.parser.BytesFeedParser.feed") method must be a string. This is of limited
utility, since the only way for such a message to be valid is for it to
contain only ASCII text or, if [`utf8`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy.utf8 "email.policy.EmailPolicy.utf8") is
`True`, no binary attachments.

Changed in version 3.3: Added the _policy_ keyword.

## Parser API [¶](https://docs.python.org/3/library/email.parser.html\#parser-api "Link to this heading")

The [`BytesParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser "email.parser.BytesParser") class, imported from the [`email.parser`](https://docs.python.org/3/library/email.parser.html#module-email.parser "email.parser: Parse flat text email messages to produce a message object structure.") module,
provides an API that can be used to parse a message when the complete contents
of the message are available in a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) or file. The
[`email.parser`](https://docs.python.org/3/library/email.parser.html#module-email.parser "email.parser: Parse flat text email messages to produce a message object structure.") module also provides [`Parser`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser "email.parser.Parser") for parsing strings,
and header-only parsers, [`BytesHeaderParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesHeaderParser "email.parser.BytesHeaderParser") and
[`HeaderParser`](https://docs.python.org/3/library/email.parser.html#email.parser.HeaderParser "email.parser.HeaderParser"), which can be used if you’re only interested in the
headers of the message. [`BytesHeaderParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesHeaderParser "email.parser.BytesHeaderParser") and [`HeaderParser`](https://docs.python.org/3/library/email.parser.html#email.parser.HeaderParser "email.parser.HeaderParser")
can be much faster in these situations, since they do not attempt to parse the
message body, instead setting the payload to the raw body.

_class_ email.parser.BytesParser( _\_class=None_, _\*_, _policy=policy.compat32_) [¶](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser "Link to this definition")

Create a [`BytesParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser "email.parser.BytesParser") instance. The _\_class_ and _policy_
arguments have the same meaning and semantics as the _\_factory_
and _policy_ arguments of [`BytesFeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesFeedParser "email.parser.BytesFeedParser").

Note: **The policy keyword should always be specified**; The default will
change to [`email.policy.default`](https://docs.python.org/3/library/email.policy.html#email.policy.default "email.policy.default") in a future version of Python.

Changed in version 3.3: Removed the _strict_ argument that was deprecated in 2.4. Added the
_policy_ keyword.

Changed in version 3.6: _\_class_ defaults to the policy `message_factory`.

parse( _fp_, _headersonly=False_) [¶](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser.parse "Link to this definition")

Read all the data from the binary file-like object _fp_, parse the
resulting bytes, and return the message object. _fp_ must support
both the [`readline()`](https://docs.python.org/3/library/io.html#io.IOBase.readline "io.IOBase.readline") and the `read()`
methods.

The bytes contained in _fp_ must be formatted as a block of [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html)
(or, if [`utf8`](https://docs.python.org/3/library/email.policy.html#email.policy.EmailPolicy.utf8 "email.policy.EmailPolicy.utf8") is `True`, [**RFC 6532**](https://datatracker.ietf.org/doc/html/rfc6532.html))
style headers and header continuation lines, optionally preceded by an
envelope header. The header block is terminated either by the end of the
data or by a blank line. Following the header block is the body of the
message (which may contain MIME-encoded subparts, including subparts
with a _Content-Transfer-Encoding_ of `8bit`).

Optional _headersonly_ is a flag specifying whether to stop parsing after
reading the headers or not. The default is `False`, meaning it parses
the entire contents of the file.

parsebytes( _bytes_, _headersonly=False_) [¶](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser.parsebytes "Link to this definition")

Similar to the [`parse()`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser.parse "email.parser.BytesParser.parse") method, except it takes a [bytes-like\\
object](https://docs.python.org/3/glossary.html#term-bytes-like-object) instead of a file-like object. Calling this method on a
[bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object) is equivalent to wrapping _bytes_ in a
[`BytesIO`](https://docs.python.org/3/library/io.html#io.BytesIO "io.BytesIO") instance first and calling [`parse()`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser.parse "email.parser.BytesParser.parse").

Optional _headersonly_ is as with the [`parse()`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser.parse "email.parser.BytesParser.parse") method.

Added in version 3.2.

_class_ email.parser.BytesHeaderParser( _\_class=None_, _\*_, _policy=policy.compat32_) [¶](https://docs.python.org/3/library/email.parser.html#email.parser.BytesHeaderParser "Link to this definition")

Exactly like [`BytesParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser "email.parser.BytesParser"), except that _headersonly_
defaults to `True`.

Added in version 3.3.

_class_ email.parser.Parser( _\_class=None_, _\*_, _policy=policy.compat32_) [¶](https://docs.python.org/3/library/email.parser.html#email.parser.Parser "Link to this definition")

This class is parallel to [`BytesParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser "email.parser.BytesParser"), but handles string input.

Changed in version 3.3: Removed the _strict_ argument. Added the _policy_ keyword.

Changed in version 3.6: _\_class_ defaults to the policy `message_factory`.

parse( _fp_, _headersonly=False_) [¶](https://docs.python.org/3/library/email.parser.html#email.parser.Parser.parse "Link to this definition")

Read all the data from the text-mode file-like object _fp_, parse the
resulting text, and return the root message object. _fp_ must support
both the [`readline()`](https://docs.python.org/3/library/io.html#io.TextIOBase.readline "io.TextIOBase.readline") and the
[`read()`](https://docs.python.org/3/library/io.html#io.TextIOBase.read "io.TextIOBase.read") methods on file-like objects.

Other than the text mode requirement, this method operates like
[`BytesParser.parse()`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser.parse "email.parser.BytesParser.parse").

parsestr( _text_, _headersonly=False_) [¶](https://docs.python.org/3/library/email.parser.html#email.parser.Parser.parsestr "Link to this definition")

Similar to the [`parse()`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser.parse "email.parser.Parser.parse") method, except it takes a string object
instead of a file-like object. Calling this method on a string is
equivalent to wrapping _text_ in a [`StringIO`](https://docs.python.org/3/library/io.html#io.StringIO "io.StringIO") instance first
and calling [`parse()`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser.parse "email.parser.Parser.parse").

Optional _headersonly_ is as with the [`parse()`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser.parse "email.parser.Parser.parse") method.

_class_ email.parser.HeaderParser( _\_class=None_, _\*_, _policy=policy.compat32_) [¶](https://docs.python.org/3/library/email.parser.html#email.parser.HeaderParser "Link to this definition")

Exactly like [`Parser`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser "email.parser.Parser"), except that _headersonly_
defaults to `True`.

Since creating a message object structure from a string or a file object is such
a common task, four functions are provided as a convenience. They are available
in the top-level [`email`](https://docs.python.org/3/library/email.html#module-email "email: Package supporting the parsing, manipulating, and generating email messages.") package namespace.

email.message\_from\_bytes( _s_, _\_class=None_, _\*_, _policy=policy.compat32_) [¶](https://docs.python.org/3/library/email.parser.html#email.message_from_bytes "Link to this definition")

Return a message object structure from a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object). This is
equivalent to `BytesParser().parsebytes(s)`. Optional _\_class_ and
_policy_ are interpreted as with the [`BytesParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser "email.parser.BytesParser") class
constructor.

Added in version 3.2.

Changed in version 3.3: Removed the _strict_ argument. Added the _policy_ keyword.

email.message\_from\_binary\_file( _fp_, _\_class=None_, _\*_, _policy=policy.compat32_) [¶](https://docs.python.org/3/library/email.parser.html#email.message_from_binary_file "Link to this definition")

Return a message object structure tree from an open binary [file\\
object](https://docs.python.org/3/glossary.html#term-file-object). This is equivalent to `BytesParser().parse(fp)`. _\_class_ and
_policy_ are interpreted as with the [`BytesParser`](https://docs.python.org/3/library/email.parser.html#email.parser.BytesParser "email.parser.BytesParser") class
constructor.

Added in version 3.2.

Changed in version 3.3: Removed the _strict_ argument. Added the _policy_ keyword.

email.message\_from\_string( _s_, _\_class=None_, _\*_, _policy=policy.compat32_) [¶](https://docs.python.org/3/library/email.parser.html#email.message_from_string "Link to this definition")

Return a message object structure from a string. This is equivalent to
`Parser().parsestr(s)`. _\_class_ and _policy_ are interpreted as
with the [`Parser`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser "email.parser.Parser") class constructor.

Changed in version 3.3: Removed the _strict_ argument. Added the _policy_ keyword.

email.message\_from\_file( _fp_, _\_class=None_, _\*_, _policy=policy.compat32_) [¶](https://docs.python.org/3/library/email.parser.html#email.message_from_file "Link to this definition")

Return a message object structure tree from an open [file object](https://docs.python.org/3/glossary.html#term-file-object).
This is equivalent to `Parser().parse(fp)`. _\_class_ and _policy_ are
interpreted as with the [`Parser`](https://docs.python.org/3/library/email.parser.html#email.parser.Parser "email.parser.Parser") class constructor.

Changed in version 3.3: Removed the _strict_ argument. Added the _policy_ keyword.

Changed in version 3.6: _\_class_ defaults to the policy `message_factory`.

Here’s an example of how you might use [`message_from_bytes()`](https://docs.python.org/3/library/email.parser.html#email.message_from_bytes "email.message_from_bytes") at an
interactive Python prompt:

Copy

```
>>> import email
>>> msg = email.message_from_bytes(myBytes)
```

## Additional notes [¶](https://docs.python.org/3/library/email.parser.html\#additional-notes "Link to this heading")

Here are some notes on the parsing semantics:

- Most non- _multipart_ type messages are parsed as a single message
object with a string payload. These objects will return `False` for
[`is_multipart()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.is_multipart "email.message.EmailMessage.is_multipart"), and
[`iter_parts()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.iter_parts "email.message.EmailMessage.iter_parts") will yield an empty list.

- All _multipart_ type messages will be parsed as a container message
object with a list of sub-message objects for their payload. The outer
container message will return `True` for
[`is_multipart()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.is_multipart "email.message.EmailMessage.is_multipart"), and
[`iter_parts()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.iter_parts "email.message.EmailMessage.iter_parts") will yield a list of subparts.

- Most messages with a content type of _message/\*_ (such as
_message/delivery-status_ and _message/rfc822_) will also
be parsed as container object containing a list payload of length 1. Their
[`is_multipart()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.is_multipart "email.message.EmailMessage.is_multipart") method will return `True`.
The single element yielded by [`iter_parts()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.iter_parts "email.message.EmailMessage.iter_parts")
will be a sub-message object.

- Some non-standards-compliant messages may not be internally consistent about
their _multipart_-edness. Such messages may have a
_Content-Type_ header of type _multipart_, but their
[`is_multipart()`](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.is_multipart "email.message.EmailMessage.is_multipart") method may return `False`.
If such messages were parsed with the [`FeedParser`](https://docs.python.org/3/library/email.parser.html#email.parser.FeedParser "email.parser.FeedParser"),
they will have an instance of the
[`MultipartInvariantViolationDefect`](https://docs.python.org/3/library/email.errors.html#email.errors.MultipartInvariantViolationDefect "email.errors.MultipartInvariantViolationDefect") class in their
_defects_ attribute list. See [`email.errors`](https://docs.python.org/3/library/email.errors.html#module-email.errors "email.errors: The exception classes used by the email package.") for details.


### [Table of Contents](https://docs.python.org/3/contents.html)

- [`email.parser`: Parsing email messages](https://docs.python.org/3/library/email.parser.html#)
  - [FeedParser API](https://docs.python.org/3/library/email.parser.html#feedparser-api)
  - [Parser API](https://docs.python.org/3/library/email.parser.html#parser-api)
  - [Additional notes](https://docs.python.org/3/library/email.parser.html#additional-notes)

#### Previous topic

[`email.message`: Representing an email message](https://docs.python.org/3/library/email.message.html "previous chapter")

#### Next topic

[`email.generator`: Generating MIME documents](https://docs.python.org/3/library/email.generator.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/email.parser.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/email.generator.html "email.generator: Generating MIME documents") \|
- [previous](https://docs.python.org/3/library/email.message.html "email.message: Representing an email message") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Internet Data Handling](https://docs.python.org/3/library/netdata.html) »
- [`email` — An email and MIME handling package](https://docs.python.org/3/library/email.html) »
- [`email.parser`: Parsing email messages](https://docs.python.org/3/library/email.parser.html)
- \|

- Theme
AutoLightDark \|