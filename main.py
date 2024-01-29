from root import MyLogger
import logging

from func import some_func

if __name__ == "__main__":
    logger = MyLogger(
        name=__name__,
        level=logging.INFO,
        logs_folder="./logs/",
    )
    
    data = {"x": [
            {"y" : "custom_value"},
            {"t" : "custom_value"},
            {"i" : "custom_value"},
            {"a" : "custom_value"},
            {"p" : "custom_value"},
        ]
    }
    logger.info("This is an info message", extra=data)
    some_func()
    logger.info("End of program")