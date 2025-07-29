import re
import argparse

suspicious_patterns = {
    "Fake URL": r"(https?://)?(www\.)?(fakesite|clickhere|freegift)\.com", 
    "OTP Scam": r"OTP\s+\d{4,6}",                                          
    "Phishy Text": r"(urgent|immediate|act now|limited time)",             
    "Fake Support": r"(customer support|helpline|toll-free)\s+\d{10}",     
    "Payment Threat": r"(payment\s+failed|card\s+blocked|verify\s+now)"    
}

def scan_text(input_text):
    for label, pattern in suspicious_patterns.items():
        try:
            if re.search(pattern, input_text, re.IGNORECASE):
                print(f"[\u260A {label}] Match found: {pattern}")
            else:
                print(f"[\u2705 {label}] No match")
        except re.error as e:
            print(f"[{label}] Invalid regex: {e}")

if __name__=="__main__":
    parser=argparse.ArgumentParser(description="Scam Pattern Scanner")
    parser.add_argument('--input', type=str, help="Text to scan")
    args=parser.parse_args()
    if args.input:
        scan_text(args.input)
    else:
        print("No input provided. Use --input \"your text here\"")