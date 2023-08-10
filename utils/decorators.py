from utils.browser import WebDriverSingleton

sdriver = None

def ensure_driver(func):
    def wrapper(*args, **kwargs):
        # if not hasattr(ensure_driver, "sdriver"):
            # ensure_driver._driver = WebDriverSingleton.get_instance()
        global sdriver
        if sdriver is None:
            sdriver = WebDriverSingleton.get_instance()
        return func(*args, **kwargs)
    return wrapper
