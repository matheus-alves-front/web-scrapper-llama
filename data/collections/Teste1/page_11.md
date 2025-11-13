### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/optparse.html "optparse — Parser for command line options") \|
- [previous](https://docs.python.org/3/howto/argparse.html "Argparse Tutorial") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
- [`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html) »
- [Migrating `optparse` code to `argparse`](https://docs.python.org/3/howto/argparse-optparse.html)
- \|

- Theme
AutoLightDark \|

# Migrating `optparse` code to `argparse` [¶](https://docs.python.org/3/howto/argparse-optparse.html\#migrating-optparse-code-to-argparse "Link to this heading")

The [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.") module offers several higher level features not natively
provided by the [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.") module, including:

- Handling positional arguments.

- Supporting subcommands.

- Allowing alternative option prefixes like `+` and `/`.

- Handling zero-or-more and one-or-more style arguments.

- Producing more informative usage messages.

- Providing a much simpler interface for custom `type` and `action`.


Originally, the [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.") module attempted to maintain compatibility
with [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library."). However, the fundamental design differences between
supporting declarative command line option processing (while leaving positional
argument processing to application code), and supporting both named options
and positional arguments in the declarative interface mean that the
API has diverged from that of `optparse` over time.

As described in [Choosing an argument parsing library](https://docs.python.org/3/library/optparse.html#choosing-an-argument-parser), applications that are
currently using [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.") and are happy with the way it works can
just continue to use `optparse`.

Application developers that are considering migrating should also review
the list of intrinsic behavioural differences described in that section
before deciding whether or not migration is desirable.

For applications that do choose to migrate from [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.") to [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library."),
the following suggestions should be helpful:

- Replace all [`optparse.OptionParser.add_option()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "optparse.OptionParser.add_option") calls with
[`ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") calls.

- Replace `(options, args) = parser.parse_args()` with `args =
parser.parse_args()` and add additional [`ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
calls for the positional arguments. Keep in mind that what was previously
called `options`, now in the [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.") context is called `args`.

- Replace [`optparse.OptionParser.disable_interspersed_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.disable_interspersed_args "optparse.OptionParser.disable_interspersed_args")
by using [`parse_intermixed_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "argparse.ArgumentParser.parse_intermixed_args") instead of
[`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args").

- Replace callback actions and the `callback_*` keyword arguments with
`type` or `action` arguments.

- Replace string names for `type` keyword arguments with the corresponding
type objects (e.g. int, float, complex, etc).

- Replace [`optparse.Values`](https://docs.python.org/3/library/optparse.html#optparse.Values "optparse.Values") with [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace") and
[`optparse.OptionError`](https://docs.python.org/3/library/optparse.html#optparse.OptionError "optparse.OptionError") and [`optparse.OptionValueError`](https://docs.python.org/3/library/optparse.html#optparse.OptionValueError "optparse.OptionValueError") with
[`ArgumentError`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentError "argparse.ArgumentError").

- Replace strings with implicit arguments such as `%default` or `%prog` with
the standard Python syntax to use dictionaries to format strings, that is,
`%(default)s` and `%(prog)s`.

- Replace the OptionParser constructor `version` argument with a call to
`parser.add_argument('--version', action='version', version='<the version>')`.


#### Previous topic

[Argparse Tutorial](https://docs.python.org/3/howto/argparse.html "previous chapter")

#### Next topic

[`optparse` — Parser for command line options](https://docs.python.org/3/library/optparse.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/howto/argparse-optparse.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/optparse.html "optparse — Parser for command line options") \|
- [previous](https://docs.python.org/3/howto/argparse.html "Argparse Tutorial") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Command-line interface libraries](https://docs.python.org/3/library/cmdlinelibs.html) »
- [`argparse` — Parser for command-line options, arguments and subcommands](https://docs.python.org/3/library/argparse.html) »
- [Migrating `optparse` code to `argparse`](https://docs.python.org/3/howto/argparse-optparse.html)
- \|

- Theme
AutoLightDark \|