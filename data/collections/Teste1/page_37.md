### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/importlib.resources.html "importlib.resources – Package resource reading, opening and access") \|
- [previous](https://docs.python.org/3/library/runpy.html "runpy — Locating and executing Python modules") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Importing Modules](https://docs.python.org/3/library/modules.html) »
- [`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html)
- \|

- Theme
AutoLightDark \|

# `importlib` — The implementation of `import` [¶](https://docs.python.org/3/library/importlib.html\#module-importlib "Link to this heading")

Added in version 3.1.

**Source code:** [Lib/importlib/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.14/Lib/importlib/__init__.py)

* * *

## Introduction [¶](https://docs.python.org/3/library/importlib.html\#introduction "Link to this heading")

The purpose of the [`importlib`](https://docs.python.org/3/library/importlib.html#module-importlib "importlib: The implementation of the import machinery.") package is three-fold.

One is to provide the
implementation of the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement (and thus, by extension, the
[`__import__()`](https://docs.python.org/3/library/functions.html#import__ "__import__") function) in Python source code. This provides an
implementation of `import` which is portable to any Python
interpreter. This also provides an implementation which is easier to
comprehend than one implemented in a programming language other than Python.

Two, the components to implement [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) are exposed in this
package, making it easier for users to create their own custom objects (known
generically as an [importer](https://docs.python.org/3/glossary.html#term-importer)) to participate in the import process.

Three, the package contains modules exposing additional functionality for
managing aspects of Python packages:

- [`importlib.metadata`](https://docs.python.org/3/library/importlib.metadata.html#module-importlib.metadata "importlib.metadata: Accessing package metadata") presents access to metadata from third-party
distributions.

- [`importlib.resources`](https://docs.python.org/3/library/importlib.resources.html#module-importlib.resources "importlib.resources: Package resource reading, opening, and access") provides routines for accessing non-code
“resources” from Python packages.


See also

[The import statement](https://docs.python.org/3/reference/simple_stmts.html#import)

The language reference for the [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement.

[Packages specification](https://www.python.org/doc/essays/packages/)

Original specification of packages. Some semantics have changed since
the writing of this document (e.g. redirecting based on `None`
in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")).

The [`__import__()`](https://docs.python.org/3/library/importlib.html#importlib.__import__ "importlib.__import__") function

The [`import`](https://docs.python.org/3/reference/simple_stmts.html#import) statement is syntactic sugar for this function.

[The initialization of the sys.path module search path](https://docs.python.org/3/library/sys_path_init.html#sys-path-init)

The initialization of [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path").

[**PEP 235**](https://peps.python.org/pep-0235/)

Import on Case-Insensitive Platforms

[**PEP 263**](https://peps.python.org/pep-0263/)

Defining Python Source Code Encodings

[**PEP 302**](https://peps.python.org/pep-0302/)

New Import Hooks

[**PEP 328**](https://peps.python.org/pep-0328/)

Imports: Multi-Line and Absolute/Relative

[**PEP 366**](https://peps.python.org/pep-0366/)

Main module explicit relative imports

[**PEP 420**](https://peps.python.org/pep-0420/)

Implicit namespace packages

[**PEP 451**](https://peps.python.org/pep-0451/)

A ModuleSpec Type for the Import System

[**PEP 488**](https://peps.python.org/pep-0488/)

Elimination of PYO files

[**PEP 489**](https://peps.python.org/pep-0489/)

Multi-phase extension module initialization

[**PEP 552**](https://peps.python.org/pep-0552/)

Deterministic pycs

[**PEP 3120**](https://peps.python.org/pep-3120/)

Using UTF-8 as the Default Source Encoding

[**PEP 3147**](https://peps.python.org/pep-3147/)

PYC Repository Directories

## Functions [¶](https://docs.python.org/3/library/importlib.html\#functions "Link to this heading")

importlib.\_\_import\_\_( _name_, _globals=None_, _locals=None_, _fromlist=()_, _level=0_) [¶](https://docs.python.org/3/library/importlib.html#importlib.__import__ "Link to this definition")

An implementation of the built-in [`__import__()`](https://docs.python.org/3/library/functions.html#import__ "__import__") function.

Note

Programmatic importing of modules should use [`import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module")
instead of this function.

importlib.import\_module( _name_, _package=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.import_module "Link to this definition")

Import a module. The _name_ argument specifies what module to
import in absolute or relative terms
(e.g. either `pkg.mod` or `..mod`). If the name is
specified in relative terms, then the _package_ argument must be set to
the name of the package which is to act as the anchor for resolving the
package name (e.g. `import_module('..mod', 'pkg.subpkg')` will import
`pkg.mod`).

The [`import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module") function acts as a simplifying wrapper around
[`importlib.__import__()`](https://docs.python.org/3/library/importlib.html#importlib.__import__ "importlib.__import__"). This means all semantics of the function are
derived from [`importlib.__import__()`](https://docs.python.org/3/library/importlib.html#importlib.__import__ "importlib.__import__"). The most important difference
between these two functions is that [`import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module") returns the
specified package or module (e.g. `pkg.mod`), while [`__import__()`](https://docs.python.org/3/library/functions.html#import__ "__import__")
returns the top-level package or module (e.g. `pkg`).

If you are dynamically importing a module that was created since the
interpreter began execution (e.g., created a Python source file), you may
need to call [`invalidate_caches()`](https://docs.python.org/3/library/importlib.html#importlib.invalidate_caches "importlib.invalidate_caches") in order for the new module to be
noticed by the import system.

Changed in version 3.3: Parent packages are automatically imported.

importlib.invalidate\_caches() [¶](https://docs.python.org/3/library/importlib.html#importlib.invalidate_caches "Link to this definition")

Invalidate the internal caches of finders stored at
[`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path"). If a finder implements `invalidate_caches()` then it
will be called to perform the invalidation. This function should be called
if any modules are created/installed while your program is running to
guarantee all finders will notice the new module’s existence.

Added in version 3.3.

Changed in version 3.10: Namespace packages created/installed in a different [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
location after the same namespace was already imported are noticed.

importlib.reload( _module_) [¶](https://docs.python.org/3/library/importlib.html#importlib.reload "Link to this definition")

Reload a previously imported _module_. The argument must be a module object,
so it must have been successfully imported before. This is useful if you
have edited the module source file using an external editor and want to try
out the new version without leaving the Python interpreter. The return value
is the module object (which can be different if re-importing causes a
different object to be placed in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules")).

When [`reload()`](https://docs.python.org/3/library/importlib.html#importlib.reload "importlib.reload") is executed:

- Python module’s code is recompiled and the module-level code re-executed,
defining a new set of objects which are bound to names in the module’s
dictionary by reusing the [loader](https://docs.python.org/3/glossary.html#term-loader) which originally loaded the
module. The `init` function of extension modules is not called a second
time.

- As with all other objects in Python the old objects are only reclaimed
after their reference counts drop to zero.

- The names in the module namespace are updated to point to any new or
changed objects.

- Other references to the old objects (such as names external to the module) are
not rebound to refer to the new objects and must be updated in each namespace
where they occur if that is desired.


There are a number of other caveats:

When a module is reloaded, its dictionary (containing the module’s global
variables) is retained. Redefinitions of names will override the old
definitions, so this is generally not a problem. If the new version of a
module does not define a name that was defined by the old version, the old
definition remains. This feature can be used to the module’s advantage if it
maintains a global table or cache of objects — with a [`try`](https://docs.python.org/3/reference/compound_stmts.html#try)
statement it can test for the table’s presence and skip its initialization if
desired:

Copy

```
try:
    cache
except NameError:
    cache = {}
```

It is generally not very useful to reload built-in or dynamically loaded
modules. Reloading [`sys`](https://docs.python.org/3/library/sys.html#module-sys "sys: Access system-specific parameters and functions."), [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``."), [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") and other
key modules is not recommended. In many cases extension modules are not
designed to be initialized more than once, and may fail in arbitrary ways
when reloaded.

If a module imports objects from another module using [`from`](https://docs.python.org/3/reference/simple_stmts.html#from) …
[`import`](https://docs.python.org/3/reference/simple_stmts.html#import) …, calling [`reload()`](https://docs.python.org/3/library/importlib.html#importlib.reload "importlib.reload") for the other module does not
redefine the objects imported from it — one way around this is to
re-execute the `from` statement, another is to use `import`
and qualified names ( _module.name_) instead.

If a module instantiates instances of a class, reloading the module that
defines the class does not affect the method definitions of the instances —
they continue to use the old class definition. The same is true for derived
classes.

Added in version 3.4.

Changed in version 3.7: [`ModuleNotFoundError`](https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError "ModuleNotFoundError") is raised when the module being reloaded lacks
a [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec").

Warning

This function is not thread-safe. Calling it from multiple threads can result
in unexpected behavior. It’s recommended to use the [`threading.Lock`](https://docs.python.org/3/library/threading.html#threading.Lock "threading.Lock")
or other synchronization primitives for thread-safe module reloading.

## [`importlib.abc`](https://docs.python.org/3/library/importlib.html\#module-importlib.abc "importlib.abc: Abstract base classes related to import") – Abstract base classes related to import [¶](https://docs.python.org/3/library/importlib.html\#module-importlib.abc "Link to this heading")

**Source code:** [Lib/importlib/abc.py](https://github.com/python/cpython/tree/3.14/Lib/importlib/abc.py)

* * *

The [`importlib.abc`](https://docs.python.org/3/library/importlib.html#module-importlib.abc "importlib.abc: Abstract base classes related to import") module contains all of the core abstract base classes
used by [`import`](https://docs.python.org/3/reference/simple_stmts.html#import). Some subclasses of the core abstract base classes
are also provided to help in implementing the core ABCs.

ABC hierarchy:

Copy

```
object
 +-- MetaPathFinder
 +-- PathEntryFinder
 +-- Loader
      +-- ResourceLoader --------+
      +-- InspectLoader          |
           +-- ExecutionLoader --+
                                 +-- FileLoader
                                 +-- SourceLoader
```

_class_ importlib.abc.MetaPathFinder [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "Link to this definition")

An abstract base class representing a [meta path finder](https://docs.python.org/3/glossary.html#term-meta-path-finder).

Added in version 3.3.

Changed in version 3.10: No longer a subclass of `Finder`.

find\_spec( _fullname_, _path_, _target=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.find_spec "Link to this definition")

An abstract method for finding a [spec](https://docs.python.org/3/glossary.html#term-module-spec) for
the specified module. If this is a top-level import, _path_ will
be `None`. Otherwise, this is a search for a subpackage or
module and _path_ will be the value of [`__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__") from the
parent package. If a spec cannot be found, `None` is returned.
When passed in, `target` is a module object that the finder may
use to make a more educated guess about what spec to return.
[`importlib.util.spec_from_loader()`](https://docs.python.org/3/library/importlib.html#importlib.util.spec_from_loader "importlib.util.spec_from_loader") may be useful for implementing
concrete `MetaPathFinders`.

Added in version 3.4.

invalidate\_caches() [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder.invalidate_caches "Link to this definition")

An optional method which, when called, should invalidate any internal
cache used by the finder. Used by [`importlib.invalidate_caches()`](https://docs.python.org/3/library/importlib.html#importlib.invalidate_caches "importlib.invalidate_caches")
when invalidating the caches of all finders on [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path").

Changed in version 3.4: Returns `None` when called instead of [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented").

_class_ importlib.abc.PathEntryFinder [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder "Link to this definition")

An abstract base class representing a [path entry finder](https://docs.python.org/3/glossary.html#term-path-entry-finder). Though
it bears some similarities to [`MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder"), `PathEntryFinder`
is meant for use only within the path-based import subsystem provided
by [`importlib.machinery.PathFinder`](https://docs.python.org/3/library/importlib.html#importlib.machinery.PathFinder "importlib.machinery.PathFinder").

Added in version 3.3.

Changed in version 3.10: No longer a subclass of `Finder`.

find\_spec( _fullname_, _target=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder.find_spec "Link to this definition")

An abstract method for finding a [spec](https://docs.python.org/3/glossary.html#term-module-spec) for
the specified module. The finder will search for the module only
within the [path entry](https://docs.python.org/3/glossary.html#term-path-entry) to which it is assigned. If a spec
cannot be found, `None` is returned. When passed in, `target`
is a module object that the finder may use to make a more educated
guess about what spec to return. [`importlib.util.spec_from_loader()`](https://docs.python.org/3/library/importlib.html#importlib.util.spec_from_loader "importlib.util.spec_from_loader")
may be useful for implementing concrete `PathEntryFinders`.

Added in version 3.4.

invalidate\_caches() [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder.invalidate_caches "Link to this definition")

An optional method which, when called, should invalidate any internal
cache used by the finder. Used by
[`importlib.machinery.PathFinder.invalidate_caches()`](https://docs.python.org/3/library/importlib.html#importlib.machinery.PathFinder.invalidate_caches "importlib.machinery.PathFinder.invalidate_caches")
when invalidating the caches of all cached finders.

_class_ importlib.abc.Loader [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader "Link to this definition")

An abstract base class for a [loader](https://docs.python.org/3/glossary.html#term-loader).
See [**PEP 302**](https://peps.python.org/pep-0302/) for the exact definition for a loader.

Loaders that wish to support resource reading should implement a
`get_resource_reader()` method as specified by
[`importlib.resources.abc.ResourceReader`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader "importlib.resources.abc.ResourceReader").

Changed in version 3.7: Introduced the optional `get_resource_reader()` method.

create\_module( _spec_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "Link to this definition")

A method that returns the module object to use when
importing a module. This method may return `None`,
indicating that default module creation semantics should take place.

Added in version 3.4.

Changed in version 3.6: This method is no longer optional when
[`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") is defined.

exec\_module( _module_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "Link to this definition")

An abstract method that executes the module in its own namespace
when a module is imported or reloaded. The module should already
be initialized when [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") is called. When this method exists,
[`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module") must be defined.

Added in version 3.4.

Changed in version 3.6: [`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module") must also be defined.

load\_module( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "Link to this definition")

A legacy method for loading a module. If the module cannot be
loaded, [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") is raised, otherwise the loaded module is
returned.

If the requested module already exists in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules"), that
module should be used and reloaded.
Otherwise the loader should create a new module and insert it into
[`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules") before any loading begins, to prevent recursion
from the import. If the loader inserted a module and the load fails, it
must be removed by the loader from [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules"); modules already
in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules") before the loader began execution should be left
alone.

The loader should set several attributes on the module
(note that some of these attributes can change when a module is
reloaded):

- [`module.__name__`](https://docs.python.org/3/reference/datamodel.html#module.__name__ "module.__name__")

- [`module.__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__")

- [`module.__cached__`](https://docs.python.org/3/reference/datamodel.html#module.__cached__ "module.__cached__") _(deprecated)_

- [`module.__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__")

- [`module.__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__") _(deprecated)_

- [`module.__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__") _(deprecated)_


When [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") is available then backwards-compatible
functionality is provided.

Changed in version 3.4: Raise [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") when called instead of
[`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError"). Functionality provided when
[`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") is available.

Deprecated since version 3.4, will be removed in version 3.15: The recommended API for loading a module is [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module")
(and [`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module")). Loaders should implement it instead of
[`load_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "importlib.abc.Loader.load_module"). The import machinery takes care of all the
other responsibilities of [`load_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "importlib.abc.Loader.load_module") when
[`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") is implemented.

_class_ importlib.abc.ResourceLoader [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader "Link to this definition")

_Superseded by TraversableResources_

> An abstract base class for a [loader](https://docs.python.org/3/glossary.html#term-loader) which implements the optional
> [**PEP 302**](https://peps.python.org/pep-0302/) protocol for loading arbitrary resources from the storage
> back-end.
>
> Deprecated since version 3.7: This ABC is deprecated in favour of supporting resource loading
> through [`importlib.resources.abc.TraversableResources`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources "importlib.resources.abc.TraversableResources").
> This class exists for backwards compatibility only with other ABCs in
> this module.
>
> _abstractmethod_ get\_data( _path_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader.get_data "Link to this definition")
>
> > An abstract method to return the bytes for the data located at _path_.
> > Loaders that have a file-like storage back-end
> > that allows storing arbitrary data
> > can implement this abstract method to give direct access
> > to the data stored. [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is to be raised if the _path_ cannot
> > be found. The _path_ is expected to be constructed using a module’s
> > [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__") attribute or an item from a package’s
> > [`__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__").
> >
> > Changed in version 3.4: Raises [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

_class_ importlib.abc.InspectLoader [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "Link to this definition")

An abstract base class for a [loader](https://docs.python.org/3/glossary.html#term-loader) which implements the optional
[**PEP 302**](https://peps.python.org/pep-0302/) protocol for loaders that inspect modules.

get\_code( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.get_code "Link to this definition")

Return the code object for a module, or `None` if the module does not
have a code object (as would be the case, for example, for a built-in
module). Raise an [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") if loader cannot find the
requested module.

Note

While the method has a default implementation, it is suggested that
it be overridden if possible for performance.

Changed in version 3.4: No longer abstract and a concrete implementation is provided.

_abstractmethod_ get\_source( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.get_source "Link to this definition")

> An abstract method to return the source of a module. It is returned as
> a text string using [universal newlines](https://docs.python.org/3/glossary.html#term-universal-newlines), translating all
> recognized line separators into `'\n'` characters. Returns `None`
> if no source is available (e.g. a built-in module). Raises
> [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") if the loader cannot find the module specified.
>
> Changed in version 3.4: Raises [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

is\_package( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.is_package "Link to this definition")

An optional method to return a true value if the module is a package, a
false value otherwise. [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") is raised if the
[loader](https://docs.python.org/3/glossary.html#term-loader) cannot find the module.

Changed in version 3.4: Raises [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

_static_ source\_to\_code( _data_, _path='<string>'_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.source_to_code "Link to this definition")

Create a code object from Python source.

The _data_ argument can be whatever the [`compile()`](https://docs.python.org/3/library/functions.html#compile "compile") function
supports (i.e. string or bytes). The _path_ argument should be
the “path” to where the source code originated from, which can be an
abstract concept (e.g. location in a zip file).

With the subsequent code object one can execute it in a module by
running `exec(code, module.__dict__)`.

Added in version 3.4.

Changed in version 3.5: Made the method static.

exec\_module( _module_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.exec_module "Link to this definition")

Implementation of [`Loader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module").

Added in version 3.4.

load\_module( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.load_module "Link to this definition")

Implementation of [`Loader.load_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "importlib.abc.Loader.load_module").

Deprecated since version 3.4, will be removed in version 3.15: use [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.exec_module "importlib.abc.InspectLoader.exec_module") instead.

_class_ importlib.abc.ExecutionLoader [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader "Link to this definition")

An abstract base class which inherits from [`InspectLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "importlib.abc.InspectLoader") that,
when implemented, helps a module to be executed as a script. The ABC
represents an optional [**PEP 302**](https://peps.python.org/pep-0302/) protocol.

_abstractmethod_ get\_filename( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader.get_filename "Link to this definition")

> An abstract method that is to return the value of
> [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__") for the specified module. If no path is
> available, [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") is raised.
>
> If source code is available, then the method should return the path to
> the source file, regardless of whether a bytecode was used to load the
> module.
>
> Changed in version 3.4: Raises [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

_class_ importlib.abc.FileLoader( _fullname_, _path_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader "Link to this definition")

An abstract base class which inherits from [`ResourceLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader "importlib.abc.ResourceLoader") and
[`ExecutionLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader "importlib.abc.ExecutionLoader"), providing concrete implementations of
[`ResourceLoader.get_data()`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader.get_data "importlib.abc.ResourceLoader.get_data") and [`ExecutionLoader.get_filename()`](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader.get_filename "importlib.abc.ExecutionLoader.get_filename").

The _fullname_ argument is a fully resolved name of the module the loader is
to handle. The _path_ argument is the path to the file for the module.

Added in version 3.3.

name [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.name "Link to this definition")

The name of the module the loader can handle.

path [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.path "Link to this definition")

Path to the file of the module.

load\_module( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.load_module "Link to this definition")

Calls super’s `load_module()`.

Deprecated since version 3.4, will be removed in version 3.15: Use [`Loader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") instead.

_abstractmethod_ get\_filename( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.get_filename "Link to this definition")

Returns [`path`](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.path "importlib.abc.FileLoader.path").

_abstractmethod_ get\_data( _path_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader.get_data "Link to this definition")

Reads _path_ as a binary file and returns the bytes from it.

_class_ importlib.abc.SourceLoader [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader "Link to this definition")

An abstract base class for implementing source (and optionally bytecode)
file loading. The class inherits from both [`ResourceLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader "importlib.abc.ResourceLoader") and
[`ExecutionLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader "importlib.abc.ExecutionLoader"), requiring the implementation of:

- [`ResourceLoader.get_data()`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceLoader.get_data "importlib.abc.ResourceLoader.get_data")

- [`ExecutionLoader.get_filename()`](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader.get_filename "importlib.abc.ExecutionLoader.get_filename")

Should only return the path to the source file; sourceless
loading is not supported.


The abstract methods defined by this class are to add optional bytecode
file support. Not implementing these optional methods (or causing them to
raise [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError")) causes the loader to
only work with source code. Implementing the methods allows the loader to
work with source _and_ bytecode files; it does not allow for _sourceless_
loading where only bytecode is provided. Bytecode files are an
optimization to speed up loading by removing the parsing step of Python’s
compiler, and so no bytecode-specific API is exposed.

path\_stats( _path_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.path_stats "Link to this definition")

Optional abstract method which returns a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") containing
metadata about the specified path. Supported dictionary keys are:

- `'mtime'` (mandatory): an integer or floating-point number
representing the modification time of the source code;

- `'size'` (optional): the size in bytes of the source code.


Any other keys in the dictionary are ignored, to allow for future
extensions. If the path cannot be handled, [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") is raised.

Added in version 3.3.

Changed in version 3.4: Raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

path\_mtime( _path_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.path_mtime "Link to this definition")

Optional abstract method which returns the modification time for the
specified path.

Deprecated since version 3.3: This method is deprecated in favour of [`path_stats()`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.path_stats "importlib.abc.SourceLoader.path_stats"). You don’t
have to implement it, but it is still available for compatibility
purposes. Raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") if the path cannot be handled.

Changed in version 3.4: Raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") instead of [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError").

set\_data( _path_, _data_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.set_data "Link to this definition")

Optional abstract method which writes the specified bytes to a file
path. Any intermediate directories which do not exist are to be created
automatically.

When writing to the path fails because the path is read-only
( [`errno.EACCES`](https://docs.python.org/3/library/errno.html#errno.EACCES "errno.EACCES")/ [`PermissionError`](https://docs.python.org/3/library/exceptions.html#PermissionError "PermissionError")), do not propagate the
exception.

Changed in version 3.4: No longer raises [`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") when called.

get\_code( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.get_code "Link to this definition")

Concrete implementation of [`InspectLoader.get_code()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.get_code "importlib.abc.InspectLoader.get_code").

exec\_module( _module_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.exec_module "Link to this definition")

Concrete implementation of [`Loader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module").

Added in version 3.4.

load\_module( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.load_module "Link to this definition")

Concrete implementation of [`Loader.load_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "importlib.abc.Loader.load_module").

Deprecated since version 3.4, will be removed in version 3.15: Use [`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.exec_module "importlib.abc.SourceLoader.exec_module") instead.

get\_source( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.get_source "Link to this definition")

Concrete implementation of [`InspectLoader.get_source()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.get_source "importlib.abc.InspectLoader.get_source").

is\_package( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.is_package "Link to this definition")

Concrete implementation of [`InspectLoader.is_package()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.is_package "importlib.abc.InspectLoader.is_package"). A module
is determined to be a package if its file path (as provided by
[`ExecutionLoader.get_filename()`](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader.get_filename "importlib.abc.ExecutionLoader.get_filename")) is a file named
`__init__` when the file extension is removed **and** the module name
itself does not end in `__init__`.

_class_ importlib.abc.ResourceReader [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceReader "Link to this definition")

_Superseded by TraversableResources_

An [abstract base class](https://docs.python.org/3/glossary.html#term-abstract-base-class) to provide the ability to read
_resources_.

From the perspective of this ABC, a _resource_ is a binary
artifact that is shipped within a package. Typically this is
something like a data file that lives next to the `__init__.py`
file of the package. The purpose of this class is to help abstract
out the accessing of such data files so that it does not matter if
the package and its data file(s) are stored e.g. in a zip file
versus on the file system.

For any of methods of this class, a _resource_ argument is
expected to be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) which represents
conceptually just a file name. This means that no subdirectory
paths should be included in the _resource_ argument. This is
because the location of the package the reader is for, acts as the
“directory”. Hence the metaphor for directories and file
names is packages and resources, respectively. This is also why
instances of this class are expected to directly correlate to
a specific package (instead of potentially representing multiple
packages or a module).

Loaders that wish to support resource reading are expected to
provide a method called `get_resource_reader(fullname)` which
returns an object implementing this ABC’s interface. If the module
specified by fullname is not a package, this method should return
[`None`](https://docs.python.org/3/library/constants.html#None "None"). An object compatible with this ABC should only be
returned when the specified module is a package.

Added in version 3.7.

Deprecated since version 3.12, removed in version 3.14: Use [`importlib.resources.abc.TraversableResources`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources "importlib.resources.abc.TraversableResources") instead.

_abstractmethod_ open\_resource( _resource_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceReader.open_resource "Link to this definition")

> Returns an opened, [file-like object](https://docs.python.org/3/glossary.html#term-file-like-object) for binary reading
> of the _resource_.
>
> If the resource cannot be found, [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") is
> raised.

_abstractmethod_ resource\_path( _resource_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceReader.resource_path "Link to this definition")

> Returns the file system path to the _resource_.
>
> If the resource does not concretely exist on the file system,
> raise [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError").

_abstractmethod_ is\_resource( _name_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceReader.is_resource "Link to this definition")

> Returns `True` if the named _name_ is considered a resource.
> [`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") is raised if _name_ does not exist.

_abstractmethod_ contents() [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceReader.contents "Link to this definition")

> Returns an [iterable](https://docs.python.org/3/glossary.html#term-iterable) of strings over the contents of
> the package. Do note that it is not required that all names
> returned by the iterator be actual resources, e.g. it is
> acceptable to return names for which [`is_resource()`](https://docs.python.org/3/library/importlib.html#importlib.abc.ResourceReader.is_resource "importlib.abc.ResourceReader.is_resource") would
> be false.
>
> Allowing non-resource names to be returned is to allow for
> situations where how a package and its resources are stored
> are known a priori and the non-resource names would be useful.
> For instance, returning subdirectory names is allowed so that
> when it is known that the package and resources are stored on
> the file system then those subdirectory names can be used
> directly.
>
> The abstract method returns an iterable of no items.

_class_ importlib.abc.Traversable [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Traversable "Link to this definition")

An object with a subset of [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html#pathlib.Path "pathlib.Path") methods suitable for
traversing directories and opening files.

For a representation of the object on the file-system, use
[`importlib.resources.as_file()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.as_file "importlib.resources.as_file").

Added in version 3.9.

Deprecated since version 3.12, removed in version 3.14: Use [`importlib.resources.abc.Traversable`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable") instead.

name [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Traversable.name "Link to this definition")

Abstract. The base name of this object without any parent references.

_abstractmethod_ iterdir() [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Traversable.iterdir "Link to this definition")

Yield `Traversable` objects in `self`.

_abstractmethod_ is\_dir() [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Traversable.is_dir "Link to this definition")

Return `True` if `self` is a directory.

_abstractmethod_ is\_file() [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Traversable.is_file "Link to this definition")

Return `True` if `self` is a file.

_abstractmethod_ joinpath( _child_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Traversable.joinpath "Link to this definition")

Return Traversable child in `self`.

_abstractmethod_\_\_truediv\_\_( _child_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Traversable.__truediv__ "Link to this definition")

Return `Traversable` child in `self`.

_abstractmethod_ open( _mode='r'_, _\*args_, _\*\*kwargs_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Traversable.open "Link to this definition")

_mode_ may be ‘r’ or ‘rb’ to open as text or binary. Return a handle
suitable for reading (same as [`pathlib.Path.open`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.open "pathlib.Path.open")).

When opening as text, accepts encoding parameters such as those
accepted by [`io.TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper").

read\_bytes() [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Traversable.read_bytes "Link to this definition")

Read contents of `self` as bytes.

read\_text( _encoding=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.Traversable.read_text "Link to this definition")

Read contents of `self` as text.

_class_ importlib.abc.TraversableResources [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.TraversableResources "Link to this definition")

An abstract base class for resource readers capable of serving
the [`importlib.resources.files()`](https://docs.python.org/3/library/importlib.resources.html#importlib.resources.files "importlib.resources.files") interface. Subclasses
[`importlib.resources.abc.ResourceReader`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader "importlib.resources.abc.ResourceReader") and provides
concrete implementations of the [`importlib.resources.abc.ResourceReader`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.ResourceReader "importlib.resources.abc.ResourceReader")’s
abstract methods. Therefore, any loader supplying
[`importlib.abc.TraversableResources`](https://docs.python.org/3/library/importlib.html#importlib.abc.TraversableResources "importlib.abc.TraversableResources") also supplies ResourceReader.

Loaders that wish to support resource reading are expected to
implement this interface.

Added in version 3.9.

Deprecated since version 3.12, removed in version 3.14: Use [`importlib.resources.abc.TraversableResources`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.TraversableResources "importlib.resources.abc.TraversableResources") instead.

_abstractmethod_ files() [¶](https://docs.python.org/3/library/importlib.html#importlib.abc.TraversableResources.files "Link to this definition")

Returns a [`importlib.resources.abc.Traversable`](https://docs.python.org/3/library/importlib.resources.abc.html#importlib.resources.abc.Traversable "importlib.resources.abc.Traversable") object for the loaded
package.

## [`importlib.machinery`](https://docs.python.org/3/library/importlib.html\#module-importlib.machinery "importlib.machinery: Importers and path hooks") – Importers and path hooks [¶](https://docs.python.org/3/library/importlib.html\#module-importlib.machinery "Link to this heading")

**Source code:** [Lib/importlib/machinery.py](https://github.com/python/cpython/tree/3.14/Lib/importlib/machinery.py)

* * *

This module contains the various objects that help [`import`](https://docs.python.org/3/reference/simple_stmts.html#import)
find and load modules.

importlib.machinery.SOURCE\_SUFFIXES [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SOURCE_SUFFIXES "Link to this definition")

A list of strings representing the recognized file suffixes for source
modules.

Added in version 3.3.

importlib.machinery.DEBUG\_BYTECODE\_SUFFIXES [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.DEBUG_BYTECODE_SUFFIXES "Link to this definition")

A list of strings representing the file suffixes for non-optimized bytecode
modules.

Added in version 3.3.

Deprecated since version 3.5: Use [`BYTECODE_SUFFIXES`](https://docs.python.org/3/library/importlib.html#importlib.machinery.BYTECODE_SUFFIXES "importlib.machinery.BYTECODE_SUFFIXES") instead.

importlib.machinery.OPTIMIZED\_BYTECODE\_SUFFIXES [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES "Link to this definition")

A list of strings representing the file suffixes for optimized bytecode
modules.

Added in version 3.3.

Deprecated since version 3.5: Use [`BYTECODE_SUFFIXES`](https://docs.python.org/3/library/importlib.html#importlib.machinery.BYTECODE_SUFFIXES "importlib.machinery.BYTECODE_SUFFIXES") instead.

importlib.machinery.BYTECODE\_SUFFIXES [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.BYTECODE_SUFFIXES "Link to this definition")

A list of strings representing the recognized file suffixes for bytecode
modules (including the leading dot).

Added in version 3.3.

Changed in version 3.5: The value is no longer dependent on `__debug__`.

importlib.machinery.EXTENSION\_SUFFIXES [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.EXTENSION_SUFFIXES "Link to this definition")

A list of strings representing the recognized file suffixes for
extension modules.

Added in version 3.3.

importlib.machinery.all\_suffixes() [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.all_suffixes "Link to this definition")

Returns a combined list of strings representing all file suffixes for
modules recognized by the standard import machinery. This is a
helper for code which simply needs to know if a filesystem path
potentially refers to a module without needing any details on the kind
of module (for example, [`inspect.getmodulename()`](https://docs.python.org/3/library/inspect.html#inspect.getmodulename "inspect.getmodulename")).

Added in version 3.3.

_class_ importlib.machinery.BuiltinImporter [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.BuiltinImporter "Link to this definition")

An [importer](https://docs.python.org/3/glossary.html#term-importer) for built-in modules. All known built-in modules are
listed in [`sys.builtin_module_names`](https://docs.python.org/3/library/sys.html#sys.builtin_module_names "sys.builtin_module_names"). This class implements the
[`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder") and
[`importlib.abc.InspectLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "importlib.abc.InspectLoader") ABCs.

Only class methods are defined by this class to alleviate the need for
instantiation.

Changed in version 3.5: As part of [**PEP 489**](https://peps.python.org/pep-0489/), the builtin importer now implements
`Loader.create_module()` and `Loader.exec_module()`

_class_ importlib.machinery.FrozenImporter [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.FrozenImporter "Link to this definition")

An [importer](https://docs.python.org/3/glossary.html#term-importer) for frozen modules. This class implements the
[`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder") and
[`importlib.abc.InspectLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "importlib.abc.InspectLoader") ABCs.

Only class methods are defined by this class to alleviate the need for
instantiation.

Changed in version 3.4: Gained `create_module()` and `exec_module()`
methods.

_class_ importlib.machinery.WindowsRegistryFinder [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.WindowsRegistryFinder "Link to this definition")

[Finder](https://docs.python.org/3/glossary.html#term-finder) for modules declared in the Windows registry. This class
implements the [`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder") ABC.

Only class methods are defined by this class to alleviate the need for
instantiation.

Added in version 3.3.

Deprecated since version 3.6: Use [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") configuration instead. Future versions of Python may
not enable this finder by default.

_class_ importlib.machinery.PathFinder [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.PathFinder "Link to this definition")

A [Finder](https://docs.python.org/3/glossary.html#term-finder) for [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") and package `__path__` attributes.
This class implements the [`importlib.abc.MetaPathFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.MetaPathFinder "importlib.abc.MetaPathFinder") ABC.

Only class methods are defined by this class to alleviate the need for
instantiation.

_classmethod_ find\_spec( _fullname_, _path=None_, _target=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.PathFinder.find_spec "Link to this definition")

Class method that attempts to find a [spec](https://docs.python.org/3/glossary.html#term-module-spec)
for the module specified by _fullname_ on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") or, if
defined, on _path_. For each path entry that is searched,
[`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache") is checked. If a non-false object
is found then it is used as the [path entry finder](https://docs.python.org/3/glossary.html#term-path-entry-finder) to look
for the module being searched for. If no entry is found in
[`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache"), then [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks") is
searched for a finder for the path entry and, if found, is stored
in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache") along with being queried about
the module. If no finder is ever found then `None` is both
stored in the cache and returned.

Added in version 3.4.

Changed in version 3.5: If the current working directory – represented by an empty string –
is no longer valid then `None` is returned but no value is cached
in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache").

_classmethod_ invalidate\_caches() [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.PathFinder.invalidate_caches "Link to this definition")

Calls [`importlib.abc.PathEntryFinder.invalidate_caches()`](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder.invalidate_caches "importlib.abc.PathEntryFinder.invalidate_caches") on all
finders stored in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache") that define the method.
Otherwise entries in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache") set to `None` are
deleted.

Changed in version 3.7: Entries of `None` in [`sys.path_importer_cache`](https://docs.python.org/3/library/sys.html#sys.path_importer_cache "sys.path_importer_cache") are deleted.

Changed in version 3.4: Calls objects in [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks") with the current working
directory for `''` (i.e. the empty string).

_class_ importlib.machinery.FileFinder( _path_, _\*loader\_details_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder "Link to this definition")

A concrete implementation of [`importlib.abc.PathEntryFinder`](https://docs.python.org/3/library/importlib.html#importlib.abc.PathEntryFinder "importlib.abc.PathEntryFinder") which
caches results from the file system.

The _path_ argument is the directory for which the finder is in charge of
searching.

The _loader\_details_ argument is a variable number of 2-item tuples each
containing a loader and a sequence of file suffixes the loader recognizes.
The loaders are expected to be callables which accept two arguments of
the module’s name and the path to the file found.

The finder will cache the directory contents as necessary, making stat calls
for each module search to verify the cache is not outdated. Because cache
staleness relies upon the granularity of the operating system’s state
information of the file system, there is a potential race condition of
searching for a module, creating a new file, and then searching for the
module the new file represents. If the operations happen fast enough to fit
within the granularity of stat calls, then the module search will fail. To
prevent this from happening, when you create a module dynamically, make sure
to call [`importlib.invalidate_caches()`](https://docs.python.org/3/library/importlib.html#importlib.invalidate_caches "importlib.invalidate_caches").

Added in version 3.3.

path [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder.path "Link to this definition")

The path the finder will search in.

find\_spec( _fullname_, _target=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder.find_spec "Link to this definition")

Attempt to find the spec to handle _fullname_ within [`path`](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder.path "importlib.machinery.FileFinder.path").

Added in version 3.4.

invalidate\_caches() [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder.invalidate_caches "Link to this definition")

Clear out the internal cache.

_classmethod_ path\_hook( _\*loader\_details_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder.path_hook "Link to this definition")

A class method which returns a closure for use on [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks").
An instance of [`FileFinder`](https://docs.python.org/3/library/importlib.html#importlib.machinery.FileFinder "importlib.machinery.FileFinder") is returned by the closure using the
path argument given to the closure directly and _loader\_details_
indirectly.

If the argument to the closure is not an existing directory,
[`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") is raised.

_class_ importlib.machinery.SourceFileLoader( _fullname_, _path_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader "Link to this definition")

A concrete implementation of [`importlib.abc.SourceLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader "importlib.abc.SourceLoader") by
subclassing [`importlib.abc.FileLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader "importlib.abc.FileLoader") and providing some concrete
implementations of other methods.

Added in version 3.3.

name [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.name "Link to this definition")

The name of the module that this loader will handle.

path [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.path "Link to this definition")

The path to the source file.

is\_package( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.is_package "Link to this definition")

Return `True` if [`path`](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.path "importlib.machinery.SourceFileLoader.path") appears to be for a package.

path\_stats( _path_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.path_stats "Link to this definition")

Concrete implementation of [`importlib.abc.SourceLoader.path_stats()`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.path_stats "importlib.abc.SourceLoader.path_stats").

set\_data( _path_, _data_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.set_data "Link to this definition")

Concrete implementation of [`importlib.abc.SourceLoader.set_data()`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader.set_data "importlib.abc.SourceLoader.set_data").

load\_module( _name=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourceFileLoader.load_module "Link to this definition")

Concrete implementation of [`importlib.abc.Loader.load_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "importlib.abc.Loader.load_module") where
specifying the name of the module to load is optional.

Deprecated since version 3.6, will be removed in version 3.15: Use [`importlib.abc.Loader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") instead.

_class_ importlib.machinery.SourcelessFileLoader( _fullname_, _path_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader "Link to this definition")

A concrete implementation of [`importlib.abc.FileLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.FileLoader "importlib.abc.FileLoader") which can
import bytecode files (i.e. no source code files exist).

Please note that direct use of bytecode files (and thus not source code
files) inhibits your modules from being usable by all Python
implementations or new versions of Python which change the bytecode
format.

Added in version 3.3.

name [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.name "Link to this definition")

The name of the module the loader will handle.

path [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.path "Link to this definition")

The path to the bytecode file.

is\_package( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.is_package "Link to this definition")

Determines if the module is a package based on [`path`](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.path "importlib.machinery.SourcelessFileLoader.path").

get\_code( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.get_code "Link to this definition")

Returns the code object for [`name`](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.name "importlib.machinery.SourcelessFileLoader.name") created from [`path`](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.path "importlib.machinery.SourcelessFileLoader.path").

get\_source( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.get_source "Link to this definition")

Returns `None` as bytecode files have no source when this loader is
used.

load\_module( _name=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.SourcelessFileLoader.load_module "Link to this definition")

Concrete implementation of [`importlib.abc.Loader.load_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.load_module "importlib.abc.Loader.load_module") where
specifying the name of the module to load is optional.

Deprecated since version 3.6, will be removed in version 3.15: Use [`importlib.abc.Loader.exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") instead.

_class_ importlib.machinery.ExtensionFileLoader( _fullname_, _path_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader "Link to this definition")

A concrete implementation of [`importlib.abc.ExecutionLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.ExecutionLoader "importlib.abc.ExecutionLoader") for
extension modules.

The _fullname_ argument specifies the name of the module the loader is to
support. The _path_ argument is the path to the extension module’s file.

Note that, by default, importing an extension module will fail
in subinterpreters if it doesn’t implement multi-phase init
(see [**PEP 489**](https://peps.python.org/pep-0489/)), even if it would otherwise import successfully.

Added in version 3.3.

Changed in version 3.12: Multi-phase init is now required for use in subinterpreters.

name [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.name "Link to this definition")

Name of the module the loader supports.

path [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.path "Link to this definition")

Path to the extension module.

create\_module( _spec_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.create_module "Link to this definition")

Creates the module object from the given specification in accordance
with [**PEP 489**](https://peps.python.org/pep-0489/).

Added in version 3.5.

exec\_module( _module_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.exec_module "Link to this definition")

Initializes the given module object in accordance with [**PEP 489**](https://peps.python.org/pep-0489/).

Added in version 3.5.

is\_package( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.is_package "Link to this definition")

Returns `True` if the file path points to a package’s `__init__`
module based on [`EXTENSION_SUFFIXES`](https://docs.python.org/3/library/importlib.html#importlib.machinery.EXTENSION_SUFFIXES "importlib.machinery.EXTENSION_SUFFIXES").

get\_code( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.get_code "Link to this definition")

Returns `None` as extension modules lack a code object.

get\_source( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.get_source "Link to this definition")

Returns `None` as extension modules do not have source code.

get\_filename( _fullname_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.get_filename "Link to this definition")

Returns [`path`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader.path "importlib.machinery.ExtensionFileLoader.path").

Added in version 3.4.

_class_ importlib.machinery.NamespaceLoader( _name_, _path_, _path\_finder_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.NamespaceLoader "Link to this definition")

A concrete implementation of [`importlib.abc.InspectLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader "importlib.abc.InspectLoader") for
namespace packages. This is an alias for a private class and is only made
public for introspecting the `__loader__` attribute on namespace
packages:

Copy

```
>>> from importlib.machinery import NamespaceLoader
>>> import my_namespace
>>> isinstance(my_namespace.__loader__, NamespaceLoader)
True
>>> import importlib.abc
>>> isinstance(my_namespace.__loader__, importlib.abc.Loader)
True
```

Added in version 3.11.

_class_ importlib.machinery.ModuleSpec( _name_, _loader_, _\*_, _origin=None_, _loader\_state=None_, _is\_package=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "Link to this definition")

A specification for a module’s import-system-related state. This is
typically exposed as the module’s [`__spec__`](https://docs.python.org/3/reference/datamodel.html#module.__spec__ "module.__spec__") attribute. Many
of these attributes are also available directly on a module: for example,
`module.__spec__.origin == module.__file__`. Note, however, that
while the _values_ are usually equivalent, they can differ since there is
no synchronization between the two objects. For example, it is possible to
update the module’s [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__") at runtime and this will not be
automatically reflected in the module’s
[`__spec__.origin`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.origin "importlib.machinery.ModuleSpec.origin"), and vice versa.

Added in version 3.4.

name [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.name "Link to this definition")

The module’s fully qualified name (see [`module.__name__`](https://docs.python.org/3/reference/datamodel.html#module.__name__ "module.__name__")).
The [finder](https://docs.python.org/3/glossary.html#term-finder) should always set this attribute to a non-empty string.

loader [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.loader "Link to this definition")

The [loader](https://docs.python.org/3/glossary.html#term-loader) used to load the module (see [`module.__loader__`](https://docs.python.org/3/reference/datamodel.html#module.__loader__ "module.__loader__")).
The [finder](https://docs.python.org/3/glossary.html#term-finder) should always set this attribute.

origin [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.origin "Link to this definition")

The location the [loader](https://docs.python.org/3/glossary.html#term-loader) should use to load the module
(see [`module.__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__")).
For example, for modules loaded from a `.py` file this is the filename.
The [finder](https://docs.python.org/3/glossary.html#term-finder) should always set this attribute to a meaningful value
for the [loader](https://docs.python.org/3/glossary.html#term-loader) to use. In the uncommon case that there is not one
(like for namespace packages), it should be set to `None`.

submodule\_search\_locations [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.submodule_search_locations "Link to this definition")

A (possibly empty) [sequence](https://docs.python.org/3/glossary.html#term-sequence) of strings enumerating the locations
in which a package’s submodules will be found
(see [`module.__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__")). Most of the time there will only be a
single directory in this list.

The [finder](https://docs.python.org/3/glossary.html#term-finder) should set this attribute to a sequence, even an empty
one, to indicate
to the import system that the module is a package. It should be set to `None` for
non-package modules. It is set automatically later to a special object for
namespace packages.

loader\_state [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.loader_state "Link to this definition")

The [finder](https://docs.python.org/3/glossary.html#term-finder) may set this attribute to an object containing additional,
module-specific data to use when loading the module. Otherwise it should be
set to `None`.

cached [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.cached "Link to this definition")

The filename of a compiled version of the module’s code
(see [`module.__cached__`](https://docs.python.org/3/reference/datamodel.html#module.__cached__ "module.__cached__")).
The [finder](https://docs.python.org/3/glossary.html#term-finder) should always set this attribute but it may be `None`
for modules that do not need compiled code stored.

parent [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.parent "Link to this definition")

(Read-only) The fully qualified name of the package the module is in (or the
empty string for a top-level module).
See [`module.__package__`](https://docs.python.org/3/reference/datamodel.html#module.__package__ "module.__package__").
If the module is a package then this is the same as [`name`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.name "importlib.machinery.ModuleSpec.name").

has\_location [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.has_location "Link to this definition")

`True` if the spec’s [`origin`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec.origin "importlib.machinery.ModuleSpec.origin") refers to a loadable location,
`False` otherwise. This value impacts how `origin` is interpreted
and how the module’s [`__file__`](https://docs.python.org/3/reference/datamodel.html#module.__file__ "module.__file__") is populated.

_class_ importlib.machinery.AppleFrameworkLoader( _name_, _path_) [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.AppleFrameworkLoader "Link to this definition")

A specialization of [`importlib.machinery.ExtensionFileLoader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader "importlib.machinery.ExtensionFileLoader") that
is able to load extension modules in Framework format.

For compatibility with the iOS App Store, _all_ binary modules in an iOS app
must be dynamic libraries, contained in a framework with appropriate
metadata, stored in the `Frameworks` folder of the packaged app. There can
be only a single binary per framework, and there can be no executable binary
material outside the Frameworks folder.

To accommodate this requirement, when running on iOS, extension module
binaries are _not_ packaged as `.so` files on `sys.path`, but as
individual standalone frameworks. To discover those frameworks, this loader
is registered against the `.fwork` file extension, with a `.fwork`
file acting as a placeholder in the original location of the binary on
`sys.path`. The `.fwork` file contains the path of the actual binary in
the `Frameworks` folder, relative to the app bundle. To allow for
resolving a framework-packaged binary back to the original location, the
framework is expected to contain a `.origin` file that contains the
location of the `.fwork` file, relative to the app bundle.

For example, consider the case of an import `from foo.bar import _whiz`,
where `_whiz` is implemented with the binary module
`sources/foo/bar/_whiz.abi3.so`, with `sources` being the location
registered on `sys.path`, relative to the application bundle. This module
_must_ be distributed as
`Frameworks/foo.bar._whiz.framework/foo.bar._whiz` (creating the framework
name from the full import path of the module), with an `Info.plist` file
in the `.framework` directory identifying the binary as a framework. The
`foo.bar._whiz` module would be represented in the original location with
a `sources/foo/bar/_whiz.abi3.fwork` marker file, containing the path
`Frameworks/foo.bar._whiz/foo.bar._whiz`. The framework would also contain
`Frameworks/foo.bar._whiz.framework/foo.bar._whiz.origin`, containing the
path to the `.fwork` file.

When a module is loaded with this loader, the `__file__` for the module
will report as the location of the `.fwork` file. This allows code to use
the `__file__` of a module as an anchor for file system traversal.
However, the spec origin will reference the location of the _actual_ binary
in the `.framework` folder.

The Xcode project building the app is responsible for converting any `.so`
files from wherever they exist in the `PYTHONPATH` into frameworks in the
`Frameworks` folder (including stripping extensions from the module file,
the addition of framework metadata, and signing the resulting framework),
and creating the `.fwork` and `.origin` files. This will usually be done
with a build step in the Xcode project; see the iOS documentation for
details on how to construct this build step.

Added in version 3.13.

[Availability](https://docs.python.org/3/library/intro.html#availability): iOS.

name [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.AppleFrameworkLoader.name "Link to this definition")

Name of the module the loader supports.

path [¶](https://docs.python.org/3/library/importlib.html#importlib.machinery.AppleFrameworkLoader.path "Link to this definition")

Path to the `.fwork` file for the extension module.

## [`importlib.util`](https://docs.python.org/3/library/importlib.html\#module-importlib.util "importlib.util: Utility code for importers") – Utility code for importers [¶](https://docs.python.org/3/library/importlib.html\#module-importlib.util "Link to this heading")

**Source code:** [Lib/importlib/util.py](https://github.com/python/cpython/tree/3.14/Lib/importlib/util.py)

* * *

This module contains the various objects that help in the construction of
an [importer](https://docs.python.org/3/glossary.html#term-importer).

importlib.util.MAGIC\_NUMBER [¶](https://docs.python.org/3/library/importlib.html#importlib.util.MAGIC_NUMBER "Link to this definition")

The bytes which represent the bytecode version number. If you need help with
loading/writing bytecode then consider [`importlib.abc.SourceLoader`](https://docs.python.org/3/library/importlib.html#importlib.abc.SourceLoader "importlib.abc.SourceLoader").

Added in version 3.4.

importlib.util.cache\_from\_source( _path_, _debug\_override=None_, _\*_, _optimization=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.util.cache_from_source "Link to this definition")

Return the [**PEP 3147**](https://peps.python.org/pep-3147/)/ [**PEP 488**](https://peps.python.org/pep-0488/) path to the byte-compiled file associated
with the source _path_. For example, if _path_ is `/foo/bar/baz.py` the return
value would be `/foo/bar/__pycache__/baz.cpython-32.pyc` for Python 3.2.
The `cpython-32` string comes from the current magic tag (see
`get_tag()`; if `sys.implementation.cache_tag` is not defined then
[`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") will be raised).

The _optimization_ parameter is used to specify the optimization level of the
bytecode file. An empty string represents no optimization, so
`/foo/bar/baz.py` with an _optimization_ of `''` will result in a
bytecode path of `/foo/bar/__pycache__/baz.cpython-32.pyc`. `None` causes
the interpreter’s optimization level to be used. Any other value’s string
representation is used, so `/foo/bar/baz.py` with an _optimization_ of
`2` will lead to the bytecode path of
`/foo/bar/__pycache__/baz.cpython-32.opt-2.pyc`. The string representation
of _optimization_ can only be alphanumeric, else [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.

The _debug\_override_ parameter is deprecated and can be used to override
the system’s value for `__debug__`. A `True` value is the equivalent of
setting _optimization_ to the empty string. A `False` value is the same as
setting _optimization_ to `1`. If both _debug\_override_ an _optimization_
are not `None` then [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") is raised.

Added in version 3.4.

Changed in version 3.5: The _optimization_ parameter was added and the _debug\_override_ parameter
was deprecated.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

importlib.util.source\_from\_cache( _path_) [¶](https://docs.python.org/3/library/importlib.html#importlib.util.source_from_cache "Link to this definition")

Given the _path_ to a [**PEP 3147**](https://peps.python.org/pep-3147/) file name, return the associated source code
file path. For example, if _path_ is
`/foo/bar/__pycache__/baz.cpython-32.pyc` the returned path would be
`/foo/bar/baz.py`. _path_ need not exist, however if it does not conform
to [**PEP 3147**](https://peps.python.org/pep-3147/) or [**PEP 488**](https://peps.python.org/pep-0488/) format, a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. If
`sys.implementation.cache_tag` is not defined,
[`NotImplementedError`](https://docs.python.org/3/library/exceptions.html#NotImplementedError "NotImplementedError") is raised.

Added in version 3.4.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

importlib.util.decode\_source( _source\_bytes_) [¶](https://docs.python.org/3/library/importlib.html#importlib.util.decode_source "Link to this definition")

Decode the given bytes representing source code and return it as a string
with universal newlines (as required by
[`importlib.abc.InspectLoader.get_source()`](https://docs.python.org/3/library/importlib.html#importlib.abc.InspectLoader.get_source "importlib.abc.InspectLoader.get_source")).

Added in version 3.4.

importlib.util.resolve\_name( _name_, _package_) [¶](https://docs.python.org/3/library/importlib.html#importlib.util.resolve_name "Link to this definition")

Resolve a relative module name to an absolute one.

If **name** has no leading dots, then **name** is simply returned. This
allows for usage such as
`importlib.util.resolve_name('sys', __spec__.parent)` without doing a
check to see if the **package** argument is needed.

[`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") is raised if **name** is a relative module name but
**package** is a false value (e.g. `None` or the empty string).
[`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") is also raised if a relative name would escape its
containing package (e.g. requesting `..bacon` from within the `spam`
package).

Added in version 3.3.

Changed in version 3.9: To improve consistency with import statements, raise
[`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") instead of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") for invalid relative
import attempts.

importlib.util.find\_spec( _name_, _package=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.util.find_spec "Link to this definition")

Find the [spec](https://docs.python.org/3/glossary.html#term-module-spec) for a module, optionally relative to
the specified **package** name. If the module is in [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules"),
then `sys.modules[name].__spec__` is returned (unless the spec would be
`None` or is not set, in which case [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised).
Otherwise a search using [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path") is done. `None` is
returned if no spec is found.

If **name** is for a submodule (contains a dot), the parent module is
automatically imported.

**name** and **package** work the same as for `import_module()`.

Added in version 3.4.

Changed in version 3.7: Raises [`ModuleNotFoundError`](https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError "ModuleNotFoundError") instead of [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") if
**package** is in fact not a package (i.e. lacks a
[`__path__`](https://docs.python.org/3/reference/datamodel.html#module.__path__ "module.__path__") attribute).

importlib.util.module\_from\_spec( _spec_) [¶](https://docs.python.org/3/library/importlib.html#importlib.util.module_from_spec "Link to this definition")

Create a new module based on **spec** and
[`spec.loader.create_module`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module").

If [`spec.loader.create_module`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module")
does not return `None`, then any pre-existing attributes will not be reset.
Also, no [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError") will be raised if triggered while accessing
**spec** or setting an attribute on the module.

This function is preferred over using [`types.ModuleType`](https://docs.python.org/3/library/types.html#types.ModuleType "types.ModuleType") to create a
new module as **spec** is used to set as many import-controlled attributes on
the module as possible.

Added in version 3.5.

importlib.util.spec\_from\_loader( _name_, _loader_, _\*_, _origin=None_, _is\_package=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.util.spec_from_loader "Link to this definition")

A factory function for creating a [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec")
instance based on a loader. The parameters have the same meaning as they do
for ModuleSpec. The function uses available [loader](https://docs.python.org/3/glossary.html#term-loader) APIs, such as
`InspectLoader.is_package()`, to fill in any missing
information on the spec.

Added in version 3.4.

importlib.util.spec\_from\_file\_location( _name_, _location_, _\*_, _loader=None_, _submodule\_search\_locations=None_) [¶](https://docs.python.org/3/library/importlib.html#importlib.util.spec_from_file_location "Link to this definition")

A factory function for creating a [`ModuleSpec`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ModuleSpec "importlib.machinery.ModuleSpec")
instance based on the path to a file. Missing information will be filled in
on the spec by making use of loader APIs and by the implication that the
module will be file-based.

Added in version 3.4.

Changed in version 3.6: Accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

importlib.util.source\_hash( _source\_bytes_) [¶](https://docs.python.org/3/library/importlib.html#importlib.util.source_hash "Link to this definition")

Return the hash of _source\_bytes_ as bytes. A hash-based `.pyc` file embeds
the [`source_hash()`](https://docs.python.org/3/library/importlib.html#importlib.util.source_hash "importlib.util.source_hash") of the corresponding source file’s contents in its
header.

Added in version 3.7.

importlib.util.\_incompatible\_extension\_module\_restrictions( _\*_, _disable\_check_) [¶](https://docs.python.org/3/library/importlib.html#importlib.util._incompatible_extension_module_restrictions "Link to this definition")

A context manager that can temporarily skip the compatibility check
for extension modules. By default the check is enabled and will fail
when a single-phase init module is imported in a subinterpreter.
It will also fail for a multi-phase init module that doesn’t
explicitly support a per-interpreter GIL, when imported
in an interpreter with its own GIL.

Note that this function is meant to accommodate an unusual case;
one which is likely to eventually go away. There’s is a pretty good
chance this is not what you were looking for.

You can get the same effect as this function by implementing the
basic interface of multi-phase init ( [**PEP 489**](https://peps.python.org/pep-0489/)) and lying about
support for multiple interpreters (or per-interpreter GIL).

Warning

Using this function to disable the check can lead to
unexpected behavior and even crashes. It should only be used during
extension module development.

Added in version 3.12.

_class_ importlib.util.LazyLoader( _loader_) [¶](https://docs.python.org/3/library/importlib.html#importlib.util.LazyLoader "Link to this definition")

A class which postpones the execution of the loader of a module until the
module has an attribute accessed.

This class **only** works with loaders that define
[`exec_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.exec_module "importlib.abc.Loader.exec_module") as control over what module type
is used for the module is required. For those same reasons, the loader’s
[`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module") method must return `None` or a
type for which its `__class__` attribute can be mutated along with not
using [slots](https://docs.python.org/3/glossary.html#term-__slots__). Finally, modules which substitute the object
placed into [`sys.modules`](https://docs.python.org/3/library/sys.html#sys.modules "sys.modules") will not work as there is no way to properly
replace the module references throughout the interpreter safely;
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised if such a substitution is detected.

Note

For projects where startup time is critical, this class allows for
potentially minimizing the cost of loading a module if it is never used.
For projects where startup time is not essential then use of this class is
**heavily** discouraged due to error messages created during loading being
postponed and thus occurring out of context.

Added in version 3.5.

Changed in version 3.6: Began calling [`create_module()`](https://docs.python.org/3/library/importlib.html#importlib.abc.Loader.create_module "importlib.abc.Loader.create_module"), removing the
compatibility warning for [`importlib.machinery.BuiltinImporter`](https://docs.python.org/3/library/importlib.html#importlib.machinery.BuiltinImporter "importlib.machinery.BuiltinImporter") and
[`importlib.machinery.ExtensionFileLoader`](https://docs.python.org/3/library/importlib.html#importlib.machinery.ExtensionFileLoader "importlib.machinery.ExtensionFileLoader").

_classmethod_ factory( _loader_) [¶](https://docs.python.org/3/library/importlib.html#importlib.util.LazyLoader.factory "Link to this definition")

A class method which returns a callable that creates a lazy loader. This
is meant to be used in situations where the loader is passed by class
instead of by instance.

Copy

```
suffixes = importlib.machinery.SOURCE_SUFFIXES
loader = importlib.machinery.SourceFileLoader
lazy_loader = importlib.util.LazyLoader.factory(loader)
finder = importlib.machinery.FileFinder(path, (lazy_loader, suffixes))
```

## Examples [¶](https://docs.python.org/3/library/importlib.html\#examples "Link to this heading")

### Importing programmatically [¶](https://docs.python.org/3/library/importlib.html\#importing-programmatically "Link to this heading")

To programmatically import a module, use [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module").

Copy

```
import importlib

itertools = importlib.import_module('itertools')
```

### Checking if a module can be imported [¶](https://docs.python.org/3/library/importlib.html\#checking-if-a-module-can-be-imported "Link to this heading")

If you need to find out if a module can be imported without actually doing the
import, then you should use [`importlib.util.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.util.find_spec "importlib.util.find_spec").

Note that if `name` is a submodule (contains a dot),
[`importlib.util.find_spec()`](https://docs.python.org/3/library/importlib.html#importlib.util.find_spec "importlib.util.find_spec") will import the parent module.

Copy

```
import importlib.util
import sys

# For illustrative purposes.
name = 'itertools'

if name in sys.modules:
    print(f"{name!r} already in sys.modules")
elif (spec := importlib.util.find_spec(name)) is not None:
    # If you chose to perform the actual import ...
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    print(f"{name!r} has been imported")
else:
    print(f"can't find the {name!r} module")
```

### Importing a source file directly [¶](https://docs.python.org/3/library/importlib.html\#importing-a-source-file-directly "Link to this heading")

This recipe should be used with caution: it is an approximation of an import
statement where the file path is specified directly, rather than
[`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") being searched. Alternatives should first be considered first,
such as modifying [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") when a proper module is required, or using
[`runpy.run_path()`](https://docs.python.org/3/library/runpy.html#runpy.run_path "runpy.run_path") when the global namespace resulting from running a Python
file is appropriate.

To import a Python source file directly from a path, use the following recipe:

Copy

```
import importlib.util
import sys

def import_from_path(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

# For illustrative purposes only (use of `json` is arbitrary).
import json
file_path = json.__file__
module_name = json.__name__

# Similar outcome as `import json`.
json = import_from_path(module_name, file_path)
```

### Implementing lazy imports [¶](https://docs.python.org/3/library/importlib.html\#implementing-lazy-imports "Link to this heading")

The example below shows how to implement lazy imports:

Copy

```
>>> import importlib.util
>>> import sys
>>> def lazy_import(name):
...     spec = importlib.util.find_spec(name)
...     loader = importlib.util.LazyLoader(spec.loader)
...     spec.loader = loader
...     module = importlib.util.module_from_spec(spec)
...     sys.modules[name] = module
...     loader.exec_module(module)
...     return module
...
>>> lazy_typing = lazy_import("typing")
>>> #lazy_typing is a real module object,
>>> #but it is not loaded in memory yet.
>>> lazy_typing.TYPE_CHECKING
False
```

### Setting up an importer [¶](https://docs.python.org/3/library/importlib.html\#setting-up-an-importer "Link to this heading")

For deep customizations of import, you typically want to implement an
[importer](https://docs.python.org/3/glossary.html#term-importer). This means managing both the [finder](https://docs.python.org/3/glossary.html#term-finder) and [loader](https://docs.python.org/3/glossary.html#term-loader)
side of things. For finders there are two flavours to choose from depending on
your needs: a [meta path finder](https://docs.python.org/3/glossary.html#term-meta-path-finder) or a [path entry finder](https://docs.python.org/3/glossary.html#term-path-entry-finder). The
former is what you would put on [`sys.meta_path`](https://docs.python.org/3/library/sys.html#sys.meta_path "sys.meta_path") while the latter is what
you create using a [path entry hook](https://docs.python.org/3/glossary.html#term-path-entry-hook) on [`sys.path_hooks`](https://docs.python.org/3/library/sys.html#sys.path_hooks "sys.path_hooks") which works
with [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path") entries to potentially create a finder. This example will
show you how to register your own importers so that import will use them (for
creating an importer for yourself, read the documentation for the appropriate
classes defined within this package):

Copy

```
import importlib.machinery
import sys

# For illustrative purposes only.
SpamMetaPathFinder = importlib.machinery.PathFinder
SpamPathEntryFinder = importlib.machinery.FileFinder
loader_details = (importlib.machinery.SourceFileLoader,
                  importlib.machinery.SOURCE_SUFFIXES)

# Setting up a meta path finder.
# Make sure to put the finder in the proper location in the list in terms of
# priority.
sys.meta_path.append(SpamMetaPathFinder)

# Setting up a path entry finder.
# Make sure to put the path hook in the proper location in the list in terms
# of priority.
sys.path_hooks.append(SpamPathEntryFinder.path_hook(loader_details))
```

### Approximating [`importlib.import_module()`](https://docs.python.org/3/library/importlib.html\#importlib.import_module "importlib.import_module") [¶](https://docs.python.org/3/library/importlib.html\#approximating-importlib-import-module "Link to this heading")

Import itself is implemented in Python code, making it possible to
expose most of the import machinery through importlib. The following
helps illustrate the various APIs that importlib exposes by providing an
approximate implementation of
[`importlib.import_module()`](https://docs.python.org/3/library/importlib.html#importlib.import_module "importlib.import_module"):

Copy

```
import importlib.util
import sys

def import_module(name, package=None):
    """An approximate implementation of import."""
    absolute_name = importlib.util.resolve_name(name, package)
    try:
        return sys.modules[absolute_name]
    except KeyError:
        pass

    path = None
    if '.' in absolute_name:
        parent_name, _, child_name = absolute_name.rpartition('.')
        parent_module = import_module(parent_name)
        path = parent_module.__spec__.submodule_search_locations
    for finder in sys.meta_path:
        spec = finder.find_spec(absolute_name, path)
        if spec is not None:
            break
    else:
        msg = f'No module named {absolute_name!r}'
        raise ModuleNotFoundError(msg, name=absolute_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[absolute_name] = module
    spec.loader.exec_module(module)
    if path is not None:
        setattr(parent_module, child_name, module)
    return module
```

### [Table of Contents](https://docs.python.org/3/contents.html)

- [`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html#)
  - [Introduction](https://docs.python.org/3/library/importlib.html#introduction)
  - [Functions](https://docs.python.org/3/library/importlib.html#functions)
  - [`importlib.abc` – Abstract base classes related to import](https://docs.python.org/3/library/importlib.html#module-importlib.abc)
  - [`importlib.machinery` – Importers and path hooks](https://docs.python.org/3/library/importlib.html#module-importlib.machinery)
  - [`importlib.util` – Utility code for importers](https://docs.python.org/3/library/importlib.html#module-importlib.util)
  - [Examples](https://docs.python.org/3/library/importlib.html#examples)
    - [Importing programmatically](https://docs.python.org/3/library/importlib.html#importing-programmatically)
    - [Checking if a module can be imported](https://docs.python.org/3/library/importlib.html#checking-if-a-module-can-be-imported)
    - [Importing a source file directly](https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly)
    - [Implementing lazy imports](https://docs.python.org/3/library/importlib.html#implementing-lazy-imports)
    - [Setting up an importer](https://docs.python.org/3/library/importlib.html#setting-up-an-importer)
    - [Approximating `importlib.import_module()`](https://docs.python.org/3/library/importlib.html#approximating-importlib-import-module)

#### Previous topic

[`runpy` — Locating and executing Python modules](https://docs.python.org/3/library/runpy.html "previous chapter")

#### Next topic

[`importlib.resources` – Package resource reading, opening and access](https://docs.python.org/3/library/importlib.resources.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/importlib.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/importlib.resources.html "importlib.resources – Package resource reading, opening and access") \|
- [previous](https://docs.python.org/3/library/runpy.html "runpy — Locating and executing Python modules") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Importing Modules](https://docs.python.org/3/library/modules.html) »
- [`importlib` — The implementation of `import`](https://docs.python.org/3/library/importlib.html)
- \|

- Theme
AutoLightDark \|