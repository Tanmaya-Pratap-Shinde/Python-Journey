from scanner import ping
from logger import log_result, log_error
from config import TARGETS

for domain in TARGETS:
    try:
        result=ping(domain)
        print("\U0001F4E1", result)
        log_result(result)
    except Exception as e:
        print("\u26A0 Error: ", e)
        log_error(e)