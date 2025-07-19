from r_i_scanner import ping
from r_i_logger import log_results_i, log_error_i
from r_i_exporter import export_csv_i, export_json_i
from r_i_filters import (match_pattern, match_pattern_2, match_pattern_3, match_regex, keyword_check)

def load_targets(file="r_i_targets.txt"):
    with open(file, "r") as f:
        return [line.strip() for line in f if line.strip()]

targets=load_targets()
results=[]
summary_stats={
    "resolved":0,
    "unresolved":0,
    "gov.in":0,
    "edu":0,
    "numeric":0,
    "keyword_hit":0
}

for domain in targets:
    try:
        status=ping(domain)
        print("\U0001F4E1", status)
        log_results_i(status)
        results.append((domain, status))

        if"\u2705" in status:
            summary_stats["resolved"] +=1
        else:
            summary_stats["unresolved"] +=1
        if match_pattern(domain):
            summary_stats["gov.in"] +=1
        if match_pattern_2(domain):
            summary_stats["edu"] +=1
        if match_pattern_3(domain):
            summary_stats["numeric"] +=1
        if match_regex(domain, r"\.org$", find_all=False):
            print(f"\U0001F3DB {domain} is an .org domain")
        if keyword_check(domain):
            summary_stats["keyword_hit"] +=1
    except Exception as e:
        print("\u26A0 Error: ", e)
        log_error_i(e)

export_csv_i(results)
export_json_i(results)

with open("summary.txt","w",encoding="utf-8") as f:
    f.write("\U0001F4CA Scan Summary: \n")
    for key, value in summary_stats.items():
        f.write(f"{key.capitalize()}: {value}\n")

print("\u2705 All exports completed. Summary saved to summary.txt")