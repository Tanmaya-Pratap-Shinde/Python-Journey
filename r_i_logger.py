import time

def log_results_i(message, file="r_i_recon_log.txt"):
    with open(file, "a", encoding="utf-8") as f:
        f.write(message + "\n")

def log_error_i(error, file="r_i_error_log.txt"):
    timestamp=time.strftime("[%Y-%m-%d %H:%M:%S]")
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {str(error)}\n")