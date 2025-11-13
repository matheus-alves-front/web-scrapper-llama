### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/xml.sax.handler.html "xml.sax.handler — Base classes for SAX handlers") \|
- [previous](https://docs.python.org/3/library/xml.dom.pulldom.html "xml.dom.pulldom — Support for building partial DOM trees") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
- [`xml.sax` — Support for SAX2 parsers](https://docs.python.org/3/library/xml.sax.html)
- \|

- Theme
AutoLightDark \|

# `xml.sax` — Support for SAX2 parsers [¶](https://docs.python.org/3/library/xml.sax.html\#module-xml.sax "Link to this heading")

**Source code:** [Lib/xml/sax/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.14/Lib/xml/sax/__init__.py)

* * *

The [`xml.sax`](https://docs.python.org/3/library/xml.sax.html#module-xml.sax "xml.sax: Package containing SAX2 base classes and convenience functions.") package provides a number of modules which implement the
Simple API for XML (SAX) interface for Python. The package itself provides the
SAX exceptions and the convenience functions which will be most used by users of
the SAX API.

Note

If you need to parse untrusted or unauthenticated data, see
[XML security](https://docs.python.org/3/library/xml.html#xml-security).

Changed in version 3.7.1: The SAX parser no longer processes general external entities by default
to increase security. Before, the parser created network connections
to fetch remote files or loaded local files from the file
system for DTD and entities. The feature can be enabled again with method
[`setFeature()`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader.setFeature "xml.sax.xmlreader.XMLReader.setFeature") on the parser object
and argument [`feature_external_ges`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.feature_external_ges "xml.sax.handler.feature_external_ges").

The convenience functions are:

xml.sax.make\_parser( _parser\_list=\[\]_) [¶](https://docs.python.org/3/library/xml.sax.html#xml.sax.make_parser "Link to this definition")

Create and return a SAX [`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") object. The
first parser found will
be used. If _parser\_list_ is provided, it must be an iterable of strings which
name modules that have a function named `create_parser()`. Modules listed
in _parser\_list_ will be used before modules in the default list of parsers.

Changed in version 3.8: The _parser\_list_ argument can be any iterable, not just a list.

xml.sax.parse( _filename\_or\_stream_, _handler_, _error\_handler=handler.ErrorHandler()_) [¶](https://docs.python.org/3/library/xml.sax.html#xml.sax.parse "Link to this definition")

Create a SAX parser and use it to parse a document. The document, passed in as
_filename\_or\_stream_, can be a filename or a file object. The _handler_
parameter needs to be a SAX [`ContentHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ContentHandler "xml.sax.handler.ContentHandler") instance. If
_error\_handler_ is given, it must be a SAX [`ErrorHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler "xml.sax.handler.ErrorHandler")
instance; if
omitted, [`SAXParseException`](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXParseException "xml.sax.SAXParseException") will be raised on all errors. There is no
return value; all work must be done by the _handler_ passed in.

xml.sax.parseString( _string_, _handler_, _error\_handler=handler.ErrorHandler()_) [¶](https://docs.python.org/3/library/xml.sax.html#xml.sax.parseString "Link to this definition")

Similar to [`parse()`](https://docs.python.org/3/library/xml.sax.html#xml.sax.parse "xml.sax.parse"), but parses from a buffer _string_ received as a
parameter. _string_ must be a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") instance or a
[bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).

Changed in version 3.5: Added support of [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") instances.

A typical SAX application uses three kinds of objects: readers, handlers and
input sources. “Reader” in this context is another term for parser, i.e. some
piece of code that reads the bytes or characters from the input source, and
produces a sequence of events. The events then get distributed to the handler
objects, i.e. the reader invokes a method on the handler. A SAX application
must therefore obtain a reader object, create or open the input sources, create
the handlers, and connect these objects all together. As the final step of
preparation, the reader is called to parse the input. During parsing, methods on
the handler objects are called based on structural and syntactic events from the
input data.

For these objects, only the interfaces are relevant; they are normally not
instantiated by the application itself. Since Python does not have an explicit
notion of interface, they are formally introduced as classes, but applications
may use implementations which do not inherit from the provided classes. The
[`InputSource`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource"), [`Locator`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.Locator "xml.sax.xmlreader.Locator"),
`Attributes`, `AttributesNS`,
and [`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") interfaces are defined in the
module [`xml.sax.xmlreader`](https://docs.python.org/3/library/xml.sax.reader.html#module-xml.sax.xmlreader "xml.sax.xmlreader: Interface which SAX-compliant XML parsers must implement."). The handler interfaces are defined in
[`xml.sax.handler`](https://docs.python.org/3/library/xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers."). For convenience,
[`InputSource`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.InputSource "xml.sax.xmlreader.InputSource") (which is often
instantiated directly) and the handler classes are also available from
[`xml.sax`](https://docs.python.org/3/library/xml.sax.html#module-xml.sax "xml.sax: Package containing SAX2 base classes and convenience functions."). These interfaces are described below.

In addition to these classes, [`xml.sax`](https://docs.python.org/3/library/xml.sax.html#module-xml.sax "xml.sax: Package containing SAX2 base classes and convenience functions.") provides the following exception
classes.

_exception_ xml.sax.SAXException( _msg_, _exception=None_) [¶](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXException "Link to this definition")

Encapsulate an XML error or warning. This class can contain basic error or
warning information from either the XML parser or the application: it can be
subclassed to provide additional functionality or to add localization. Note
that although the handlers defined in the
[`ErrorHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler "xml.sax.handler.ErrorHandler") interface
receive instances of this exception, it is not required to actually raise the
exception — it is also useful as a container for information.

When instantiated, _msg_ should be a human-readable description of the error.
The optional _exception_ parameter, if given, should be `None` or an exception
that was caught by the parsing code and is being passed along as information.

This is the base class for the other SAX exception classes.

_exception_ xml.sax.SAXParseException( _msg_, _exception_, _locator_) [¶](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXParseException "Link to this definition")

Subclass of [`SAXException`](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXException "xml.sax.SAXException") raised on parse errors. Instances of this
class are passed to the methods of the SAX
[`ErrorHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.ErrorHandler "xml.sax.handler.ErrorHandler") interface to provide information
about the parse error. This class supports the SAX
[`Locator`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.Locator "xml.sax.xmlreader.Locator") interface as well as the
[`SAXException`](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXException "xml.sax.SAXException") interface.

_exception_ xml.sax.SAXNotRecognizedException( _msg_, _exception=None_) [¶](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXNotRecognizedException "Link to this definition")

Subclass of [`SAXException`](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXException "xml.sax.SAXException") raised when a SAX
[`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") is
confronted with an unrecognized feature or property. SAX applications and
extensions may use this class for similar purposes.

_exception_ xml.sax.SAXNotSupportedException( _msg_, _exception=None_) [¶](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXNotSupportedException "Link to this definition")

Subclass of [`SAXException`](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXException "xml.sax.SAXException") raised when a SAX
[`XMLReader`](https://docs.python.org/3/library/xml.sax.reader.html#xml.sax.xmlreader.XMLReader "xml.sax.xmlreader.XMLReader") is asked to
enable a feature that is not supported, or to set a property to a value that the
implementation does not support. SAX applications and extensions may use this
class for similar purposes.

See also

[SAX: The Simple API for XML](http://www.saxproject.org/)

This site is the focal point for the definition of the SAX API. It provides a
Java implementation and online documentation. Links to implementations and
historical information are also available.

Module [`xml.sax.handler`](https://docs.python.org/3/library/xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers.")

Definitions of the interfaces for application-provided objects.

Module [`xml.sax.saxutils`](https://docs.python.org/3/library/xml.sax.utils.html#module-xml.sax.saxutils "xml.sax.saxutils: Convenience functions and classes for use with SAX.")

Convenience functions for use in SAX applications.

Module [`xml.sax.xmlreader`](https://docs.python.org/3/library/xml.sax.reader.html#module-xml.sax.xmlreader "xml.sax.xmlreader: Interface which SAX-compliant XML parsers must implement.")

Definitions of the interfaces for parser-provided objects.

## SAXException Objects [¶](https://docs.python.org/3/library/xml.sax.html\#saxexception-objects "Link to this heading")

The [`SAXException`](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXException "xml.sax.SAXException") exception class supports the following methods:

SAXException.getMessage() [¶](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXException.getMessage "Link to this definition")

Return a human-readable message describing the error condition.

SAXException.getException() [¶](https://docs.python.org/3/library/xml.sax.html#xml.sax.SAXException.getException "Link to this definition")

Return an encapsulated exception object, or `None`.

### [Table of Contents](https://docs.python.org/3/contents.html)

- [`xml.sax` — Support for SAX2 parsers](https://docs.python.org/3/library/xml.sax.html#)
  - [SAXException Objects](https://docs.python.org/3/library/xml.sax.html#saxexception-objects)

#### Previous topic

[`xml.dom.pulldom` — Support for building partial DOM trees](https://docs.python.org/3/library/xml.dom.pulldom.html "previous chapter")

#### Next topic

[`xml.sax.handler` — Base classes for SAX handlers](https://docs.python.org/3/library/xml.sax.handler.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/xml.sax.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/xml.sax.handler.html "xml.sax.handler — Base classes for SAX handlers") \|
- [previous](https://docs.python.org/3/library/xml.dom.pulldom.html "xml.dom.pulldom — Support for building partial DOM trees") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Structured Markup Processing Tools](https://docs.python.org/3/library/markup.html) »
- [`xml.sax` — Support for SAX2 parsers](https://docs.python.org/3/library/xml.sax.html)
- \|

- Theme
AutoLightDark \|