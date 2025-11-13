### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/asyncio-sync.html "Synchronization Primitives") \|
- [previous](https://docs.python.org/3/library/asyncio-task.html "Coroutines and Tasks") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
- [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html) »
- [Streams](https://docs.python.org/3/library/asyncio-stream.html)
- \|

- Theme
AutoLightDark \|

# Streams [¶](https://docs.python.org/3/library/asyncio-stream.html\#streams "Link to this heading")

**Source code:** [Lib/asyncio/streams.py](https://github.com/python/cpython/tree/3.14/Lib/asyncio/streams.py)

* * *

Streams are high-level async/await-ready primitives to work with
network connections. Streams allow sending and receiving data without
using callbacks or low-level protocols and transports.

Here is an example of a TCP echo client written using asyncio
streams:

Copy

```
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))
```

See also the [Examples](https://docs.python.org/3/library/asyncio-stream.html#examples) section below.

Stream Functions

The following top-level asyncio functions can be used to create
and work with streams:

_async_ asyncio.open\_connection( _host=None_, _port=None_, _\*_, _limit=None_, _ssl=None_, _family=0_, _proto=0_, _flags=0_, _sock=None_, _local\_addr=None_, _server\_hostname=None_, _ssl\_handshake\_timeout=None_, _ssl\_shutdown\_timeout=None_, _happy\_eyeballs\_delay=None_, _interleave=None_) [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection "Link to this definition")

Establish a network connection and return a pair of
`(reader, writer)` objects.

The returned _reader_ and _writer_ objects are instances of
[`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader") and [`StreamWriter`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter") classes.

_limit_ determines the buffer size limit used by the
returned [`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader") instance. By default the _limit_
is set to 64 KiB.

The rest of the arguments are passed directly to
[`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection").

Note

The _sock_ argument transfers ownership of the socket to the
[`StreamWriter`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter") created. To close the socket, call its
[`close()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.close "asyncio.StreamWriter.close") method.

Changed in version 3.7: Added the _ssl\_handshake\_timeout_ parameter.

Changed in version 3.8: Added the _happy\_eyeballs\_delay_ and _interleave_ parameters.

Changed in version 3.10: Removed the _loop_ parameter.

Changed in version 3.11: Added the _ssl\_shutdown\_timeout_ parameter.

_async_ asyncio.start\_server( _client\_connected\_cb_, _host=None_, _port=None_, _\*_, _limit=None_, _family=socket.AF\_UNSPEC_, _flags=socket.AI\_PASSIVE_, _sock=None_, _backlog=100_, _ssl=None_, _reuse\_address=None_, _reuse\_port=None_, _keep\_alive=None_, _ssl\_handshake\_timeout=None_, _ssl\_shutdown\_timeout=None_, _start\_serving=True_) [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_server "Link to this definition")

Start a socket server.

The _client\_connected\_cb_ callback is called whenever a new client
connection is established. It receives a `(reader, writer)` pair
as two arguments, instances of the [`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader") and
[`StreamWriter`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter") classes.

_client\_connected\_cb_ can be a plain callable or a
[coroutine function](https://docs.python.org/3/library/asyncio-task.html#coroutine); if it is a coroutine function,
it will be automatically scheduled as a [`Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task").

_limit_ determines the buffer size limit used by the
returned [`StreamReader`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "asyncio.StreamReader") instance. By default the _limit_
is set to 64 KiB.

The rest of the arguments are passed directly to
[`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server").

Note

The _sock_ argument transfers ownership of the socket to the
server created. To close the socket, call the server’s
[`close()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.close "asyncio.Server.close") method.

Changed in version 3.7: Added the _ssl\_handshake\_timeout_ and _start\_serving_ parameters.

Changed in version 3.10: Removed the _loop_ parameter.

Changed in version 3.11: Added the _ssl\_shutdown\_timeout_ parameter.

Changed in version 3.13: Added the _keep\_alive_ parameter.

Unix Sockets

_async_ asyncio.open\_unix\_connection( _path=None_, _\*_, _limit=None_, _ssl=None_, _sock=None_, _server\_hostname=None_, _ssl\_handshake\_timeout=None_, _ssl\_shutdown\_timeout=None_) [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_unix_connection "Link to this definition")

Establish a Unix socket connection and return a pair of
`(reader, writer)`.

Similar to [`open_connection()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection") but operates on Unix sockets.

See also the documentation of [`loop.create_unix_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_connection "asyncio.loop.create_unix_connection").

Note

The _sock_ argument transfers ownership of the socket to the
[`StreamWriter`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter "asyncio.StreamWriter") created. To close the socket, call its
[`close()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.close "asyncio.StreamWriter.close") method.

[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

Changed in version 3.7: Added the _ssl\_handshake\_timeout_ parameter.
The _path_ parameter can now be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)

Changed in version 3.10: Removed the _loop_ parameter.

Changed in version 3.11: Added the _ssl\_shutdown\_timeout_ parameter.

_async_ asyncio.start\_unix\_server( _client\_connected\_cb_, _path=None_, _\*_, _limit=None_, _sock=None_, _backlog=100_, _ssl=None_, _ssl\_handshake\_timeout=None_, _ssl\_shutdown\_timeout=None_, _start\_serving=True_, _cleanup\_socket=True_) [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_unix_server "Link to this definition")

Start a Unix socket server.

Similar to [`start_server()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server") but works with Unix sockets.

If _cleanup\_socket_ is true then the Unix socket will automatically
be removed from the filesystem when the server is closed, unless the
socket has been replaced after the server has been created.

See also the documentation of [`loop.create_unix_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_unix_server "asyncio.loop.create_unix_server").

Note

The _sock_ argument transfers ownership of the socket to the
server created. To close the socket, call the server’s
[`close()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.Server.close "asyncio.Server.close") method.

[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

Changed in version 3.7: Added the _ssl\_handshake\_timeout_ and _start\_serving_ parameters.
The _path_ parameter can now be a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

Changed in version 3.10: Removed the _loop_ parameter.

Changed in version 3.11: Added the _ssl\_shutdown\_timeout_ parameter.

Changed in version 3.13: Added the _cleanup\_socket_ parameter.

## StreamReader [¶](https://docs.python.org/3/library/asyncio-stream.html\#streamreader "Link to this heading")

_class_ asyncio.StreamReader [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader "Link to this definition")

Represents a reader object that provides APIs to read data
from the IO stream. As an [asynchronous iterable](https://docs.python.org/3/glossary.html#term-asynchronous-iterable), the
object supports the [`async for`](https://docs.python.org/3/reference/compound_stmts.html#async-for) statement.

It is not recommended to instantiate _StreamReader_ objects
directly; use [`open_connection()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection") and [`start_server()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server")
instead.

feed\_eof() [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader.feed_eof "Link to this definition")

Acknowledge the EOF.

_async_ read( _n=-1_) [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader.read "Link to this definition")

Read up to _n_ bytes from the stream.

If _n_ is not provided or set to `-1`,
read until EOF, then return all read [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").
If EOF was received and the internal buffer is empty,
return an empty `bytes` object.

If _n_ is `0`, return an empty `bytes` object immediately.

If _n_ is positive, return at most _n_ available `bytes`
as soon as at least 1 byte is available in the internal buffer.
If EOF is received before any byte is read, return an empty
`bytes` object.

_async_ readline() [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader.readline "Link to this definition")

Read one line, where “line” is a sequence of bytes
ending with `\n`.

If EOF is received and `\n` was not found, the method
returns partially read data.

If EOF is received and the internal buffer is empty,
return an empty `bytes` object.

_async_ readexactly( _n_) [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader.readexactly "Link to this definition")

Read exactly _n_ bytes.

Raise an [`IncompleteReadError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.IncompleteReadError "asyncio.IncompleteReadError") if EOF is reached before _n_
can be read. Use the [`IncompleteReadError.partial`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.IncompleteReadError.partial "asyncio.IncompleteReadError.partial")
attribute to get the partially read data.

_async_ readuntil( _separator=b'\\n'_) [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader.readuntil "Link to this definition")

Read data from the stream until _separator_ is found.

On success, the data and separator will be removed from the
internal buffer (consumed). Returned data will include the
separator at the end.

If the amount of data read exceeds the configured stream limit, a
[`LimitOverrunError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.LimitOverrunError "asyncio.LimitOverrunError") exception is raised, and the data
is left in the internal buffer and can be read again.

If EOF is reached before the complete separator is found,
an [`IncompleteReadError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.IncompleteReadError "asyncio.IncompleteReadError") exception is raised, and the internal
buffer is reset. The [`IncompleteReadError.partial`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.IncompleteReadError.partial "asyncio.IncompleteReadError.partial") attribute
may contain a portion of the separator.

The _separator_ may also be a tuple of separators. In this
case the return value will be the shortest possible that has any
separator as the suffix. For the purposes of [`LimitOverrunError`](https://docs.python.org/3/library/asyncio-exceptions.html#asyncio.LimitOverrunError "asyncio.LimitOverrunError"),
the shortest possible separator is considered to be the one that
matched.

Added in version 3.5.2.

Changed in version 3.13: The _separator_ parameter may now be a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") of
separators.

at\_eof() [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader.at_eof "Link to this definition")

Return `True` if the buffer is empty and [`feed_eof()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamReader.feed_eof "asyncio.StreamReader.feed_eof")
was called.

## StreamWriter [¶](https://docs.python.org/3/library/asyncio-stream.html\#streamwriter "Link to this heading")

_class_ asyncio.StreamWriter [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter "Link to this definition")

Represents a writer object that provides APIs to write data
to the IO stream.

It is not recommended to instantiate _StreamWriter_ objects
directly; use [`open_connection()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection") and [`start_server()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server")
instead.

write( _data_) [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.write "Link to this definition")

The method attempts to write the _data_ to the underlying socket immediately.
If that fails, the data is queued in an internal write buffer until it can be
sent.

The _data_ buffer should be a bytes, bytearray, or C-contiguous one-dimensional
memoryview object.

The method should be used along with the `drain()` method:

Copy

```
stream.write(data)
await stream.drain()
```

writelines( _data_) [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.writelines "Link to this definition")

The method writes a list (or any iterable) of bytes to the underlying socket
immediately.
If that fails, the data is queued in an internal write buffer until it can be
sent.

The method should be used along with the `drain()` method:

Copy

```
stream.writelines(lines)
await stream.drain()
```

close() [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.close "Link to this definition")

The method closes the stream and the underlying socket.

The method should be used, though not mandatory,
along with the `wait_closed()` method:

Copy

```
stream.close()
await stream.wait_closed()
```

can\_write\_eof() [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.can_write_eof "Link to this definition")

Return `True` if the underlying transport supports
the [`write_eof()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.write_eof "asyncio.StreamWriter.write_eof") method, `False` otherwise.

write\_eof() [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.write_eof "Link to this definition")

Close the write end of the stream after the buffered write
data is flushed.

transport [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.transport "Link to this definition")

Return the underlying asyncio transport.

get\_extra\_info( _name_, _default=None_) [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.get_extra_info "Link to this definition")

Access optional transport information; see
[`BaseTransport.get_extra_info()`](https://docs.python.org/3/library/asyncio-protocol.html#asyncio.BaseTransport.get_extra_info "asyncio.BaseTransport.get_extra_info") for details.

_async_ drain() [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.drain "Link to this definition")

Wait until it is appropriate to resume writing to the stream.
Example:

Copy

```
writer.write(data)
await writer.drain()
```

This is a flow control method that interacts with the underlying
IO write buffer. When the size of the buffer reaches
the high watermark, _drain()_ blocks until the size of the
buffer is drained down to the low watermark and writing can
be resumed. When there is nothing to wait for, the [`drain()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.drain "asyncio.StreamWriter.drain")
returns immediately.

_async_ start\_tls( _sslcontext_, _\*_, _server\_hostname=None_, _ssl\_handshake\_timeout=None_, _ssl\_shutdown\_timeout=None_) [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.start_tls "Link to this definition")

Upgrade an existing stream-based connection to TLS.

Parameters:

- _sslcontext_: a configured instance of [`SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext").

- _server\_hostname_: sets or overrides the host name that the target
server’s certificate will be matched against.

- _ssl\_handshake\_timeout_ is the time in seconds to wait for the TLS
handshake to complete before aborting the connection. `60.0` seconds
if `None` (default).

- _ssl\_shutdown\_timeout_ is the time in seconds to wait for the SSL shutdown
to complete before aborting the connection. `30.0` seconds if `None`
(default).


Added in version 3.11.

Changed in version 3.12: Added the _ssl\_shutdown\_timeout_ parameter.

is\_closing() [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.is_closing "Link to this definition")

Return `True` if the stream is closed or in the process of
being closed.

Added in version 3.7.

_async_ wait\_closed() [¶](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.wait_closed "Link to this definition")

Wait until the stream is closed.

Should be called after [`close()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.StreamWriter.close "asyncio.StreamWriter.close") to wait until the underlying
connection is closed, ensuring that all data has been flushed
before e.g. exiting the program.

Added in version 3.7.

## Examples [¶](https://docs.python.org/3/library/asyncio-stream.html\#examples "Link to this heading")

### TCP echo client using streams [¶](https://docs.python.org/3/library/asyncio-stream.html\#tcp-echo-client-using-streams "Link to this heading")

TCP echo client using the [`asyncio.open_connection()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection") function:

Copy

```
import asyncio

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())
    await writer.drain()

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))
```

See also

The [TCP echo client protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-example-tcp-echo-client-protocol)
example uses the low-level [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection") method.

### TCP echo server using streams [¶](https://docs.python.org/3/library/asyncio-stream.html\#tcp-echo-server-using-streams "Link to this heading")

TCP echo server using the [`asyncio.start_server()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.start_server "asyncio.start_server") function:

Copy

```
import asyncio

async def handle_echo(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    writer.write(data)
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(
        handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
```

See also

The [TCP echo server protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-example-tcp-echo-server-protocol)
example uses the [`loop.create_server()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_server "asyncio.loop.create_server") method.

### Get HTTP headers [¶](https://docs.python.org/3/library/asyncio-stream.html\#get-http-headers "Link to this heading")

Simple example querying HTTP headers of the URL passed on the command line:

Copy

```
import asyncio
import urllib.parse
import sys

async def print_http_headers(url):
    url = urllib.parse.urlsplit(url)
    if url.scheme == 'https':
        reader, writer = await asyncio.open_connection(
            url.hostname, 443, ssl=True)
    else:
        reader, writer = await asyncio.open_connection(
            url.hostname, 80)

    query = (
        f"HEAD {url.path or '/'} HTTP/1.0\r\n"
        f"Host: {url.hostname}\r\n"
        f"\r\n"
    )

    writer.write(query.encode('latin-1'))
    while True:
        line = await reader.readline()
        if not line:
            break

        line = line.decode('latin1').rstrip()
        if line:
            print(f'HTTP header> {line}')

    # Ignore the body, close the socket
    writer.close()
    await writer.wait_closed()

url = sys.argv[1]
asyncio.run(print_http_headers(url))
```

Usage:

Copy

```
python example.py http://example.com/path/page.html
```

or with HTTPS:

Copy

```
python example.py https://example.com/path/page.html
```

### Register an open socket to wait for data using streams [¶](https://docs.python.org/3/library/asyncio-stream.html\#register-an-open-socket-to-wait-for-data-using-streams "Link to this heading")

Coroutine waiting until a socket receives data using the
[`open_connection()`](https://docs.python.org/3/library/asyncio-stream.html#asyncio.open_connection "asyncio.open_connection") function:

Copy

```
import asyncio
import socket

async def wait_for_data():
    # Get a reference to the current event loop because
    # we want to access low-level APIs.
    loop = asyncio.get_running_loop()

    # Create a pair of connected sockets.
    rsock, wsock = socket.socketpair()

    # Register the open socket to wait for data.
    reader, writer = await asyncio.open_connection(sock=rsock)

    # Simulate the reception of data from the network
    loop.call_soon(wsock.send, 'abc'.encode())

    # Wait for data
    data = await reader.read(100)

    # Got data, we are done: close the socket
    print("Received:", data.decode())
    writer.close()
    await writer.wait_closed()

    # Close the second socket
    wsock.close()

asyncio.run(wait_for_data())
```

See also

The [register an open socket to wait for data using a protocol](https://docs.python.org/3/library/asyncio-protocol.html#asyncio-example-create-connection) example uses a low-level protocol and
the [`loop.create_connection()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.create_connection "asyncio.loop.create_connection") method.

The [watch a file descriptor for read events](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio-example-watch-fd) example uses the low-level
[`loop.add_reader()`](https://docs.python.org/3/library/asyncio-eventloop.html#asyncio.loop.add_reader "asyncio.loop.add_reader") method to watch a file descriptor.

### [Table of Contents](https://docs.python.org/3/contents.html)

- [Streams](https://docs.python.org/3/library/asyncio-stream.html#)
  - [StreamReader](https://docs.python.org/3/library/asyncio-stream.html#streamreader)
  - [StreamWriter](https://docs.python.org/3/library/asyncio-stream.html#streamwriter)
  - [Examples](https://docs.python.org/3/library/asyncio-stream.html#examples)
    - [TCP echo client using streams](https://docs.python.org/3/library/asyncio-stream.html#tcp-echo-client-using-streams)
    - [TCP echo server using streams](https://docs.python.org/3/library/asyncio-stream.html#tcp-echo-server-using-streams)
    - [Get HTTP headers](https://docs.python.org/3/library/asyncio-stream.html#get-http-headers)
    - [Register an open socket to wait for data using streams](https://docs.python.org/3/library/asyncio-stream.html#register-an-open-socket-to-wait-for-data-using-streams)

#### Previous topic

[Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html "previous chapter")

#### Next topic

[Synchronization Primitives](https://docs.python.org/3/library/asyncio-sync.html "next chapter")

### This page

- [Report a bug](https://docs.python.org/3/bugs.html)
- [Show source](https://github.com/python/cpython/blob/main/Doc/library/asyncio-stream.rst?plain=1)

«

### Navigation

- [index](https://docs.python.org/3/genindex.html "General Index")
- [modules](https://docs.python.org/3/py-modindex.html "Python Module Index") \|
- [next](https://docs.python.org/3/library/asyncio-sync.html "Synchronization Primitives") \|
- [previous](https://docs.python.org/3/library/asyncio-task.html "Coroutines and Tasks") \|
- ![Python logo](https://docs.python.org/3/_static/py.svg)
- [Python](https://www.python.org/) »
- Greek \| ΕλληνικάEnglishSpanish \| españolFrench \| françaisItalian \| italianoJapanese \| 日本語Korean \| 한국어Polish \| polskiBrazilian Portuguese \| Português brasileiroRomanian \| RomâneșteTurkish \| TürkçeSimplified Chinese \| 简体中文Traditional Chinese \| 繁體中文

dev (3.15)3.14.03.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6

- [3.14.0 Documentation](https://docs.python.org/3/index.html) »

- [The Python Standard Library](https://docs.python.org/3/library/index.html) »
- [Networking and Interprocess Communication](https://docs.python.org/3/library/ipc.html) »
- [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html) »
- [Streams](https://docs.python.org/3/library/asyncio-stream.html)
- \|

- Theme
AutoLightDark \|