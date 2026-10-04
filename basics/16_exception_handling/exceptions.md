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
