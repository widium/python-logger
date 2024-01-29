from root import MyLogger
logger = MyLogger(name=__name__)

def some_func():
    try:
        logger.info("This is a message at the start of some_func")
        raise ValueError("Example exception")
        logger.info("This message should not appear")
    
    except Exception as e:
        logger.exception("An error occurred in some_func")
