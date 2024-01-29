## Overview
`MyLogger` is a customizable logging utility for Python applications. It simplifies the process of logging messages to both the console and a file, with the added capability of including extra data in log messages. This utility is ideal for tracking application behavior, debugging, and maintaining records of operations with precise timestamps.

## Features
- Customizable log level and output folder.
- Simultaneous logging to console and file.
- Support for adding extra data in log messages.
- Seamless integration into Python scripts and modules.

## Usage

### 1. Basic Setup and Logging
**Code:**
```python
from my_logger import MyLogger

logger = MyLogger(name=__name__, level=logging.INFO, logs_folder="./logs/")

logger.info("This is a basic info message")
```

### 2. Changing Log Level
Specify different logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).

**Code:**
```python
logger = MyLogger(name=__name__, level=logging.DEBUG)

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

### 5. Using `MyLogger` in Another File
Integrate `MyLogger` into various modules of your application for consistent logging.

**func.py:**
```python
from my_logger import MyLogger

logger = MyLogger(__name__)

def some_func():
    logger.info("This is from some_func")
```

**main.py:**
```python
from my_logger import MyLogger
from func import some_func

logger = MyLogger(__name__)
some_func()
```

**Output:**
```
[2024-01-29 14:23:10 | INFO | func:some_func:4 | Thread: MainThread] :  This is from some_func | Extra Data: N/A
```