# AdvancedLogger: Custom Logging Tool for Python

## Overview
AdvancedLogger is a custom Python logger designed to streamline logging in your Python projects. It captures stdout, logs objects, and gracefully handles exceptions. It's easy to integrate and use in various scenarios.

## Installation
Copy the `logger.py` file containing the `AdvancedLogger` class into your project directory.

## Basic Usage
Import `AdvancedLogger` and use it within a `with` statement to start logging:

```python
from logger import AdvancedLogger

logger = AdvancedLogger(log_directory="logs")

with logger.logging_context():
    print("Your log message here")
```

## Features

### Standard Logging
Logs standard messages with timestamps:

```python
from logger import AdvancedLogger

logger = AdvancedLogger(log_directory="logs")

with logger.logging_context():
    print("This message will be logged.")
```
**Output:**
```
2023-12-22 10:45:01 | This message will be logged.
```

### Multi-Line Logging
Handles multi-line messages, indenting subsequent lines for readability:

```python
with logger.logging_context():
    print("This message has multiple lines\nThis is the second line\nThis is the third line")
```
**Output:**
```
2023-12-22 10:45:01 | This message has multiple lines
    This is the second line
    This is the third line
```

### Logging Objects
Log complex objects with `log_object()`. Note: Must be used within the logging context:

```python
from logger import AdvancedLogger
from your_module import YourObject

def some_function():
    obj = YourObject()
    AdvancedLogger.log_object(obj)

with logger.logging_context():
    some_function()
```
**Output:**
```
2023-12-22 10:45:01 | [YourObject] Content: ...
```

### Exception Handling
Automatically logs exceptions occurring within the logging context:

```python
with logger.logging_context():
    raise Exception("This is an exception")
```
**Output:**
```
2023-12-22 10:49:45 | This message will be logged.
2023-12-22 10:49:45 | [CRASH]: This is an exception
    
    Traceback (most recent call last):
      ...
```

### Accessing Log File Name
Retrieve the log file name within the logging context:

```python
with logger.logging_context() as tracker:
    print("This message will be logged.")
print(tracker.log_path)
```
**Output:**
```
2023-12-22 10:53:46 | This message will be logged.
...
logs/2023-12-22_10-53-46.log
```

## Best Practices
- Always use `AdvancedLogger` within a `with` statement for proper start and stop of logging.
- Use `AdvancedLogger.log_object()` to log complex objects. Ensure it's within the logging context.
- Check `tracker.log_path` for the log file name and path.