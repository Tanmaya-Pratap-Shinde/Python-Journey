import time

def log_result_(message, file="_recon_log.txt"):
    with open(file, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def log_error_(error, file="_error_log.txt"):
    timestamp=time.strftime("[%Y=%m-%d %H:%M:%S]")
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {str(error)}\n")