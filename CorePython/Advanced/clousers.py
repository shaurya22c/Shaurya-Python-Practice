# closure occurs in python when nested function remembers the state of variables even after outer function has finished exexcuting

def logger(log_prefix):
    def log_message(message):
        print(f"{log_prefix}: {message}")
    return log_message

info_logger = logger("INFO")
error_logger = logger("ERROR")

info_logger("This is info message")
error_logger("This is error message")