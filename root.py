# import logging
# import logging.config
# from datetime import datetime
# from pathlib import Path

# class CustomFormatter(logging.Formatter):
#     def __init__(self):
#         fmt = "[%(asctime)s | %(levelname)s | %(module)s:%(funcName)s:%(lineno)s | Thread: %(threadName)s] :  %(message)s | Extra Data: %(x)s"
#         super().__init__(fmt)

#     def format(self, record):
#         record.x = record.__dict__.get('x', 'N/A')
#         return super(CustomFormatter, self).format(record)

# class MyLogger:
#     def __init__(self, level: str = "INFO", logs_folder: str = "./logs/"):
#         self.logs_folder = logs_folder
#         self.level = level
#         self.setup_root_logger()

#     def setup_root_logger(self):
#         logs_folder_path = Path(self.logs_folder)
#         if not logs_folder_path.exists():
#             logs_folder_path.mkdir(parents=True, exist_ok=True)
#             print(f"Created logs folder [{logs_folder_path}]")

#         timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
#         log_file_path = logs_folder_path / f"log_{timestamp}.log"

#         logging_config = {
#             "version": 1,
#             "formatters": {
#                 "custom": {
#                     "()": CustomFormatter
#                 }
#             },
#             "handlers": {
#                 "file": {
#                     "class": "logging.FileHandler",
#                     "formatter": "custom",
#                     "filename": str(log_file_path),
#                     "mode": "a"
#                 },
#                 "console": {
#                     "class": "logging.StreamHandler",
#                     "formatter": "custom"
#                 }
#             },
#             "root": {
#                 "level": self.level,
#                 "handlers": ["file", "console"]
#             }
#         }

#         logging.config.dictConfig(logging_config)


import logging
import logging.config
from datetime import datetime
from pathlib import Path

class CustomFormatter(logging.Formatter):
    def __init__(self):
        fmt = "[%(asctime)s | %(levelname)s | %(module)s:%(funcName)s:%(lineno)s | Thread: %(threadName)s] : %(message)s | Extra Data: %(x)s"
        super().__init__(fmt)

    def format(self, record):
        record.x = record.__dict__.get('x', 'N/A')
        return super(CustomFormatter, self).format(record)

class RootLogger:
    def __init__(self, level: str = "INFO", logs_folder: str = "./logs/"):
        self.logs_folder = logs_folder
        self.level = level
        self.setup_root_logger()

        # Ensure logs folder exists
        logs_folder_path = Path(logs_folder)
        logs_folder_path.mkdir(parents=True, exist_ok=True)

        # Define log file path
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file_path = logs_folder_path / f"log_{timestamp}.log"

        # Configure handlers
        file_handler = logging.FileHandler(str(log_file_path), mode='a')
        console_handler = logging.StreamHandler()

        # Set formatter
        formatter = CustomFormatter()
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.addHandler(file_handler)
        self.addHandler(console_handler)