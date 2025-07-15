import time
def log_result(message, file="recon_log.txt"):
    with open(file, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def log_error(error, file="error_log.txt"):
    timestamp = time.strftime("[%Y-%m-%d %H:%M:%S]")
    with open(file, "a") as f:
        f.write(f"{timestamp} {str(error)}\n")