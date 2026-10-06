import logging
logging.debug()
logging.info()
logging.warning()
logging.error() --> can be variables...
logging.critical()

- Basic configuration with logging.basicConfig(\*\*kwargs)
  - Common params:
    level
    filename
    filemode: mode to open file in, a (append) by default
    format: the format of the log message

```python
import logging

logging.basicConfig(
    filename="app.log",
    filemode="w",
    format="%(name)s - %(levelname)s - %(message)s"
)

logging.warning("This will get logged to a file")
```

file Output: root - WARNING - This will get logged to a file

# set up:

my_project/
├── main.py
├── app.log
└── ...

my_app/
├── main.py
├── logs/
│ └── app.log
└── .gitignore --> logs/

# Capturing stack traces

- exc_info param as True
  - if is False, the program output will not show the track trace, just the message

```python
import logging

a = 5
b = 0

try:
    c = a / b
except Exception as e:
    logging.error("Exception occurred", exc_info=True)
```
