def new_log_result(message, file="new_recon_log.txt"):
    with open(file, "a", encoding="utf-8") as f:
        f.write(message+"\n")

def new_log_error(error, file="new_error_log.txt"):
    import time
    timestamp=time.strftime("[%Y-%m-%d %H:%M:%S]")
    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp} {str(error)} \n")