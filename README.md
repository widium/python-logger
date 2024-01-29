## Overview
`RootLogger` is a customizable logging utility for Python applications. It provides an easy way to log messages both to the console and to a file, with support for adding extra data to log messages. This utility is particularly useful for tracking application behavior, debugging, and keeping records of operations with timestamps.

## Features
- Customizable log level and output folder.
- Simultaneous logging to console and file.
- Support for adding extra data in log messages.
- Seamless integration into Python scripts and modules.

## Usage

### 1. Basic Setup and Logging
**Code:**
```python
from root import RootLogger
import logging

RootLogger(level="INFO", logs_folder="./logs/")
logger = logging.getLogger()

logger.info("This is a basic info message")
```

### 2. Changing Log Level
Specify different logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).

**Code:**
```python
RootLogger(level="DEBUG")
logger = logging.getLogger()

logger.debug("This is a debug message")
```

**Output:**
```
Created logs folder [logs]
[2024-01-29 14:18:10 | DEBUG | __main__:<module>:6 | Thread: MainThread] :  This is a debug message | Extra Data: N/A
```

### 3. Logging Exceptions
Efficiently log exceptions in your code, including stack trace.

**Code:**
```python
try:
    raise ValueError("Example exception")
except Exception as e:
    logger.exception("An error occurred")
```

**Output:**
```
[2024-01-29 14:19:30 | ERROR | __main__:<module>:5 | Thread: MainThread] :  An error occurred | Extra Data: N/A
Traceback (most recent call last):
  File "<string>", line 2, in <module>
ValueError: Example exception
```

### 4. Logging with Extra Data
Log additional information using the `extra` parameter.

**Code:**
```python
data = {"x": "custom_value"}
logger.info("Logging with extra data", extra=data)
```

**Output:**
```
[2024-01-29 14:21:01 | INFO | __main__:<module>:6 | Thread: MainThread] :  Logging with extra data | Extra Data: custom_value
```

### 5. Using `RootLogger` in Another File
Easily integrate `RootLogger` into different modules of your application.

**func.py:**
```python
from my_logger import MyLogger

logger = MyLogger(__name__)

def some_func():
    logger.info("This is from some_func")
```

**main.py:**
```python
from root import RootLogger
from func import some_func

RootLogger()
some_func()
```

**Output:**
```
[2024-01-29 14:23:10 | INFO | func:some_func:4 | Thread: MainThread] :  This is from some_func | Extra Data: N/A
```