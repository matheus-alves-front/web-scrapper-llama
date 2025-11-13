### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/reference/grammar.html "10. Full Grammar specification") \|
- [previous](https://docs.python.org/3/reference/compound_stmts.html "8. Compound statements") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Language Reference](https://docs.python.org/3/reference/index.html) »
- [9\. Top-level components](https://docs.python.org/3/reference/toplevel_components.html)
- \|

- Theme
AutoLightDark \|

# 9\. Top-level components [¶](https://docs.python.org/3/reference/toplevel_components.html\#top-level-components "Link to this heading")

The Python interpreter can get its input from a number of sources: from a script
passed to it as standard input or as program argument, typed in interactively,
from a module source file, etc. This chapter gives the syntax used in these
cases.

## 9.1. Complete Python programs [¶](https://docs.python.org/3/reference/toplevel_components.html\#complete-python-programs "Link to this heading")

While a language specification need not prescribe how the language interpreter
is invoked, it is useful to have a notion of a complete Python program. A
complete Python program is executed in a minimally initialized environment: all
built-in and standard modules are available, but none have been initialized,
except for [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.") (various system services), [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") (built-in
functions, exceptions and `None`) and [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``."). The latter is used to
provide the local and global namespace for execution of the complete program.

The syntax for a complete Python program is that for file input, described in
the next section.

The interpreter may also be invoked in interactive mode; in this case, it does
not read and execute a complete program but reads and executes one statement
(possibly compound) at a time. The initial environment is identical to that of
a complete program; each statement is executed in the namespace of
[`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.").

A complete program can be passed to the interpreter
in three forms: with the [`-c`](https://docs.python.org/3/using/cmdline.html#cmdoption-c) _string_ command line option, as a file
passed as the first command line argument, or as standard input. If the file
or standard input is a tty device, the interpreter enters interactive mode;
otherwise, it executes the file as a complete program.

## 9.2. File input [¶](https://docs.python.org/3/reference/toplevel_components.html\#file-input "Link to this heading")

All input read from non-interactive files has the same form:

```
file_input: (NEWLINE | statement)* ENDMARKER
```

This syntax is used in the following situations:

- when parsing a complete Python program (from a file or from a string);

- when parsing a module;

- when parsing a string passed to the [`exec()`](https://docs.python.org/3/library/functions.html#exec "exec") function;


## 9.3. Interactive input [¶](https://docs.python.org/3/reference/toplevel_components.html\#interactive-input "Link to this heading")

Input in interactive mode is parsed using the following grammar:

```
interactive_input: [stmt_list] NEWLINE | compound_stmt NEWLINE | ENDMARKER
```

Note that a (top-level) compound statement must be followed by a blank line in
interactive mode; this is needed to help the parser detect the end of the input.

## 9.4. Expression input [¶](https://docs.python.org/3/reference/toplevel_components.html\#expression-input "Link to this heading")

[`eval()`](https://docs.python.org/3/library/functions.html#eval "eval") is used for expression input. It ignores leading whitespace. The
string argument to [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval") must have the following form:

```
eval_input: expression_list NEWLINE* ENDMARKER
```

### [Table of Contents](https://docs.python.org/3/contents.html)

- [9\. Top-level components](https://docs.python.org/3/reference/toplevel_components.html#)
  - [9.1. Complete Python programs](https://docs.python.org/3/reference/toplevel_components.html#complete-python-programs)
  - [9.2. File input](https://docs.python.org/3/reference/toplevel_components.html#file-input)
  - [9.3. Interactive input](https://docs.python.org/3/reference/toplevel_components.html#interactive-input)
  - [9.4. Expression input](https://docs.python.org/3/reference/toplevel_components.html#expression-input)

#### Previous topic

[8\. Compound statements](https://docs.python.org/3/reference/compound_stmts.html "previous chapter")

#### Next topic

[10\. Full Grammar specification](https://docs.python.org/3/reference/grammar.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/reference/toplevel_components.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/reference/grammar.html "10. Full Grammar specification") \|
- [previous](https://docs.python.org/3/reference/compound_stmts.html "8. Compound statements") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Language Reference](https://docs.python.org/3/reference/index.html) »
- [9\. Top-level components](https://docs.python.org/3/reference/toplevel_components.html)
- \|

- Theme
AutoLightDark \|