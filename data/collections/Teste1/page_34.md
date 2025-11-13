### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/keyword.html "keyword — Testing for Python keywords") \|
- [previous](https://docs.python.org/3/library/symtable.html "symtable — Access to the compiler’s symbol tables") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Python Language Services](https://docs.python.org/3/library/language.html) »
- [`token` — Constants used with Python parse trees](https://docs.python.org/3/library/token.html)
- \|

- Theme
AutoLightDark \|

# `token` — Constants used with Python parse trees [¶](https://docs.python.org/3/library/token.html\#module-token "Link to this heading")

**Source code:** [Lib/token.py](https://github.com/python/cpython/tree/3.14/Lib/token.py)

* * *

This module provides constants which represent the numeric values of leaf nodes
of the parse tree (terminal tokens). Refer to the file `Grammar/Tokens`
in the Python distribution for the definitions of the names in the context of
the language grammar. The specific numeric values which the names map to may
change between Python versions.

The module also provides a mapping from numeric codes to names and some
functions. The functions mirror definitions in the Python C header files.

Note that a token’s value may depend on tokenizer options. For example, a
`"+"` token may be reported as either [`PLUS`](https://docs.python.org/3/library/token.html#token.PLUS "token.PLUS") or [`OP`](https://docs.python.org/3/library/token.html#token.OP "token.OP"), or
a `"match"` token may be either [`NAME`](https://docs.python.org/3/library/token.html#token.NAME "token.NAME") or [`SOFT_KEYWORD`](https://docs.python.org/3/library/token.html#token.SOFT_KEYWORD "token.SOFT_KEYWORD").

token.tok\_name [¶](https://docs.python.org/3/library/token.html#token.tok_name "Link to this definition")

Dictionary mapping the numeric values of the constants defined in this module
back to name strings, allowing more human-readable representation of parse trees
to be generated.

token.ISTERMINAL( _x_) [¶](https://docs.python.org/3/library/token.html#token.ISTERMINAL "Link to this definition")

Return `True` for terminal token values.

token.ISNONTERMINAL( _x_) [¶](https://docs.python.org/3/library/token.html#token.ISNONTERMINAL "Link to this definition")

Return `True` for non-terminal token values.

token.ISEOF( _x_) [¶](https://docs.python.org/3/library/token.html#token.ISEOF "Link to this definition")

Return `True` if _x_ is the marker indicating the end of input.

The token constants are:

token.NAME [¶](https://docs.python.org/3/library/token.html#token.NAME "Link to this definition")

Token value that indicates an [identifier](https://docs.python.org/3/reference/lexical_analysis.html#identifiers).
Note that keywords are also initially tokenized as `NAME` tokens.

token.NUMBER [¶](https://docs.python.org/3/library/token.html#token.NUMBER "Link to this definition")

Token value that indicates a [numeric literal](https://docs.python.org/3/reference/lexical_analysis.html#numbers)

token.STRING [¶](https://docs.python.org/3/library/token.html#token.STRING "Link to this definition")

Token value that indicates a [string or byte literal](https://docs.python.org/3/reference/lexical_analysis.html#strings),
excluding [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings).
The token string is not interpreted:
it includes the surrounding quotation marks and the prefix (if given);
backslashes are included literally, without processing escape sequences.

token.OP [¶](https://docs.python.org/3/library/token.html#token.OP "Link to this definition")

A generic token value that indicates an
[operator](https://docs.python.org/3/reference/lexical_analysis.html#operators) or [delimiter](https://docs.python.org/3/reference/lexical_analysis.html#delimiters).

**CPython implementation detail:** This value is only reported by the [`tokenize`](https://docs.python.org/3/library/tokenize.html#module-tokenize "tokenize: Lexical scanner for Python source code.") module.
Internally, the tokenizer uses
[exact token types](https://docs.python.org/3/library/token.html#token-operators-delimiters) instead.

token.COMMENT [¶](https://docs.python.org/3/library/token.html#token.COMMENT "Link to this definition")

Token value used to indicate a comment.
The parser ignores `COMMENT` tokens.

token.NEWLINE [¶](https://docs.python.org/3/library/token.html#token.NEWLINE "Link to this definition")

Token value that indicates the end of a [logical line](https://docs.python.org/3/reference/lexical_analysis.html#logical-lines).

token.NL [¶](https://docs.python.org/3/library/token.html#token.NL "Link to this definition")

Token value used to indicate a non-terminating newline.
`NL` tokens are generated when a logical line of code is continued
over multiple physical lines. The parser ignores `NL` tokens.

token.INDENT [¶](https://docs.python.org/3/library/token.html#token.INDENT "Link to this definition")

Token value used at the beginning of a [logical line](https://docs.python.org/3/reference/lexical_analysis.html#logical-lines)
to indicate the start of an [indented block](https://docs.python.org/3/reference/lexical_analysis.html#indentation).

token.DEDENT [¶](https://docs.python.org/3/library/token.html#token.DEDENT "Link to this definition")

Token value used at the beginning of a [logical line](https://docs.python.org/3/reference/lexical_analysis.html#logical-lines)
to indicate the end of an [indented block](https://docs.python.org/3/reference/lexical_analysis.html#indentation).

token.FSTRING\_START [¶](https://docs.python.org/3/library/token.html#token.FSTRING_START "Link to this definition")

Token value used to indicate the beginning of an
[f-string literal](https://docs.python.org/3/reference/lexical_analysis.html#f-strings).

**CPython implementation detail:** The token string includes the prefix and the opening quote(s), but none
of the contents of the literal.

token.FSTRING\_MIDDLE [¶](https://docs.python.org/3/library/token.html#token.FSTRING_MIDDLE "Link to this definition")

Token value used for literal text inside an [f-string literal](https://docs.python.org/3/reference/lexical_analysis.html#f-strings),
including format specifications.

**CPython implementation detail:** Replacement fields (that is, the non-literal parts of f-strings) use
the same tokens as other expressions, and are delimited by
[`LBRACE`](https://docs.python.org/3/library/token.html#token.LBRACE "token.LBRACE"), [`RBRACE`](https://docs.python.org/3/library/token.html#token.RBRACE "token.RBRACE"), [`EXCLAMATION`](https://docs.python.org/3/library/token.html#token.EXCLAMATION "token.EXCLAMATION") and [`COLON`](https://docs.python.org/3/library/token.html#token.COLON "token.COLON")
tokens.

token.FSTRING\_END [¶](https://docs.python.org/3/library/token.html#token.FSTRING_END "Link to this definition")

Token value used to indicate the end of a [f-string](https://docs.python.org/3/reference/lexical_analysis.html#f-strings).

**CPython implementation detail:** The token string contains the closing quote(s).

token.TSTRING\_START [¶](https://docs.python.org/3/library/token.html#token.TSTRING_START "Link to this definition")

Token value used to indicate the beginning of a template string literal.

**CPython implementation detail:** The token string includes the prefix and the opening quote(s), but none
of the contents of the literal.

Added in version 3.14.

token.TSTRING\_MIDDLE [¶](https://docs.python.org/3/library/token.html#token.TSTRING_MIDDLE "Link to this definition")

Token value used for literal text inside a template string literal
including format specifications.

**CPython implementation detail:** Replacement fields (that is, the non-literal parts of t-strings) use
the same tokens as other expressions, and are delimited by
[`LBRACE`](https://docs.python.org/3/library/token.html#token.LBRACE "token.LBRACE"), [`RBRACE`](https://docs.python.org/3/library/token.html#token.RBRACE "token.RBRACE"), [`EXCLAMATION`](https://docs.python.org/3/library/token.html#token.EXCLAMATION "token.EXCLAMATION") and [`COLON`](https://docs.python.org/3/library/token.html#token.COLON "token.COLON")
tokens.

Added in version 3.14.

token.TSTRING\_END [¶](https://docs.python.org/3/library/token.html#token.TSTRING_END "Link to this definition")

Token value used to indicate the end of a template string literal.

**CPython implementation detail:** The token string contains the closing quote(s).

Added in version 3.14.

token.ENDMARKER [¶](https://docs.python.org/3/library/token.html#token.ENDMARKER "Link to this definition")

Token value that indicates the end of input.
Used in [top-level grammar rules](https://docs.python.org/3/reference/toplevel_components.html#top-level).

token.ENCODING [¶](https://docs.python.org/3/library/token.html#token.ENCODING "Link to this definition")

Token value that indicates the encoding used to decode the source bytes
into text. The first token returned by [`tokenize.tokenize()`](https://docs.python.org/3/library/tokenize.html#tokenize.tokenize "tokenize.tokenize") will
always be an `ENCODING` token.

**CPython implementation detail:** This token type isn’t used by the C tokenizer but is needed for
the [`tokenize`](https://docs.python.org/3/library/tokenize.html#module-tokenize "tokenize: Lexical scanner for Python source code.") module.

The following token types are not produced by the [`tokenize`](https://docs.python.org/3/library/tokenize.html#module-tokenize "tokenize: Lexical scanner for Python source code.") module,
and are defined for special uses in the tokenizer or parser:

token.TYPE\_IGNORE [¶](https://docs.python.org/3/library/token.html#token.TYPE_IGNORE "Link to this definition")

Token value indicating that a `type: ignore` comment was recognized.
Such tokens are produced instead of regular [`COMMENT`](https://docs.python.org/3/library/token.html#token.COMMENT "token.COMMENT") tokens only
with the [`PyCF_TYPE_COMMENTS`](https://docs.python.org/3/library/ast.html#ast.PyCF_TYPE_COMMENTS "ast.PyCF_TYPE_COMMENTS") flag.

token.TYPE\_COMMENT [¶](https://docs.python.org/3/library/token.html#token.TYPE_COMMENT "Link to this definition")

Token value indicating that a type comment was recognized.
Such tokens are produced instead of regular [`COMMENT`](https://docs.python.org/3/library/token.html#token.COMMENT "token.COMMENT") tokens only
with the [`PyCF_TYPE_COMMENTS`](https://docs.python.org/3/library/ast.html#ast.PyCF_TYPE_COMMENTS "ast.PyCF_TYPE_COMMENTS") flag.

token.SOFT\_KEYWORD [¶](https://docs.python.org/3/library/token.html#token.SOFT_KEYWORD "Link to this definition")

Token value indicating a [soft keyword](https://docs.python.org/3/reference/lexical_analysis.html#soft-keywords).

The tokenizer never produces this value.
To check for a soft keyword, pass a [`NAME`](https://docs.python.org/3/library/token.html#token.NAME "token.NAME") token’s string to
[`keyword.issoftkeyword()`](https://docs.python.org/3/library/keyword.html#keyword.issoftkeyword "keyword.issoftkeyword").

token.ERRORTOKEN [¶](https://docs.python.org/3/library/token.html#token.ERRORTOKEN "Link to this definition")

Token value used to indicate wrong input.

The [`tokenize`](https://docs.python.org/3/library/tokenize.html#module-tokenize "tokenize: Lexical scanner for Python source code.") module generally indicates errors by
raising exceptions instead of emitting this token.
It can also emit tokens such as [`OP`](https://docs.python.org/3/library/token.html#token.OP "token.OP") or [`NAME`](https://docs.python.org/3/library/token.html#token.NAME "token.NAME") with strings that
are later rejected by the parser.

The remaining tokens represent specific [operators](https://docs.python.org/3/reference/lexical_analysis.html#operators) and
[delimiters](https://docs.python.org/3/reference/lexical_analysis.html#delimiters).
(The [`tokenize`](https://docs.python.org/3/library/tokenize.html#module-tokenize "tokenize: Lexical scanner for Python source code.") module reports these as [`OP`](https://docs.python.org/3/library/token.html#token.OP "token.OP"); see `exact_type`
in the [`tokenize`](https://docs.python.org/3/library/tokenize.html#module-tokenize "tokenize: Lexical scanner for Python source code.") documentation for details.)

| Token | Value |
| --- | --- |
| token.LPAR [¶](https://docs.python.org/3/library/token.html#token.LPAR "Link to this definition") | `"("` |
| token.RPAR [¶](https://docs.python.org/3/library/token.html#token.RPAR "Link to this definition") | `")"` |
| token.LSQB [¶](https://docs.python.org/3/library/token.html#token.LSQB "Link to this definition") | `"["` |\
| token.RSQB [¶](https://docs.python.org/3/library/token.html#token.RSQB "Link to this definition") | `"]"` |
| token.COLON [¶](https://docs.python.org/3/library/token.html#token.COLON "Link to this definition") | `":"` |
| token.COMMA [¶](https://docs.python.org/3/library/token.html#token.COMMA "Link to this definition") | `","` |
| token.SEMI [¶](https://docs.python.org/3/library/token.html#token.SEMI "Link to this definition") | `";"` |
| token.PLUS [¶](https://docs.python.org/3/library/token.html#token.PLUS "Link to this definition") | `"+"` |
| token.MINUS [¶](https://docs.python.org/3/library/token.html#token.MINUS "Link to this definition") | `"-"` |
| token.STAR [¶](https://docs.python.org/3/library/token.html#token.STAR "Link to this definition") | `"*"` |
| token.SLASH [¶](https://docs.python.org/3/library/token.html#token.SLASH "Link to this definition") | `"/"` |
| token.VBAR [¶](https://docs.python.org/3/library/token.html#token.VBAR "Link to this definition") | `"|"` |
| token.AMPER [¶](https://docs.python.org/3/library/token.html#token.AMPER "Link to this definition") | `"&"` |
| token.LESS [¶](https://docs.python.org/3/library/token.html#token.LESS "Link to this definition") | `"<"` |
| token.GREATER [¶](https://docs.python.org/3/library/token.html#token.GREATER "Link to this definition") | `">"` |
| token.EQUAL [¶](https://docs.python.org/3/library/token.html#token.EQUAL "Link to this definition") | `"="` |
| token.DOT [¶](https://docs.python.org/3/library/token.html#token.DOT "Link to this definition") | `"."` |
| token.PERCENT [¶](https://docs.python.org/3/library/token.html#token.PERCENT "Link to this definition") | `"%"` |
| token.LBRACE [¶](https://docs.python.org/3/library/token.html#token.LBRACE "Link to this definition") | `"{"` |
| token.RBRACE [¶](https://docs.python.org/3/library/token.html#token.RBRACE "Link to this definition") | `"}"` |
| token.EQEQUAL [¶](https://docs.python.org/3/library/token.html#token.EQEQUAL "Link to this definition") | `"=="` |
| token.NOTEQUAL [¶](https://docs.python.org/3/library/token.html#token.NOTEQUAL "Link to this definition") | `"!="` |
| token.LESSEQUAL [¶](https://docs.python.org/3/library/token.html#token.LESSEQUAL "Link to this definition") | `"<="` |
| token.GREATEREQUAL [¶](https://docs.python.org/3/library/token.html#token.GREATEREQUAL "Link to this definition") | `">="` |
| token.TILDE [¶](https://docs.python.org/3/library/token.html#token.TILDE "Link to this definition") | `"~"` |
| token.CIRCUMFLEX [¶](https://docs.python.org/3/library/token.html#token.CIRCUMFLEX "Link to this definition") | `"^"` |
| token.LEFTSHIFT [¶](https://docs.python.org/3/library/token.html#token.LEFTSHIFT "Link to this definition") | `"<<"` |
| token.RIGHTSHIFT [¶](https://docs.python.org/3/library/token.html#token.RIGHTSHIFT "Link to this definition") | `">>"` |
| token.DOUBLESTAR [¶](https://docs.python.org/3/library/token.html#token.DOUBLESTAR "Link to this definition") | `"**"` |
| token.PLUSEQUAL [¶](https://docs.python.org/3/library/token.html#token.PLUSEQUAL "Link to this definition") | `"+="` |
| token.MINEQUAL [¶](https://docs.python.org/3/library/token.html#token.MINEQUAL "Link to this definition") | `"-="` |
| token.STAREQUAL [¶](https://docs.python.org/3/library/token.html#token.STAREQUAL "Link to this definition") | `"*="` |
| token.SLASHEQUAL [¶](https://docs.python.org/3/library/token.html#token.SLASHEQUAL "Link to this definition") | `"/="` |
| token.PERCENTEQUAL [¶](https://docs.python.org/3/library/token.html#token.PERCENTEQUAL "Link to this definition") | `"%="` |
| token.AMPEREQUAL [¶](https://docs.python.org/3/library/token.html#token.AMPEREQUAL "Link to this definition") | `"&="` |
| token.VBAREQUAL [¶](https://docs.python.org/3/library/token.html#token.VBAREQUAL "Link to this definition") | `"|="` |
| token.CIRCUMFLEXEQUAL [¶](https://docs.python.org/3/library/token.html#token.CIRCUMFLEXEQUAL "Link to this definition") | `"^="` |
| token.LEFTSHIFTEQUAL [¶](https://docs.python.org/3/library/token.html#token.LEFTSHIFTEQUAL "Link to this definition") | `"<<="` |
| token.RIGHTSHIFTEQUAL [¶](https://docs.python.org/3/library/token.html#token.RIGHTSHIFTEQUAL "Link to this definition") | `">>="` |
| token.DOUBLESTAREQUAL [¶](https://docs.python.org/3/library/token.html#token.DOUBLESTAREQUAL "Link to this definition") | `"**="` |
| token.DOUBLESLASH [¶](https://docs.python.org/3/library/token.html#token.DOUBLESLASH "Link to this definition") | `"//"` |
| token.DOUBLESLASHEQUAL [¶](https://docs.python.org/3/library/token.html#token.DOUBLESLASHEQUAL "Link to this definition") | `"//="` |
| token.AT [¶](https://docs.python.org/3/library/token.html#token.AT "Link to this definition") | `"@"` |
| token.ATEQUAL [¶](https://docs.python.org/3/library/token.html#token.ATEQUAL "Link to this definition") | `"@="` |
| token.RARROW [¶](https://docs.python.org/3/library/token.html#token.RARROW "Link to this definition") | `"->"` |
| token.ELLIPSIS [¶](https://docs.python.org/3/library/token.html#token.ELLIPSIS "Link to this definition") | `"..."` |
| token.COLONEQUAL [¶](https://docs.python.org/3/library/token.html#token.COLONEQUAL "Link to this definition") | `":="` |
| token.EXCLAMATION [¶](https://docs.python.org/3/library/token.html#token.EXCLAMATION "Link to this definition") | `"!"` |

The following non-token constants are provided:

token.N\_TOKENS [¶](https://docs.python.org/3/library/token.html#token.N_TOKENS "Link to this definition")

The number of token types defined in this module.

token.EXACT\_TOKEN\_TYPES [¶](https://docs.python.org/3/library/token.html#token.EXACT_TOKEN_TYPES "Link to this definition")

A dictionary mapping the string representation of a token to its numeric code.

Added in version 3.8.

Changed in version 3.5: Added `AWAIT` and `ASYNC` tokens.

Changed in version 3.7: Added [`COMMENT`](https://docs.python.org/3/library/token.html#token.COMMENT "token.COMMENT"), [`NL`](https://docs.python.org/3/library/token.html#token.NL "token.NL") and [`ENCODING`](https://docs.python.org/3/library/token.html#token.ENCODING "token.ENCODING") tokens.

Changed in version 3.7: Removed `AWAIT` and `ASYNC` tokens. “async” and “await” are
now tokenized as [`NAME`](https://docs.python.org/3/library/token.html#token.NAME "token.NAME") tokens.

Changed in version 3.8: Added [`TYPE_COMMENT`](https://docs.python.org/3/library/token.html#token.TYPE_COMMENT "token.TYPE_COMMENT"), [`TYPE_IGNORE`](https://docs.python.org/3/library/token.html#token.TYPE_IGNORE "token.TYPE_IGNORE"), [`COLONEQUAL`](https://docs.python.org/3/library/token.html#token.COLONEQUAL "token.COLONEQUAL").
Added `AWAIT` and `ASYNC` tokens back (they’re needed
to support parsing older Python versions for [`ast.parse()`](https://docs.python.org/3/library/ast.html#ast.parse "ast.parse") with
`feature_version` set to 6 or lower).

Changed in version 3.12: Added [`EXCLAMATION`](https://docs.python.org/3/library/token.html#token.EXCLAMATION "token.EXCLAMATION").

Changed in version 3.13: Removed `AWAIT` and `ASYNC` tokens again.

#### Previous topic

[`symtable` — Access to the compiler’s symbol tables](https://docs.python.org/3/library/symtable.html "previous chapter")

#### Next topic

[`keyword` — Testing for Python keywords](https://docs.python.org/3/library/keyword.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/token.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/keyword.html "keyword — Testing for Python keywords") \|
- [previous](https://docs.python.org/3/library/symtable.html "symtable — Access to the compiler’s symbol tables") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Python Language Services](https://docs.python.org/3/library/language.html) »
- [`token` — Constants used with Python parse trees](https://docs.python.org/3/library/token.html)
- \|

- Theme
AutoLightDark \|