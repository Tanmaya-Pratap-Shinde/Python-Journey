import socket
def ping(domain):
    try:
        ip=socket.gethostbyname(domain)
        return f"\u2705 {domain} -> {ip}"
    except socket.gaierror:
        return f"\u274C Could not resolve {domain}"
        