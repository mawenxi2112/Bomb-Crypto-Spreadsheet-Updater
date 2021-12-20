from datetime import datetime
import sys
import yaml
import os

stream = open("./config.yaml", 'r')
cfg = yaml.safe_load(stream)

COLOR = {
    'blue': '\033[94m',
    'default': '\033[99m',
    'grey': '\033[90m',
    'yellow': '\033[93m',
    'black': '\033[90m',
    'cyan': '\033[96m',
    'green': '\033[92m',
    'magenta': '\033[95m',
    'white': '\033[97m',
    'red': '\033[91m'
}


def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def date_formatted(format = "%d/%m/%Y %I:%M:%S%p"):
    return datetime.now().strftime(format)


def logger(message, color='default'):

    color_formatted = COLOR.get(color.lower(), COLOR['default'])

    formatted_datetime = date_formatted()
    formatted_message = "[{}] {}".format(formatted_datetime, message)
    formatted_message_colored = color_formatted + formatted_message + '\033[0m'

    print(formatted_message_colored + "\n")

    if cfg['save_log_to_file']:
        logger_file = open("./logs/logger.log", "a", encoding='utf-8')
        logger_file.write(formatted_message + '\n')
        logger_file.close()

    return True
