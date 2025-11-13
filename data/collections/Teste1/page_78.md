### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/cmdline.html "Modules command-line interface (CLI)") \|
- [previous](https://docs.python.org/3/library/resource.html "resource — Resource usage information") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Unix-specific services](https://docs.python.org/3/library/unix.html) »
- [`syslog` — Unix syslog library routines](https://docs.python.org/3/library/syslog.html)
- \|

- Theme
AutoLightDark \|

# `syslog` — Unix syslog library routines [¶](https://docs.python.org/3/library/syslog.html\#module-syslog "Link to this heading")

* * *

This module provides an interface to the Unix `syslog` library routines.
Refer to the Unix manual pages for a detailed description of the `syslog`
facility.

[Availability](https://docs.python.org/3/library/intro.html#availability): Unix, not WASI, not iOS.

This module wraps the system `syslog` family of routines. A pure Python
library that can speak to a syslog server is available in the
[`logging.handlers`](https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers "logging.handlers: Handlers for the logging module.") module as [`SysLogHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SysLogHandler "logging.handlers.SysLogHandler").

The module defines the following functions:

syslog.syslog( _message_) [¶](https://docs.python.org/3/library/syslog.html#syslog.syslog "Link to this definition")syslog.syslog( _priority_, _message_)

Send the string _message_ to the system logger. A trailing newline is added
if necessary. Each message is tagged with a priority composed of a
_facility_ and a _level_. The optional _priority_ argument, which defaults
to [`LOG_INFO`](https://docs.python.org/3/library/syslog.html#syslog.LOG_INFO "syslog.LOG_INFO"), determines the message priority. If the facility is
not encoded in _priority_ using logical-or (`LOG_INFO | LOG_USER`), the
value given in the [`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") call is used.

If [`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") has not been called prior to the call to [`syslog()`](https://docs.python.org/3/library/syslog.html#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)"),
[`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") will be called with no arguments.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)`syslog.syslog` with arguments `priority`, `message`.

Changed in version 3.2: In previous versions, [`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") would not be called automatically if
it wasn’t called prior to the call to [`syslog()`](https://docs.python.org/3/library/syslog.html#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)"), deferring to the syslog
implementation to call `openlog()`.

Changed in version 3.12: This function is restricted in subinterpreters.
(Only code that runs in multiple interpreters is affected and
the restriction is not relevant for most users.)
[`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") must be called in the main interpreter before [`syslog()`](https://docs.python.org/3/library/syslog.html#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)") may be used
in a subinterpreter. Otherwise it will raise [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError").

syslog.openlog(\[ _ident_\[, _logoption_\[, _facility_\]\]\]) [¶](https://docs.python.org/3/library/syslog.html#syslog.openlog "Link to this definition")

Logging options of subsequent [`syslog()`](https://docs.python.org/3/library/syslog.html#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)") calls can be set by calling
[`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog"). [`syslog()`](https://docs.python.org/3/library/syslog.html#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)") will call [`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") with no arguments
if the log is not currently open.

The optional _ident_ keyword argument is a string which is prepended to every
message, and defaults to `sys.argv[0]` with leading path components
stripped. The optional _logoption_ keyword argument (default is 0) is a bit
field – see below for possible values to combine. The optional _facility_
keyword argument (default is [`LOG_USER`](https://docs.python.org/3/library/syslog.html#syslog.LOG_USER "syslog.LOG_USER")) sets the default facility for
messages which do not have a facility explicitly encoded.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)`syslog.openlog` with arguments `ident`, `logoption`, `facility`.

Changed in version 3.2: In previous versions, keyword arguments were not allowed, and _ident_ was
required.

Changed in version 3.12: This function is restricted in subinterpreters.
(Only code that runs in multiple interpreters is affected and
the restriction is not relevant for most users.)
This may only be called in the main interpreter.
It will raise [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") if called in a subinterpreter.

syslog.closelog() [¶](https://docs.python.org/3/library/syslog.html#syslog.closelog "Link to this definition")

Reset the syslog module values and call the system library `closelog()`.

This causes the module to behave as it does when initially imported. For
example, [`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") will be called on the first [`syslog()`](https://docs.python.org/3/library/syslog.html#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)") call (if
[`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") hasn’t already been called), and _ident_ and other
[`openlog()`](https://docs.python.org/3/library/syslog.html#syslog.openlog "syslog.openlog") parameters are reset to defaults.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)`syslog.closelog` with no arguments.

Changed in version 3.12: This function is restricted in subinterpreters.
(Only code that runs in multiple interpreters is affected and
the restriction is not relevant for most users.)
This may only be called in the main interpreter.
It will raise [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError") if called in a subinterpreter.

syslog.setlogmask( _maskpri_) [¶](https://docs.python.org/3/library/syslog.html#syslog.setlogmask "Link to this definition")

Set the priority mask to _maskpri_ and return the previous mask value. Calls
to [`syslog()`](https://docs.python.org/3/library/syslog.html#module-syslog "syslog: An interface to the Unix syslog library routines. (Unix)") with a priority level not set in _maskpri_ are ignored.
The default is to log all priorities. The function `LOG_MASK(pri)`
calculates the mask for the individual priority _pri_. The function
`LOG_UPTO(pri)` calculates the mask for all priorities up to and including
_pri_.

Raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing)`syslog.setlogmask` with argument `maskpri`.

The module defines the following constants:

syslog.LOG\_EMERG [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_EMERG "Link to this definition")syslog.LOG\_ALERT [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_ALERT "Link to this definition")syslog.LOG\_CRIT [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_CRIT "Link to this definition")syslog.LOG\_ERR [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_ERR "Link to this definition")syslog.LOG\_WARNING [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_WARNING "Link to this definition")syslog.LOG\_NOTICE [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_NOTICE "Link to this definition")syslog.LOG\_INFO [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_INFO "Link to this definition")syslog.LOG\_DEBUG [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_DEBUG "Link to this definition")

Priority levels (high to low).

syslog.LOG\_AUTH [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_AUTH "Link to this definition")syslog.LOG\_AUTHPRIV [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_AUTHPRIV "Link to this definition")syslog.LOG\_CRON [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_CRON "Link to this definition")syslog.LOG\_DAEMON [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_DAEMON "Link to this definition")syslog.LOG\_FTP [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_FTP "Link to this definition")syslog.LOG\_INSTALL [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_INSTALL "Link to this definition")syslog.LOG\_KERN [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_KERN "Link to this definition")syslog.LOG\_LAUNCHD [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LAUNCHD "Link to this definition")syslog.LOG\_LPR [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LPR "Link to this definition")syslog.LOG\_MAIL [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_MAIL "Link to this definition")syslog.LOG\_NETINFO [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_NETINFO "Link to this definition")syslog.LOG\_NEWS [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_NEWS "Link to this definition")syslog.LOG\_RAS [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_RAS "Link to this definition")syslog.LOG\_REMOTEAUTH [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_REMOTEAUTH "Link to this definition")syslog.LOG\_SYSLOG [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_SYSLOG "Link to this definition")syslog.LOG\_USER [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_USER "Link to this definition")syslog.LOG\_UUCP [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_UUCP "Link to this definition")syslog.LOG\_LOCAL0 [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL0 "Link to this definition")syslog.LOG\_LOCAL1 [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL1 "Link to this definition")syslog.LOG\_LOCAL2 [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL2 "Link to this definition")syslog.LOG\_LOCAL3 [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL3 "Link to this definition")syslog.LOG\_LOCAL4 [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL4 "Link to this definition")syslog.LOG\_LOCAL5 [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL5 "Link to this definition")syslog.LOG\_LOCAL6 [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL6 "Link to this definition")syslog.LOG\_LOCAL7 [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_LOCAL7 "Link to this definition")

Facilities, depending on availability in `<syslog.h>` for [`LOG_AUTHPRIV`](https://docs.python.org/3/library/syslog.html#syslog.LOG_AUTHPRIV "syslog.LOG_AUTHPRIV"),
[`LOG_FTP`](https://docs.python.org/3/library/syslog.html#syslog.LOG_FTP "syslog.LOG_FTP"), [`LOG_NETINFO`](https://docs.python.org/3/library/syslog.html#syslog.LOG_NETINFO "syslog.LOG_NETINFO"), [`LOG_REMOTEAUTH`](https://docs.python.org/3/library/syslog.html#syslog.LOG_REMOTEAUTH "syslog.LOG_REMOTEAUTH"),
[`LOG_INSTALL`](https://docs.python.org/3/library/syslog.html#syslog.LOG_INSTALL "syslog.LOG_INSTALL") and [`LOG_RAS`](https://docs.python.org/3/library/syslog.html#syslog.LOG_RAS "syslog.LOG_RAS").

Changed in version 3.13: Added [`LOG_FTP`](https://docs.python.org/3/library/syslog.html#syslog.LOG_FTP "syslog.LOG_FTP"), [`LOG_NETINFO`](https://docs.python.org/3/library/syslog.html#syslog.LOG_NETINFO "syslog.LOG_NETINFO"), [`LOG_REMOTEAUTH`](https://docs.python.org/3/library/syslog.html#syslog.LOG_REMOTEAUTH "syslog.LOG_REMOTEAUTH"),
[`LOG_INSTALL`](https://docs.python.org/3/library/syslog.html#syslog.LOG_INSTALL "syslog.LOG_INSTALL"), [`LOG_RAS`](https://docs.python.org/3/library/syslog.html#syslog.LOG_RAS "syslog.LOG_RAS"), and [`LOG_LAUNCHD`](https://docs.python.org/3/library/syslog.html#syslog.LOG_LAUNCHD "syslog.LOG_LAUNCHD").

syslog.LOG\_PID [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_PID "Link to this definition")syslog.LOG\_CONS [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_CONS "Link to this definition")syslog.LOG\_NDELAY [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_NDELAY "Link to this definition")syslog.LOG\_ODELAY [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_ODELAY "Link to this definition")syslog.LOG\_NOWAIT [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_NOWAIT "Link to this definition")syslog.LOG\_PERROR [¶](https://docs.python.org/3/library/syslog.html#syslog.LOG_PERROR "Link to this definition")

Log options, depending on availability in `<syslog.h>` for
[`LOG_ODELAY`](https://docs.python.org/3/library/syslog.html#syslog.LOG_ODELAY "syslog.LOG_ODELAY"), [`LOG_NOWAIT`](https://docs.python.org/3/library/syslog.html#syslog.LOG_NOWAIT "syslog.LOG_NOWAIT") and [`LOG_PERROR`](https://docs.python.org/3/library/syslog.html#syslog.LOG_PERROR "syslog.LOG_PERROR").

## Examples [¶](https://docs.python.org/3/library/syslog.html\#examples "Link to this heading")

### Simple example [¶](https://docs.python.org/3/library/syslog.html\#simple-example "Link to this heading")

A simple set of examples:

Copy

```
import syslog

syslog.syslog('Processing started')
if error:
    syslog.syslog(syslog.LOG_ERR, 'Processing started')
```

An example of setting some log options, these would include the process ID in
logged messages, and write the messages to the destination facility used for
mail logging:

Copy

```
syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_MAIL)
syslog.syslog('E-mail processing initiated...')
```

### [Table of Contents](https://docs.python.org/3/contents.html)

- [`syslog` — Unix syslog library routines](https://docs.python.org/3/library/syslog.html#)
  - [Examples](https://docs.python.org/3/library/syslog.html#examples)
    - [Simple example](https://docs.python.org/3/library/syslog.html#simple-example)

#### Previous topic

[`resource` — Resource usage information](https://docs.python.org/3/library/resource.html "previous chapter")

#### Next topic

[Modules command-line interface (CLI)](https://docs.python.org/3/library/cmdline.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/syslog.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/cmdline.html "Modules command-line interface (CLI)") \|
- [previous](https://docs.python.org/3/library/resource.html "resource — Resource usage information") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Unix-specific services](https://docs.python.org/3/library/unix.html) »
- [`syslog` — Unix syslog library routines](https://docs.python.org/3/library/syslog.html)
- \|

- Theme
AutoLightDark \|