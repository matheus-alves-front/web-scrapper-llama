### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/wsgiref.html "wsgiref — WSGI Utilities and Reference Implementation") \|
- [previous](https://docs.python.org/3/library/internet.html "Internet Protocols and Support") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
- [`webbrowser` — Convenient web-browser controller](https://docs.python.org/3/library/webbrowser.html)
- \|

- Theme
AutoLightDark \|

# `webbrowser` — Convenient web-browser controller [¶](https://docs.python.org/3/library/webbrowser.html\#module-webbrowser "Link to this heading")

**Source code:** [Lib/webbrowser.py](https://github.com/python/cpython/tree/3.14/Lib/webbrowser.py)

* * *

The [`webbrowser`](https://docs.python.org/3/library/webbrowser.html#module-webbrowser "webbrowser: Easy-to-use controller for web browsers.") module provides a high-level interface to allow displaying
web-based documents to users. Under most circumstances, simply calling the
[`open()`](https://docs.python.org/3/library/webbrowser.html#webbrowser.open "webbrowser.open") function from this module will do the right thing.

Under Unix, graphical browsers are preferred under X11, but text-mode browsers
will be used if graphical browsers are not available or an X11 display isn’t
available. If text-mode browsers are used, the calling process will block until
the user exits the browser.

If the environment variable `BROWSER` exists, it is interpreted as the
[`os.pathsep`](https://docs.python.org/3/library/os.html#os.pathsep "os.pathsep")-separated list of browsers to try ahead of the platform
defaults. When the value of a list part contains the string `%s`, then it is
interpreted as a literal browser command line to be used with the argument URL
substituted for `%s`; if the value is a single word that refers to one of the
already registered browsers this browser is added to the front of the search list;
if the part does not contain `%s`, it is simply interpreted as the name of the
browser to launch. [\[1\]](https://docs.python.org/3/library/webbrowser.html#id2)

Changed in version 3.14: The `BROWSER` variable can now also be used to reorder the list of
platform defaults. This is particularly useful on macOS where the platform
defaults do not refer to command-line tools on `PATH`.

For non-Unix platforms, or when a remote browser is available on Unix, the
controlling process will not wait for the user to finish with the browser, but
allow the remote browser to maintain its own windows on the display. If remote
browsers are not available on Unix, the controlling process will launch a new
browser and wait.

On iOS, the `BROWSER` environment variable, as well as any arguments
controlling autoraise, browser preference, and new tab/window creation will be
ignored. Web pages will _always_ be opened in the user’s preferred browser, in
a new tab, with the browser being brought to the foreground. The use of the
[`webbrowser`](https://docs.python.org/3/library/webbrowser.html#module-webbrowser "webbrowser: Easy-to-use controller for web browsers.") module on iOS requires the [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.") module. If
[`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "ctypes: A foreign function library for Python.") isn’t available, calls to [`open()`](https://docs.python.org/3/library/webbrowser.html#webbrowser.open "webbrowser.open") will fail.

The script **webbrowser** can be used as a command-line interface for the
module. It accepts a URL as the argument. It accepts the following optional
parameters:

-n,--new-window [¶](https://docs.python.org/3/library/webbrowser.html#cmdoption-webbrowser-n "Link to this definition")

Opens the URL in a new browser window, if possible.

-t,--new-tab [¶](https://docs.python.org/3/library/webbrowser.html#cmdoption-webbrowser-t "Link to this definition")

Opens the URL in a new browser tab.

The options are, naturally, mutually exclusive. Usage example:

```
python -m webbrowser -t "https://www.python.org"
```

[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI, not Android.

The following exception is defined:

_exception_ webbrowser.Error [¶](https://docs.python.org/3/library/webbrowser.html#webbrowser.Error "Link to this definition")

Exception raised when a browser control error occurs.

The following functions are defined:

webbrowser.open( _url_, _new=0_, _autoraise=True_) [¶](https://docs.python.org/3/library/webbrowser.html#webbrowser.open "Link to this definition")

Display _url_ using the default browser. If _new_ is 0, the _url_ is opened
in the same browser window if possible. If _new_ is 1, a new browser window
is opened if possible. If _new_ is 2, a new browser page (“tab”) is opened
if possible. If _autoraise_ is `True`, the window is raised if possible
(note that under many window managers this will occur regardless of the
setting of this variable).

Returns `True` if a browser was successfully launched, `False` otherwise.

Note that on some platforms, trying to open a filename using this function,
may work and start the operating system’s associated program. However, this
is neither supported nor portable.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)`webbrowser.open` with argument `url`.

webbrowser.open\_new( _url_) [¶](https://docs.python.org/3/library/webbrowser.html#webbrowser.open_new "Link to this definition")

Open _url_ in a new window of the default browser, if possible, otherwise, open
_url_ in the only browser window.

Returns `True` if a browser was successfully launched, `False` otherwise.

webbrowser.open\_new\_tab( _url_) [¶](https://docs.python.org/3/library/webbrowser.html#webbrowser.open_new_tab "Link to this definition")

Open _url_ in a new page (“tab”) of the default browser, if possible, otherwise
equivalent to [`open_new()`](https://docs.python.org/3/library/webbrowser.html#webbrowser.open_new "webbrowser.open_new").

Returns `True` if a browser was successfully launched, `False` otherwise.

webbrowser.get( _using=None_) [¶](https://docs.python.org/3/library/webbrowser.html#webbrowser.get "Link to this definition")

Return a controller object for the browser type _using_. If _using_ is
`None`, return a controller for a default browser appropriate to the
caller’s environment.

webbrowser.register( _name_, _constructor_, _instance=None_, _\*_, _preferred=False_) [¶](https://docs.python.org/3/library/webbrowser.html#webbrowser.register "Link to this definition")

Register the browser type _name_. Once a browser type is registered, the
[`get()`](https://docs.python.org/3/library/webbrowser.html#webbrowser.get "webbrowser.get") function can return a controller for that browser type. If
_instance_ is not provided, or is `None`, _constructor_ will be called without
parameters to create an instance when needed. If _instance_ is provided,
_constructor_ will never be called, and may be `None`.

Setting _preferred_ to `True` makes this browser a preferred result for
a [`get()`](https://docs.python.org/3/library/webbrowser.html#webbrowser.get "webbrowser.get") call with no argument. Otherwise, this entry point is only
useful if you plan to either set the `BROWSER` variable or call
[`get()`](https://docs.python.org/3/library/webbrowser.html#webbrowser.get "webbrowser.get") with a nonempty argument matching the name of a handler you
declare.

Changed in version 3.7: _preferred_ keyword-only parameter was added.

A number of browser types are predefined. This table gives the type names that
may be passed to the [`get()`](https://docs.python.org/3/library/webbrowser.html#webbrowser.get "webbrowser.get") function and the corresponding instantiations
for the controller classes, all defined in this module.

| Type Name | Class Name | Notes |
| --- | --- | --- |
| `'mozilla'` | `Mozilla('mozilla')` |  |
| `'firefox'` | `Mozilla('mozilla')` |  |
| `'epiphany'` | `Epiphany('epiphany')` |  |
| `'kfmclient'` | `Konqueror()` | (1) |
| `'konqueror'` | `Konqueror()` | (1) |
| `'kfm'` | `Konqueror()` | (1) |
| `'opera'` | `Opera()` |  |
| `'links'` | `GenericBrowser('links')` |  |
| `'elinks'` | `Elinks('elinks')` |  |
| `'lynx'` | `GenericBrowser('lynx')` |  |
| `'w3m'` | `GenericBrowser('w3m')` |  |
| `'windows-default'` | `WindowsDefault` | (2) |
| `'macosx'` | `MacOSXOSAScript('default')` | (3) |
| `'safari'` | `MacOSXOSAScript('safari')` | (3) |
| `'google-chrome'` | `Chrome('google-chrome')` |  |
| `'chrome'` | `Chrome('chrome')` |  |
| `'chromium'` | `Chromium('chromium')` |  |
| `'chromium-browser'` | `Chromium('chromium-browser')` |  |
| `'iosbrowser'` | `IOSBrowser` | (4) |

Notes:

1. “Konqueror” is the file manager for the KDE desktop environment for Unix, and
only makes sense to use if KDE is running. Some way of reliably detecting KDE
would be nice; the `KDEDIR` variable is not sufficient. Note also that
the name “kfm” is used even when using the **konqueror** command with KDE
2 — the implementation selects the best strategy for running Konqueror.

2. Only on Windows platforms.

3. Only on macOS.

4. Only on iOS.


Added in version 3.2: A new `MacOSXOSAScript` class has been added
and is used on Mac instead of the previous `MacOSX` class.
This adds support for opening browsers not currently set as the OS default.

Added in version 3.3: Support for Chrome/Chromium has been added.

Changed in version 3.12: Support for several obsolete browsers has been removed.
Removed browsers include Grail, Mosaic, Netscape, Galeon,
Skipstone, Iceape, and Firefox versions 35 and below.

Changed in version 3.13: Support for iOS has been added.

Here are some simple examples:

Copy

```
url = 'https://docs.python.org/'

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url)

# Open URL in new window, raising the window if possible.
webbrowser.open_new(url)
```

## Browser Controller Objects [¶](https://docs.python.org/3/library/webbrowser.html\#browser-controller-objects "Link to this heading")

Browser controllers provide the [`name`](https://docs.python.org/3/library/webbrowser.html#webbrowser.controller.name "webbrowser.controller.name") attribute,
and the following three methods which parallel module-level convenience functions:

controller.name [¶](https://docs.python.org/3/library/webbrowser.html#webbrowser.controller.name "Link to this definition")

System-dependent name for the browser.

controller.open( _url_, _new=0_, _autoraise=True_) [¶](https://docs.python.org/3/library/webbrowser.html#webbrowser.controller.open "Link to this definition")

Display _url_ using the browser handled by this controller. If _new_ is 1, a new
browser window is opened if possible. If _new_ is 2, a new browser page (“tab”)
is opened if possible.

controller.open\_new( _url_) [¶](https://docs.python.org/3/library/webbrowser.html#webbrowser.controller.open_new "Link to this definition")

Open _url_ in a new window of the browser handled by this controller, if
possible, otherwise, open _url_ in the only browser window. Alias
[`open_new()`](https://docs.python.org/3/library/webbrowser.html#webbrowser.open_new "webbrowser.open_new").

controller.open\_new\_tab( _url_) [¶](https://docs.python.org/3/library/webbrowser.html#webbrowser.controller.open_new_tab "Link to this definition")

Open _url_ in a new page (“tab”) of the browser handled by this controller, if
possible, otherwise equivalent to [`open_new()`](https://docs.python.org/3/library/webbrowser.html#webbrowser.open_new "webbrowser.open_new").

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

- [`webbrowser` — Convenient web-browser controller](https://docs.python.org/3/library/webbrowser.html#)
  - [Browser Controller Objects](https://docs.python.org/3/library/webbrowser.html#browser-controller-objects)

#### Previous topic

[Internet Protocols and Support](https://docs.python.org/3/library/internet.html "previous chapter")

#### Next topic

[`wsgiref` — WSGI Utilities and Reference Implementation](https://docs.python.org/3/library/wsgiref.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/webbrowser.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/wsgiref.html "wsgiref — WSGI Utilities and Reference Implementation") \|
- [previous](https://docs.python.org/3/library/internet.html "Internet Protocols and Support") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Internet Protocols and Support](https://docs.python.org/3/library/internet.html) »
- [`webbrowser` — Convenient web-browser controller](https://docs.python.org/3/library/webbrowser.html)
- \|

- Theme
AutoLightDark \|