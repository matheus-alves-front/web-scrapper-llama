### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/whatsnew/3.9.html "What’s New In Python 3.9") \|
- [previous](https://docs.python.org/3/whatsnew/3.11.html "What’s New In Python 3.11") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [What’s New in Python](https://docs.python.org/3/whatsnew/index.html) »
- [What’s New In Python 3.10](https://docs.python.org/3/whatsnew/3.10.html)
- \|

- Theme
AutoLightDark \|

# What’s New In Python 3.10 [¶](https://docs.python.org/3/whatsnew/3.10.html\#what-s-new-in-python-3-10 "Link to this heading")

Editor:

Pablo Galindo Salgado

This article explains the new features in Python 3.10, compared to 3.9.
Python 3.10 was released on October 4, 2021.
For full details, see the [changelog](https://docs.python.org/3/whatsnew/changelog.html#changelog).

## Summary – Release highlights [¶](https://docs.python.org/3/whatsnew/3.10.html\#summary-release-highlights "Link to this heading")

New syntax features:

- [**PEP 634**](https://peps.python.org/pep-0634/), Structural Pattern Matching: Specification

- [**PEP 635**](https://peps.python.org/pep-0635/), Structural Pattern Matching: Motivation and Rationale

- [**PEP 636**](https://peps.python.org/pep-0636/), Structural Pattern Matching: Tutorial

- [bpo-12782](https://bugs.python.org/issue?@action=redirect&bpo=12782), Parenthesized context managers are now officially allowed.


New features in the standard library:

- [**PEP 618**](https://peps.python.org/pep-0618/), Add Optional Length-Checking To zip.


Interpreter improvements:

- [**PEP 626**](https://peps.python.org/pep-0626/), Precise line numbers for debugging and other tools.


New typing features:

- [**PEP 604**](https://peps.python.org/pep-0604/), Allow writing union types as X \| Y

- [**PEP 612**](https://peps.python.org/pep-0612/), Parameter Specification Variables

- [**PEP 613**](https://peps.python.org/pep-0613/), Explicit Type Aliases

- [**PEP 647**](https://peps.python.org/pep-0647/), User-Defined Type Guards


Important deprecations, removals or restrictions:

- [**PEP 644**](https://peps.python.org/pep-0644/), Require OpenSSL 1.1.1 or newer

- [**PEP 632**](https://peps.python.org/pep-0632/), Deprecate distutils module.

- [**PEP 623**](https://peps.python.org/pep-0623/), Deprecate and prepare for the removal of the wstr member in PyUnicodeObject.

- [**PEP 624**](https://peps.python.org/pep-0624/), Remove Py\_UNICODE encoder APIs

- [**PEP 597**](https://peps.python.org/pep-0597/), Add optional EncodingWarning


## New Features [¶](https://docs.python.org/3/whatsnew/3.10.html\#new-features "Link to this heading")

### Parenthesized context managers [¶](https://docs.python.org/3/whatsnew/3.10.html\#parenthesized-context-managers "Link to this heading")

Using enclosing parentheses for continuation across multiple lines
in context managers is now supported. This allows formatting a long
collection of context managers in multiple lines in a similar way
as it was previously possible with import statements. For instance,
all these examples are now valid:

Copy

```
with (CtxManager() as example):
    ...

with (
    CtxManager1(),
    CtxManager2()
):
    ...

with (CtxManager1() as example,
      CtxManager2()):
    ...

with (CtxManager1(),
      CtxManager2() as example):
    ...

with (
    CtxManager1() as example1,
    CtxManager2() as example2
):
    ...
```

it is also possible to use a trailing comma at the end of the
enclosed group:

Copy

```
with (
    CtxManager1() as example1,
    CtxManager2() as example2,
    CtxManager3() as example3,
):
    ...
```

This new syntax uses the non LL(1) capacities of the new parser.
Check [**PEP 617**](https://peps.python.org/pep-0617/) for more details.

(Contributed by Guido van Rossum, Pablo Galindo and Lysandros Nikolaou
in [bpo-12782](https://bugs.python.org/issue?@action=redirect&bpo=12782) and [bpo-40334](https://bugs.python.org/issue?@action=redirect&bpo=40334).)

### Better error messages [¶](https://docs.python.org/3/whatsnew/3.10.html\#better-error-messages "Link to this heading")

#### SyntaxErrors [¶](https://docs.python.org/3/whatsnew/3.10.html\#syntaxerrors "Link to this heading")

When parsing code that contains unclosed parentheses or brackets the interpreter
now includes the location of the unclosed bracket of parentheses instead of displaying
_SyntaxError: unexpected EOF while parsing_ or pointing to some incorrect location.
For instance, consider the following code (notice the unclosed ‘{‘):

Copy

```
expected = {9: 1, 18: 2, 19: 2, 27: 3, 28: 3, 29: 3, 36: 4, 37: 4,
            38: 4, 39: 4, 45: 5, 46: 5, 47: 5, 48: 5, 49: 5, 54: 6,
some_other_code = foo()
```

Previous versions of the interpreter reported confusing places as the location of
the syntax error:

Copy

```
File "example.py", line 3
    some_other_code = foo()
                    ^
SyntaxError: invalid syntax
```

but in Python 3.10 a more informative error is emitted:

Copy

```
File "example.py", line 1
    expected = {9: 1, 18: 2, 19: 2, 27: 3, 28: 3, 29: 3, 36: 4, 37: 4,
               ^
SyntaxError: '{' was never closed
```

In a similar way, errors involving unclosed string literals (single and triple
quoted) now point to the start of the string instead of reporting EOF/EOL.

These improvements are inspired by previous work in the PyPy interpreter.

(Contributed by Pablo Galindo in [bpo-42864](https://bugs.python.org/issue?@action=redirect&bpo=42864) and Batuhan Taskaya in
[bpo-40176](https://bugs.python.org/issue?@action=redirect&bpo=40176).)

[`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") exceptions raised by the interpreter will now highlight the
full error range of the expression that constitutes the syntax error itself,
instead of just where the problem is detected. In this way, instead of displaying
(before Python 3.10):

Copy

```
>>> foo(x, z for z in range(10), t, w)
  File "<stdin>", line 1
    foo(x, z for z in range(10), t, w)
           ^
SyntaxError: Generator expression must be parenthesized
```

now Python 3.10 will display the exception as:

Copy

```
>>> foo(x, z for z in range(10), t, w)
  File "<stdin>", line 1
    foo(x, z for z in range(10), t, w)
           ^^^^^^^^^^^^^^^^^^^^
SyntaxError: Generator expression must be parenthesized
```

This improvement was contributed by Pablo Galindo in [bpo-43914](https://bugs.python.org/issue?@action=redirect&bpo=43914).

A considerable amount of new specialized messages for [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") exceptions
have been incorporated. Some of the most notable ones are as follows:

- Missing `:` before blocks:



Copy

```
>>> if rocket.position > event_horizon
    File "<stdin>", line 1
      if rocket.position > event_horizon
                                        ^
SyntaxError: expected ':'
```





(Contributed by Pablo Galindo in [bpo-42997](https://bugs.python.org/issue?@action=redirect&bpo=42997).)

- Unparenthesised tuples in comprehensions targets:



Copy

```
>>> {x,y for x,y in zip('abcd', '1234')}
    File "<stdin>", line 1
      {x,y for x,y in zip('abcd', '1234')}
       ^
SyntaxError: did you forget parentheses around the comprehension target?
```





(Contributed by Pablo Galindo in [bpo-43017](https://bugs.python.org/issue?@action=redirect&bpo=43017).)

- Missing commas in collection literals and between expressions:



Copy

```
>>> items = {
... x: 1,
... y: 2
... z: 3,
    File "<stdin>", line 3
      y: 2
         ^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
```





(Contributed by Pablo Galindo in [bpo-43822](https://bugs.python.org/issue?@action=redirect&bpo=43822).)

- Multiple Exception types without parentheses:



Copy

```
>>> try:
...     build_dyson_sphere()
... except NotEnoughScienceError, NotEnoughResourcesError:
    File "<stdin>", line 3
      except NotEnoughScienceError, NotEnoughResourcesError:
             ^
SyntaxError: multiple exception types must be parenthesized
```





(Contributed by Pablo Galindo in [bpo-43149](https://bugs.python.org/issue?@action=redirect&bpo=43149).)

- Missing `:` and values in dictionary literals:



Copy

```
>>> values = {
... x: 1,
... y: 2,
... z:
... }
    File "<stdin>", line 4
      z:
       ^
SyntaxError: expression expected after dictionary key and ':'

>>> values = {x:1, y:2, z w:3}
    File "<stdin>", line 1
      values = {x:1, y:2, z w:3}
                          ^
SyntaxError: ':' expected after dictionary key
```





(Contributed by Pablo Galindo in [bpo-43823](https://bugs.python.org/issue?@action=redirect&bpo=43823).)

- `try` blocks without `except` or `finally` blocks:



Copy

```
>>> try:
...     x = 2
... something = 3
    File "<stdin>", line 3
      something  = 3
      ^^^^^^^^^
SyntaxError: expected 'except' or 'finally' block
```





(Contributed by Pablo Galindo in [bpo-44305](https://bugs.python.org/issue?@action=redirect&bpo=44305).)

- Usage of `=` instead of `==` in comparisons:



Copy

```
>>> if rocket.position = event_horizon:
    File "<stdin>", line 1
      if rocket.position = event_horizon:
                         ^
SyntaxError: cannot assign to attribute here. Maybe you meant '==' instead of '='?
```





(Contributed by Pablo Galindo in [bpo-43797](https://bugs.python.org/issue?@action=redirect&bpo=43797).)

- Usage of `*` in f-strings:



Copy

```
>>> f"Black holes {*all_black_holes} and revelations"
    File "<stdin>", line 1
      (*all_black_holes)
       ^
SyntaxError: f-string: cannot use starred expression here
```





(Contributed by Pablo Galindo in [bpo-41064](https://bugs.python.org/issue?@action=redirect&bpo=41064).)


#### IndentationErrors [¶](https://docs.python.org/3/whatsnew/3.10.html\#indentationerrors "Link to this heading")

Many [`IndentationError`](https://docs.python.org/3/library/exceptions.html#IndentationError "IndentationError") exceptions now have more context regarding what kind of block
was expecting an indentation, including the location of the statement:

Copy

```
>>> def foo():
...    if lel:
...    x = 2
  File "<stdin>", line 3
    x = 2
    ^
IndentationError: expected an indented block after 'if' statement in line 2
```

#### AttributeErrors [¶](https://docs.python.org/3/whatsnew/3.10.html\#attributeerrors "Link to this heading")

When printing [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError"), `PyErr_Display()` will offer
suggestions of similar attribute names in the object that the exception was
raised from:

Copy

```
>>> collections.namedtoplo
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'collections' has no attribute 'namedtoplo'. Did you mean: namedtuple?
```

(Contributed by Pablo Galindo in [bpo-38530](https://bugs.python.org/issue?@action=redirect&bpo=38530).)

Warning

Notice this won’t work if `PyErr_Display()` is not called to display the error
which can happen if some other custom error display function is used. This is a common
scenario in some REPLs like IPython.

#### NameErrors [¶](https://docs.python.org/3/whatsnew/3.10.html\#nameerrors "Link to this heading")

When printing [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError "NameError") raised by the interpreter, `PyErr_Display()`
will offer suggestions of similar variable names in the function that the exception
was raised from:

Copy

```
>>> schwarzschild_black_hole = None
>>> schwarschild_black_hole
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'schwarschild_black_hole' is not defined. Did you mean: schwarzschild_black_hole?
```

(Contributed by Pablo Galindo in [bpo-38530](https://bugs.python.org/issue?@action=redirect&bpo=38530).)

Warning

Notice this won’t work if `PyErr_Display()` is not called to display the error,
which can happen if some other custom error display function is used. This is a common
scenario in some REPLs like IPython.

### PEP 626: Precise line numbers for debugging and other tools [¶](https://docs.python.org/3/whatsnew/3.10.html\#pep-626-precise-line-numbers-for-debugging-and-other-tools "Link to this heading")

PEP 626 brings more precise and reliable line numbers for debugging, profiling and coverage tools.
Tracing events, with the correct line number, are generated for all lines of code executed and only for lines of code that are executed.

The [`f_lineno`](https://docs.python.org/3/reference/datamodel.html#frame.f_lineno "frame.f_lineno") attribute of frame objects will always contain the
expected line number.

The [`co_lnotab`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_lnotab "codeobject.co_lnotab") attribute of
[code objects](https://docs.python.org/3/reference/datamodel.html#code-objects) is deprecated and
will be removed in 3.12.
Code that needs to convert from offset to line number should use the new
[`co_lines()`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_lines "codeobject.co_lines") method instead.

### PEP 634: Structural Pattern Matching [¶](https://docs.python.org/3/whatsnew/3.10.html\#pep-634-structural-pattern-matching "Link to this heading")

Structural pattern matching has been added in the form of a _match statement_
and _case statements_ of patterns with associated actions. Patterns
consist of sequences, mappings, primitive data types as well as class instances.
Pattern matching enables programs to extract information from complex data types,
branch on the structure of data, and apply specific actions based on different
forms of data.

#### Syntax and operations [¶](https://docs.python.org/3/whatsnew/3.10.html\#syntax-and-operations "Link to this heading")

The generic syntax of pattern matching is:

Copy

```
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
```

A match statement takes an expression and compares its value to successive
patterns given as one or more case blocks. Specifically, pattern matching
operates by:

1. using data with type and shape (the `subject`)

2. evaluating the `subject` in the `match` statement

3. comparing the subject with each pattern in a `case` statement
from top to bottom until a match is confirmed.

4. executing the action associated with the pattern of the confirmed
match

5. If an exact match is not confirmed, the last case, a wildcard `_`,
if provided, will be used as the matching case. If an exact match is
not confirmed and a wildcard case does not exist, the entire match
block is a no-op.


#### Declarative approach [¶](https://docs.python.org/3/whatsnew/3.10.html\#declarative-approach "Link to this heading")

Readers may be aware of pattern matching through the simple example of matching
a subject (data object) to a literal (pattern) with the switch statement found
in C, Java or JavaScript (and many other languages). Often the switch statement
is used for comparison of an object/expression with case statements containing
literals.

More powerful examples of pattern matching can be found in languages such as
Scala and Elixir. With structural pattern matching, the approach is “declarative” and
explicitly states the conditions (the patterns) for data to match.

While an “imperative” series of instructions using nested “if” statements
could be used to accomplish something similar to structural pattern matching,
it is less clear than the “declarative” approach. Instead the “declarative”
approach states the conditions to meet for a match and is more readable through
its explicit patterns. While structural pattern matching can be used in its
simplest form comparing a variable to a literal in a case statement, its
true value for Python lies in its handling of the subject’s type and shape.

#### Simple pattern: match to a literal [¶](https://docs.python.org/3/whatsnew/3.10.html\#simple-pattern-match-to-a-literal "Link to this heading")

Let’s look at this example as pattern matching in its simplest form: a value,
the subject, being matched to several literals, the patterns. In the example
below, `status` is the subject of the match statement. The patterns are
each of the case statements, where literals represent request status codes.
The associated action to the case is executed after a match:

Copy

```
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

If the above function is passed a `status` of 418, “I’m a teapot” is returned.
If the above function is passed a `status` of 500, the case statement with
`_` will match as a wildcard, and “Something’s wrong with the internet” is
returned.
Note the last block: the variable name, `_`, acts as a _wildcard_ and insures
the subject will always match. The use of `_` is optional.

You can combine several literals in a single pattern using `|` (“or”):

Copy

```
case 401 | 403 | 404:
    return "Not allowed"
```

##### Behavior without the wildcard [¶](https://docs.python.org/3/whatsnew/3.10.html\#behavior-without-the-wildcard "Link to this heading")

If we modify the above example by removing the last case block, the example
becomes:

Copy

```
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
```

Without the use of `_` in a case statement, a match may not exist. If no
match exists, the behavior is a no-op. For example, if `status` of 500 is
passed, a no-op occurs.

#### Patterns with a literal and variable [¶](https://docs.python.org/3/whatsnew/3.10.html\#patterns-with-a-literal-and-variable "Link to this heading")

Patterns can look like unpacking assignments, and a pattern may be used to bind
variables. In this example, a data point can be unpacked to its x-coordinate
and y-coordinate:

Copy

```
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

The first pattern has two literals, `(0, 0)`, and may be thought of as an
extension of the literal pattern shown above. The next two patterns combine a
literal and a variable, and the variable _binds_ a value from the subject
(`point`). The fourth pattern captures two values, which makes it
conceptually similar to the unpacking assignment `(x, y) = point`.

#### Patterns and classes [¶](https://docs.python.org/3/whatsnew/3.10.html\#patterns-and-classes "Link to this heading")

If you are using classes to structure your data, you can use as a pattern
the class name followed by an argument list resembling a constructor. This
pattern has the ability to capture instance attributes into variables:

Copy

```
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def location(point):
    match point:
        case Point(x=0, y=0):
            print("Origin is the point's location.")
        case Point(x=0, y=y):
            print(f"Y={y} and the point is on the y-axis.")
        case Point(x=x, y=0):
            print(f"X={x} and the point is on the x-axis.")
        case Point():
            print("The point is located somewhere else on the plane.")
        case _:
            print("Not a point")
```

##### Patterns with positional parameters [¶](https://docs.python.org/3/whatsnew/3.10.html\#patterns-with-positional-parameters "Link to this heading")

You can use positional parameters with some builtin classes that provide an
ordering for their attributes (e.g. dataclasses). You can also define a specific
position for attributes in patterns by setting the `__match_args__` special
attribute in your classes. If it’s set to (“x”, “y”), the following patterns
are all equivalent (and all bind the `y` attribute to the `var` variable):

Copy

```
Point(1, var)
Point(1, y=var)
Point(x=1, y=var)
Point(y=var, x=1)
```

#### Nested patterns [¶](https://docs.python.org/3/whatsnew/3.10.html\#nested-patterns "Link to this heading")

Patterns can be arbitrarily nested. For example, if our data is a short
list of points, it could be matched like this:

Copy

```
match points:
    case []:
        print("No points in the list.")
    case [Point(0, 0)]:
        print("The origin is the only point in the list.")
    case [Point(x, y)]:
        print(f"A single point {x}, {y} is in the list.")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two points on the Y axis at {y1}, {y2} are in the list.")
    case _:
        print("Something else is found in the list.")
```

#### Complex patterns and the wildcard [¶](https://docs.python.org/3/whatsnew/3.10.html\#complex-patterns-and-the-wildcard "Link to this heading")

To this point, the examples have used `_` alone in the last case statement.
A wildcard can be used in more complex patterns, such as `('error', code, _)`.
For example:

Copy

```
match test_variable:
    case ('warning', code, 40):
        print("A warning has been received.")
    case ('error', code, _):
        print(f"An error {code} occurred.")
```

In the above case, `test_variable` will match for (‘error’, code, 100) and
(‘error’, code, 800).

#### Guard [¶](https://docs.python.org/3/whatsnew/3.10.html\#guard "Link to this heading")

We can add an `if` clause to a pattern, known as a “guard”. If the
guard is false, `match` goes on to try the next case block. Note
that value capture happens before the guard is evaluated:

Copy

```
match point:
    case Point(x, y) if x == y:
        print(f"The point is located on the diagonal Y=X at {x}.")
    case Point(x, y):
        print(f"Point is not on the diagonal.")
```

#### Other Key Features [¶](https://docs.python.org/3/whatsnew/3.10.html\#other-key-features "Link to this heading")

Several other key features:

- Like unpacking assignments, tuple and list patterns have exactly the
same meaning and actually match arbitrary sequences. Technically,
the subject must be a sequence.
Therefore, an important exception is that patterns don’t match iterators.
Also, to prevent a common mistake, sequence patterns don’t match strings.

- Sequence patterns support wildcards: `[x, y, *rest]` and `(x, y,
*rest)` work similar to wildcards in unpacking assignments. The
name after `*` may also be `_`, so `(x, y, *_)` matches a sequence
of at least two items without binding the remaining items.

- Mapping patterns: `{"bandwidth": b, "latency": l}` captures the
`"bandwidth"` and `"latency"` values from a dict. Unlike sequence
patterns, extra keys are ignored. A wildcard `**rest` is also
supported. (But `**_` would be redundant, so is not allowed.)

- Subpatterns may be captured using the `as` keyword:



Copy

```
case (Point(x1, y1), Point(x2, y2) as p2): ...
```





This binds x1, y1, x2, y2 like you would expect without the `as` clause,
and p2 to the entire second item of the subject.

- Most literals are compared by equality. However, the singletons `True`,
`False` and `None` are compared by identity.

- Named constants may be used in patterns. These named constants must be
dotted names to prevent the constant from being interpreted as a capture
variable:



Copy

```
from enum import Enum
class Color(Enum):
      RED = 0
      GREEN = 1
      BLUE = 2

color = Color.GREEN
match color:
      case Color.RED:
          print("I see red!")
      case Color.GREEN:
          print("Grass is green")
      case Color.BLUE:
          print("I'm feeling the blues :(")
```


For the full specification see [**PEP 634**](https://peps.python.org/pep-0634/). Motivation and rationale
are in [**PEP 635**](https://peps.python.org/pep-0635/), and a longer tutorial is in [**PEP 636**](https://peps.python.org/pep-0636/).

### Optional `EncodingWarning` and `encoding="locale"` option [¶](https://docs.python.org/3/whatsnew/3.10.html\#optional-encodingwarning-and-encoding-locale-option "Link to this heading")

The default encoding of [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") and [`open()`](https://docs.python.org/3/library/functions.html#open "open") is
platform and locale dependent. Since UTF-8 is used on most Unix
platforms, omitting `encoding` option when opening UTF-8 files
(e.g. JSON, YAML, TOML, Markdown) is a very common bug. For example:

Copy

```
# BUG: "rb" mode or encoding="utf-8" should be used.
with open("data.json") as f:
    data = json.load(f)
```

To find this type of bug, an optional `EncodingWarning` is added.
It is emitted when [`sys.flags.warn_default_encoding`](https://docs.python.org/3/library/sys.html#sys.flags "sys.flags")
is true and locale-specific default encoding is used.

`-X warn_default_encoding` option and [`PYTHONWARNDEFAULTENCODING`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONWARNDEFAULTENCODING)
are added to enable the warning.

See [Text Encoding](https://docs.python.org/3/library/io.html#io-text-encoding) for more information.

## New Features Related to Type Hints [¶](https://docs.python.org/3/whatsnew/3.10.html\#new-features-related-to-type-hints "Link to this heading")

This section covers major changes affecting [**PEP 484**](https://peps.python.org/pep-0484/) type hints and
the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") module.

### PEP 604: New Type Union Operator [¶](https://docs.python.org/3/whatsnew/3.10.html\#pep-604-new-type-union-operator "Link to this heading")

A new type union operator was introduced which enables the syntax `X | Y`.
This provides a cleaner way of expressing ‘either type X or type Y’ instead of
using [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union"), especially in type hints.

In previous versions of Python, to apply a type hint for functions accepting
arguments of multiple types, [`typing.Union`](https://docs.python.org/3/library/typing.html#typing.Union "typing.Union") was used:

Copy

```
def square(number: Union[int, float]) -> Union[int, float]:
    return number ** 2
```

Type hints can now be written in a more succinct manner:

Copy

```
def square(number: int | float) -> int | float:
    return number ** 2
```

This new syntax is also accepted as the second argument to [`isinstance()`](https://docs.python.org/3/library/functions.html#isinstance "isinstance")
and [`issubclass()`](https://docs.python.org/3/library/functions.html#issubclass "issubclass"):

Copy

```
>>> isinstance(1, int | str)
True
```

See [Union Type](https://docs.python.org/3/library/stdtypes.html#types-union) and [**PEP 604**](https://peps.python.org/pep-0604/) for more details.

(Contributed by Maggie Moss and Philippe Prados in [bpo-41428](https://bugs.python.org/issue?@action=redirect&bpo=41428),
with additions by Yurii Karabas and Serhiy Storchaka in [bpo-44490](https://bugs.python.org/issue?@action=redirect&bpo=44490).)

### PEP 612: Parameter Specification Variables [¶](https://docs.python.org/3/whatsnew/3.10.html\#pep-612-parameter-specification-variables "Link to this heading")

Two new options to improve the information provided to static type checkers for
[**PEP 484**](https://peps.python.org/pep-0484/)‘s `Callable` have been added to the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") module.

The first is the parameter specification variable. They are used to forward the
parameter types of one callable to another callable – a pattern commonly
found in higher order functions and decorators. Examples of usage can be found
in [`typing.ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec"). Previously, there was no easy way to type annotate
dependency of parameter types in such a precise manner.

The second option is the new `Concatenate` operator. It’s used in conjunction
with parameter specification variables to type annotate a higher order callable
which adds or removes parameters of another callable. Examples of usage can
be found in [`typing.Concatenate`](https://docs.python.org/3/library/typing.html#typing.Concatenate "typing.Concatenate").

See [`typing.Callable`](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable"), [`typing.ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec"),
[`typing.Concatenate`](https://docs.python.org/3/library/typing.html#typing.Concatenate "typing.Concatenate"), [`typing.ParamSpecArgs`](https://docs.python.org/3/library/typing.html#typing.ParamSpecArgs "typing.ParamSpecArgs"),
[`typing.ParamSpecKwargs`](https://docs.python.org/3/library/typing.html#typing.ParamSpecKwargs "typing.ParamSpecKwargs"), and [**PEP 612**](https://peps.python.org/pep-0612/) for more details.

(Contributed by Ken Jin in [bpo-41559](https://bugs.python.org/issue?@action=redirect&bpo=41559), with minor enhancements by Jelle
Zijlstra in [bpo-43783](https://bugs.python.org/issue?@action=redirect&bpo=43783). PEP written by Mark Mendoza.)

### PEP 613: TypeAlias [¶](https://docs.python.org/3/whatsnew/3.10.html\#pep-613-typealias "Link to this heading")

[**PEP 484**](https://peps.python.org/pep-0484/) introduced the concept of type aliases, only requiring them to be
top-level unannotated assignments. This simplicity sometimes made it difficult
for type checkers to distinguish between type aliases and ordinary assignments,
especially when forward references or invalid types were involved. Compare:

Copy

```
StrCache = 'Cache[str]'  # a type alias
LOG_PREFIX = 'LOG[DEBUG]'  # a module constant
```

Now the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") module has a special value [`TypeAlias`](https://docs.python.org/3/library/typing.html#typing.TypeAlias "typing.TypeAlias")
which lets you declare type aliases more explicitly:

Copy

```
StrCache: TypeAlias = 'Cache[str]'  # a type alias
LOG_PREFIX = 'LOG[DEBUG]'  # a module constant
```

See [**PEP 613**](https://peps.python.org/pep-0613/) for more details.

(Contributed by Mikhail Golubev in [bpo-41923](https://bugs.python.org/issue?@action=redirect&bpo=41923).)

### PEP 647: User-Defined Type Guards [¶](https://docs.python.org/3/whatsnew/3.10.html\#pep-647-user-defined-type-guards "Link to this heading")

[`TypeGuard`](https://docs.python.org/3/library/typing.html#typing.TypeGuard "typing.TypeGuard") has been added to the [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") module to annotate
type guard functions and improve information provided to static type checkers
during type narrowing. For more information, please see
[`TypeGuard`](https://docs.python.org/3/library/typing.html#typing.TypeGuard "typing.TypeGuard")‘s documentation, and [**PEP 647**](https://peps.python.org/pep-0647/).

(Contributed by Ken Jin and Guido van Rossum in [bpo-43766](https://bugs.python.org/issue?@action=redirect&bpo=43766).
PEP written by Eric Traut.)

## Other Language Changes [¶](https://docs.python.org/3/whatsnew/3.10.html\#other-language-changes "Link to this heading")

- The [`int`](https://docs.python.org/3/library/functions.html#int "int") type has a new method [`int.bit_count()`](https://docs.python.org/3/library/stdtypes.html#int.bit_count "int.bit_count"), returning the
number of ones in the binary expansion of a given integer, also known
as the population count. (Contributed by Niklas Fiekas in [bpo-29882](https://bugs.python.org/issue?@action=redirect&bpo=29882).)

- The views returned by [`dict.keys()`](https://docs.python.org/3/library/stdtypes.html#dict.keys "dict.keys"), [`dict.values()`](https://docs.python.org/3/library/stdtypes.html#dict.values "dict.values") and
[`dict.items()`](https://docs.python.org/3/library/stdtypes.html#dict.items "dict.items") now all have a `mapping` attribute that gives a
[`types.MappingProxyType`](https://docs.python.org/3/library/types.html#types.MappingProxyType "types.MappingProxyType") object wrapping the original
dictionary. (Contributed by Dennis Sweeney in [bpo-40890](https://bugs.python.org/issue?@action=redirect&bpo=40890).)

- [**PEP 618**](https://peps.python.org/pep-0618/): The [`zip()`](https://docs.python.org/3/library/functions.html#zip "zip") function now has an optional `strict` flag, used
to require that all the iterables have an equal length.

- Builtin and extension functions that take integer arguments no longer accept
[`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") s, [`Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction") s and other
objects that can be converted to integers only with a loss (e.g. that have
the [`__int__()`](https://docs.python.org/3/reference/datamodel.html#object.__int__ "object.__int__") method but do not have the
[`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") method).
(Contributed by Serhiy Storchaka in [bpo-37999](https://bugs.python.org/issue?@action=redirect&bpo=37999).)

- If [`object.__ipow__()`](https://docs.python.org/3/reference/datamodel.html#object.__ipow__ "object.__ipow__") returns [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented"), the operator will
correctly fall back to [`object.__pow__()`](https://docs.python.org/3/reference/datamodel.html#object.__pow__ "object.__pow__") and [`object.__rpow__()`](https://docs.python.org/3/reference/datamodel.html#object.__rpow__ "object.__rpow__") as expected.
(Contributed by Alex Shkop in [bpo-38302](https://bugs.python.org/issue?@action=redirect&bpo=38302).)

- Assignment expressions can now be used unparenthesized within set literals
and set comprehensions, as well as in sequence indexes (but not slices).

- Functions have a new `__builtins__` attribute which is used to look for
builtin symbols when a function is executed, instead of looking into
`__globals__['__builtins__']`. The attribute is initialized from
`__globals__["__builtins__"]` if it exists, else from the current builtins.
(Contributed by Mark Shannon in [bpo-42990](https://bugs.python.org/issue?@action=redirect&bpo=42990).)

- Two new builtin functions – [`aiter()`](https://docs.python.org/3/library/functions.html#aiter "aiter") and [`anext()`](https://docs.python.org/3/library/functions.html#anext "anext") have been added
to provide asynchronous counterparts to [`iter()`](https://docs.python.org/3/library/functions.html#iter "iter") and [`next()`](https://docs.python.org/3/library/functions.html#next "next"),
respectively.
(Contributed by Joshua Bronson, Daniel Pope, and Justin Wang in [bpo-31861](https://bugs.python.org/issue?@action=redirect&bpo=31861).)

- Static methods ( [`@staticmethod`](https://docs.python.org/3/library/functions.html#staticmethod "staticmethod")) and class methods
( [`@classmethod`](https://docs.python.org/3/library/functions.html#classmethod "classmethod")) now inherit the method attributes
(`__module__`, `__name__`, `__qualname__`, `__doc__`,
`__annotations__`) and have a new `__wrapped__` attribute.
Moreover, static methods are now callable as regular functions.
(Contributed by Victor Stinner in [bpo-43682](https://bugs.python.org/issue?@action=redirect&bpo=43682).)

- Annotations for complex targets (everything beside `simple name` targets
defined by [**PEP 526**](https://peps.python.org/pep-0526/)) no longer cause any runtime effects with `from __future__ import annotations`.
(Contributed by Batuhan Taskaya in [bpo-42737](https://bugs.python.org/issue?@action=redirect&bpo=42737).)

- Class and module objects now lazy-create empty annotations dicts on demand.
The annotations dicts are stored in the object’s `__dict__` for
backwards compatibility. This improves the best practices for working
with `__annotations__`; for more information, please see
[Annotations Best Practices](https://docs.python.org/3/howto/annotations.html#annotations-howto).
(Contributed by Larry Hastings in [bpo-43901](https://bugs.python.org/issue?@action=redirect&bpo=43901).)

- Annotations consist of `yield`, `yield from`, `await` or named expressions
are now forbidden under `from __future__ import annotations` due to their side
effects.
(Contributed by Batuhan Taskaya in [bpo-42725](https://bugs.python.org/issue?@action=redirect&bpo=42725).)

- Usage of unbound variables, `super()` and other expressions that might
alter the processing of symbol table as annotations are now rendered
effectless under `from __future__ import annotations`.
(Contributed by Batuhan Taskaya in [bpo-42725](https://bugs.python.org/issue?@action=redirect&bpo=42725).)

- Hashes of NaN values of both [`float`](https://docs.python.org/3/library/functions.html#float "float") type and
[`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") type now depend on object identity. Formerly, they
always hashed to `0` even though NaN values are not equal to one another.
This caused potentially quadratic runtime behavior due to excessive hash
collisions when creating dictionaries and sets containing multiple NaNs.
(Contributed by Raymond Hettinger in [bpo-43475](https://bugs.python.org/issue?@action=redirect&bpo=43475).)

- A [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") (instead of a [`NameError`](https://docs.python.org/3/library/exceptions.html#NameError "NameError")) will be raised when deleting
the [`__debug__`](https://docs.python.org/3/library/constants.html#debug__ "__debug__") constant. (Contributed by Donghee Na in [bpo-45000](https://bugs.python.org/issue?@action=redirect&bpo=45000).)

- [`SyntaxError`](https://docs.python.org/3/library/exceptions.html#SyntaxError "SyntaxError") exceptions now have `end_lineno` and
`end_offset` attributes. They will be `None` if not determined.
(Contributed by Pablo Galindo in [bpo-43914](https://bugs.python.org/issue?@action=redirect&bpo=43914).)


## New Modules [¶](https://docs.python.org/3/whatsnew/3.10.html\#new-modules "Link to this heading")

- None.


## Improved Modules [¶](https://docs.python.org/3/whatsnew/3.10.html\#improved-modules "Link to this heading")

### asyncio [¶](https://docs.python.org/3/whatsnew/3.10.html\#asyncio "Link to this heading")

Add missing [`connect_accepted_socket()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.connect_accepted_socket "asyncio.loop.connect_accepted_socket")
method.
(Contributed by Alex Grönholm in [bpo-41332](https://bugs.python.org/issue?@action=redirect&bpo=41332).)

### argparse [¶](https://docs.python.org/3/whatsnew/3.10.html\#argparse "Link to this heading")

Misleading phrase “optional arguments” was replaced with “options” in argparse help. Some tests might require adaptation if they rely on exact output match.
(Contributed by Raymond Hettinger in [bpo-9694](https://bugs.python.org/issue?@action=redirect&bpo=9694).)

### array [¶](https://docs.python.org/3/whatsnew/3.10.html\#array "Link to this heading")

The [`index()`](https://docs.python.org/3/library/array.html#array.array.index "array.array.index") method of [`array.array`](https://docs.python.org/3/library/array.html#array.array "array.array") now has
optional _start_ and _stop_ parameters.
(Contributed by Anders Lorentsen and Zackery Spytz in [bpo-31956](https://bugs.python.org/issue?@action=redirect&bpo=31956).)

### asynchat, asyncore, smtpd [¶](https://docs.python.org/3/whatsnew/3.10.html\#asynchat-asyncore-smtpd "Link to this heading")

These modules have been marked as deprecated in their module documentation
since Python 3.6. An import-time [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") has now been
added to all three of these modules.

### base64 [¶](https://docs.python.org/3/whatsnew/3.10.html\#base64 "Link to this heading")

Add [`base64.b32hexencode()`](https://docs.python.org/3/library/base64.html#base64.b32hexencode "base64.b32hexencode") and [`base64.b32hexdecode()`](https://docs.python.org/3/library/base64.html#base64.b32hexdecode "base64.b32hexdecode") to support the
Base32 Encoding with Extended Hex Alphabet.

### bdb [¶](https://docs.python.org/3/whatsnew/3.10.html\#bdb "Link to this heading")

Add `clearBreakpoints()` to reset all set breakpoints.
(Contributed by Irit Katriel in [bpo-24160](https://bugs.python.org/issue?@action=redirect&bpo=24160).)

### bisect [¶](https://docs.python.org/3/whatsnew/3.10.html\#bisect "Link to this heading")

Added the possibility of providing a _key_ function to the APIs in the [`bisect`](https://docs.python.org/3/library/bisect.html#module-bisect "bisect: Array bisection algorithms for binary searching.")
module. (Contributed by Raymond Hettinger in [bpo-4356](https://bugs.python.org/issue?@action=redirect&bpo=4356).)

### codecs [¶](https://docs.python.org/3/whatsnew/3.10.html\#codecs "Link to this heading")

Add a [`codecs.unregister()`](https://docs.python.org/3/library/codecs.html#codecs.unregister "codecs.unregister") function to unregister a codec search function.
(Contributed by Hai Shi in [bpo-41842](https://bugs.python.org/issue?@action=redirect&bpo=41842).)

### collections.abc [¶](https://docs.python.org/3/whatsnew/3.10.html\#collections-abc "Link to this heading")

The `__args__` of the [parameterized generic](https://docs.python.org/3/library/stdtypes.html#types-genericalias) for
[`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") are now consistent with [`typing.Callable`](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable").
[`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") generic now flattens type parameters, similar
to what [`typing.Callable`](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable") currently does. This means that
`collections.abc.Callable[[int, str], str]` will have `__args__` of
`(int, str, str)`; previously this was `([int, str], str)`. To allow this
change, [`types.GenericAlias`](https://docs.python.org/3/library/types.html#types.GenericAlias "types.GenericAlias") can now be subclassed, and a subclass will
be returned when subscripting the [`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") type. Note
that a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") may be raised for invalid forms of parameterizing
[`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") which may have passed silently in Python 3.9.
(Contributed by Ken Jin in [bpo-42195](https://bugs.python.org/issue?@action=redirect&bpo=42195).)

### contextlib [¶](https://docs.python.org/3/whatsnew/3.10.html\#contextlib "Link to this heading")

Add a [`contextlib.aclosing()`](https://docs.python.org/3/library/contextlib.html#contextlib.aclosing "contextlib.aclosing") context manager to safely close async generators
and objects representing asynchronously released resources.
(Contributed by Joongi Kim and John Belmonte in [bpo-41229](https://bugs.python.org/issue?@action=redirect&bpo=41229).)

Add asynchronous context manager support to [`contextlib.nullcontext()`](https://docs.python.org/3/library/contextlib.html#contextlib.nullcontext "contextlib.nullcontext").
(Contributed by Tom Gringauz in [bpo-41543](https://bugs.python.org/issue?@action=redirect&bpo=41543).)

Add [`AsyncContextDecorator`](https://docs.python.org/3/library/contextlib.html#contextlib.AsyncContextDecorator "contextlib.AsyncContextDecorator"), for supporting usage of async
context managers as decorators.

### curses [¶](https://docs.python.org/3/whatsnew/3.10.html\#curses "Link to this heading")

The extended color functions added in ncurses 6.1 will be used transparently
by [`curses.color_content()`](https://docs.python.org/3/library/curses.html#curses.color_content "curses.color_content"), [`curses.init_color()`](https://docs.python.org/3/library/curses.html#curses.init_color "curses.init_color"),
[`curses.init_pair()`](https://docs.python.org/3/library/curses.html#curses.init_pair "curses.init_pair"), and [`curses.pair_content()`](https://docs.python.org/3/library/curses.html#curses.pair_content "curses.pair_content"). A new function,
[`curses.has_extended_color_support()`](https://docs.python.org/3/library/curses.html#curses.has_extended_color_support "curses.has_extended_color_support"), indicates whether extended color
support is provided by the underlying ncurses library.
(Contributed by Jeffrey Kintscher and Hans Petter Jansson in [bpo-36982](https://bugs.python.org/issue?@action=redirect&bpo=36982).)

The `BUTTON5_*` constants are now exposed in the [`curses`](https://docs.python.org/3/library/curses.html#module-curses "curses: An interface to the curses library, providing portable terminal handling. (Unix)") module if
they are provided by the underlying curses library.
(Contributed by Zackery Spytz in [bpo-39273](https://bugs.python.org/issue?@action=redirect&bpo=39273).)

### dataclasses [¶](https://docs.python.org/3/whatsnew/3.10.html\#dataclasses "Link to this heading")

#### \_\_slots\_\_ [¶](https://docs.python.org/3/whatsnew/3.10.html\#slots "Link to this heading")

Added `slots` parameter in [`dataclasses.dataclass()`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass") decorator.
(Contributed by Yurii Karabas in [bpo-42269](https://bugs.python.org/issue?@action=redirect&bpo=42269))

#### Keyword-only fields [¶](https://docs.python.org/3/whatsnew/3.10.html\#keyword-only-fields "Link to this heading")

dataclasses now supports fields that are keyword-only in the
generated \_\_init\_\_ method. There are a number of ways of specifying
keyword-only fields.

You can say that every field is keyword-only:

Copy

```
from dataclasses import dataclass

@dataclass(kw_only=True)
class Birthday:
    name: str
    birthday: datetime.date
```

Both `name` and `birthday` are keyword-only parameters to the
generated \_\_init\_\_ method.

You can specify keyword-only on a per-field basis:

Copy

```
from dataclasses import dataclass, field

@dataclass
class Birthday:
    name: str
    birthday: datetime.date = field(kw_only=True)
```

Here only `birthday` is keyword-only. If you set `kw_only` on
individual fields, be aware that there are rules about re-ordering
fields due to keyword-only fields needing to follow non-keyword-only
fields. See the full dataclasses documentation for details.

You can also specify that all fields following a KW\_ONLY marker are
keyword-only. This will probably be the most common usage:

Copy

```
from dataclasses import dataclass, KW_ONLY

@dataclass
class Point:
    x: float
    y: float
    _: KW_ONLY
    z: float = 0.0
    t: float = 0.0
```

Here, `z` and `t` are keyword-only parameters, while `x` and
`y` are not.
(Contributed by Eric V. Smith in [bpo-43532](https://bugs.python.org/issue?@action=redirect&bpo=43532).)

### distutils [¶](https://docs.python.org/3/whatsnew/3.10.html\#distutils "Link to this heading")

The entire `distutils` package is deprecated, to be removed in Python
3.12. Its functionality for specifying package builds has already been
completely replaced by third-party packages `setuptools` and
`packaging`, and most other commonly used APIs are available elsewhere
in the standard library (such as [`platform`](https://docs.python.org/3/library/platform.html#module-platform "platform: Retrieves as much platform identifying data as possible."), [`shutil`](https://docs.python.org/3/library/shutil.html#module-shutil "shutil: High-level file operations, including copying."),
[`subprocess`](https://docs.python.org/3/library/subprocess.html#module-subprocess "subprocess: Subprocess management.") or [`sysconfig`](https://docs.python.org/3/library/sysconfig.html#module-sysconfig "sysconfig: Python's configuration information")). There are no plans to migrate
any other functionality from `distutils`, and applications that are
using other functions should plan to make private copies of the code.
Refer to [**PEP 632**](https://peps.python.org/pep-0632/) for discussion.

The `bdist_wininst` command deprecated in Python 3.8 has been removed.
The `bdist_wheel` command is now recommended to distribute binary packages
on Windows.
(Contributed by Victor Stinner in [bpo-42802](https://bugs.python.org/issue?@action=redirect&bpo=42802).)

### doctest [¶](https://docs.python.org/3/whatsnew/3.10.html\#doctest "Link to this heading")

When a module does not define `__loader__`, fall back to `__spec__.loader`.
(Contributed by Brett Cannon in [bpo-42133](https://bugs.python.org/issue?@action=redirect&bpo=42133).)

### encodings [¶](https://docs.python.org/3/whatsnew/3.10.html\#encodings "Link to this heading")

[`encodings.normalize_encoding()`](https://docs.python.org/3/library/codecs.html#encodings.normalize_encoding "encodings.normalize_encoding") now ignores non-ASCII characters.
(Contributed by Hai Shi in [bpo-39337](https://bugs.python.org/issue?@action=redirect&bpo=39337).)

### enum [¶](https://docs.python.org/3/whatsnew/3.10.html\#enum "Link to this heading")

[`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum") [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__") now returns `enum_name.member_name` and
[`__str__()`](https://docs.python.org/3/reference/datamodel.html#object.__str__ "object.__str__") now returns `member_name`. Stdlib enums available as
module constants have a [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") of `module_name.member_name`.
(Contributed by Ethan Furman in [bpo-40066](https://bugs.python.org/issue?@action=redirect&bpo=40066).)

Add [`enum.StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum") for enums where all members are strings.
(Contributed by Ethan Furman in [bpo-41816](https://bugs.python.org/issue?@action=redirect&bpo=41816).)

### fileinput [¶](https://docs.python.org/3/whatsnew/3.10.html\#fileinput "Link to this heading")

Add _encoding_ and _errors_ parameters in [`fileinput.input()`](https://docs.python.org/3/library/fileinput.html#fileinput.input "fileinput.input") and
[`fileinput.FileInput`](https://docs.python.org/3/library/fileinput.html#fileinput.FileInput "fileinput.FileInput").
(Contributed by Inada Naoki in [bpo-43712](https://bugs.python.org/issue?@action=redirect&bpo=43712).)

[`fileinput.hook_compressed()`](https://docs.python.org/3/library/fileinput.html#fileinput.hook_compressed "fileinput.hook_compressed") now returns [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper") object
when _mode_ is “r” and file is compressed, like uncompressed files.
(Contributed by Inada Naoki in [bpo-5758](https://bugs.python.org/issue?@action=redirect&bpo=5758).)

### faulthandler [¶](https://docs.python.org/3/whatsnew/3.10.html\#faulthandler "Link to this heading")

The [`faulthandler`](https://docs.python.org/3/library/faulthandler.html#module-faulthandler "faulthandler: Dump the Python traceback.") module now detects if a fatal error occurs during a
garbage collector collection.
(Contributed by Victor Stinner in [bpo-44466](https://bugs.python.org/issue?@action=redirect&bpo=44466).)

### gc [¶](https://docs.python.org/3/whatsnew/3.10.html\#gc "Link to this heading")

Add audit hooks for [`gc.get_objects()`](https://docs.python.org/3/library/gc.html#gc.get_objects "gc.get_objects"), [`gc.get_referrers()`](https://docs.python.org/3/library/gc.html#gc.get_referrers "gc.get_referrers") and
[`gc.get_referents()`](https://docs.python.org/3/library/gc.html#gc.get_referents "gc.get_referents"). (Contributed by Pablo Galindo in [bpo-43439](https://bugs.python.org/issue?@action=redirect&bpo=43439).)

### glob [¶](https://docs.python.org/3/whatsnew/3.10.html\#glob "Link to this heading")

Add the _root\_dir_ and _dir\_fd_ parameters in [`glob()`](https://docs.python.org/3/library/glob.html#glob.glob "glob.glob") and
[`iglob()`](https://docs.python.org/3/library/glob.html#glob.iglob "glob.iglob") which allow to specify the root directory for searching.
(Contributed by Serhiy Storchaka in [bpo-38144](https://bugs.python.org/issue?@action=redirect&bpo=38144).)

### hashlib [¶](https://docs.python.org/3/whatsnew/3.10.html\#hashlib "Link to this heading")

The hashlib module requires OpenSSL 1.1.1 or newer.
(Contributed by Christian Heimes in [**PEP 644**](https://peps.python.org/pep-0644/) and [bpo-43669](https://bugs.python.org/issue?@action=redirect&bpo=43669).)

The hashlib module has preliminary support for OpenSSL 3.0.0.
(Contributed by Christian Heimes in [bpo-38820](https://bugs.python.org/issue?@action=redirect&bpo=38820) and other issues.)

The pure-Python fallback of [`pbkdf2_hmac()`](https://docs.python.org/3/library/hashlib.html#hashlib.pbkdf2_hmac "hashlib.pbkdf2_hmac") is deprecated. In
the future PBKDF2-HMAC will only be available when Python has been built with
OpenSSL support.
(Contributed by Christian Heimes in [bpo-43880](https://bugs.python.org/issue?@action=redirect&bpo=43880).)

### hmac [¶](https://docs.python.org/3/whatsnew/3.10.html\#hmac "Link to this heading")

The hmac module now uses OpenSSL’s HMAC implementation internally.
(Contributed by Christian Heimes in [bpo-40645](https://bugs.python.org/issue?@action=redirect&bpo=40645).)

### IDLE and idlelib [¶](https://docs.python.org/3/whatsnew/3.10.html\#idle-and-idlelib "Link to this heading")

Make IDLE invoke [`sys.excepthook()`](https://docs.python.org/3/library/sys.html#sys.excepthook "sys.excepthook") (when started without ‘-n’).
User hooks were previously ignored. (Contributed by Ken Hilton in
[bpo-43008](https://bugs.python.org/issue?@action=redirect&bpo=43008).)

Rearrange the settings dialog. Split the General tab into Windows
and Shell/Ed tabs. Move help sources, which extend the Help menu, to the
Extensions tab. Make space for new options and shorten the dialog. The
latter makes the dialog better fit small screens. (Contributed by Terry Jan
Reedy in [bpo-40468](https://bugs.python.org/issue?@action=redirect&bpo=40468).) Move the indent space setting from the Font tab to
the new Windows tab. (Contributed by Mark Roseman and Terry Jan Reedy in
[bpo-33962](https://bugs.python.org/issue?@action=redirect&bpo=33962).)

The changes above were backported to a 3.9 maintenance release.

Add a Shell sidebar. Move the primary prompt (‘>>>’) to the sidebar.
Add secondary prompts (’…’) to the sidebar. Left click and optional
drag selects one or more lines of text, as with the editor
line number sidebar. Right click after selecting text lines displays
a context menu with ‘copy with prompts’. This zips together prompts
from the sidebar with lines from the selected text. This option also
appears on the context menu for the text. (Contributed by Tal Einat
in [bpo-37903](https://bugs.python.org/issue?@action=redirect&bpo=37903).)

Use spaces instead of tabs to indent interactive code. This makes
interactive code entries ‘look right’. Making this feasible was a
major motivation for adding the shell sidebar. (Contributed by
Terry Jan Reedy in [bpo-37892](https://bugs.python.org/issue?@action=redirect&bpo=37892).)

Highlight the new [soft keywords](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords) [`match`](https://docs.python.org/3/reference/compound_stmts.html#match),
[`case`](https://docs.python.org/3/reference/compound_stmts.html#match), and [`_`](https://docs.python.org/3/reference/compound_stmts.html#wildcard-patterns) in
pattern-matching statements. However, this highlighting is not perfect
and will be incorrect in some rare cases, including some `_`-s in
`case` patterns. (Contributed by Tal Einat in [bpo-44010](https://bugs.python.org/issue?@action=redirect&bpo=44010).)

New in 3.10 maintenance releases.

Apply syntax highlighting to `.pyi` files. (Contributed by Alex
Waygood and Terry Jan Reedy in [bpo-45447](https://bugs.python.org/issue?@action=redirect&bpo=45447).)

Include prompts when saving Shell with inputs and outputs.
(Contributed by Terry Jan Reedy in [gh-95191](https://github.com/python/cpython/issues/95191).)

### importlib.metadata [¶](https://docs.python.org/3/whatsnew/3.10.html\#importlib-metadata "Link to this heading")

Feature parity with `importlib_metadata` 4.6
( [history](https://importlib-metadata.readthedocs.io/en/latest/history.html)).

[importlib.metadata entry points](https://docs.python.org/3/library/importlib.metadata.html#entry-points)
now provide a nicer experience
for selecting entry points by group and name through a new
[importlib.metadata.EntryPoints](https://docs.python.org/3/library/importlib.metadata.html#entry-points) class. See the Compatibility
Note in the docs for more info on the deprecation and usage.

Added [importlib.metadata.packages\_distributions()](https://docs.python.org/3/library/importlib.metadata.html#package-distributions)
for resolving top-level Python modules and packages to their
[importlib.metadata.Distribution](https://docs.python.org/3/library/importlib.metadata.html#distributions).

### inspect [¶](https://docs.python.org/3/whatsnew/3.10.html\#inspect "Link to this heading")

When a module does not define `__loader__`, fall back to `__spec__.loader`.
(Contributed by Brett Cannon in [bpo-42133](https://bugs.python.org/issue?@action=redirect&bpo=42133).)

Add [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations"), which safely computes the annotations
defined on an object. It works around the quirks of accessing the annotations
on various types of objects, and makes very few assumptions about the object
it examines. [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations") can also correctly un-stringize
stringized annotations. [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations") is now considered
best practice for accessing the annotations dict defined on any Python object;
for more information on best practices for working with annotations, please see
[Annotations Best Practices](https://docs.python.org/3/howto/annotations.html#annotations-howto).
Relatedly, [`inspect.signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature"),
[`inspect.Signature.from_callable()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.from_callable "inspect.Signature.from_callable"), and `inspect.Signature.from_function()`
now call [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations "inspect.get_annotations") to retrieve annotations. This means
[`inspect.signature()`](https://docs.python.org/3/library/inspect.html#inspect.signature "inspect.signature") and [`inspect.Signature.from_callable()`](https://docs.python.org/3/library/inspect.html#inspect.Signature.from_callable "inspect.Signature.from_callable") can
also now un-stringize stringized annotations.
(Contributed by Larry Hastings in [bpo-43817](https://bugs.python.org/issue?@action=redirect&bpo=43817).)

### itertools [¶](https://docs.python.org/3/whatsnew/3.10.html\#itertools "Link to this heading")

Add [`itertools.pairwise()`](https://docs.python.org/3/library/itertools.html#itertools.pairwise "itertools.pairwise").
(Contributed by Raymond Hettinger in [bpo-38200](https://bugs.python.org/issue?@action=redirect&bpo=38200).)

### linecache [¶](https://docs.python.org/3/whatsnew/3.10.html\#linecache "Link to this heading")

When a module does not define `__loader__`, fall back to `__spec__.loader`.
(Contributed by Brett Cannon in [bpo-42133](https://bugs.python.org/issue?@action=redirect&bpo=42133).)

### os [¶](https://docs.python.org/3/whatsnew/3.10.html\#os "Link to this heading")

Add [`os.cpu_count()`](https://docs.python.org/3/library/os.html#os.cpu_count "os.cpu_count") support for VxWorks RTOS.
(Contributed by Peixing Xin in [bpo-41440](https://bugs.python.org/issue?@action=redirect&bpo=41440).)

Add a new function [`os.eventfd()`](https://docs.python.org/3/library/os.html#os.eventfd "os.eventfd") and related helpers to wrap the
`eventfd2` syscall on Linux.
(Contributed by Christian Heimes in [bpo-41001](https://bugs.python.org/issue?@action=redirect&bpo=41001).)

Add [`os.splice()`](https://docs.python.org/3/library/os.html#os.splice "os.splice") that allows to move data between two file
descriptors without copying between kernel address space and user
address space, where one of the file descriptors must refer to a
pipe. (Contributed by Pablo Galindo in [bpo-41625](https://bugs.python.org/issue?@action=redirect&bpo=41625).)

Add [`O_EVTONLY`](https://docs.python.org/3/library/os.html#os.O_EVTONLY "os.O_EVTONLY"), [`O_FSYNC`](https://docs.python.org/3/library/os.html#os.O_FSYNC "os.O_FSYNC"), [`O_SYMLINK`](https://docs.python.org/3/library/os.html#os.O_SYMLINK "os.O_SYMLINK")
and [`O_NOFOLLOW_ANY`](https://docs.python.org/3/library/os.html#os.O_NOFOLLOW_ANY "os.O_NOFOLLOW_ANY") for macOS.
(Contributed by Donghee Na in [bpo-43106](https://bugs.python.org/issue?@action=redirect&bpo=43106).)

### os.path [¶](https://docs.python.org/3/whatsnew/3.10.html\#os-path "Link to this heading")

[`os.path.realpath()`](https://docs.python.org/3/library/os.path.html#os.path.realpath "os.path.realpath") now accepts a _strict_ keyword-only argument. When set
to `True`, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised if a path doesn’t exist or a symlink loop
is encountered.
(Contributed by Barney Gale in [bpo-43757](https://bugs.python.org/issue?@action=redirect&bpo=43757).)

### pathlib [¶](https://docs.python.org/3/whatsnew/3.10.html\#pathlib "Link to this heading")

Add slice support to [`PurePath.parents`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parents "pathlib.PurePath.parents").
(Contributed by Joshua Cannon in [bpo-35498](https://bugs.python.org/issue?@action=redirect&bpo=35498).)

Add negative indexing support to [`PurePath.parents`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parents "pathlib.PurePath.parents").
(Contributed by Yaroslav Pankovych in [bpo-21041](https://bugs.python.org/issue?@action=redirect&bpo=21041).)

Add [`Path.hardlink_to`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.hardlink_to "pathlib.Path.hardlink_to") method that
supersedes `link_to()`. The new method has the same argument
order as [`symlink_to()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.symlink_to "pathlib.Path.symlink_to").
(Contributed by Barney Gale in [bpo-39950](https://bugs.python.org/issue?@action=redirect&bpo=39950).)

[`pathlib.Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat "pathlib.Path.stat") and [`chmod()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.chmod "pathlib.Path.chmod") now accept a
_follow\_symlinks_ keyword-only argument for consistency with corresponding
functions in the [`os`](https://docs.python.org/3/library/os.html#module-os "os: Miscellaneous operating system interfaces.") module.
(Contributed by Barney Gale in [bpo-39906](https://bugs.python.org/issue?@action=redirect&bpo=39906).)

### platform [¶](https://docs.python.org/3/whatsnew/3.10.html\#platform "Link to this heading")

Add [`platform.freedesktop_os_release()`](https://docs.python.org/3/library/platform.html#platform.freedesktop_os_release "platform.freedesktop_os_release") to retrieve operation system
identification from [freedesktop.org os-release](https://www.freedesktop.org/software/systemd/man/os-release.html) standard file.
(Contributed by Christian Heimes in [bpo-28468](https://bugs.python.org/issue?@action=redirect&bpo=28468).)

### pprint [¶](https://docs.python.org/3/whatsnew/3.10.html\#pprint "Link to this heading")

[`pprint.pprint()`](https://docs.python.org/3/library/pprint.html#pprint.pprint "pprint.pprint") now accepts a new `underscore_numbers` keyword argument.
(Contributed by sblondon in [bpo-42914](https://bugs.python.org/issue?@action=redirect&bpo=42914).)

[`pprint`](https://docs.python.org/3/library/pprint.html#module-pprint "pprint: Data pretty printer.") can now pretty-print [`dataclasses.dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass") instances.
(Contributed by Lewis Gaul in [bpo-43080](https://bugs.python.org/issue?@action=redirect&bpo=43080).)

### py\_compile [¶](https://docs.python.org/3/whatsnew/3.10.html\#py-compile "Link to this heading")

Add `--quiet` option to command-line interface of [`py_compile`](https://docs.python.org/3/library/py_compile.html#module-py_compile "py_compile: Generate byte-code files from Python source files.").
(Contributed by Gregory Schevchenko in [bpo-38731](https://bugs.python.org/issue?@action=redirect&bpo=38731).)

### pyclbr [¶](https://docs.python.org/3/whatsnew/3.10.html\#pyclbr "Link to this heading")

Add an `end_lineno` attribute to the `Function` and `Class`
objects in the tree returned by [`pyclbr.readmodule()`](https://docs.python.org/3/library/pyclbr.html#pyclbr.readmodule "pyclbr.readmodule") and
[`pyclbr.readmodule_ex()`](https://docs.python.org/3/library/pyclbr.html#pyclbr.readmodule_ex "pyclbr.readmodule_ex"). It matches the existing (start) `lineno`.
(Contributed by Aviral Srivastava in [bpo-38307](https://bugs.python.org/issue?@action=redirect&bpo=38307).)

### shelve [¶](https://docs.python.org/3/whatsnew/3.10.html\#shelve "Link to this heading")

The [`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence.") module now uses [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") by default
instead of [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") protocol `3` when creating shelves.
(Contributed by Zackery Spytz in [bpo-34204](https://bugs.python.org/issue?@action=redirect&bpo=34204).)

### statistics [¶](https://docs.python.org/3/whatsnew/3.10.html\#statistics "Link to this heading")

Add [`covariance()`](https://docs.python.org/3/library/statistics.html#statistics.covariance "statistics.covariance"), Pearson’s
[`correlation()`](https://docs.python.org/3/library/statistics.html#statistics.correlation "statistics.correlation"), and simple
[`linear_regression()`](https://docs.python.org/3/library/statistics.html#statistics.linear_regression "statistics.linear_regression") functions.
(Contributed by Tymoteusz Wołodźko in [bpo-38490](https://bugs.python.org/issue?@action=redirect&bpo=38490).)

### site [¶](https://docs.python.org/3/whatsnew/3.10.html\#site "Link to this heading")

When a module does not define `__loader__`, fall back to `__spec__.loader`.
(Contributed by Brett Cannon in [bpo-42133](https://bugs.python.org/issue?@action=redirect&bpo=42133).)

### socket [¶](https://docs.python.org/3/whatsnew/3.10.html\#socket "Link to this heading")

The exception [`socket.timeout`](https://docs.python.org/3/library/socket.html#socket.timeout "socket.timeout") is now an alias of [`TimeoutError`](https://docs.python.org/3/library/exceptions.html#TimeoutError "TimeoutError").
(Contributed by Christian Heimes in [bpo-42413](https://bugs.python.org/issue?@action=redirect&bpo=42413).)

Add option to create MPTCP sockets with `IPPROTO_MPTCP`
(Contributed by Rui Cunha in [bpo-43571](https://bugs.python.org/issue?@action=redirect&bpo=43571).)

Add `IP_RECVTOS` option to receive the type of service (ToS) or DSCP/ECN fields
(Contributed by Georg Sauthoff in [bpo-44077](https://bugs.python.org/issue?@action=redirect&bpo=44077).)

### ssl [¶](https://docs.python.org/3/whatsnew/3.10.html\#ssl "Link to this heading")

The ssl module requires OpenSSL 1.1.1 or newer.
(Contributed by Christian Heimes in [**PEP 644**](https://peps.python.org/pep-0644/) and [bpo-43669](https://bugs.python.org/issue?@action=redirect&bpo=43669).)

The ssl module has preliminary support for OpenSSL 3.0.0 and new option
[`OP_IGNORE_UNEXPECTED_EOF`](https://docs.python.org/3/library/ssl.html#ssl.OP_IGNORE_UNEXPECTED_EOF "ssl.OP_IGNORE_UNEXPECTED_EOF").
(Contributed by Christian Heimes in [bpo-38820](https://bugs.python.org/issue?@action=redirect&bpo=38820), [bpo-43794](https://bugs.python.org/issue?@action=redirect&bpo=43794),
[bpo-43788](https://bugs.python.org/issue?@action=redirect&bpo=43788), [bpo-43791](https://bugs.python.org/issue?@action=redirect&bpo=43791), [bpo-43799](https://bugs.python.org/issue?@action=redirect&bpo=43799), [bpo-43920](https://bugs.python.org/issue?@action=redirect&bpo=43920),
[bpo-43789](https://bugs.python.org/issue?@action=redirect&bpo=43789), and [bpo-43811](https://bugs.python.org/issue?@action=redirect&bpo=43811).)

Deprecated function and use of deprecated constants now result in
a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning"). [`ssl.SSLContext.options`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.options "ssl.SSLContext.options") has
[`OP_NO_SSLv2`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv2 "ssl.OP_NO_SSLv2") and [`OP_NO_SSLv3`](https://docs.python.org/3/library/ssl.html#ssl.OP_NO_SSLv3 "ssl.OP_NO_SSLv3") set by default and
therefore cannot warn about setting the flag again. The
[deprecation section](https://docs.python.org/3/whatsnew/3.10.html#whatsnew310-deprecated) has a list of deprecated
features.
(Contributed by Christian Heimes in [bpo-43880](https://bugs.python.org/issue?@action=redirect&bpo=43880).)

The ssl module now has more secure default settings. Ciphers without forward
secrecy or SHA-1 MAC are disabled by default. Security level 2 prohibits
weak RSA, DH, and ECC keys with less than 112 bits of security.
[`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") defaults to minimum protocol version TLS 1.2.
Settings are based on Hynek Schlawack’s research.
(Contributed by Christian Heimes in [bpo-43998](https://bugs.python.org/issue?@action=redirect&bpo=43998).)

The deprecated protocols SSL 3.0, TLS 1.0, and TLS 1.1 are no longer
officially supported. Python does not block them actively. However
OpenSSL build options, distro configurations, vendor patches, and cipher
suites may prevent a successful handshake.

Add a _timeout_ parameter to the [`ssl.get_server_certificate()`](https://docs.python.org/3/library/ssl.html#ssl.get_server_certificate "ssl.get_server_certificate") function.
(Contributed by Zackery Spytz in [bpo-31870](https://bugs.python.org/issue?@action=redirect&bpo=31870).)

The ssl module uses heap-types and multi-phase initialization.
(Contributed by Christian Heimes in [bpo-42333](https://bugs.python.org/issue?@action=redirect&bpo=42333).)

A new verify flag [`VERIFY_X509_PARTIAL_CHAIN`](https://docs.python.org/3/library/ssl.html#ssl.VERIFY_X509_PARTIAL_CHAIN "ssl.VERIFY_X509_PARTIAL_CHAIN") has been added.
(Contributed by l0x in [bpo-40849](https://bugs.python.org/issue?@action=redirect&bpo=40849).)

### sqlite3 [¶](https://docs.python.org/3/whatsnew/3.10.html\#sqlite3 "Link to this heading")

Add audit events for [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect"),
[`enable_load_extension()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.enable_load_extension "sqlite3.Connection.enable_load_extension"), and
[`load_extension()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.load_extension "sqlite3.Connection.load_extension").
(Contributed by Erlend E. Aasland in [bpo-43762](https://bugs.python.org/issue?@action=redirect&bpo=43762).)

### sys [¶](https://docs.python.org/3/whatsnew/3.10.html\#sys "Link to this heading")

Add [`sys.orig_argv`](https://docs.python.org/3/library/sys.html#sys.orig_argv "sys.orig_argv") attribute: the list of the original command line
arguments passed to the Python executable.
(Contributed by Victor Stinner in [bpo-23427](https://bugs.python.org/issue?@action=redirect&bpo=23427).)

Add [`sys.stdlib_module_names`](https://docs.python.org/3/library/sys.html#sys.stdlib_module_names "sys.stdlib_module_names"), containing the list of the standard library
module names.
(Contributed by Victor Stinner in [bpo-42955](https://bugs.python.org/issue?@action=redirect&bpo=42955).)

### \_thread [¶](https://docs.python.org/3/whatsnew/3.10.html\#thread "Link to this heading")

[`_thread.interrupt_main()`](https://docs.python.org/3/library/_thread.html#thread.interrupt_main "_thread.interrupt_main") now takes an optional signal number to
simulate (the default is still [`signal.SIGINT`](https://docs.python.org/3/library/signal.html#signal.SIGINT "signal.SIGINT")).
(Contributed by Antoine Pitrou in [bpo-43356](https://bugs.python.org/issue?@action=redirect&bpo=43356).)

### threading [¶](https://docs.python.org/3/whatsnew/3.10.html\#threading "Link to this heading")

Add [`threading.gettrace()`](https://docs.python.org/3/library/threading.html#threading.gettrace "threading.gettrace") and [`threading.getprofile()`](https://docs.python.org/3/library/threading.html#threading.getprofile "threading.getprofile") to
retrieve the functions set by [`threading.settrace()`](https://docs.python.org/3/library/threading.html#threading.settrace "threading.settrace") and
[`threading.setprofile()`](https://docs.python.org/3/library/threading.html#threading.setprofile "threading.setprofile") respectively.
(Contributed by Mario Corchero in [bpo-42251](https://bugs.python.org/issue?@action=redirect&bpo=42251).)

Add [`threading.__excepthook__`](https://docs.python.org/3/library/threading.html#threading.__excepthook__ "threading.__excepthook__") to allow retrieving the original value
of [`threading.excepthook()`](https://docs.python.org/3/library/threading.html#threading.excepthook "threading.excepthook") in case it is set to a broken or a different
value.
(Contributed by Mario Corchero in [bpo-42308](https://bugs.python.org/issue?@action=redirect&bpo=42308).)

### traceback [¶](https://docs.python.org/3/whatsnew/3.10.html\#traceback "Link to this heading")

The [`format_exception()`](https://docs.python.org/3/library/traceback.html#traceback.format_exception "traceback.format_exception"),
[`format_exception_only()`](https://docs.python.org/3/library/traceback.html#traceback.format_exception_only "traceback.format_exception_only"), and
[`print_exception()`](https://docs.python.org/3/library/traceback.html#traceback.print_exception "traceback.print_exception") functions can now take an exception object
as a positional-only argument.
(Contributed by Zackery Spytz and Matthias Bussonnier in [bpo-26389](https://bugs.python.org/issue?@action=redirect&bpo=26389).)

### types [¶](https://docs.python.org/3/whatsnew/3.10.html\#types "Link to this heading")

Reintroduce the [`types.EllipsisType`](https://docs.python.org/3/library/types.html#types.EllipsisType "types.EllipsisType"), [`types.NoneType`](https://docs.python.org/3/library/types.html#types.NoneType "types.NoneType")
and [`types.NotImplementedType`](https://docs.python.org/3/library/types.html#types.NotImplementedType "types.NotImplementedType") classes, providing a new set
of types readily interpretable by type checkers.
(Contributed by Bas van Beek in [bpo-41810](https://bugs.python.org/issue?@action=redirect&bpo=41810).)

### typing [¶](https://docs.python.org/3/whatsnew/3.10.html\#typing "Link to this heading")

For major changes, see [New Features Related to Type Hints](https://docs.python.org/3/whatsnew/3.10.html#new-feat-related-type-hints).

The behavior of [`typing.Literal`](https://docs.python.org/3/library/typing.html#typing.Literal "typing.Literal") was changed to conform with [**PEP 586**](https://peps.python.org/pep-0586/)
and to match the behavior of static type checkers specified in the PEP.

1. `Literal` now de-duplicates parameters.

2. Equality comparisons between `Literal` objects are now order independent.

3. `Literal` comparisons now respect types. For example,
`Literal[0] == Literal[False]` previously evaluated to `True`. It is
now `False`. To support this change, the internally used type cache now
supports differentiating types.

4. `Literal` objects will now raise a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") exception during
equality comparisons if any of their parameters are not [hashable](https://docs.python.org/3/glossary.html#term-hashable).
Note that declaring `Literal` with unhashable parameters will not throw
an error:



Copy

```
>>> from typing import Literal
>>> Literal[{0}]
>>> Literal[{0}] == Literal[{False}]
Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'set'
```


(Contributed by Yurii Karabas in [bpo-42345](https://bugs.python.org/issue?@action=redirect&bpo=42345).)

Add new function [`typing.is_typeddict()`](https://docs.python.org/3/library/typing.html#typing.is_typeddict "typing.is_typeddict") to introspect if an annotation
is a [`typing.TypedDict`](https://docs.python.org/3/library/typing.html#typing.TypedDict "typing.TypedDict").
(Contributed by Patrick Reader in [bpo-41792](https://bugs.python.org/issue?@action=redirect&bpo=41792).)

Subclasses of `typing.Protocol` which only have data variables declared
will now raise a `TypeError` when checked with `isinstance` unless they
are decorated with [`runtime_checkable()`](https://docs.python.org/3/library/typing.html#typing.runtime_checkable "typing.runtime_checkable"). Previously, these checks
passed silently. Users should decorate their
subclasses with the `runtime_checkable()` decorator
if they want runtime protocols.
(Contributed by Yurii Karabas in [bpo-38908](https://bugs.python.org/issue?@action=redirect&bpo=38908).)

Importing from the `typing.io` and `typing.re` submodules will now emit
[`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning"). These submodules have been deprecated since
Python 3.8 and will be removed in a future version of Python. Anything
belonging to those submodules should be imported directly from
[`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") instead.
(Contributed by Sebastian Rittau in [bpo-38291](https://bugs.python.org/issue?@action=redirect&bpo=38291).)

### unittest [¶](https://docs.python.org/3/whatsnew/3.10.html\#unittest "Link to this heading")

Add new method [`assertNoLogs()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertNoLogs "unittest.TestCase.assertNoLogs") to complement the
existing [`assertLogs()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertLogs "unittest.TestCase.assertLogs"). (Contributed by Kit Yan Choi
in [bpo-39385](https://bugs.python.org/issue?@action=redirect&bpo=39385).)

### urllib.parse [¶](https://docs.python.org/3/whatsnew/3.10.html\#urllib-parse "Link to this heading")

Python versions earlier than Python 3.10 allowed using both `;` and `&` as
query parameter separators in [`urllib.parse.parse_qs()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qs "urllib.parse.parse_qs") and
[`urllib.parse.parse_qsl()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.parse_qsl "urllib.parse.parse_qsl"). Due to security concerns, and to conform with
newer W3C recommendations, this has been changed to allow only a single
separator key, with `&` as the default. This change also affects
`cgi.parse()` and `cgi.parse_multipart()` as they use the affected
functions internally. For more details, please see their respective
documentation.
(Contributed by Adam Goldschmidt, Senthil Kumaran and Ken Jin in [bpo-42967](https://bugs.python.org/issue?@action=redirect&bpo=42967).)

The presence of newline or tab characters in parts of a URL allows for some
forms of attacks. Following the WHATWG specification that updates [**RFC 3986**](https://datatracker.ietf.org/doc/html/rfc3986.html),
ASCII newline `\n`, `\r` and tab `\t` characters are stripped from the
URL by the parser in [`urllib.parse`](https://docs.python.org/3/library/urllib.parse.html#module-urllib.parse "urllib.parse: Parse URLs into or assemble them from components.") preventing such attacks. The removal
characters are controlled by a new module level variable
`urllib.parse._UNSAFE_URL_BYTES_TO_REMOVE`. (See [gh-88048](https://github.com/python/cpython/issues/88048))

### xml [¶](https://docs.python.org/3/whatsnew/3.10.html\#xml "Link to this heading")

Add a [`LexicalHandler`](https://docs.python.org/3/library/xml.sax.handler.html#xml.sax.handler.LexicalHandler "xml.sax.handler.LexicalHandler") class to the
[`xml.sax.handler`](https://docs.python.org/3/library/xml.sax.handler.html#module-xml.sax.handler "xml.sax.handler: Base classes for SAX event handlers.") module.
(Contributed by Jonathan Gossage and Zackery Spytz in [bpo-35018](https://bugs.python.org/issue?@action=redirect&bpo=35018).)

### zipimport [¶](https://docs.python.org/3/whatsnew/3.10.html\#zipimport "Link to this heading")

Add methods related to [**PEP 451**](https://peps.python.org/pep-0451/): [`find_spec()`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.find_spec "zipimport.zipimporter.find_spec"),
[`zipimport.zipimporter.create_module()`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.create_module "zipimport.zipimporter.create_module"), and
[`zipimport.zipimporter.exec_module()`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.exec_module "zipimport.zipimporter.exec_module").
(Contributed by Brett Cannon in [bpo-42131](https://bugs.python.org/issue?@action=redirect&bpo=42131).)

Add [`invalidate_caches()`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.invalidate_caches "zipimport.zipimporter.invalidate_caches") method.
(Contributed by Desmond Cheong in [bpo-14678](https://bugs.python.org/issue?@action=redirect&bpo=14678).)

## Optimizations [¶](https://docs.python.org/3/whatsnew/3.10.html\#optimizations "Link to this heading")

- Constructors [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str"), [`bytes()`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and [`bytearray()`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") are now faster
(around 30–40% for small objects).
(Contributed by Serhiy Storchaka in [bpo-41334](https://bugs.python.org/issue?@action=redirect&bpo=41334).)

- The [`runpy`](https://docs.python.org/3/library/runpy.html#module-runpy "runpy: Locate and run Python modules without importing them first.") module now imports fewer modules.
The `python3 -m module-name` command startup time is 1.4x faster in
average. On Linux, `python3 -I -m module-name` imports 69 modules on Python
3.9, whereas it only imports 51 modules (-18) on Python 3.10.
(Contributed by Victor Stinner in [bpo-41006](https://bugs.python.org/issue?@action=redirect&bpo=41006) and [bpo-41718](https://bugs.python.org/issue?@action=redirect&bpo=41718).)

- The `LOAD_ATTR` instruction now uses new “per opcode cache” mechanism. It
is about 36% faster now for regular attributes and 44% faster for slots.
(Contributed by Pablo Galindo and Yury Selivanov in [bpo-42093](https://bugs.python.org/issue?@action=redirect&bpo=42093) and Guido
van Rossum in [bpo-42927](https://bugs.python.org/issue?@action=redirect&bpo=42927), based on ideas implemented originally in PyPy
and MicroPython.)

- When building Python with [`--enable-optimizations`](https://docs.python.org/3/using/configure.html#cmdoption-enable-optimizations) now
`-fno-semantic-interposition` is added to both the compile and link line.
This speeds builds of the Python interpreter created with [`--enable-shared`](https://docs.python.org/3/using/configure.html#cmdoption-enable-shared)
with `gcc` by up to 30%. See [this article](https://developers.redhat.com/blog/2020/06/25/red-hat-enterprise-linux-8-2-brings-faster-python-3-8-run-speeds/)
for more details. (Contributed by Victor Stinner and Pablo Galindo in
[bpo-38980](https://bugs.python.org/issue?@action=redirect&bpo=38980).)

- Use a new output buffer management code for [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.") / [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") /
[`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") modules, and add `.readall()` function to
`_compression.DecompressReader` class. bz2 decompression is now 1.09x ~ 1.17x
faster, lzma decompression 1.20x ~ 1.32x faster, `GzipFile.read(-1)` 1.11x
~ 1.18x faster. (Contributed by Ma Lin, reviewed by Gregory P. Smith, in [bpo-41486](https://bugs.python.org/issue?@action=redirect&bpo=41486))

- When using stringized annotations, annotations dicts for functions are no longer
created when the function is created. Instead, they are stored as a tuple of
strings, and the function object lazily converts this into the annotations dict
on demand. This optimization cuts the CPU time needed to define an annotated
function by half.
(Contributed by Yurii Karabas and Inada Naoki in [bpo-42202](https://bugs.python.org/issue?@action=redirect&bpo=42202).)

- Substring search functions such as `str1 in str2` and `str2.find(str1)`
now sometimes use Crochemore & Perrin’s “Two-Way” string searching
algorithm to avoid quadratic behavior on long strings. (Contributed
by Dennis Sweeney in [bpo-41972](https://bugs.python.org/issue?@action=redirect&bpo=41972))

- Add micro-optimizations to `_PyType_Lookup()` to improve type attribute cache lookup
performance in the common case of cache hits. This makes the interpreter 1.04 times faster
on average. (Contributed by Dino Viehland in [bpo-43452](https://bugs.python.org/issue?@action=redirect&bpo=43452).)

- The following built-in functions now support the faster [**PEP 590**](https://peps.python.org/pep-0590/) vectorcall calling convention:
[`map()`](https://docs.python.org/3/library/functions.html#map "map"), [`filter()`](https://docs.python.org/3/library/functions.html#filter "filter"), [`reversed()`](https://docs.python.org/3/library/functions.html#reversed "reversed"), [`bool()`](https://docs.python.org/3/library/functions.html#bool "bool") and [`float()`](https://docs.python.org/3/library/functions.html#float "float").
(Contributed by Donghee Na and Jeroen Demeyer in [bpo-43575](https://bugs.python.org/issue?@action=redirect&bpo=43575), [bpo-43287](https://bugs.python.org/issue?@action=redirect&bpo=43287), [bpo-41922](https://bugs.python.org/issue?@action=redirect&bpo=41922), [bpo-41873](https://bugs.python.org/issue?@action=redirect&bpo=41873) and [bpo-41870](https://bugs.python.org/issue?@action=redirect&bpo=41870).)

- [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File") performance is improved by removing internal `RLock`.
This makes `BZ2File` thread unsafe in the face of multiple simultaneous
readers or writers, just like its equivalent classes in [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.") and
[`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.") have always been. (Contributed by Inada Naoki in [bpo-43785](https://bugs.python.org/issue?@action=redirect&bpo=43785).)


## Deprecated [¶](https://docs.python.org/3/whatsnew/3.10.html\#deprecated "Link to this heading")

- Currently Python accepts numeric literals immediately followed by keywords,
for example `0in x`, `1or x`, `0if 1else 2`. It allows confusing
and ambiguous expressions like `[0x1for x in y]` (which can be
interpreted as `[0x1 for x in y]` or `[0x1f or x in y]`). Starting in
this release, a deprecation warning is raised if the numeric literal is
immediately followed by one of keywords [`and`](https://docs.python.org/3/reference/expressions.html#and), [`else`](https://docs.python.org/3/reference/compound_stmts.html#else),
[`for`](https://docs.python.org/3/reference/compound_stmts.html#for), [`if`](https://docs.python.org/3/reference/compound_stmts.html#if), [`in`](https://docs.python.org/3/reference/expressions.html#in), [`is`](https://docs.python.org/3/reference/expressions.html#is) and [`or`](https://docs.python.org/3/reference/expressions.html#or).
In future releases it will be changed to syntax warning, and finally to
syntax error.
(Contributed by Serhiy Storchaka in [bpo-43833](https://bugs.python.org/issue?@action=redirect&bpo=43833).)

- Starting in this release, there will be a concerted effort to begin
cleaning up old import semantics that were kept for Python 2.7
compatibility. Specifically,
`find_loader()`/`find_module()`
(superseded by [`find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec "importlib.abc.MetaPathFinder.find_spec")),
[`load_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "importlib.abc.Loader.load_module")
(superseded by [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module")),
`module_repr()` (which the import system
takes care of for you), the `__package__` attribute
(superseded by `__spec__.parent`), the `__loader__` attribute
(superseded by `__spec__.loader`), and the `__cached__` attribute
(superseded by `__spec__.cached`) will slowly be removed (as well
as other classes and methods in [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.")).
[`ImportWarning`](https://docs.python.org/3/library/exceptions.html#ImportWarning "ImportWarning") and/or [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") will be raised
as appropriate to help identify code which needs updating during
this transition.

- The entire `distutils` namespace is deprecated, to be removed in
Python 3.12. Refer to the [module changes](https://docs.python.org/3/whatsnew/3.10.html#distutils-deprecated)
section for more information.

- Non-integer arguments to [`random.randrange()`](https://docs.python.org/3/library/random.html#random.randrange "random.randrange") are deprecated.
The [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is deprecated in favor of a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").
(Contributed by Serhiy Storchaka and Raymond Hettinger in [bpo-37319](https://bugs.python.org/issue?@action=redirect&bpo=37319).)

- The various `load_module()` methods of [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.") have been
documented as deprecated since Python 3.6, but will now also trigger
a [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning"). Use
[`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") instead.
(Contributed by Brett Cannon in [bpo-26131](https://bugs.python.org/issue?@action=redirect&bpo=26131).)

- `zimport.zipimporter.load_module()` has been deprecated in
preference for [`exec_module()`](https://docs.python.org/3/library/zipimport.html#zipimport.zipimporter.exec_module "zipimport.zipimporter.exec_module").
(Contributed by Brett Cannon in [bpo-26131](https://bugs.python.org/issue?@action=redirect&bpo=26131).)

- The use of [`load_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "importlib.abc.Loader.load_module") by the import
system now triggers an [`ImportWarning`](https://docs.python.org/3/library/exceptions.html#ImportWarning "ImportWarning") as
[`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") is preferred.
(Contributed by Brett Cannon in [bpo-26131](https://bugs.python.org/issue?@action=redirect&bpo=26131).)

- The use of `importlib.abc.MetaPathFinder.find_module()` and
`importlib.abc.PathEntryFinder.find_module()` by the import system now
trigger an [`ImportWarning`](https://docs.python.org/3/library/exceptions.html#ImportWarning "ImportWarning") as
[`importlib.abc.MetaPathFinder.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec "importlib.abc.MetaPathFinder.find_spec") and
[`importlib.abc.PathEntryFinder.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder.find_spec "importlib.abc.PathEntryFinder.find_spec")
are preferred, respectively. You can use
[`importlib.util.spec_from_loader()`](https://docs.python.org/3/library/importlib.html#importlib.util.spec_from_loader "importlib.util.spec_from_loader") to help in porting.
(Contributed by Brett Cannon in [bpo-42134](https://bugs.python.org/issue?@action=redirect&bpo=42134).)

- The use of `importlib.abc.PathEntryFinder.find_loader()` by the import
system now triggers an [`ImportWarning`](https://docs.python.org/3/library/exceptions.html#ImportWarning "ImportWarning") as
[`importlib.abc.PathEntryFinder.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder.find_spec "importlib.abc.PathEntryFinder.find_spec") is preferred. You can use
[`importlib.util.spec_from_loader()`](https://docs.python.org/3/library/importlib.html#importlib.util.spec_from_loader "importlib.util.spec_from_loader") to help in porting.
(Contributed by Brett Cannon in [bpo-43672](https://bugs.python.org/issue?@action=redirect&bpo=43672).)

- The various implementations of
`importlib.abc.MetaPathFinder.find_module()` (
`importlib.machinery.BuiltinImporter.find_module()`,
`importlib.machinery.FrozenImporter.find_module()`,
`importlib.machinery.WindowsRegistryFinder.find_module()`,
`importlib.machinery.PathFinder.find_module()`,
`importlib.abc.MetaPathFinder.find_module()` ),
`importlib.abc.PathEntryFinder.find_module()` (
`importlib.machinery.FileFinder.find_module()` ), and
`importlib.abc.PathEntryFinder.find_loader()` (
`importlib.machinery.FileFinder.find_loader()` )
now raise [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") and are slated for removal in
Python 3.12 (previously they were documented as deprecated in Python 3.4).
(Contributed by Brett Cannon in [bpo-42135](https://bugs.python.org/issue?@action=redirect&bpo=42135).)

- `importlib.abc.Finder` is deprecated (including its sole method,
`find_module()`). Both
[`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder") and [`importlib.abc.PathEntryFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder "importlib.abc.PathEntryFinder")
no longer inherit from the class. Users should inherit from one of these two
classes as appropriate instead.
(Contributed by Brett Cannon in [bpo-42135](https://bugs.python.org/issue?@action=redirect&bpo=42135).)

- The deprecations of `imp`, `importlib.find_loader()`,
`importlib.util.set_package_wrapper()`,
`importlib.util.set_loader_wrapper()`,
`importlib.util.module_for_loader()`,
`pkgutil.ImpImporter`, and
`pkgutil.ImpLoader` have all been updated to list Python 3.12 as the
slated version of removal (they began raising [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") in
previous versions of Python).
(Contributed by Brett Cannon in [bpo-43720](https://bugs.python.org/issue?@action=redirect&bpo=43720).)

- The import system now uses the `__spec__` attribute on modules before
falling back on `module_repr()` for a module’s
`__repr__()` method. Removal of the use of `module_repr()` is scheduled
for Python 3.12.
(Contributed by Brett Cannon in [bpo-42137](https://bugs.python.org/issue?@action=redirect&bpo=42137).)

- `importlib.abc.Loader.module_repr()`,
`importlib.machinery.FrozenLoader.module_repr()`, and
`importlib.machinery.BuiltinLoader.module_repr()` are deprecated and
slated for removal in Python 3.12.
(Contributed by Brett Cannon in [bpo-42136](https://bugs.python.org/issue?@action=redirect&bpo=42136).)

- `sqlite3.OptimizedUnicode` has been undocumented and obsolete since Python
3.3, when it was made an alias to [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). It is now deprecated,
scheduled for removal in Python 3.12.
(Contributed by Erlend E. Aasland in [bpo-42264](https://bugs.python.org/issue?@action=redirect&bpo=42264).)

- The undocumented built-in function `sqlite3.enable_shared_cache` is now
deprecated, scheduled for removal in Python 3.12. Its use is strongly
discouraged by the SQLite3 documentation. See [the SQLite3 docs](https://sqlite.org/c3ref/enable_shared_cache.html) for more details.
If a shared cache must be used, open the database in URI mode using the
`cache=shared` query parameter.
(Contributed by Erlend E. Aasland in [bpo-24464](https://bugs.python.org/issue?@action=redirect&bpo=24464).)

- The following `threading` methods are now deprecated:


  - `threading.currentThread` =\> [`threading.current_thread()`](https://docs.python.org/3/library/threading.html#threading.current_thread "threading.current_thread")

  - `threading.activeCount` =\> [`threading.active_count()`](https://docs.python.org/3/library/threading.html#threading.active_count "threading.active_count")

  - `threading.Condition.notifyAll` =>
    [`threading.Condition.notify_all()`](https://docs.python.org/3/library/threading.html#threading.Condition.notify_all "threading.Condition.notify_all")

  - `threading.Event.isSet` =\> [`threading.Event.is_set()`](https://docs.python.org/3/library/threading.html#threading.Event.is_set "threading.Event.is_set")

  - `threading.Thread.setName` =\> [`threading.Thread.name`](https://docs.python.org/3/library/threading.html#threading.Thread.name "threading.Thread.name")

  - `threading.thread.getName` =\> [`threading.Thread.name`](https://docs.python.org/3/library/threading.html#threading.Thread.name "threading.Thread.name")

  - `threading.Thread.isDaemon` =\> [`threading.Thread.daemon`](https://docs.python.org/3/library/threading.html#threading.Thread.daemon "threading.Thread.daemon")

  - `threading.Thread.setDaemon` =\> [`threading.Thread.daemon`](https://docs.python.org/3/library/threading.html#threading.Thread.daemon "threading.Thread.daemon")


(Contributed by Jelle Zijlstra in [gh-87889](https://github.com/python/cpython/issues/87889).)

- `pathlib.Path.link_to()` is deprecated and slated for removal in
Python 3.12. Use [`pathlib.Path.hardlink_to()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.hardlink_to "pathlib.Path.hardlink_to") instead.
(Contributed by Barney Gale in [bpo-39950](https://bugs.python.org/issue?@action=redirect&bpo=39950).)

- `cgi.log()` is deprecated and slated for removal in Python 3.12.
(Contributed by Inada Naoki in [bpo-41139](https://bugs.python.org/issue?@action=redirect&bpo=41139).)

- The following [`ssl`](https://docs.python.org/3/library/ssl.html#module-ssl "ssl: TLS/SSL wrapper for socket objects") features have been deprecated since Python 3.6,
Python 3.7, or OpenSSL 1.1.0 and will be removed in 3.11:

  - `OP_NO_SSLv2`, `OP_NO_SSLv3`, `OP_NO_TLSv1`,
    `OP_NO_TLSv1_1`, `OP_NO_TLSv1_2`, and
    `OP_NO_TLSv1_3` are replaced by
    [`minimum_version`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.minimum_version "ssl.SSLContext.minimum_version") and
    [`maximum_version`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.maximum_version "ssl.SSLContext.maximum_version").

  - `PROTOCOL_SSLv2`, `PROTOCOL_SSLv3`,
    `PROTOCOL_SSLv23`, `PROTOCOL_TLSv1`,
    `PROTOCOL_TLSv1_1`, `PROTOCOL_TLSv1_2`, and
    `PROTOCOL_TLS` are deprecated in favor of
    [`PROTOCOL_TLS_CLIENT`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_CLIENT "ssl.PROTOCOL_TLS_CLIENT") and [`PROTOCOL_TLS_SERVER`](https://docs.python.org/3/library/ssl.html#ssl.PROTOCOL_TLS_SERVER "ssl.PROTOCOL_TLS_SERVER")

  - `wrap_socket()` is replaced by [`ssl.SSLContext.wrap_socket()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.wrap_socket "ssl.SSLContext.wrap_socket")

  - `match_hostname()`

  - `RAND_pseudo_bytes()`, `RAND_egd()`

  - NPN features like [`ssl.SSLSocket.selected_npn_protocol()`](https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.selected_npn_protocol "ssl.SSLSocket.selected_npn_protocol") and
    [`ssl.SSLContext.set_npn_protocols()`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext.set_npn_protocols "ssl.SSLContext.set_npn_protocols") are replaced by ALPN.
- The threading debug (`PYTHONTHREADDEBUG` environment variable) is
deprecated in Python 3.10 and will be removed in Python 3.12. This feature
requires a [debug build of Python](https://docs.python.org/3/using/configure.html#debug-build).
(Contributed by Victor Stinner in [bpo-44584](https://bugs.python.org/issue?@action=redirect&bpo=44584).)

- Importing from the `typing.io` and `typing.re` submodules will now emit
[`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning"). These submodules will be removed in a future version
of Python. Anything belonging to these submodules should be imported directly
from [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints (see :pep:`484`).") instead.
(Contributed by Sebastian Rittau in [bpo-38291](https://bugs.python.org/issue?@action=redirect&bpo=38291).)


## Removed [¶](https://docs.python.org/3/whatsnew/3.10.html\#removed "Link to this heading")

- Removed special methods `__int__`, `__float__`, `__floordiv__`,
`__mod__`, `__divmod__`, `__rfloordiv__`, `__rmod__` and
`__rdivmod__` of the [`complex`](https://docs.python.org/3/library/functions.html#complex "complex") class. They always raised
a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").
(Contributed by Serhiy Storchaka in [bpo-41974](https://bugs.python.org/issue?@action=redirect&bpo=41974).)

- The `ParserBase.error()` method from the private and undocumented `_markupbase`
module has been removed. [`html.parser.HTMLParser`](https://docs.python.org/3/library/html.parser.html#html.parser.HTMLParser "html.parser.HTMLParser") is the only subclass of
`ParserBase` and its `error()` implementation was already removed in
Python 3.5.
(Contributed by Berker Peksag in [bpo-31844](https://bugs.python.org/issue?@action=redirect&bpo=31844).)

- Removed the `unicodedata.ucnhash_CAPI` attribute which was an internal
PyCapsule object. The related private `_PyUnicode_Name_CAPI` structure was
moved to the internal C API.
(Contributed by Victor Stinner in [bpo-42157](https://bugs.python.org/issue?@action=redirect&bpo=42157).)

- Removed the `parser` module, which was deprecated in 3.9 due to the
switch to the new PEG parser, as well as all the C source and header files
that were only being used by the old parser, including `node.h`, `parser.h`,
`graminit.h` and `grammar.h`.

- Removed the Public C API functions `PyParser_SimpleParseStringFlags`,
`PyParser_SimpleParseStringFlagsFilename`,
`PyParser_SimpleParseFileFlags` and `PyNode_Compile`
that were deprecated in 3.9 due to the switch to the new PEG parser.

- Removed the `formatter` module, which was deprecated in Python 3.4.
It is somewhat obsolete, little used, and not tested. It was originally
scheduled to be removed in Python 3.6, but such removals were delayed until
after Python 2.7 EOL. Existing users should copy whatever classes they use
into their code.
(Contributed by Donghee Na and Terry J. Reedy in [bpo-42299](https://bugs.python.org/issue?@action=redirect&bpo=42299).)

- Removed the `PyModule_GetWarningsModule()` function that was useless
now due to the `_warnings` module was converted to a builtin module in 2.6.
(Contributed by Hai Shi in [bpo-42599](https://bugs.python.org/issue?@action=redirect&bpo=42599).)

- Remove deprecated aliases to [Collections Abstract Base Classes](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes) from
the [`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes") module.
(Contributed by Victor Stinner in [bpo-37324](https://bugs.python.org/issue?@action=redirect&bpo=37324).)

- The `loop` parameter has been removed from most of [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")‘s
[high-level API](https://docs.python.org/3/library/asyncio-api-index.html) following deprecation
in Python 3.8. The motivation behind this change is multifold:


1. This simplifies the high-level API.

2. The functions in the high-level API have been implicitly getting the
     current thread’s running event loop since Python 3.7. There isn’t a need to
     pass the event loop to the API in most normal use cases.

3. Event loop passing is error-prone especially when dealing with loops
     running in different threads.


Note that the low-level API will still accept `loop`.
See [Changes in the Python API](https://docs.python.org/3/whatsnew/3.10.html#changes-python-api) for examples of how to replace existing code.

(Contributed by Yurii Karabas, Andrew Svetlov, Yury Selivanov and Kyle Stanley
in [bpo-42392](https://bugs.python.org/issue?@action=redirect&bpo=42392).)

## Porting to Python 3.10 [¶](https://docs.python.org/3/whatsnew/3.10.html\#porting-to-python-3-10 "Link to this heading")

This section lists previously described changes and other bugfixes
that may require changes to your code.

### Changes in the Python syntax [¶](https://docs.python.org/3/whatsnew/3.10.html\#changes-in-the-python-syntax "Link to this heading")

- Deprecation warning is now emitted when compiling previously valid syntax
if the numeric literal is immediately followed by a keyword (like in `0in x`).
In future releases it will be changed to syntax warning, and finally to a
syntax error. To get rid of the warning and make the code compatible with
future releases just add a space between the numeric literal and the
following keyword.
(Contributed by Serhiy Storchaka in [bpo-43833](https://bugs.python.org/issue?@action=redirect&bpo=43833).)


### Changes in the Python API [¶](https://docs.python.org/3/whatsnew/3.10.html\#changes-in-the-python-api "Link to this heading")

- The _etype_ parameters of the [`format_exception()`](https://docs.python.org/3/library/traceback.html#traceback.format_exception "traceback.format_exception"),
[`format_exception_only()`](https://docs.python.org/3/library/traceback.html#traceback.format_exception_only "traceback.format_exception_only"), and
[`print_exception()`](https://docs.python.org/3/library/traceback.html#traceback.print_exception "traceback.print_exception") functions in the [`traceback`](https://docs.python.org/3/library/traceback.html#module-traceback "traceback: Print or retrieve a stack traceback.") module
have been renamed to _exc_.
(Contributed by Zackery Spytz and Matthias Bussonnier in [bpo-26389](https://bugs.python.org/issue?@action=redirect&bpo=26389).)

- [`atexit`](https://docs.python.org/3/library/atexit.html#module-atexit "atexit: Register and execute cleanup functions."): At Python exit, if a callback registered with
[`atexit.register()`](https://docs.python.org/3/library/atexit.html#atexit.register "atexit.register") fails, its exception is now logged. Previously, only
some exceptions were logged, and the last exception was always silently
ignored.
(Contributed by Victor Stinner in [bpo-42639](https://bugs.python.org/issue?@action=redirect&bpo=42639).)

- [`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") generic now flattens type parameters, similar
to what [`typing.Callable`](https://docs.python.org/3/library/typing.html#typing.Callable "typing.Callable") currently does. This means that
`collections.abc.Callable[[int, str], str]` will have `__args__` of
`(int, str, str)`; previously this was `([int, str], str)`. Code which
accesses the arguments via [`typing.get_args()`](https://docs.python.org/3/library/typing.html#typing.get_args "typing.get_args") or `__args__` need to account
for this change. Furthermore, [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") may be raised for invalid forms
of parameterizing [`collections.abc.Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") which may have passed
silently in Python 3.9.
(Contributed by Ken Jin in [bpo-42195](https://bugs.python.org/issue?@action=redirect&bpo=42195).)

- [`socket.htons()`](https://docs.python.org/3/library/socket.html#socket.htons "socket.htons") and [`socket.ntohs()`](https://docs.python.org/3/library/socket.html#socket.ntohs "socket.ntohs") now raise [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError")
instead of [`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning") if the given parameter will not fit in
a 16-bit unsigned integer.
(Contributed by Erlend E. Aasland in [bpo-42393](https://bugs.python.org/issue?@action=redirect&bpo=42393).)

- The `loop` parameter has been removed from most of [`asyncio`](https://docs.python.org/3/library/asyncio.html#module-asyncio "asyncio: Asynchronous I/O.")‘s
[high-level API](https://docs.python.org/3/library/asyncio-api-index.html) following deprecation
in Python 3.8.

A coroutine that currently looks like this:



Copy

```
async def foo(loop):
      await asyncio.sleep(1, loop=loop)
```





Should be replaced with this:



Copy

```
async def foo():
      await asyncio.sleep(1)
```





If `foo()` was specifically designed _not_ to run in the current thread’s
running event loop (e.g. running in another thread’s event loop), consider
using [`asyncio.run_coroutine_threadsafe()`](https://docs.python.org/3/library/asyncio-task.html#asyncio.run_coroutine_threadsafe "asyncio.run_coroutine_threadsafe") instead.

(Contributed by Yurii Karabas, Andrew Svetlov, Yury Selivanov and Kyle Stanley
in [bpo-42392](https://bugs.python.org/issue?@action=redirect&bpo=42392).)

- The [`types.FunctionType`](https://docs.python.org/3/library/types.html#types.FunctionType "types.FunctionType") constructor now inherits the current builtins
if the _globals_ dictionary has no `"__builtins__"` key, rather than using
`{"None": None}` as builtins: same behavior as [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval") and
[`exec()`](https://docs.python.org/3/library/functions.html#exec "exec") functions. Defining a function with `def function(...): ...`
in Python is not affected, globals cannot be overridden with this syntax: it
also inherits the current builtins.
(Contributed by Victor Stinner in [bpo-42990](https://bugs.python.org/issue?@action=redirect&bpo=42990).)


### Changes in the C API [¶](https://docs.python.org/3/whatsnew/3.10.html\#changes-in-the-c-api "Link to this heading")

- The C API functions `PyParser_SimpleParseStringFlags`,
`PyParser_SimpleParseStringFlagsFilename`,
`PyParser_SimpleParseFileFlags`, `PyNode_Compile` and the type
used by these functions, `struct _node`, were removed due to the switch
to the new PEG parser.

Source should be now be compiled directly to a code object using, for
example, [`Py_CompileString()`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileString "Py_CompileString"). The resulting code object can then be
evaluated using, for example, [`PyEval_EvalCode()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_EvalCode "PyEval_EvalCode").

Specifically:

  - A call to `PyParser_SimpleParseStringFlags` followed by
    `PyNode_Compile` can be replaced by calling [`Py_CompileString()`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileString "Py_CompileString").

  - There is no direct replacement for `PyParser_SimpleParseFileFlags`.
    To compile code from a `FILE *` argument, you will need to read
    the file in C and pass the resulting buffer to [`Py_CompileString()`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileString "Py_CompileString").

  - To compile a file given a `char *` filename, explicitly open the file, read
    it and compile the result. One way to do this is using the [`io`](https://docs.python.org/3/library/io.html#module-io "io: Core tools for working with streams.")
    module with [`PyImport_ImportModule()`](https://docs.python.org/3/c-api/import.html#c.PyImport_ImportModule "PyImport_ImportModule"), [`PyObject_CallMethod()`](https://docs.python.org/3/c-api/call.html#c.PyObject_CallMethod "PyObject_CallMethod"),
    [`PyBytes_AsString()`](https://docs.python.org/3/c-api/bytes.html#c.PyBytes_AsString "PyBytes_AsString") and [`Py_CompileString()`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileString "Py_CompileString"),
    as sketched below. (Declarations and error handling are omitted.)



    Copy

    ```
    io_module = Import_ImportModule("io");
    fileobject = PyObject_CallMethod(io_module, "open", "ss", filename, "rb");
    source_bytes_object = PyObject_CallMethod(fileobject, "read", "");
    result = PyObject_CallMethod(fileobject, "close", "");
    source_buf = PyBytes_AsString(source_bytes_object);
    code = Py_CompileString(source_buf, filename, Py_file_input);
    ```

  - For `FrameObject` objects, the [`f_lasti`](https://docs.python.org/3/reference/datamodel.html#frame.f_lasti "frame.f_lasti") member now represents a wordcode
    offset instead of a simple offset into the bytecode string. This means that this
    number needs to be multiplied by 2 to be used with APIs that expect a byte offset
    instead (like [`PyCode_Addr2Line()`](https://docs.python.org/3/c-api/code.html#c.PyCode_Addr2Line "PyCode_Addr2Line") for example). Notice as well that the
    `f_lasti` member of `FrameObject` objects is not considered stable: please
    use [`PyFrame_GetLineNumber()`](https://docs.python.org/3/c-api/frame.html#c.PyFrame_GetLineNumber "PyFrame_GetLineNumber") instead.

## CPython bytecode changes [¶](https://docs.python.org/3/whatsnew/3.10.html\#cpython-bytecode-changes "Link to this heading")

- The `MAKE_FUNCTION` instruction now accepts either a dict or a tuple of
strings as the function’s annotations.
(Contributed by Yurii Karabas and Inada Naoki in [bpo-42202](https://bugs.python.org/issue?@action=redirect&bpo=42202).)


## Build Changes [¶](https://docs.python.org/3/whatsnew/3.10.html\#build-changes "Link to this heading")

- [**PEP 644**](https://peps.python.org/pep-0644/): Python now requires OpenSSL 1.1.1 or newer. OpenSSL 1.0.2 is no
longer supported.
(Contributed by Christian Heimes in [bpo-43669](https://bugs.python.org/issue?@action=redirect&bpo=43669).)

- The C99 functions `snprintf()` and `vsnprintf()` are now required
to build Python.
(Contributed by Victor Stinner in [bpo-36020](https://bugs.python.org/issue?@action=redirect&bpo=36020).)

- [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.") requires SQLite 3.7.15 or higher. (Contributed by Sergey Fedoseev
and Erlend E. Aasland in [bpo-40744](https://bugs.python.org/issue?@action=redirect&bpo=40744) and [bpo-40810](https://bugs.python.org/issue?@action=redirect&bpo=40810).)

- The [`atexit`](https://docs.python.org/3/library/atexit.html#module-atexit "atexit: Register and execute cleanup functions.") module must now always be built as a built-in module.
(Contributed by Victor Stinner in [bpo-42639](https://bugs.python.org/issue?@action=redirect&bpo=42639).)

- Add [`--disable-test-modules`](https://docs.python.org/3/using/configure.html#cmdoption-disable-test-modules) option to the `configure` script:
don’t build nor install test modules.
(Contributed by Xavier de Gaye, Thomas Petazzoni and Peixing Xin in [bpo-27640](https://bugs.python.org/issue?@action=redirect&bpo=27640).)

- Add [`--with-wheel-pkg-dir=PATH option`](https://docs.python.org/3/using/configure.html#cmdoption-with-wheel-pkg-dir)
to the `./configure` script. If
specified, the [`ensurepip`](https://docs.python.org/3/library/ensurepip.html#module-ensurepip "ensurepip: Bootstrapping the \"pip\" installer into an existing Python installation or virtual environment.") module looks for `setuptools` and `pip`
wheel packages in this directory: if both are present, these wheel packages
are used instead of ensurepip bundled wheel packages.

Some Linux distribution packaging policies recommend against bundling
dependencies. For example, Fedora installs wheel packages in the
`/usr/share/python-wheels/` directory and don’t install the
`ensurepip._bundled` package.

(Contributed by Victor Stinner in [bpo-42856](https://bugs.python.org/issue?@action=redirect&bpo=42856).)

- Add a new [`configure --without-static-libpython option`](https://docs.python.org/3/using/configure.html#cmdoption-without-static-libpython) to not build the `libpythonMAJOR.MINOR.a`
static library and not install the `python.o` object file.

(Contributed by Victor Stinner in [bpo-43103](https://bugs.python.org/issue?@action=redirect&bpo=43103).)

- The `configure` script now uses the `pkg-config` utility, if available,
to detect the location of Tcl/Tk headers and libraries. As before, those
locations can be explicitly specified with the `--with-tcltk-includes`
and `--with-tcltk-libs` configuration options.
(Contributed by Manolis Stamatogiannakis in [bpo-42603](https://bugs.python.org/issue?@action=redirect&bpo=42603).)

- Add [`--with-openssl-rpath`](https://docs.python.org/3/using/configure.html#cmdoption-with-openssl-rpath) option to `configure` script. The option
simplifies building Python with a custom OpenSSL installation, e.g.
`./configure --with-openssl=/path/to/openssl --with-openssl-rpath=auto`.
(Contributed by Christian Heimes in [bpo-43466](https://bugs.python.org/issue?@action=redirect&bpo=43466).)


## C API Changes [¶](https://docs.python.org/3/whatsnew/3.10.html\#c-api-changes "Link to this heading")

### PEP 652: Maintaining the Stable ABI [¶](https://docs.python.org/3/whatsnew/3.10.html\#pep-652-maintaining-the-stable-abi "Link to this heading")

The Stable ABI (Application Binary Interface) for extension modules or
embedding Python is now explicitly defined.
[C API Stability](https://docs.python.org/3/c-api/stable.html#stable) describes C API and ABI stability guarantees along with best
practices for using the Stable ABI.

(Contributed by Petr Viktorin in [**PEP 652**](https://peps.python.org/pep-0652/) and [bpo-43795](https://bugs.python.org/issue?@action=redirect&bpo=43795).)

### New Features [¶](https://docs.python.org/3/whatsnew/3.10.html\#id1 "Link to this heading")

- The result of [`PyNumber_Index()`](https://docs.python.org/3/c-api/number.html#c.PyNumber_Index "PyNumber_Index") now always has exact type [`int`](https://docs.python.org/3/library/functions.html#int "int").
Previously, the result could have been an instance of a subclass of `int`.
(Contributed by Serhiy Storchaka in [bpo-40792](https://bugs.python.org/issue?@action=redirect&bpo=40792).)

- Add a new [`orig_argv`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.orig_argv "PyConfig.orig_argv") member to the [`PyConfig`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig "PyConfig")
structure: the list of the original command line arguments passed to the
Python executable.
(Contributed by Victor Stinner in [bpo-23427](https://bugs.python.org/issue?@action=redirect&bpo=23427).)

- The [`PyDateTime_DATE_GET_TZINFO()`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_DATE_GET_TZINFO "PyDateTime_DATE_GET_TZINFO") and
[`PyDateTime_TIME_GET_TZINFO()`](https://docs.python.org/3/c-api/datetime.html#c.PyDateTime_TIME_GET_TZINFO "PyDateTime_TIME_GET_TZINFO") macros have been added for accessing
the `tzinfo` attributes of [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") and
[`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") objects.
(Contributed by Zackery Spytz in [bpo-30155](https://bugs.python.org/issue?@action=redirect&bpo=30155).)

- Add a [`PyCodec_Unregister()`](https://docs.python.org/3/c-api/codec.html#c.PyCodec_Unregister "PyCodec_Unregister") function to unregister a codec
search function.
(Contributed by Hai Shi in [bpo-41842](https://bugs.python.org/issue?@action=redirect&bpo=41842).)

- The [`PyIter_Send()`](https://docs.python.org/3/c-api/iter.html#c.PyIter_Send "PyIter_Send") function was added to allow
sending value into iterator without raising `StopIteration` exception.
(Contributed by Vladimir Matveev in [bpo-41756](https://bugs.python.org/issue?@action=redirect&bpo=41756).)

- Add [`PyUnicode_AsUTF8AndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize "PyUnicode_AsUTF8AndSize") to the limited C API.
(Contributed by Alex Gaynor in [bpo-41784](https://bugs.python.org/issue?@action=redirect&bpo=41784).)

- Add [`PyModule_AddObjectRef()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObjectRef "PyModule_AddObjectRef") function: similar to
[`PyModule_AddObject()`](https://docs.python.org/3/c-api/module.html#c.PyModule_AddObject "PyModule_AddObject") but don’t steal a reference to the value on
success.
(Contributed by Victor Stinner in [bpo-1635741](https://bugs.python.org/issue?@action=redirect&bpo=1635741).)

- Add [`Py_NewRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_NewRef "Py_NewRef") and [`Py_XNewRef()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_XNewRef "Py_XNewRef") functions to increment the
reference count of an object and return the object.
(Contributed by Victor Stinner in [bpo-42262](https://bugs.python.org/issue?@action=redirect&bpo=42262).)

- The [`PyType_FromSpecWithBases()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromSpecWithBases "PyType_FromSpecWithBases") and [`PyType_FromModuleAndSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromModuleAndSpec "PyType_FromModuleAndSpec")
functions now accept a single class as the _bases_ argument.
(Contributed by Serhiy Storchaka in [bpo-42423](https://bugs.python.org/issue?@action=redirect&bpo=42423).)

- The [`PyType_FromModuleAndSpec()`](https://docs.python.org/3/c-api/type.html#c.PyType_FromModuleAndSpec "PyType_FromModuleAndSpec") function now accepts NULL `tp_doc`
slot.
(Contributed by Hai Shi in [bpo-41832](https://bugs.python.org/issue?@action=redirect&bpo=41832).)

- The [`PyType_GetSlot()`](https://docs.python.org/3/c-api/type.html#c.PyType_GetSlot "PyType_GetSlot") function can accept
[static types](https://docs.python.org/3/c-api/typeobj.html#static-types).
(Contributed by Hai Shi and Petr Viktorin in [bpo-41073](https://bugs.python.org/issue?@action=redirect&bpo=41073).)

- Add a new [`PySet_CheckExact()`](https://docs.python.org/3/c-api/set.html#c.PySet_CheckExact "PySet_CheckExact") function to the C-API to check if an
object is an instance of [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") but not an instance of a subtype.
(Contributed by Pablo Galindo in [bpo-43277](https://bugs.python.org/issue?@action=redirect&bpo=43277).)

- Add [`PyErr_SetInterruptEx()`](https://docs.python.org/3/c-api/exceptions.html#c.PyErr_SetInterruptEx "PyErr_SetInterruptEx") which allows passing a signal number
to simulate.
(Contributed by Antoine Pitrou in [bpo-43356](https://bugs.python.org/issue?@action=redirect&bpo=43356).)

- The limited C API is now supported if [Python is built in debug mode](https://docs.python.org/3/using/configure.html#debug-build) (if the `Py_DEBUG` macro is defined). In the limited C API,
the [`Py_INCREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_INCREF "Py_INCREF") and [`Py_DECREF()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_DECREF "Py_DECREF") functions are now implemented
as opaque function
calls, rather than accessing directly the [`PyObject.ob_refcnt`](https://docs.python.org/3/c-api/structures.html#c.PyObject.ob_refcnt "PyObject.ob_refcnt")
member, if Python is built in debug mode and the `Py_LIMITED_API` macro
targets Python 3.10 or newer. It became possible to support the limited C API
in debug mode because the [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject") structure is the same in release
and debug mode since Python 3.8 (see [bpo-36465](https://bugs.python.org/issue?@action=redirect&bpo=36465)).

The limited C API is still not supported in the [`--with-trace-refs`](https://docs.python.org/3/using/configure.html#cmdoption-with-trace-refs)
special build (`Py_TRACE_REFS` macro).
(Contributed by Victor Stinner in [bpo-43688](https://bugs.python.org/issue?@action=redirect&bpo=43688).)

- Add the [`Py_Is(x, y)`](https://docs.python.org/3/c-api/structures.html#c.Py_Is "Py_Is") function to test if the _x_ object is
the _y_ object, the same as `x is y` in Python. Add also the
[`Py_IsNone()`](https://docs.python.org/3/c-api/structures.html#c.Py_IsNone "Py_IsNone"), [`Py_IsTrue()`](https://docs.python.org/3/c-api/structures.html#c.Py_IsTrue "Py_IsTrue"), [`Py_IsFalse()`](https://docs.python.org/3/c-api/structures.html#c.Py_IsFalse "Py_IsFalse") functions to
test if an object is, respectively, the `None` singleton, the `True`
singleton or the `False` singleton.
(Contributed by Victor Stinner in [bpo-43753](https://bugs.python.org/issue?@action=redirect&bpo=43753).)

- Add new functions to control the garbage collector from C code:
[`PyGC_Enable()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyGC_Enable "PyGC_Enable"),
[`PyGC_Disable()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyGC_Disable "PyGC_Disable"),
[`PyGC_IsEnabled()`](https://docs.python.org/3/c-api/gcsupport.html#c.PyGC_IsEnabled "PyGC_IsEnabled").
These functions allow to activate, deactivate and query the state of the garbage collector from C code without
having to import the [`gc`](https://docs.python.org/3/library/gc.html#module-gc "gc: Interface to the cycle-detecting garbage collector.") module.

- Add a new [`Py_TPFLAGS_DISALLOW_INSTANTIATION`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_DISALLOW_INSTANTIATION "Py_TPFLAGS_DISALLOW_INSTANTIATION") type flag to disallow
creating type instances.
(Contributed by Victor Stinner in [bpo-43916](https://bugs.python.org/issue?@action=redirect&bpo=43916).)

- Add a new [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE "Py_TPFLAGS_IMMUTABLETYPE") type flag for creating immutable
type objects: type attributes cannot be set nor deleted.
(Contributed by Victor Stinner and Erlend E. Aasland in [bpo-43908](https://bugs.python.org/issue?@action=redirect&bpo=43908).)


### Porting to Python 3.10 [¶](https://docs.python.org/3/whatsnew/3.10.html\#id2 "Link to this heading")

- The `PY_SSIZE_T_CLEAN` macro must now be defined to use
[`PyArg_ParseTuple()`](https://docs.python.org/3/c-api/arg.html#c.PyArg_ParseTuple "PyArg_ParseTuple") and [`Py_BuildValue()`](https://docs.python.org/3/c-api/arg.html#c.Py_BuildValue "Py_BuildValue") formats which use
`#`: `es#`, `et#`, `s#`, `u#`, `y#`, `z#`, `U#` and `Z#`.
See [Parsing arguments and building values](https://docs.python.org/3/c-api/arg.html#arg-parsing) and [**PEP 353**](https://peps.python.org/pep-0353/).
(Contributed by Victor Stinner in [bpo-40943](https://bugs.python.org/issue?@action=redirect&bpo=40943).)

- Since [`Py_REFCNT()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_REFCNT "Py_REFCNT") is changed to the inline static function,
`Py_REFCNT(obj) = new_refcnt` must be replaced with `Py_SET_REFCNT(obj, new_refcnt)`:
see [`Py_SET_REFCNT()`](https://docs.python.org/3/c-api/refcounting.html#c.Py_SET_REFCNT "Py_SET_REFCNT") (available since Python 3.9). For backward
compatibility, this macro can be used:



Copy

```
#if PY_VERSION_HEX < 0x030900A4
#  define Py_SET_REFCNT(obj, refcnt) ((Py_REFCNT(obj) = (refcnt)), (void)0)
#endif
```





(Contributed by Victor Stinner in [bpo-39573](https://bugs.python.org/issue?@action=redirect&bpo=39573).)

- Calling [`PyDict_GetItem()`](https://docs.python.org/3/c-api/dict.html#c.PyDict_GetItem "PyDict_GetItem") without [GIL](https://docs.python.org/3/glossary.html#term-GIL) held had been allowed
for historical reason. It is no longer allowed.
(Contributed by Victor Stinner in [bpo-40839](https://bugs.python.org/issue?@action=redirect&bpo=40839).)

- `PyUnicode_FromUnicode(NULL, size)` and `PyUnicode_FromStringAndSize(NULL, size)`
raise `DeprecationWarning` now. Use [`PyUnicode_New()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_New "PyUnicode_New") to allocate
Unicode object without initial data.
(Contributed by Inada Naoki in [bpo-36346](https://bugs.python.org/issue?@action=redirect&bpo=36346).)

- The private `_PyUnicode_Name_CAPI` structure of the PyCapsule API
`unicodedata.ucnhash_CAPI` has been moved to the internal C API.
(Contributed by Victor Stinner in [bpo-42157](https://bugs.python.org/issue?@action=redirect&bpo=42157).)

- [`Py_GetPath()`](https://docs.python.org/3/c-api/init.html#c.Py_GetPath "Py_GetPath"), [`Py_GetPrefix()`](https://docs.python.org/3/c-api/init.html#c.Py_GetPrefix "Py_GetPrefix"), [`Py_GetExecPrefix()`](https://docs.python.org/3/c-api/init.html#c.Py_GetExecPrefix "Py_GetExecPrefix"),
[`Py_GetProgramFullPath()`](https://docs.python.org/3/c-api/init.html#c.Py_GetProgramFullPath "Py_GetProgramFullPath"), [`Py_GetPythonHome()`](https://docs.python.org/3/c-api/init.html#c.Py_GetPythonHome "Py_GetPythonHome") and
[`Py_GetProgramName()`](https://docs.python.org/3/c-api/init.html#c.Py_GetProgramName "Py_GetProgramName") functions now return `NULL` if called before
[`Py_Initialize()`](https://docs.python.org/3/c-api/init.html#c.Py_Initialize "Py_Initialize") (before Python is initialized). Use the new
[Python Initialization Configuration](https://docs.python.org/3/c-api/init_config.html#init-config) API to get the [Python Path Configuration](https://docs.python.org/3/c-api/init_config.html#init-path-config).
(Contributed by Victor Stinner in [bpo-42260](https://bugs.python.org/issue?@action=redirect&bpo=42260).)

- [`PyList_SET_ITEM()`](https://docs.python.org/3/c-api/list.html#c.PyList_SET_ITEM "PyList_SET_ITEM"), [`PyTuple_SET_ITEM()`](https://docs.python.org/3/c-api/tuple.html#c.PyTuple_SET_ITEM "PyTuple_SET_ITEM") and
[`PyCell_SET()`](https://docs.python.org/3/c-api/cell.html#c.PyCell_SET "PyCell_SET") macros can no longer be used as l-value or r-value.
For example, `x = PyList_SET_ITEM(a, b, c)` and
`PyList_SET_ITEM(a, b, c) = x` now fail with a compiler error. It prevents
bugs like `if (PyList_SET_ITEM (a, b, c) < 0) ...` test.
(Contributed by Zackery Spytz and Victor Stinner in [bpo-30459](https://bugs.python.org/issue?@action=redirect&bpo=30459).)

- The non-limited API files `odictobject.h`, `parser_interface.h`,
`picklebufobject.h`, `pyarena.h`, `pyctype.h`, `pydebug.h`,
`pyfpe.h`, and `pytime.h` have been moved to the `Include/cpython`
directory. These files must not be included directly, as they are already
included in `Python.h`; see [Include Files](https://docs.python.org/3/c-api/intro.html#api-includes). If they have
been included directly, consider including `Python.h` instead.
(Contributed by Nicholas Sim in [bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134).)

- Use the [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE "Py_TPFLAGS_IMMUTABLETYPE") type flag to create immutable type
objects. Do not rely on [`Py_TPFLAGS_HEAPTYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_HEAPTYPE "Py_TPFLAGS_HEAPTYPE") to decide if a type
object is mutable or not; check if [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE "Py_TPFLAGS_IMMUTABLETYPE") is set
instead.
(Contributed by Victor Stinner and Erlend E. Aasland in [bpo-43908](https://bugs.python.org/issue?@action=redirect&bpo=43908).)

- The undocumented function `Py_FrozenMain` has been removed from the
limited API. The function is mainly useful for custom builds of Python.
(Contributed by Petr Viktorin in [bpo-26241](https://bugs.python.org/issue?@action=redirect&bpo=26241).)


### Deprecated [¶](https://docs.python.org/3/whatsnew/3.10.html\#id3 "Link to this heading")

- The `PyUnicode_InternImmortal()` function is now deprecated
and will be removed in Python 3.12: use [`PyUnicode_InternInPlace()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_InternInPlace "PyUnicode_InternInPlace")
instead.
(Contributed by Victor Stinner in [bpo-41692](https://bugs.python.org/issue?@action=redirect&bpo=41692).)


### Removed [¶](https://docs.python.org/3/whatsnew/3.10.html\#id4 "Link to this heading")

- Removed `Py_UNICODE_str*` functions manipulating `Py_UNICODE*` strings.
(Contributed by Inada Naoki in [bpo-41123](https://bugs.python.org/issue?@action=redirect&bpo=41123).)

  - `Py_UNICODE_strlen`: use [`PyUnicode_GetLength()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GetLength "PyUnicode_GetLength") or
    [`PyUnicode_GET_LENGTH`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_GET_LENGTH "PyUnicode_GET_LENGTH")

  - `Py_UNICODE_strcat`: use [`PyUnicode_CopyCharacters()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CopyCharacters "PyUnicode_CopyCharacters") or
    [`PyUnicode_FromFormat()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FromFormat "PyUnicode_FromFormat")

  - `Py_UNICODE_strcpy`, `Py_UNICODE_strncpy`: use
    [`PyUnicode_CopyCharacters()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_CopyCharacters "PyUnicode_CopyCharacters") or [`PyUnicode_Substring()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Substring "PyUnicode_Substring")

  - `Py_UNICODE_strcmp`: use [`PyUnicode_Compare()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Compare "PyUnicode_Compare")

  - `Py_UNICODE_strncmp`: use [`PyUnicode_Tailmatch()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_Tailmatch "PyUnicode_Tailmatch")

  - `Py_UNICODE_strchr`, `Py_UNICODE_strrchr`: use
    [`PyUnicode_FindChar()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_FindChar "PyUnicode_FindChar")
- Removed `PyUnicode_GetMax()`. Please migrate to new ( [**PEP 393**](https://peps.python.org/pep-0393/)) APIs.
(Contributed by Inada Naoki in [bpo-41103](https://bugs.python.org/issue?@action=redirect&bpo=41103).)

- Removed `PyLong_FromUnicode()`. Please migrate to [`PyLong_FromUnicodeObject()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromUnicodeObject "PyLong_FromUnicodeObject").
(Contributed by Inada Naoki in [bpo-41103](https://bugs.python.org/issue?@action=redirect&bpo=41103).)

- Removed `PyUnicode_AsUnicodeCopy()`. Please use [`PyUnicode_AsUCS4Copy()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUCS4Copy "PyUnicode_AsUCS4Copy") or
[`PyUnicode_AsWideCharString()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsWideCharString "PyUnicode_AsWideCharString")
(Contributed by Inada Naoki in [bpo-41103](https://bugs.python.org/issue?@action=redirect&bpo=41103).)

- Removed `_Py_CheckRecursionLimit` variable: it has been replaced by
`ceval.recursion_limit` of the [`PyInterpreterState`](https://docs.python.org/3/c-api/init.html#c.PyInterpreterState "PyInterpreterState") structure.
(Contributed by Victor Stinner in [bpo-41834](https://bugs.python.org/issue?@action=redirect&bpo=41834).)

- Removed undocumented macros `Py_ALLOW_RECURSION` and
`Py_END_ALLOW_RECURSION` and the `recursion_critical` field of the
[`PyInterpreterState`](https://docs.python.org/3/c-api/init.html#c.PyInterpreterState "PyInterpreterState") structure.
(Contributed by Serhiy Storchaka in [bpo-41936](https://bugs.python.org/issue?@action=redirect&bpo=41936).)

- Removed the undocumented `PyOS_InitInterrupts()` function. Initializing
Python already implicitly installs signal handlers: see
[`PyConfig.install_signal_handlers`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.install_signal_handlers "PyConfig.install_signal_handlers").
(Contributed by Victor Stinner in [bpo-41713](https://bugs.python.org/issue?@action=redirect&bpo=41713).)

- Remove the `PyAST_Validate()` function. It is no longer possible to build a
AST object (`mod_ty` type) with the public C API. The function was already
excluded from the limited C API ( [**PEP 384**](https://peps.python.org/pep-0384/)).
(Contributed by Victor Stinner in [bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244).)

- Remove the `symtable.h` header file and the undocumented functions:


  - `PyST_GetScope()`

  - `PySymtable_Build()`

  - `PySymtable_BuildObject()`

  - `PySymtable_Free()`

  - `Py_SymtableString()`

  - `Py_SymtableStringObject()`


The `Py_SymtableString()` function was part the stable ABI by mistake but
it could not be used, because the `symtable.h` header file was excluded
from the limited C API.

Use Python [`symtable`](https://docs.python.org/3/library/symtable.html#module-symtable "symtable: Interface to the compiler's internal symbol tables.") module instead.
(Contributed by Victor Stinner in [bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244).)

- Remove [`PyOS_ReadlineFunctionPointer()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_ReadlineFunctionPointer "PyOS_ReadlineFunctionPointer") from the limited C API headers
and from `python3.dll`, the library that provides the stable ABI on
Windows. Since the function takes a `FILE*` argument, its ABI stability
cannot be guaranteed.
(Contributed by Petr Viktorin in [bpo-43868](https://bugs.python.org/issue?@action=redirect&bpo=43868).)

- Remove `ast.h`, `asdl.h`, and `Python-ast.h` header files.
These functions were undocumented and excluded from the limited C API.
Most names defined by these header files were not prefixed by `Py` and so
could create names conflicts. For example, `Python-ast.h` defined a
`Yield` macro which was conflict with the `Yield` name used by the
Windows `<winbase.h>` header. Use the Python [`ast`](https://docs.python.org/3/library/ast.html#module-ast "ast: Abstract Syntax Tree classes and manipulation.") module instead.
(Contributed by Victor Stinner in [bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244).)

- Remove the compiler and parser functions using `struct _mod` type, because
the public AST C API was removed:


  - `PyAST_Compile()`

  - `PyAST_CompileEx()`

  - `PyAST_CompileObject()`

  - `PyFuture_FromAST()`

  - `PyFuture_FromASTObject()`

  - `PyParser_ASTFromFile()`

  - `PyParser_ASTFromFileObject()`

  - `PyParser_ASTFromFilename()`

  - `PyParser_ASTFromString()`

  - `PyParser_ASTFromStringObject()`


These functions were undocumented and excluded from the limited C API.
(Contributed by Victor Stinner in [bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244).)

- Remove the `pyarena.h` header file with functions:


  - `PyArena_New()`

  - `PyArena_Free()`

  - `PyArena_Malloc()`

  - `PyArena_AddPyObject()`


These functions were undocumented, excluded from the limited C API, and were
only used internally by the compiler.
(Contributed by Victor Stinner in [bpo-43244](https://bugs.python.org/issue?@action=redirect&bpo=43244).)

- The `PyThreadState.use_tracing` member has been removed to optimize Python.
(Contributed by Mark Shannon in [bpo-43760](https://bugs.python.org/issue?@action=redirect&bpo=43760).)


## Notable security feature in 3.10.7 [¶](https://docs.python.org/3/whatsnew/3.10.html\#notable-security-feature-in-3-10-7 "Link to this heading")

Converting between [`int`](https://docs.python.org/3/library/functions.html#int "int") and [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") in bases other than 2
(binary), 4, 8 (octal), 16 (hexadecimal), or 32 such as base 10 (decimal)
now raises a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the number of digits in string form is
above a limit to avoid potential denial of service attacks due to the
algorithmic complexity. This is a mitigation for [**CVE 2020-10735**](https://www.cve.org/CVERecord?id=CVE-2020-10735).
This limit can be configured or disabled by environment variable, command
line flag, or [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions.") APIs. See the [integer string conversion\\
length limitation](https://docs.python.org/3/library/stdtypes.html#int-max-str-digits) documentation. The default limit
is 4300 digits in string form.

## Notable security feature in 3.10.8 [¶](https://docs.python.org/3/whatsnew/3.10.html\#notable-security-feature-in-3-10-8 "Link to this heading")

The deprecated `mailcap` module now refuses to inject unsafe text
(filenames, MIME types, parameters) into shell commands. Instead of using such
text, it will warn and act as if a match was not found (or for test commands,
as if the test failed).
(Contributed by Petr Viktorin in [gh-98966](https://github.com/python/cpython/issues/98966).)

## Notable changes in 3.10.12 [¶](https://docs.python.org/3/whatsnew/3.10.html\#notable-changes-in-3-10-12 "Link to this heading")

### tarfile [¶](https://docs.python.org/3/whatsnew/3.10.html\#tarfile "Link to this heading")

- The extraction methods in [`tarfile`](https://docs.python.org/3/library/tarfile.html#module-tarfile "tarfile: Read and write tar-format archive files."), and [`shutil.unpack_archive()`](https://docs.python.org/3/library/shutil.html#shutil.unpack_archive "shutil.unpack_archive"),
have a new a _filter_ argument that allows limiting tar features than may be
surprising or dangerous, such as creating files outside the destination
directory.
See [Extraction filters](https://docs.python.org/3/library/tarfile.html#tarfile-extraction-filter) for details.
In Python 3.12, use without the _filter_ argument will show a
[`DeprecationWarning`](https://docs.python.org/3/library/exceptions.html#DeprecationWarning "DeprecationWarning").
In Python 3.14, the default will switch to `'data'`.
(Contributed by Petr Viktorin in [**PEP 706**](https://peps.python.org/pep-0706/).)


### [Table of Contents](https://docs.python.org/3/contents.html)

- [What’s New In Python 3.10](https://docs.python.org/3/whatsnew/3.10.html#)
  - [Summary – Release highlights](https://docs.python.org/3/whatsnew/3.10.html#summary-release-highlights)
  - [New Features](https://docs.python.org/3/whatsnew/3.10.html#new-features)
    - [Parenthesized context managers](https://docs.python.org/3/whatsnew/3.10.html#parenthesized-context-managers)
    - [Better error messages](https://docs.python.org/3/whatsnew/3.10.html#better-error-messages)
      - [SyntaxErrors](https://docs.python.org/3/whatsnew/3.10.html#syntaxerrors)
      - [IndentationErrors](https://docs.python.org/3/whatsnew/3.10.html#indentationerrors)
      - [AttributeErrors](https://docs.python.org/3/whatsnew/3.10.html#attributeerrors)
      - [NameErrors](https://docs.python.org/3/whatsnew/3.10.html#nameerrors)
    - [PEP 626: Precise line numbers for debugging and other tools](https://docs.python.org/3/whatsnew/3.10.html#pep-626-precise-line-numbers-for-debugging-and-other-tools)
    - [PEP 634: Structural Pattern Matching](https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching)
      - [Syntax and operations](https://docs.python.org/3/whatsnew/3.10.html#syntax-and-operations)
      - [Declarative approach](https://docs.python.org/3/whatsnew/3.10.html#declarative-approach)
      - [Simple pattern: match to a literal](https://docs.python.org/3/whatsnew/3.10.html#simple-pattern-match-to-a-literal)
        - [Behavior without the wildcard](https://docs.python.org/3/whatsnew/3.10.html#behavior-without-the-wildcard)
      - [Patterns with a literal and variable](https://docs.python.org/3/whatsnew/3.10.html#patterns-with-a-literal-and-variable)
      - [Patterns and classes](https://docs.python.org/3/whatsnew/3.10.html#patterns-and-classes)
        - [Patterns with positional parameters](https://docs.python.org/3/whatsnew/3.10.html#patterns-with-positional-parameters)
      - [Nested patterns](https://docs.python.org/3/whatsnew/3.10.html#nested-patterns)
      - [Complex patterns and the wildcard](https://docs.python.org/3/whatsnew/3.10.html#complex-patterns-and-the-wildcard)
      - [Guard](https://docs.python.org/3/whatsnew/3.10.html#guard)
      - [Other Key Features](https://docs.python.org/3/whatsnew/3.10.html#other-key-features)
    - [Optional `EncodingWarning` and `encoding="locale"` option](https://docs.python.org/3/whatsnew/3.10.html#optional-encodingwarning-and-encoding-locale-option)
  - [New Features Related to Type Hints](https://docs.python.org/3/whatsnew/3.10.html#new-features-related-to-type-hints)
    - [PEP 604: New Type Union Operator](https://docs.python.org/3/whatsnew/3.10.html#pep-604-new-type-union-operator)
    - [PEP 612: Parameter Specification Variables](https://docs.python.org/3/whatsnew/3.10.html#pep-612-parameter-specification-variables)
    - [PEP 613: TypeAlias](https://docs.python.org/3/whatsnew/3.10.html#pep-613-typealias)
    - [PEP 647: User-Defined Type Guards](https://docs.python.org/3/whatsnew/3.10.html#pep-647-user-defined-type-guards)
  - [Other Language Changes](https://docs.python.org/3/whatsnew/3.10.html#other-language-changes)
  - [New Modules](https://docs.python.org/3/whatsnew/3.10.html#new-modules)
  - [Improved Modules](https://docs.python.org/3/whatsnew/3.10.html#improved-modules)
    - [asyncio](https://docs.python.org/3/whatsnew/3.10.html#asyncio)
    - [argparse](https://docs.python.org/3/whatsnew/3.10.html#argparse)
    - [array](https://docs.python.org/3/whatsnew/3.10.html#array)
    - [asynchat, asyncore, smtpd](https://docs.python.org/3/whatsnew/3.10.html#asynchat-asyncore-smtpd)
    - [base64](https://docs.python.org/3/whatsnew/3.10.html#base64)
    - [bdb](https://docs.python.org/3/whatsnew/3.10.html#bdb)
    - [bisect](https://docs.python.org/3/whatsnew/3.10.html#bisect)
    - [codecs](https://docs.python.org/3/whatsnew/3.10.html#codecs)
    - [collections.abc](https://docs.python.org/3/whatsnew/3.10.html#collections-abc)
    - [contextlib](https://docs.python.org/3/whatsnew/3.10.html#contextlib)
    - [curses](https://docs.python.org/3/whatsnew/3.10.html#curses)
    - [dataclasses](https://docs.python.org/3/whatsnew/3.10.html#dataclasses)
      - [\_\_slots\_\_](https://docs.python.org/3/whatsnew/3.10.html#slots)
      - [Keyword-only fields](https://docs.python.org/3/whatsnew/3.10.html#keyword-only-fields)
    - [distutils](https://docs.python.org/3/whatsnew/3.10.html#distutils)
    - [doctest](https://docs.python.org/3/whatsnew/3.10.html#doctest)
    - [encodings](https://docs.python.org/3/whatsnew/3.10.html#encodings)
    - [enum](https://docs.python.org/3/whatsnew/3.10.html#enum)
    - [fileinput](https://docs.python.org/3/whatsnew/3.10.html#fileinput)
    - [faulthandler](https://docs.python.org/3/whatsnew/3.10.html#faulthandler)
    - [gc](https://docs.python.org/3/whatsnew/3.10.html#gc)
    - [glob](https://docs.python.org/3/whatsnew/3.10.html#glob)
    - [hashlib](https://docs.python.org/3/whatsnew/3.10.html#hashlib)
    - [hmac](https://docs.python.org/3/whatsnew/3.10.html#hmac)
    - [IDLE and idlelib](https://docs.python.org/3/whatsnew/3.10.html#idle-and-idlelib)
    - [importlib.metadata](https://docs.python.org/3/whatsnew/3.10.html#importlib-metadata)
    - [inspect](https://docs.python.org/3/whatsnew/3.10.html#inspect)
    - [itertools](https://docs.python.org/3/whatsnew/3.10.html#itertools)
    - [linecache](https://docs.python.org/3/whatsnew/3.10.html#linecache)
    - [os](https://docs.python.org/3/whatsnew/3.10.html#os)
    - [os.path](https://docs.python.org/3/whatsnew/3.10.html#os-path)
    - [pathlib](https://docs.python.org/3/whatsnew/3.10.html#pathlib)
    - [platform](https://docs.python.org/3/whatsnew/3.10.html#platform)
    - [pprint](https://docs.python.org/3/whatsnew/3.10.html#pprint)
    - [py\_compile](https://docs.python.org/3/whatsnew/3.10.html#py-compile)
    - [pyclbr](https://docs.python.org/3/whatsnew/3.10.html#pyclbr)
    - [shelve](https://docs.python.org/3/whatsnew/3.10.html#shelve)
    - [statistics](https://docs.python.org/3/whatsnew/3.10.html#statistics)
    - [site](https://docs.python.org/3/whatsnew/3.10.html#site)
    - [socket](https://docs.python.org/3/whatsnew/3.10.html#socket)
    - [ssl](https://docs.python.org/3/whatsnew/3.10.html#ssl)
    - [sqlite3](https://docs.python.org/3/whatsnew/3.10.html#sqlite3)
    - [sys](https://docs.python.org/3/whatsnew/3.10.html#sys)
    - [\_thread](https://docs.python.org/3/whatsnew/3.10.html#thread)
    - [threading](https://docs.python.org/3/whatsnew/3.10.html#threading)
    - [traceback](https://docs.python.org/3/whatsnew/3.10.html#traceback)
    - [types](https://docs.python.org/3/whatsnew/3.10.html#types)
    - [typing](https://docs.python.org/3/whatsnew/3.10.html#typing)
    - [unittest](https://docs.python.org/3/whatsnew/3.10.html#unittest)
    - [urllib.parse](https://docs.python.org/3/whatsnew/3.10.html#urllib-parse)
    - [xml](https://docs.python.org/3/whatsnew/3.10.html#xml)
    - [zipimport](https://docs.python.org/3/whatsnew/3.10.html#zipimport)
  - [Optimizations](https://docs.python.org/3/whatsnew/3.10.html#optimizations)
  - [Deprecated](https://docs.python.org/3/whatsnew/3.10.html#deprecated)
  - [Removed](https://docs.python.org/3/whatsnew/3.10.html#removed)
  - [Porting to Python 3.10](https://docs.python.org/3/whatsnew/3.10.html#porting-to-python-3-10)
    - [Changes in the Python syntax](https://docs.python.org/3/whatsnew/3.10.html#changes-in-the-python-syntax)
    - [Changes in the Python API](https://docs.python.org/3/whatsnew/3.10.html#changes-in-the-python-api)
    - [Changes in the C API](https://docs.python.org/3/whatsnew/3.10.html#changes-in-the-c-api)
  - [CPython bytecode changes](https://docs.python.org/3/whatsnew/3.10.html#cpython-bytecode-changes)
  - [Build Changes](https://docs.python.org/3/whatsnew/3.10.html#build-changes)
  - [C API Changes](https://docs.python.org/3/whatsnew/3.10.html#c-api-changes)
    - [PEP 652: Maintaining the Stable ABI](https://docs.python.org/3/whatsnew/3.10.html#pep-652-maintaining-the-stable-abi)
    - [New Features](https://docs.python.org/3/whatsnew/3.10.html#id1)
    - [Porting to Python 3.10](https://docs.python.org/3/whatsnew/3.10.html#id2)
    - [Deprecated](https://docs.python.org/3/whatsnew/3.10.html#id3)
    - [Removed](https://docs.python.org/3/whatsnew/3.10.html#id4)
  - [Notable security feature in 3.10.7](https://docs.python.org/3/whatsnew/3.10.html#notable-security-feature-in-3-10-7)
  - [Notable security feature in 3.10.8](https://docs.python.org/3/whatsnew/3.10.html#notable-security-feature-in-3-10-8)
  - [Notable changes in 3.10.12](https://docs.python.org/3/whatsnew/3.10.html#notable-changes-in-3-10-12)
    - [tarfile](https://docs.python.org/3/whatsnew/3.10.html#tarfile)

#### Previous topic

[What’s New In Python 3.11](https://docs.python.org/3/whatsnew/3.11.html "previous chapter")

#### Next topic

[What’s New In Python 3.9](https://docs.python.org/3/whatsnew/3.9.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/whatsnew/3.10.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/whatsnew/3.9.html "What’s New In Python 3.9") \|
- [previous](https://docs.python.org/3/whatsnew/3.11.html "What’s New In Python 3.11") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [What’s New in Python](https://docs.python.org/3/whatsnew/index.html) »
- [What’s New In Python 3.10](https://docs.python.org/3/whatsnew/3.10.html)
- \|

- Theme
AutoLightDark \|