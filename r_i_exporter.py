import csv
import json

def export_csv_i(results, file="r_i_recon_results.csv"):
    with open(file, "w", newline='', encoding="utf-8") as f:
        writer=csv.writer(f)
        writer.writerow(["Domain","Status"])
        for domain, status in results:
            writer.writerow([domain, status])

def export_json_i(results, file="r_i_recon-results.json"):
    data={domain: status for domain, status in results}
    with open(file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)