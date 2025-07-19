from r_scanner import ping
from r_logger import log_result_, log_error_
from r_exporter import export_csv, export_json

def load_targets(file="targets.txt"):
    with open(file, "r") as f:
        return [line.strip() for line in f if line.strip()]

targets=load_targets()
results=[]

for domain in targets:
    try:
        status=ping(domain)
        print("\U0001F4E1", status)
        log_result_(status)
        results.append((domain, status))
    except Exception as e:
        print("\u26A0 Error: ",e)
        log_error_(e)

export_csv(results)
export_json(results)
print("\u2705 Results saved to CSV and JSON.")