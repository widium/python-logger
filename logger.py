# *************************************************************************** #
#                                                                              #
#    logger.py                                                                 #
#                                                                              #
#    By: Widium <ebennace@student.42lausanne.ch>                               #
#    Github : https://github.com/widium                                        #
#                                                                              #
#    Created: 2023/12/21 16:57:55 by Widium                                    #
#    Updated: 2023/12/21 16:57:55 by Widium                                    #
#                                                                              #
# **************************************************************************** #

import sys
import json
import traceback
from contextlib import contextmanager
from datetime import datetime
from pathlib import Path

# ============================================================================= #

class AdvancedLogger:
    _instance = None

# ============================================================================= #

    def __init__(self, log_directory="logs"):
        self.original_stdout = sys.stdout
        self.log_directory = Path(log_directory)
        self.log_directory.mkdir(parents=True, exist_ok=True)
        self.log_file = None
        AdvancedLogger._instance = self

# ============================================================================= #

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            raise RuntimeError("Logger instance not active, Use inside a context manager")
        return cls._instance

# ============================================================================= #

    def start_logging(self):
        log_filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")
        self.log_path = self.log_directory / log_filename
        self.log_file = open(self.log_path, "w")
        sys.stdout = self

# ============================================================================= #

    def stop_logging(self):
        self.flush()  # Ensure all data is flushed before closing
        sys.stdout = self.original_stdout
        if self.log_file:
            self.log_file.close()
            self.log_file = None

# ============================================================================= #

    def write(self, message):
        # Manage the `print(end="")` case (call another write for just write the end)
        if message == '\n':
            return

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = message.rstrip('\n')  # Remove "\n" at the end of the message
        lines = message.split("\n")
        formatted_message = ""

        for i, line in enumerate(lines):
            if i == 0:
                formatted_message += f"{timestamp} | {line}"
            else:
                formatted_message += f"\n    {line}" # multi lines managment

        formatted_message += "\n"

        self.original_stdout.write(formatted_message)
        if self.log_file:
            self.log_file.write(formatted_message)
        self.flush()

# ============================================================================= #

    @classmethod
    def log_object(cls, obj):
        instance = cls.get_instance()
        if instance.log_file is not None:
            try:
                json_str = json.dumps(obj, indent=4)
                instance.write(json_str)
            except TypeError as e:
                instance.write(f"[WARNING]: [{obj.__class__.__name__}()] object Cannot be serialized, raw print instead\n")
                instance.write(f"[{obj.__class__.__name__}()] Content : [{str(obj)}]\n")
        else:
            raise RuntimeError("Logger context manager not active, cant log this object")

# ============================================================================= #

    def flush(self):
        self.original_stdout.flush()
        if self.log_file:
            self.log_file.flush()

# ============================================================================= #

    @contextmanager
    def logging_context(self):
        try:
            self.start_logging()
            yield
        except Exception as e:
            error_message = f"[CRASH]: {e}\n\n{traceback.format_exc()}"
            self.write(error_message)
        finally:
            self.stop_logging()
            
# ============================================================================= #

