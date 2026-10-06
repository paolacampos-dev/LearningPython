## Exception Handling

```python
try:
    # Run this code
except:
    # Execute this code when
    # there is an exception
else:
    # No exceptions? Run this code.
finally:
    # Always run this code.
```

# raise Exception()

- it the exception raise no more code will be execute

# Create class CustomException():

    pass

# assert

- AssertionError:
  if the assertion is true the exception will be raise

# Build-in Exception hierarchy:

(https://docs.python.org/3/builtins/exceptions.html)

BaseException
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
└── Exception
├── StopIteration
├── StopAsyncIteration
├── ArithmeticError
│ ├── FloatingPointError
│ ├── OverflowError
│ └── ZeroDivisionError
├── AssertionError
├── AttributeError
├── BufferError
├── EOFError
├── ImportError
│ └── ModuleNotFoundError
├── **LookupError**
│ ├── IndexError
│ └── KeyError
├── **MemoryError**
├── **NameError**
│ └── UnboundLocalError
├── **OSError**
│ ├── BlockingIOError
│ ├── ChildProcessError
│ ├── ConnectionError
│ │ ├── BrokenPipeError
│ │ ├── ConnectionAbortedError
│ │ ├── ConnectionRefusedError
│ │ └── ConnectionResetError
│ ├── FileExistsError
│ ├── FileNotFoundError
│ ├── InterruptedError
│ ├── IsADirectoryError
│ ├── NotADirectoryError
│ ├── PermissionError
│ ├── ProcessLookupError
│ └── TimeoutError
├── ReferenceError
├── RuntimeError
│ ├── NotImplementedError
│ └── RecursionError
├── SyntaxError
│ └── IndentationError
│ └── TabError
├── SystemError
├── TypeError
├── ValueError
│ └── UnicodeError
│ ├── UnicodeDecodeError
│ ├── UnicodeEncodeError
│ └── UnicodeTranslateError
└── Warning
├── DeprecationWarning
├── PendingDeprecationWarning
├── RuntimeWarning
├── SyntaxWarning
├── UserWarning
├── FutureWarning
├── ImportWarning
├── UnicodeWarning
├── BytesWarning
├── EncodingWarning
└── ResourceWarning

# Common Built-in Exceptions

| Exception | Description |
| `ImportError` | import statement can't load a module |
| `NameError` | A global or local name isn't defined |
| `AttributeError` | Accessed attribute is unavailable |
| `IndexError` | Out of range access on a sequence (list, tuple, etc.) |
| `KeyError` | Missing dictionary key referenced |
| `ZeroDivisionError` | Divide by, or modulo, zero |
| `TypeError` | Object type isn't compatible with operation |
| `ValueError` | Right type of argument, but bad value |

# LYBL vs EAFP

## When to Use Which Style

### General Guidelines

| Use LBYL for                                                           | Use EAFP for                                                               |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Operations that are likely to fail                                     | Operations that are unlikely to fail                                       |
| Irrevocable operations, and operations that may have a side effect     | Input and output (IO) operations, mainly hard drive and network operations |
| Common exceptional conditions that can be quickly prevented beforehand | Database operations that can be rolled back quickly                        |

## EX: Avoiding Race Conditions

### LBYL: Look Before You Leap

```python
connection = create_connection(db, host, user, password)

# Later in your code...
if connection.is_active():
    # Update database here...
    connection.commit()
else:
    # Handle the connection error here...
```

### EAFP: Easier to ask for Forginess

```
connection = create_connection(db, host, user, password)

# Later in your code...
try:
# Update your database here...
    connection.commit()
except ConnectionError:
    # Handle the connection error here...
```
