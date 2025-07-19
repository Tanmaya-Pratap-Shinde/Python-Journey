import re
def match_pattern(domain, pattern=r"\.gov\.in$"):
    return re.search(pattern, domain)

def match_pattern_2(domain, pattern=r"\.edu$"):
    return re.search(pattern, domain)

def match_pattern_3(domain, pattern=r"\d+"):
    return re.findall(pattern, domain)

def match_regex(domain, pattern, find_all=False):
    if find_all:
        return re.findall(pattern, domain)
    return re.search(pattern, domain)

def keyword_check(domain, keyboards=["edu","bank","health"]):
    return any(keyword in domain for keyboard in keywords)