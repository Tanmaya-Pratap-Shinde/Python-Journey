import argparse
from scanner import ping
from logger import new_log_result, new_log_error
parser=argparse.ArgumentParser(description="\U0001F4E1 ReconBot CLI Scanner")
parser.add_argument("--domain", type=str, help="Target domain to scan")
parser.add_argument("--log", type=str, default="new_recon_log.txt", help="Output log file")
parser.add_argument("--mode", choices=["safe","aggressive"], default="safe")
args=parser.parse_args()

try:
    result=ping(args.domain)
    print("\U0001F4E1", result)
    new_log_result(result, args.log)
except Exception as e:
    print("\u26A0 Error: ", e)
    new_log_error(e)