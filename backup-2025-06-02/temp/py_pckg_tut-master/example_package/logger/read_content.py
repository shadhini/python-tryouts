import logging
import logging.config
import yaml

import pkgutil


def read_content():
    data = pkgutil.get_data(__name__, "logger_config.yaml")
    print("data:", repr(data))
    text = pkgutil.get_data(__name__, "logger_config.yaml").decode()
    print("text:", repr(text))



